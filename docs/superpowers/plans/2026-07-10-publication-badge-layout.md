# Publication Badge Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make publication category badge text black and render `Analysis (Corresponding)` as a two-line badge: `Analysis` on the first line and `(Corresponding)` on the second line.

**Architecture:** Keep bibliography metadata unchanged in `_bibliography/papers.bib`; the stored `abbr` values remain semantically intact. Add a display-only Liquid label in `_layouts/bib.html` and adjust the existing publication badge Sass in `_sass/_base.scss` so two-line badges fit without overlapping adjacent publication text.

**Tech Stack:** Jekyll, Liquid, jekyll-scholar bibliography layout, Sass in `_sass/_base.scss`.

## Global Constraints

- No new dependencies.
- Do not edit `_bibliography/papers.bib`.
- Do not change publication ordering, year grouping, titles, authors, links, abstracts, or PDF/HTML buttons.
- Badge text color must be black.
- Only `Analysis (Corresponding)` should be split into two visual lines.
- Preserve venue lookup behavior using the original `entry.abbr` value.
- Commit with the repository's Lore commit protocol.

---

## File Structure

- Modify `_layouts/bib.html`: create a display-only `abbr_label` derived from `entry.abbr`, replacing ` (Corresponding)` with `<br>(Corresponding)` while preserving the original `entry.abbr` for `site.data.venues` lookup.
- Modify `_sass/_base.scss`: update the existing `.publications ol.bibliography li .abbr abbr` style so badge text is black and two-line badges have enough vertical space.
- Do not modify `_pages/publications.md`: the page already loops through years and renders bibliography entries correctly.
- Do not modify `_bibliography/papers.bib`: the requested line break is presentational, not bibliographic metadata.

---

### Task 1: Update Publication Badge Rendering

**Files:**
- Modify: `_layouts/bib.html`
- Modify: `_sass/_base.scss`

**Interfaces:**
- Consumes: `entry.abbr` from jekyll-scholar bibliography entries.
- Produces: a display label named `abbr_label` used inside each `<abbr class="badge">`; publication badge CSS that supports black text and two-line `Analysis<br>(Corresponding)` labels.

- [ ] **Step 1: Run the current failing display check**

Run:

```bash
bundle exec jekyll build
rg -n "Analysis<br>\\(Corresponding\\)" _site/publications/index.html
```

Expected: `bundle exec jekyll build` exits `0`; the `rg` command exits `1` before implementation because the current generated HTML contains `Analysis (Corresponding)` on one line.

- [ ] **Step 2: Update `_layouts/bib.html` badge label rendering**

Find this block:

```liquid
        {%- elsif entry.abbr -%}
          {%- if site.data.venues[entry.abbr] -%}
            {%- assign venue_style = nil -%}
            {%- if site.data.venues[entry.abbr].color != blank -%}
              {%- assign venue_style = site.data.venues[entry.abbr].color | prepend: 'style="background-color:' | append: '"' -%}
            {%- endif -%}
            <abbr class="badge" {% if venue_style %}{{venue_style}}{% endif %}><a href="{{site.data.venues[entry.abbr].url}}">{{entry.abbr}}</a></abbr>
          {%- else -%}
            <abbr class="badge">{{entry.abbr}}</abbr>
          {%- endif -%}
        {%- endif -%}
```

Replace it with:

```liquid
        {%- elsif entry.abbr -%}
          {%- assign abbr_label = entry.abbr | replace: ' (Corresponding)', '<br>(Corresponding)' -%}
          {%- if site.data.venues[entry.abbr] -%}
            {%- assign venue_style = nil -%}
            {%- if site.data.venues[entry.abbr].color != blank -%}
              {%- assign venue_style = site.data.venues[entry.abbr].color | prepend: 'style="background-color:' | append: '"' -%}
            {%- endif -%}
            <abbr class="badge" {% if venue_style %}{{venue_style}}{% endif %}><a href="{{site.data.venues[entry.abbr].url}}">{{abbr_label}}</a></abbr>
          {%- else -%}
            <abbr class="badge">{{abbr_label}}</abbr>
          {%- endif -%}
        {%- endif -%}
```

- [ ] **Step 3: Update `_sass/_base.scss` publication badge styling**

Find this block inside `.publications ol.bibliography li`:

```scss
      .abbr {
        height: 2rem;
        margin-bottom: 0.5rem;
        abbr {
          display: inline-block;
          background-color: var(--global-theme-color);
          padding-left: 1rem;
          padding-right: 1rem;
          a {
            color: white;
            &:hover {
              text-decoration: none;
            }
          }
        }
        .award {
          color: var(--global-theme-color) !important;
          border: 1px solid var(--global-theme-color);
        }
      }
```

Replace it with:

```scss
      .abbr {
        min-height: 2rem;
        margin-bottom: 0.5rem;
        abbr {
          background-color: var(--global-theme-color);
          color: black;
          display: inline-block;
          line-height: 1.15;
          min-width: 4.5rem;
          padding: 0.25rem 1rem;
          text-align: center;
          white-space: normal;
          a {
            color: black;
            &:hover {
              text-decoration: none;
            }
          }
        }
        .award {
          color: var(--global-theme-color) !important;
          border: 1px solid var(--global-theme-color);
        }
      }
```

- [ ] **Step 4: Build and verify generated publications markup**

Run:

```bash
bundle exec jekyll build
rg -n "Analysis<br>\\(Corresponding\\)" _site/publications/index.html
rg -n "color: black|min-width: 4.5rem|white-space: normal" _sass/_base.scss
```

Expected:
- `bundle exec jekyll build` exits `0`.
- `rg -n "Analysis<br>\\(Corresponding\\)" _site/publications/index.html` prints at least one generated publication badge line.
- `_sass/_base.scss` contains `color: black`, `min-width: 4.5rem`, and `white-space: normal` in the publication badge block.

- [ ] **Step 5: Confirm no unintended bibliography metadata edits**

Run:

```bash
git diff -- _bibliography/papers.bib
git diff --check
```

Expected:
- `git diff -- _bibliography/papers.bib` prints nothing.
- `git diff --check` exits `0`.

- [ ] **Step 6: Commit**

Run:

```bash
git add _layouts/bib.html _sass/_base.scss
git commit -m "Improve publication category badge readability" \
  -m "Constraint: keep bibliography abbr metadata unchanged and apply the corresponding-author line break only at render time" \
  -m "Rejected: editing papers.bib labels directly | display-only formatting should stay in the layout and CSS" \
  -m "Confidence: high" \
  -m "Scope-risk: narrow" \
  -m "Directive: keep publication badge labels short and readable in the left column" \
  -m "Tested: bundle exec jekyll build; generated publications page contains Analysis<br>(Corresponding); git diff --check" \
  -m "Not-tested: manual browser screenshot comparison"
```

Expected: commit succeeds with only `_layouts/bib.html` and `_sass/_base.scss` staged.

---

## Self-Review

- Spec coverage: The plan changes badge text to black and renders `Analysis (Corresponding)` as two visual lines without changing bibliography data.
- Placeholder scan: No banned placeholder phrases, vague test instructions, or undefined interfaces remain.
- Type consistency: `abbr_label` is defined in the same Liquid branch where it is used, and CSS selectors target the existing publication badge DOM.
