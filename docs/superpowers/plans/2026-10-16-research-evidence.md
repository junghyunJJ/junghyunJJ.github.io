# Research evidence and navigation implementation plan

**Goal:** Make the research questions, verified personal contributions, and usable software resources easy to find.

**Architecture:** Extend the existing shared YAML data and Jekyll includes. Keep the current pages and bibliography renderer; use conditional metadata so unannotated publications have no empty labels.

**Tech stack:** Jekyll, Liquid, YAML, SCSS, existing Python/Node checks.

**Spec:** User-approved comparison recommendations in this conversation, October 16, 2026. Execution is explicitly authorized; clarify factual uncertainties while completing independent work.

## Constraints

- Preserve the selected-paper order: ischemic stroke, MARS, JIA.
- Preserve the six pinned software projects and their order.
- Use publisher statements for author roles and personal contributions; do not equate whole-paper results with personal ownership.
- Research remains centered on agent harnesses and contrastive alignment of clinical notes with structured EHR data.
- Keep the agent Research text free of the DeepMAST name and avoid specifying EHR encoders.
- Add only verified resource URLs; install no dependencies.
- New unpublished-work entries depend on the user's scope choice; published records remain intact.

## Tasks

- [x] Verify selected-paper author roles and individual contribution statements.
- [x] Add concise research questions on the detailed Research page.
- [x] Add conditional author-role and contribution metadata to publication cards.
- [x] Add verified software resources using the existing card renderer.
- [x] Resolve the unpublished-work scope and the stroke paper's personal contribution with the user.
- [x] Present the requested unpublished records separately with accurate status and available links.
- [x] Build, run existing tests and targeted rendered-content checks, inspect desktop/mobile screenshots, and record the visual verdict.

## Verification focus

- Metadata appears only on the publication it describes; absent fields produce no empty labels.
- Existing selected-paper order, complete published bibliography, anchors, and six software cards are preserved.
- Resources have useful labels and valid targets; base URL handling and accessible names remain correct.
- Research questions complement the existing descriptions and diagrams without changing their scientific method.
- Unpublished records are never presented as accepted/published papers or given invented dates, author roles, or paper URLs.

## Evidence

- Stroke authorship: https://academic.oup.com/hmg/article/33/2/170/7308735
- Stroke full text has no individual contribution statement: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772041/
- MARS author information: https://link.springer.com/article/10.1186/s13059-021-02353-8#author-information
- JIA author information: https://link.springer.com/article/10.1186/s13075-024-03280-2#author-information
- Software resources: literal README headings in the six public repositories, verified October 16, 2026.
- Unpublished-work list: user's JJ_CV (6).pdf, updated October 16, 2026.
- HLA preprint DOI, type, and author order verified through https://api.crossref.org/works/10.1101/2023.05.22.541750.

## Resolved decisions and validation

- The user requested all eight CV entries, then clarified that Degree-GEAR and DeepMAST are in preparation. The user subsequently chose one combined Preprints & ongoing work section: five under review, two in preparation, and one preprint. Per-record status is independent of whether a public preprint link is available.
- The user confirmed leading the stroke study narrative, analyses, figures, and manuscript writing; this statement supplies its personal-contribution field.
- Default and `/preview` Jekyll builds passed. The seven site tests and four theme tests passed, as did the site tests with the `/preview` base URL.
- Browser checks passed for four research questions, three exact selected-paper roles/contributions, twelve resource links, eight unpublished records, complete published bibliography, unique IDs, shared page content, and no horizontal overflow at 1191px and 390px.
- Independent code/rendered-output review reported no findings. Eight desktop/mobile screenshots were inspected; the visual verdict is 96/pass.

## Preprint-link follow-up

- Added the user's exact bioRxiv v1 URLs to frozen single-cell representations, cell-cell interaction genes, and PersonaAI after matching titles through the Crossref DOI API.
- DOI metadata sources: `10.64898/2026.08.31.748446`, `10.64898/2026.05.08.723913`, and `10.64898/2026.01.16.699755` at `https://api.crossref.org/works/`.
- The user chose public DOI metadata over the abbreviated CV author lists. Frozen single-cell now includes H. Kim before J. Jung; PersonaAI begins B. Cho, G.-Y. Lee, J. Jung.
- HLA remains explicitly labeled Preprint in the combined list. The existing ongoing-manuscripts anchor remains available.
- Final build and seven site tests passed. Browser checks verified eight unique records, exact supplied links, author corrections, correct individual statuses, and no horizontal overflow at 1191px and 390px. Three screenshots were inspected; visual verdict 96/pass.

## Display-order follow-up

- Display public preprints first by descending initial posting date, followed by in-preparation manuscripts and then remaining under-review works. Code is a resource link attached to its manuscript.
- Current order: frozen single-cell representations, cell-cell interaction genes, PersonaAI, HLA benchmark, Degree-GEAR, DeepMAST, SPIX, Graves' disease network diffusion.
- First-posted dates were verified through Crossref's `posted` field rather than inferred from DOI identifiers: 2026-09-04, 2026-05-12, 2026-01-20, and 2023-05-24. The page displays the month and year.
- Public preprints use a primary Preprint badge; the three under-review preprints also retain their review-state text. Individual source statuses are unchanged.
- Fixed stretched metadata labels at 520px using `align-content: flex-start`. Final browser checks passed at 1191px, 390px and 520px; all eight records remain present in the exact intended order. Build, seven site tests and whitespace checks passed; final visual verdict 96/pass.
