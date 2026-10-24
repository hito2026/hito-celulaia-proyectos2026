# Agent capabilities: portfolio and simulator reference
Branch: docs/capacidades-agentes, from main 7b9fc8e. Publish two capability lines and the supplied simulator guide; update Odoo references.
Forecast: about 390 authored lines (264-line supplied document plus short portfolio/navigation additions). Passive docs; existing unittest/site checks and deployment/Odoo readback.

## Specs
S1. "si actualizala."
S2. Approved preceding proposal: "Propongo agregar una sección **“Capacidades transversales para agentes”**" covering MAPE-K supervision/audit/alerts and research→scope→design→implementation, and Testing simulation/repeatable/regression tests with J1 simulator reference and task links 39776/39777.
S3. Approved preceding proposal: "Las presentaría como capacidades que pueden servir a varios agentes, **sin convertirlas todavía en proyectos independientes ni afirmar que la implementación comenzó**."
S4. Approved preceding proposal: "La actualización sería:\n1. Modificar el plan director en el repositorio.\n2. Publicarlo para que se actualice la web desde esa misma fuente.\n3. Renovar la copia del plan en la tarea **39774**."
S5. "Además te pido que subas el archivo: Documento local de referencia: /Users/asartorio/Ale/hito/ia/j1-cliente/docs/jinzo-whatsapp-ticket-simulator.md asi desde ahi se lo puede referenciar en al tarea para que los usuarios tengan acceso"

## Tasks
T1 | S1-S5 | inline: inspect exact source, public suitability and repository state | done | evidence: source264lines/18520bytes; no customer data or actual credentials observed
T2 | S1-S5 | delegated (context backstop): update plan/navigation and add full simulator reference with source-context notice | done (structural checks passed) | commit: publication unit pending
T3 | S1-S5 | inline: publish to main/Pages, verify served content, renew Odoo39774 snapshot and add public guide reference to39777 | in_progress | commit: publication evidence pending

## Log
L1. Original request: "si actualizala. Además te pido que subas el archivo: Documento local de referencia: /Users/asartorio/Ale/hito/ia/j1-cliente/docs/jinzo-whatsapp-ticket-simulator.md asi desde ahi se lo puede referenciar en al tarea para que los usuarios tengan acceso"
L2. Read entire explicitly authorized external source. It documents simulator implementation and operator commands, not actual secrets or real customer values. Publish guide only, no code/credentials/state/transcripts. Do not execute its operational commands or claim source implementation validated. Code paths and tests described belong to source project, not this portfolio repo; add a clear provenance/context notice without changing original body.
L3. Current public main7b9fc8e. Prior proposal remains on separate branch docs/j1-casos-diagnostico (af06883); do not merge it implicitly. Preserve user-owned untracked plan_directo/borrador.md, never stage/modify it.
L4. Two current Odoo tasks:39776 MAPE-K,39777 Testing; project378 IA Interna, stage1058 T.Agentes, tag388 Agentes. No assignees/deadlines defined; leave them unchanged. Copy of plan in39774 is dated snapshot, not live sync. Existing sensitive dialogues must remain private and absent from public files.
L5. Public file destination docs/j1/jinzo-whatsapp-ticket-simulator.md; GitHub main URL should be the reference from plan and task39777. Existing Jekyll source is canonical plan_directo/plan_director.md; index.html supplies navigation. Tests python3 -m unittest discover -s tests -v. No meaningful behavior RED for passive documentation; structural checks plus real Pages compilation/HTTP verification apply.
L6. Engram incompatible; local tracker authoritative and mirror pending. New plan section explicitly records initial requirements while detailed scope/technical decisions remain pending. No unsupported simulator-test-count claims beyond attributing them to supplied document.
L7. Writer completed expected three surfaces. Parent checked new section and provenance, exact 18,520-byte source suffix, unique plan IDs, task links, sidebar anchor, no email pattern, and 4/4 existing tests plus diff whitespace checks. Simulator/code/SSH commands not executed; no runtime validity claimed. Parent clarified initial requirements already recorded in Odoo, detailed scope still pending.
L8. Read-only Odoo preflight: task39774 description exactly matches prior published-plan snapshot after header; expected revision2026-10-24 16:24:35. Task39777 expected revision2026-10-24 19:58:31 and old local-reference note present. Snapshot replacements will compare exact description hashes/revisions to avoid overwriting already-observable human changes. No writes before successful site publication.
L9. Native ASSESS unavailable because user-owned untracked borrador.md requires explicit selection. No reviewDue returned; no review started, no failed assessment claimed as pass, no verifier required by returned plan. Ordinary source/content/tests checks stand; preserve user file unchanged. No code/API/guard changes; documentation and one navigation link only.
