# Academic Website Redesign Implementation Plan

> **For agentic workers:** Use the approved conversational design below. Execute the bounded implementation and verify it in the isolated worktree.

**Goal:** Make Junghyun's research identity, selected publications, and reusable software clear while preserving the existing Jekyll/al-folio foundation and live site.

**Architecture:** Keep Markdown, YAML, BibTeX, Liquid and Sass. Compose the existing homepage from a concise introduction, three research themes, selected work, software, and recent news. Reuse the existing bibliography renderer and repository data rather than adding another content system.

**Tech Stack:** Existing Jekyll, jekyll-scholar, Bootstrap, Sass; Python standard-library smoke tests.

**Spec:** User-approved five-section design in the September 30 conversation: introduction, research, selected work, software, and recent news.

## Global Constraints

- Work only in `junghyunJJ/academic-redesign`; do not modify the original checkout or deploy.
- Preserve the user's existing bibliography badge modifications in the draft.
- Keep factual claims grounded in the existing biography, papers and repository descriptions.
- Keep existing publications, CV PDF and repository URLs available.
- Add no product dependencies; use the current Ruby lockfile locally.
- English public content; Korean progress updates.

## Review Focus

- Navigation and research links work on small screens and with keyboard input.
- Every BibTeX entry remains accessible, including future publication years.
- Preview images have meaningful alternative text and do not crop away useful figures.
- CV links resolve to the actual PDF, and internal links work under a nonempty baseurl.
- Existing abstract controls remain functional and keyboard accessible.

### Task 1: Establish the baseline and rendered-site checks

- [x] Build the existing site with the current dependencies.
- [x] Add rendered HTML checks for navigation, bibliography preservation, image accessibility, and internal links.
- [x] Run against the baseline and confirm new research/software routes are absent.

### Task 2: Implement the approved composition

**Main ownership:** `_layouts/about.html`, `_layouts/default.html`, `_layouts/bib.html`, `_includes/header.html`, `_includes/footer.html`, `_includes/research_cards.html`, `_includes/software_cards.html`, `_sass/_academic.scss`, `assets/css/main.scss`, `_pages/about.md`, `_pages/publications.md`, `_pages/repositories.md`, `_config.yml`, bibliography metadata and preview assets.

**Bounded content ownership:** `_data/home.yml`, `_data/publication_summaries.yml`, `_pages/research.md`, `_pages/software.md`.

- [x] Add research and software pages using shared card includes.
- [x] Update the homepage and shared typography, color, navigation and spacing.
- [x] Add short summaries and truthful previews for selected existing papers.
- [x] Keep the complete bibliography ordered by year without a hard-coded year cutoff.
- [x] Build and pass the rendered-site checks.

### Task 3: Verify and leave a reviewable draft

- [x] Preview in Orca's browser at desktop and mobile sizes.
- [x] Record visual-verdict output before any subsequent visual iteration.
- [x] Check abstract controls, navigation, links, accessibility and browser errors.
- [x] Build with a nonempty baseurl and rerun internal-link checks.
- [x] Review the branch changes and verify original checkout hashes and status are unchanged.
- [x] Leave the draft and local preview available; report branch, worktree and validation.
