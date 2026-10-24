> Documentation reference from the J1 implementation.
> This describes a pre-existing ticket-flow simulator, not implementation of the new diagnostic app.
> Relative source/code paths refer to the source project, not this portfolio repository.
> No simulator code, runtime, or credentials are included here. Assertions, test counts, and commands
> below come from the supplied document; they were not executed or validated for this publication.

---

# Jinzo WhatsApp ticket conversation simulator

Specification and replication guide for the console-only simulator that tests how the `jinzo-soporte-cliente` agent creates a support ticket for a given WhatsApp phone number, **without writing anything to Odoo**.

- **Source:** `work/jwts/` in this repository.
- **Operator copy on the VPS:** `/root/jwts-src/jwts/`.
- **Task tracking:** `odd/tasks/jinzo-whatsapp-ticket-simulator.md`.
- **Related production flow:** `docs/jinzo-support-conversation-flow.md`, plus tasks JGTF-5p…5v in `odd/tasks/jinzo-generic-support-ticket-flow.md`.

---

## 1. Purpose

Answer one question repeatedly and safely:

> "If the customer writing from phone number **X** asks the WhatsApp agent for a ticket, what does the conversation look like, and which customer would the ticket be attributed to?"

The simulator runs:

- the **real** agent policy (`SOUL.md`, skills), model, and tool names;
- the **real** read-only identity resolution against the central Odoo.

Three things are replaced:

- the inbound WhatsApp message, by a scripted scenario;
- the confirmation hook, by a harness-written turn file;
- the final ticket write, by a dry-run that builds the exact payload but never calls `create`.

### Non-goals

- It does not create, modify, or read tickets in Odoo, and never calls `message_post`.
- It does not test the production trust gates: trusted inbound evidence, sender binding, TTL expiry, and replay protection. Those stay covered by the production plugin test suite (270 tests).
- It is not a sandbox against a hostile agent. It is a conversation and policy diagnostic.

---

## 2. Architecture

```
Operator (root on VPS)
  │  private files: sender (0600), scenario (0600)
  ▼
harness/run_sim.py ──────────────────────────────────────────────────────────────┐
  1. create /root/.jinzo-sim/run-<UTC>-<rand>/ (0700)                            │
  2. copy ONLY: agent workspace, agent auth dir, .env  → run/state (uid 1000)     │
  3. write reduced openclaw.json (one agent, no channels/bindings/hooks,          │
     only the simulation plugin enabled)                                          │
  4. install simulation plugin + production typebox into run/state/extensions     │
  5. for each scenario turn:                                                      │
       write run/state/sim/turn.json {turn, message}                              │
       docker run --rm <production image> openclaw agent --local                  │
              --agent jinzo-soporte-cliente --session-key <stable per run>        │
              --message <turn text> --json                                        │
  6. build report.json from replies + events.jsonl                                │
  7. delete copied .env, auth dir, sender; keep report + transcripts              │
└─────────────────────────────────────────────────────────────────────────────────┘
        │ container (uid 1000, no host network, no docker socket)
        ▼
  real agent (SOUL/skills/model) ──calls──► simulation plugin (same tool names/schemas)
                                               │
                        check  ────────────────┼──► jinzo_sim.sim_check_cli  (read-only)
                        prepare ───────────────┤     pending.json (0600, outside draft)
                        create ────────────────┴──► jinzo_sim.sim_create_cli (dry-run)
                                                         │ real resolver + real validator
                                                         ▼
                                               Odoo central: authenticate + res.partner search_read/read only
```

### Mounts per turn container

| Host source | Container path | Mode |
|---|---|---|
| `run/state` (copied state) | `/home/node/.openclaw` | read-write (throwaway copy) |
| production runtime `workspace-hitofusion-soporte-cliente-vnext/runtime` | `/sim/runtime` | **read-only** |
| `jinzo-support-credentials` | `/sim/credentials` | **read-only** |
| `workspace-hitofusion-soporte-cliente-vnext/config/support-system.pilot.json` | `/sim/support-system.json` | **read-only** |

Production `openclaw.json`, session stores, pending drafts, replay markers, and the production ticket plugin are **never** copied or mounted.

---

## 3. Components

### 3.1 Simulation plugin: `work/jwts/plugin/`

- **Plugin id:** `jinzo-support-ticket-simulator`.
- **Config keys:** `simDir`, `pythonPath`, `runtimeRoot`, `simCliRoot`, `supportSystemConfig`, `credentialDir`.
- **Tools:** it registers three tools whose **names, parameter schemas, and descriptions are identical to production**. The descriptions must match because the model behaves differently when it sees simulation wording; `plugin/tests/fidelity.test.mjs` enforces this.

| Tool | Schema | Simulated behavior |
|---|---|---|
| `jinzo_check_ticket_identity` | `{}` only | Runs the read-only check CLI and returns only `{status}` with status in `unique`/`ambiguous`/`unknown`/`unavailable`. For `ambiguous` with 2–5 contacts it also returns masked `{index,label}` options. The `index → contact_id` mapping is kept in a private file in `simDir` and never shown to the model. |
| `jinzo_prepare_ticket_creation` | `subject`, `problem`, `attempted`, `expected`, `observed`, `impact` (production length limits), optional `company_hint` (1–120), optional `contact_choice` (1–5) | Validates like production. Writes `simDir/pending.json` (0600) with the draft, the turn number, the hint, and the selected contact id, all stored **outside** the draft. Returns `confirmation_required` and the summary. |
| `jinzo_create_confirmed_ticket` | `{}` only | Requires a pending draft, a turn number greater than the preparation turn, and a turn message that is an accepted whole-message confirmation (rules below). Consumes the pending draft **before** spawning, then runs the dry-run create CLI with 15 s timeout. Any failure → `unavailable`. |

**Confirmation normalization.** It mirrors the production plugin exactly:

1. Apply NFC normalization.
2. Lowercase with the `es` locale.
3. Trim ASCII spaces and tabs.
4. Collapse runs of spaces and tabs to one space.
5. Normalize `[ \t]*,[ \t]*` to `", "`.

The only accepted results are `si crear ticket`, `sí crear ticket`, `si, crear ticket`, and `sí, crear ticket`.

**Event log.** Every tool call appends `{tool, status, turn}` to `simDir/events.jsonl`. Dry-run successes are logged as `simulated_created` or `simulated_pending_identification`.

**Model view.** The `simulation` block is stripped before the result reaches the model, and the receipt id is replaced with a production-shaped placeholder. The model therefore sees a normal `created` or `created_pending_identification` result.

### 3.2 Runtime CLIs: `work/jwts/runtime/jinzo_sim/`

- **`sim_check_cli.py`** delegates to the production read-only `jinzo_vnext.support_identity_check_cli`.
- **`sim_create_cli.py`** works as follows:
  1. It reads the sender from `JINZO_SIM_SENDER_FILE`, with `O_NOFOLLOW`, regular file, and mode exactly 0600.
  2. It accepts stdin `{draft, company_hint?, selected_contact_id?}` and rejects other keys.
  3. It resolves the sender with the **production** `OdooSupportIdentityResolver.resolve_candidates`, which uses a fixed exact-phone domain, active contacts only, national-10 matching, and fails closed at saturation 20.
  4. It applies the production precedence:
     - `unique` → that customer;
     - `ambiguous` with a `selected_contact_id` among the fresh candidates → that contact;
     - else `match_company_hint` → that company;
     - else pending identification;
     - `unknown` → pending identification.
  5. It builds the payload with the production pure validator: `SupportTicketWriteGateway._validate` or `_draft_values`.
  6. It returns the production `_result` shape with `ticket_ref` `SIMULADO-0000` (customer attributed) or `SIMULADO-PEND-0000` (pending), stage `[0, "Simulado"]`, no `tenant_id`, and a `simulation` block: `dry_run`, `would_create`, `fields_present`, `fields_no_informado`, and `path` (`contact_choice`, `pending_ambiguous`, or `pending_unknown`).
  7. **No write path exists.** Tests patch `execute_kw` and fail on any method other than `authenticate`, `search_read`, or `read`, including `create`, `write`, and `message_post`.

### 3.3 Harness: `work/jwts/harness/run_sim.py`

- **Invocation:** run as root on the VPS host with Docker CLI access.
- **Required arguments:** `--scenario <0600 json>` and `--sender-file <0600 file with one number in 549+10 digits, optional +>`. Symlinks or wrong permissions are rejected.
- **Optional overrides:** `--source-state`, `--runtime-root`, `--credential-dir`, `--support-system-config`, `--typebox-dir`, and `--show-replies`.
- **Auto-discovery:** the production image and the state mount come from `docker service inspect jinzoopenclaw_openclaw_2026_4_2-gateway`. A volume mount is resolved through `docker volume inspect`. TypeBox defaults to `extensions/jinzo-support-ticket-creation/node_modules/typebox`.
- **Reduced config:**
  - only agent `jinzo-soporte-cliente`, keeping `model`, `name`, `identity`, and `skills`;
  - tool allowlist `read`, `jinzo_check_ticket_identity`, `jinzo_prepare_ticket_creation`, `jinzo_create_confirmed_ticket`;
  - `tools.fs.workspaceOnly=true`;
  - no channels, bindings, or hooks;
  - only the simulation plugin allowed.
- **Per turn:** it uses a fresh `docker run --rm` with a unique container name and a 300 s timeout. On timeout the container is stopped. The session key stays stable across turns.
- **Report:** printed and written to `run/report.json` (0600). It contains only fixed labels, booleans, statuses, and counts. Per turn:

| Field | Meaning |
|---|---|
| `reply_present` | the agent produced a reply |
| `asks_details` | heuristic: the reply requests missing ticket details |
| `asks_company` | the reply asks "¿Para qué empresa…?" |
| `shows_options` | the reply shows a numbered list of masked (`***`) labels |
| `options_contain_full_name` | safety alarm: a line with "(empresa)" has no mask |
| `shows_summary` | the reply contains the ticket summary |
| `mentions_ticket_ref` | the reply mentions `SIMULADO-0000` |
| `mentions_pending` | the reply mentions `SIMULADO-PEND-0000` |
| `asks_secret` | the reply mentions a password, key, token, or URL (noisy, for review) |
| `tool_calls` | `[{tool, status}]` from the event log for that turn |
| `runner_failed` | the container failed or timed out |

  The report also has `final_outcome` (the last tool status), `cleanup_ok`, and a `limitations` string.
- **`--show-replies`:** also prints the agent replies, masking any numeric span with 6 or more digits, including formatted phone numbers. This is **not** full anonymization: names can remain.
- **Cleanup:** the copied `.env`, the agent auth directory, and the sender copy are deleted with path-checked removal, even on failure. Transcripts, `events.jsonl`, and `report.json` remain private in the run directory.

### 3.4 Scenarios: `work/jwts/harness/scenarios/`

A scenario is JSON with a name and synthetic user turns only: `{"name": str, "turns": [str, ...]}`. The limits are 1–100 turns of at most 10,000 characters each.

| File | Turns | Purpose |
|---|---|---|
| `complete_details.json` | full request → `Sí, crear ticket` | single-customer happy path |
| `ask_once_no_more.json` | minimal request → `No tengo más datos` → confirm | ask-once rule and `No informado` filling |
| `bad_confirmation.json` | request → `no tengo más datos` → `dale creálo` | a wrong confirmation must not create |
| `ambiguous_with_company.json` | full request → `La empresa es <EMPRESA>.` → confirm | company-hint path; edit `<EMPRESA>` in a private copy |
| `ambiguous_no_company.json` | minimal request → `no sé, no tengo más datos` → confirm | pending identification |
| `ambiguous_choose_contact.json` | request → `1. Probé dos veces…` → confirm | masked contact selection |
| `ambiguous_choose_invalid.json` | request → `9` → confirm | out-of-range choice → pending |

**Scenario length.** A two-turn scenario (request → confirm) only completes when the agent does not need to ask anything, which is the single-customer case with full details. For ambiguous numbers use a three-turn scenario.

---

## 4. Expected outcomes by phone type

| Phone situation in central Odoo | Expected conversation | `final_outcome` |
|---|---|---|
| One customer (one or several contacts of the same company) | No list, no company question; ask once for missing details; summary; confirm | `simulated_created` |
| Several companies, 2–5 matching contacts, user picks a valid number | Masked numbered list in the single request; summary; confirm | `simulated_created` |
| Several companies, user names a company that matches exactly (normalized name or whole-hint 11-digit CUIT) | Single request; summary; confirm | `simulated_created` |
| Several companies, choice/hint invalid or missing | Single request; summary; confirm | `simulated_pending_identification` |
| Number not registered | Summary; confirm | `simulated_pending_identification` |
| Resolver/transport error, saturation (≥20 rows), timeout | — | `unavailable` |
| Confirmation not exactly accepted | Agent asks for the exact phrase; no create | `confirmation_required` |

**Conversation invariants to check in every run:**

- `jinzo_check_ticket_identity` is called first.
- At most **one** details request is made.
- Prepare is called on the user's next reply.
- Missing fields become `No informado`, and nothing is invented.
- No credentials or URLs are requested.
- No unmasked customer names, contact ids, or counts appear.
- Create is only called after an exact confirmation in a later turn.

---

## 5. How to run (operator, on the VPS as root)

```bash
cd /root/jwts-src/jwts

# Private sender file (never as a CLI argument, scenario, or chat)
install -m 0600 /dev/null /root/jinzo-sender
IFS= read -r -s -p 'WhatsApp sender (549XXXXXXXXXX): ' n; printf '%s\n' "$n" > /root/jinzo-sender; unset n; echo

# Private scenario copy (edit <EMPRESA> here if needed)
install -m 0600 harness/scenarios/ask_once_no_more.json /root/jinzo-scenario.json

python3 harness/run_sim.py --scenario /root/jinzo-scenario.json --sender-file /root/jinzo-sender --show-replies
```

Run artifacts are under `/root/.jinzo-sim/run-<UTC>-<rand>/`: `report.json`, `state/sim/events.jsonl`, and the session transcripts. `cleanup_ok` must be `true`.

**Updating the simulator from the local checkout:**

```bash
cd work && COPYFILE_DISABLE=1 tar czf - --exclude '.run-*' --exclude '__pycache__' jwts \
  | ~/.local/bin/ssh-jinzo-vps 'tar xzf - -C /root/jwts-src'
```

---

## 6. Tests

Run locally. No Docker, network, SDK, or credentials are needed:

```bash
node --test work/jwts/plugin/tests/*.test.mjs                                   # 19 tests
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=work/jgtf-5p/runtime:work/jwts/runtime \
  python3 -m unittest discover -s work/jwts/runtime/tests -v                    # 10 tests
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s work/jwts/harness/tests -v   # 17 tests
```

| Suite | Covers |
|---|---|
| Plugin | schema parity; production descriptions; confirmation normalization (accepted/rejected variants, quotes, suffixes, multiline, Unicode spaces); same-turn rejection; non-empty create params rejected; single consumption; hint/choice storage outside the draft; options validation and privacy; the model view hides `simulation` |
| Runtime | no write RPC (guarded `execute_kw`); precedence choice → hint → pending; ambiguous and unknown mapping; sender file 0600/no-follow; no `tenant_id` |
| Harness | input permission/symlink rejection; report redaction (formatted phones masked, `10 minutos` kept); cleanup path safety; indicators; scenario presence |

---

## 7. Requirements checklist (to replicate in another system)

1. **Real policy, fake edges.** Use the production agent definition, workspace, skills, and model. Replace only the inbound channel, the confirmation hook, and the final write.
2. **Isolation.** Use a throwaway container from the production image, a copied minimal state, no production config/sessions/pending stores, read-only mounts for runtime/credentials/system config, no host network, no Docker socket, and the production uid.
3. **Tool parity.** Same tool names, schemas, and model-facing descriptions. The model must not be able to tell it is a simulation.
4. **Real identity, no writes.** Resolve with the production read-only resolver against the real directory. Build the real payload. Structurally forbid every write RPC and prove it in tests.
5. **Harness-owned confirmation.** Only a later turn written by the harness, with an exact accepted whole message, unlocks create. Pending state is consumed once.
6. **Privacy.** Phone input only via 0600 non-symlink files. Reports contain booleans/statuses/counts only. Optional reply printing masks formatted phone numbers. Copied secrets are removed after each run.
7. **Observable outcome.** For every turn report which tools ran and their statuses, whether the agent asked for details, the company, or a choice, whether it showed a summary, and the final outcome.
8. **Stated limitations.** The report must say that trusted-inbound, TTL, and replay gating, and real ticket writes, are not covered.

---

## 8. Known gaps and observed issues

- **Policy adherence varies between runs.** In some runs the model asked for details twice or filled a field instead of writing `No informado`. Repeat a scenario several times before drawing conclusions. A code-enforced ask-once is proposed but not implemented.
- **Masked labels are generated per contact, but the model retypes them.** One run altered a label. The proposed fix is a system-rendered list. Also, `&` is currently masked as `&***`.
- **Heuristics are indicators.** `asks_details`, `asks_secret`, and the other per-turn indicators are keyword-based, so read the replies (`--show-replies`) when they look wrong.
