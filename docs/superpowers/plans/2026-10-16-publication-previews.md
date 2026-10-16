# Published Article Previews Implementation Plan

> **For agentic workers:** Use the bounded parallel asset assignments below. The leader owns integration and verification.

**Goal:** Give every one of the 29 published articles an individual concept figure matching Selected work.

**Architecture:** Reuse the three existing selected-work SVGs and add 26 paper-specific SVGs. BibTeX supplies preview filenames; publication summaries supply image alternatives. Apply the existing larger preview layout to Published articles while retaining the manuscript layout.

**Tech Stack:** Jekyll, Liquid, BibTeX, YAML, SCSS, standalone SVG, Python unittest.

**Spec:** User-approved design in this conversation: all 29 published articles, dark scientific concept diagrams grounded in each abstract, with consistent sizing and mobile presentation.

## Global Constraints

- Preserve paper ordering, author lists, links, manuscript statuses, and the homepage's three selected works.
- Use 600×480 SVGs with accessible title/description, the existing dark palette, and readable labels.
- Illustrate each paper's actual study; distinguish null findings, associations, predictions, and experiments.
- Do not fabricate data, effect sizes, individual contributions, or clinical efficacy.
- No new dependencies, commits, or deployment.

## Review Focus

- All 29 records resolve to distinct, accessible images.
- Similar COVID and transcriptomics studies remain scientifically distinct.
- Labels and connectors stay inside the image at mobile and desktop sizes.
- Published-article styles leave Preprints & ongoing work unchanged.
- The three reused homepage figures and all bibliography links remain intact.

## Tasks

- [x] Add a coverage check for all 29 rendered publication previews; confirmed the expected failure (`4 != 29`) against the current page.
- [x] Methods/genomics asset lane: MR-GGI, colorectal immunity, FactorGo, regulatory hotspots, multiple phenotypes, Dupuytren disease (6 SVGs).
- [x] COVID asset lane: exome variants, genetic architecture, critical-disease WGS, coding variants, tissue regulation, IFN null finding (6 SVGs).
- [x] Transcriptomics asset lane: shared neurodegeneration, atopic dermatitis, systemic JIA, myositis, insulin resistance, PCB77, bisphenol A (7 SVGs).
- [x] Experimental biology asset lane: maternal/neonatal immunity, spider peptides, nanoparticle toxicity, APOE neurons, dopamine reprogramming, SphK2, galectin-3 (7 SVGs).
- [x] Leader integrates filenames and image alternatives; adds a Published articles layout scope, matching 280px desktop previews and stacked mobile figures; removes the replaced FactorGo asset.
- [x] Verify SVG XML, all 29 local/live assets, default and /preview builds, site tests, and whitespace checks.
- [x] Review a contact sheet of every figure and browser screenshots at desktop/tablet/mobile widths; fix issues and persist the final visual verdict.

## File Ownership

Asset lanes own only their assigned files in `assets/img/publication_preview/` and temporary metadata in `/tmp/academic-redesign-qa/`. The leader owns `_bibliography/papers.bib`, `_data/publication_summaries.yml`, `_layouts/bib.html`, `_pages/publications.md`, `_sass/_academic.scss`, `tests/test_site.py`, and this plan.

## Verification Commands

`python3 -m unittest discover -s tests -q`

`git diff --check`

`RBENV_VERSION=3.2.2 /opt/homebrew/bin/rbenv exec bundle exec jekyll build --config _config.yml,/tmp/academic-redesign-qa/local.yml`

Repeat build/tests using `--baseurl /preview` and a temporary destination. Browser checks cover 1191px, 820px, 520px, and 390px widths, all 29 images, unchanged manuscript order, and absence of overflow.


## Completion Evidence

- All 29 published records resolve to distinct 600×480 concept SVGs: three reused figures and 26 new figures, including a replacement for the old FactorGo preview.
- Default and `/preview` Jekyll builds pass; all eight site tests pass against each output. The new preview-coverage check initially failed with four figures and passes with 29.
- All 29 live SVG responses match source bytes. XML, accessible title/description references, and native browser text geometry pass.
- Before/after comparison preserves the text, order, and links of all 37 published/manuscript records. BibTeX changes are limited to preview fields.
- Independent scientific review checked all 26 new diagrams against their abstracts. For the locally truncated NICER abstract, the [primary publication](https://link.springer.com/article/10.1186/s12864-020-07012-z) verified the tool name, SNP partitioning, parallel NICE processes, and eQTL map output.
- Every figure was reviewed in contact sheets. Browser checks at 1191, 820, 520, and 390px confirm 29 loaded previews, no overflow/overlap, responsive figure widths of 280/220/360/342px, and the original manuscript layout.
- Two bottom-caption spacing issues were corrected, followed by successful text-geometry checks and fresh builds/tests. Final visual verdict: 96/100, pass.
