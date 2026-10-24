# J1 diagnostic app: evidence and proposal
Branch: docs/j1-casos-diagnostico. Deliver a public anonymous synthesis and an Odoo reference; original only with verified private access.
Forecast: under 350 authored lines; no PR requested. Checks: corpus-derived evidence, privacy scan, Markdown structure, existing site tests and Odoo readback.

## Specs
S1. "Para que me ayuds a diseñarl el proceso de los pasos te voy a pasar un documentos con todas las converaciones que pudimos rescatar de cada uno de los usuaros pra que se entiendan el tipo de consulto y para que deberíamos preparar la app de anális."
S2. "Está todo en este archivo: /Users/asartorio/Ale/hito/ia/j1-cliente/private/jinzo-dialogs/dialogs.md"
S3. "1. incluya este documento en la tareas del proyecto con un link al archivo que está guardado en el repo que estamos usando asi se puede acceder."
S4. "2. Leugo te tipo que me ayudes a definir una propuesta  de como sería la aplicacción de analisis que pretendemos hacer en esta tarea"
S5. "Tiene que ser claros. No debería haber de 5." Assumption confirmed in conversation: at most five user-facing steps.
S6. "En cada paso seguramente se necesit que el usuario pase el link concreto donde esta opernado en su instancia de Odoo y a partir de eso por ssh poder hacer el análisis en la instancia. Luego se le pedirá al usuario de conteste algunas preguntas dandole opciones y el proceso continua."
S7. "Resumen público y original adjunto privado en Odoo" (selected explicitly). Choice effects: analyze original without publishing; create an anonymous case synthesis in the public repo and link it in the task; attach original only after checking Odoo access permissions.

## Tasks
T1 | S1-S2,S4-S6 | delegated (context backstop): analyze corpus and author public cases/proposal synthesis | done (authoring and self-checks; public boundary review in T3) | commit: pending
T2 | S3,S7 | inline: inspect Odoo access and attach private original only if evidence supports restricted access; preserve task text | done | commit: remote evidence (attachment 53238) | Risk: item 2 (private customer data)
T3 | S3-S7 | inline: check/publish synthesis, add reference to Odoo 39775 and present five-step proposal | in_progress | commit: pending | Risk: item 2 (public privacy boundary)

## Log
L1. Original request: "Para que me ayuds a diseñarl el proceso de los pasos te voy a pasar un documentos con todas las converaciones que pudimos rescatar de cada uno de los usuaros pra que se entiendan el tipo de consulto y para que deberíamos preparar la app de anális.
Está todo en este archivo: /Users/asartorio/Ale/hito/ia/j1-cliente/private/jinzo-dialogs/dialogs.md
Te pido que:
1. incluya este documento en la tareas del proyecto con un link al archivo que está guardado en el repo que estamos usando asi se puede acceder.
2. Leugo te tipo que me ayudes a definir una propuesta  de como sería la aplicacción de analisis que pretendemos hacer en esta tarea"
L2. Source header marks real customer data for internal use, not Git or sharing; original is 44,361 lines and 2,017,671 bytes. Only source path above is authorized outside project. No raw dialogues, identities, credentials, private URLs, or source extracts may enter public files, tool output summaries, memory, Git, or Pages.
L3. Human chose S7 after public-repository risk disclosure. No source file has been copied. Odoo project 378 IA Interna has privacy_visibility portal; target task 39775 is J1 diagnostic web flow. Do not assume portal means anonymous public or internal-only. Original attachment requires verified restrictions; if not provable, leave original unuploaded and report exact missing authorization/proof.
L4. Proposal only, not app implementation. Keep current Odoo stages unchanged. Diagnose/recommend does not authorize production mutations. Conversation answers in source are not verified Odoo guidance or ground truth.
L5. Public artifact: docs/j1/casos-y-propuesta.md. Synthesized examples only; do not reproduce conversations, names, telephone numbers, session identifiers, client domains, database names, amounts or identifiable business details. Corpus coverage methodology and limits must be explicit. No raw scratch exports in worktree. Existing helpers: Jekyll Markdown rendering and site contract tests remain unchanged.
L6. Engram is unavailable due to incompatible installed binary. Local file is durable tracking source; memory mirror pending. Authorized original-path access does not authorize reads of adjacent private files.
L7. T1 delegated writer produced 203-line public report. Corpus structured counts: 429 sections, 3,026 user blocks, 2,746 agent blocks. Fixed-seed sample: 60 sections/442 user blocks. Lexical, overlapping family counts are explicitly not validated semantic incident coding. No attachments or client systems were examined. Parent reproduced structural/family counts and passed all four existing tests.
L8. Writer privacy scan initially failed on five token candidates; one bounded correction classified output-context occurrences as generic grammar/business terms, with no report rewrite. Parent read full report and verified no email/phone/UUID/URL patterns. No claim that regex alone proves anonymity. Independent public-boundary check remains T3.
L9. Odoo access inspection: project privacy_visibility portal; current account internal and permitted attachment create. To avoid inheriting portal-project access, original is an unattached private ir.attachment (res_id=0, no res_model, public=false, no access token), to be linked from task, restricted to creator/system administrators by standard Odoo 17 attachment rules. Standard source inspected at https://raw.githubusercontent.com/odoo/odoo/17.0/odoo/addons/base/models/ir_attachment.py . No project ACL or task stage changes.
L10. Independent verifier found no severe public-candidate blockers, reviewed entire report, confirmed zero shared normalized 12-word sequences with source and zero direct identifier patterns. Upstream attachment rule supports creator/admin restriction for unbound originals. Candidate and baseline 4/4 site tests passed. Scanner evidence does not guarantee absolute anonymity; no live custom-override guarantee claimed. ASSESS native passive, reviewDue false; item2 escalation independently verified.
L11. Private original uploaded as attachment 53238, owner uid47, public=false/token absent/unbound metadata verified; exact source byte count and SHA1 matched. Anonymous download returned404. Original never entered worktree/Git. Odoo task still unchanged at this transition; links will be added with owner/admin-access note after public report publication.
