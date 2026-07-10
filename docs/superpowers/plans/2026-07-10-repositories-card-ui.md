# Repositories Card UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore the `/repositories/` page so GitHub cards look clean and do not collapse into oversized badge fragments when `github-readme-stats` fails.

**Architecture:** Keep the existing al-folio-derived Jekyll page structure and `github-readme-stats` image cards as the primary rendering path. Replace the current broken `shields.io` fallback with a local HTML/CSS fallback card that appears only after an image load error. Style the fallback in the existing repository Sass section so the change stays scoped.

**Tech Stack:** Jekyll, Liquid includes, Sass in `_sass/_base.scss`, Bootstrap utility classes already used by the site, Font Awesome already loaded by the theme.

## Global Constraints

- No new dependencies.
- Do not migrate the site to the latest al-folio structure.
- Do not change `_data/repositories.yml` repo/user lists in this task.
- Preserve `/repositories/` route, page title, nav order, and existing section headings.
- Keep `github-readme-stats` as the primary card source.
- Use a local fallback only when the external stats images fail to load.
- Commit with the repository's Lore commit protocol.

---

## File Structure

- Modify `_includes/repository/repo.html`: render one repository card, keep the external stats image path, and provide the local fallback markup for repositories.
- Modify `_includes/repository/repo_user.html`: render one GitHub profile card, keep the external stats image path, and provide the local fallback markup for user profiles.
- Modify `_sass/_base.scss`: style fallback cards under the existing `// Repositories` section.
- Do not modify `_pages/repositories.md`: the page already loops over users and repositories correctly.
- Do not modify `_data/repositories.yml`: content selection is separate from this UI repair.

---

### Task 1: Replace Broken Badge Fallback Markup

**Files:**
- Modify: `_includes/repository/repo.html`
- Modify: `_includes/repository/repo_user.html`

**Interfaces:**
- Consumes: `include.repository` as `owner/name`; `include.username` as a GitHub username; existing `site.repo_theme_light`, `site.repo_theme_dark`, and `site.data.repositories.github_users`.
- Produces: `.repo-card`, `.repo-card-link`, `.repo-card-fallback`, `.repo-card-fallback-body`, `.repo-card-icon`, `.repo-card-label`, `.repo-card-title`, and `.repo-card-footer` classes for Task 2 styling.

- [ ] **Step 1: Replace `_includes/repository/repo.html` with repository card markup**

Use this complete file content:

```liquid
{% assign repo_url =  include.repository | split: '/' %}

{% if site.data.repositories.github_users contains repo_url.first %}
  {% assign show_owner = false %}
{% else %}
  {% assign show_owner = true %}
{% endif %}

<div class="repo repo-card p-2">
  <a class="repo-card-link" href="https://github.com/{{ include.repository }}">
    <img class="repo-img-light w-100" alt="{{ include.repository }}" src="https://github-readme-stats.vercel.app/api/pin/?username={{ repo_url.first }}&repo={{ repo_url.last }}&theme={{ site.repo_theme_light }}&show_owner={{ show_owner }}" onerror="this.closest('.repo-card').classList.add('repo-card-error');">
    <img class="repo-img-dark w-100" alt="{{ include.repository }}" src="https://github-readme-stats.vercel.app/api/pin/?username={{ repo_url.first }}&repo={{ repo_url.last }}&theme={{ site.repo_theme_dark }}&show_owner={{ show_owner }}" onerror="this.closest('.repo-card').classList.add('repo-card-error');">
    <div class="repo-card-fallback">
      <div class="repo-card-fallback-body">
        <i class="fab fa-github repo-card-icon" aria-hidden="true"></i>
        <div>
          <div class="repo-card-label">Repository</div>
          <div class="repo-card-title">{{ include.repository }}</div>
        </div>
      </div>
      <div class="repo-card-footer">View on GitHub</div>
    </div>
  </a>
</div>
```

- [ ] **Step 2: Replace `_includes/repository/repo_user.html` with profile card markup**

Use this complete file content:

```liquid
<div class="repo repo-card p-2">
  <a class="repo-card-link" href="https://github.com/{{ include.username }}">
    <img class="repo-img-light w-100" alt="{{ include.username }}" src="https://github-readme-stats.vercel.app/api/?username={{ include.username }}&theme={{ site.repo_theme_light }}&show_icons=true" onerror="this.closest('.repo-card').classList.add('repo-card-error');">
    <img class="repo-img-dark w-100" alt="{{ include.username }}" src="https://github-readme-stats.vercel.app/api/?username={{ include.username }}&theme={{ site.repo_theme_dark }}&show_icons=true" onerror="this.closest('.repo-card').classList.add('repo-card-error');">
    <div class="repo-card-fallback">
      <div class="repo-card-fallback-body">
        <i class="fab fa-github repo-card-icon" aria-hidden="true"></i>
        <div>
          <div class="repo-card-label">GitHub Profile</div>
          <div class="repo-card-title">{{ include.username }}</div>
        </div>
      </div>
      <div class="repo-card-footer">View profile</div>
    </div>
  </a>
</div>
```

- [ ] **Step 3: Build the site to verify Liquid compiles**

Run:

```bash
bundle exec jekyll build
```

Expected: command exits `0`. Existing Imagemagick/Sass deprecation warnings may appear; the task fails only if Jekyll exits non-zero.

- [ ] **Step 4: Verify generated repositories HTML has local fallback markup**

Run:

```bash
rg -n "repo-card-fallback|repo-card-error|View on GitHub|View profile" _site/repositories/index.html
```

Expected: output includes all four strings: `repo-card-fallback`, `repo-card-error`, `View on GitHub`, and `View profile`.

- [ ] **Step 5: Commit Task 1**

Run:

```bash
git add _includes/repository/repo.html _includes/repository/repo_user.html
git commit -m "Restore repository cards with local fallback markup" \
  -m "Constraint: keep github-readme-stats as the primary card source and avoid new dependencies" \
  -m "Rejected: shields.io badge fallback | it renders as fragmented badges instead of cards" \
  -m "Confidence: high" \
  -m "Scope-risk: narrow" \
  -m "Directive: keep repository UI fixes scoped to repository includes and styles" \
  -m "Tested: bundle exec jekyll build; fallback markup present in _site/repositories/index.html" \
  -m "Not-tested: browser visual rendering before Sass fallback styles are added"
```

Expected: commit succeeds with only the two include files staged.

---

### Task 2: Style Fallback Cards

**Files:**
- Modify: `_sass/_base.scss`

**Interfaces:**
- Consumes: classes emitted by Task 1: `.repo-card`, `.repo-card-link`, `.repo-card-error`, `.repo-card-fallback`, `.repo-card-fallback-body`, `.repo-card-icon`, `.repo-card-label`, `.repo-card-title`, `.repo-card-footer`.
- Produces: stable desktop and mobile fallback card layout with no badge fragments and no layout collapse.

- [ ] **Step 1: Replace the current `// Repositories` Sass block**

Find the existing block:

```scss
// Repositories

@media (min-width: 768px) {
  .repo {
    max-width: 50%;
  }
}
```

Replace it with:

```scss
// Repositories

.repositories {
  gap: 0.75rem 0;
}

.repo {
  width: 100%;
}

.repo-card-link {
  color: var(--global-text-color);
  display: block;

  &:hover {
    color: var(--global-text-color);
    text-decoration: none;
  }
}

.repo-card-fallback {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--global-divider-color);
  border-radius: 6px;
  display: none;
  min-height: 140px;
  padding: 1rem;
  text-align: left;
}

.repo-card-error {
  .repo-img-light,
  .repo-img-dark {
    display: none !important;
  }

  .repo-card-fallback {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}

.repo-card-fallback-body {
  align-items: flex-start;
  display: flex;
  gap: 0.75rem;
}

.repo-card-icon {
  color: var(--global-theme-color);
  font-size: 1.75rem;
  line-height: 1;
  margin-top: 0.15rem;
}

.repo-card-label {
  color: var(--global-text-color-light);
  font-size: 0.85rem;
  margin-bottom: 0.25rem;
}

.repo-card-title {
  color: var(--global-text-color);
  font-size: 1rem;
  font-weight: 500;
  overflow-wrap: anywhere;
}

.repo-card-footer {
  border-top: 1px solid var(--global-divider-color);
  color: var(--global-theme-color);
  font-size: 0.9rem;
  margin-top: 1rem;
  padding-top: 0.75rem;
}

@media (min-width: 768px) {
  .repo {
    max-width: 50%;
  }
}
```

- [ ] **Step 2: Build the site to verify Sass compiles**

Run:

```bash
bundle exec jekyll build
```

Expected: command exits `0`. Existing Imagemagick/Sass deprecation warnings may appear; the task fails only if Jekyll exits non-zero.

- [ ] **Step 3: Verify generated CSS includes fallback styles**

Run:

```bash
rg -n "repo-card-fallback|repo-card-error|repo-card-footer" _site/assets/css/main.css
```

Expected: output includes selectors for `.repo-card-fallback`, `.repo-card-error`, and `.repo-card-footer`.

- [ ] **Step 4: Verify the broken badge markup is gone**

Run:

```bash
rg -n "img.shields.io|Followers|Forks for|Stars for" _includes/repository _site/repositories/index.html
```

Expected: no matches.

- [ ] **Step 5: Commit Task 2**

Run:

```bash
git add _sass/_base.scss
git commit -m "Style repository fallback cards" \
  -m "Constraint: use existing Sass and theme variables without adding JavaScript or dependencies" \
  -m "Rejected: badge-based fallback styling | it cannot match the al-folio card layout cleanly" \
  -m "Confidence: high" \
  -m "Scope-risk: narrow" \
  -m "Directive: keep fallback cards visually close to the existing repository card footprint" \
  -m "Tested: bundle exec jekyll build; fallback styles present in _site/assets/css/main.css; shields fallback removed" \
  -m "Not-tested: live production deployment rendering"
```

Expected: commit succeeds with only `_sass/_base.scss` staged.

---

### Task 3: Browser Visual Verification and Push

**Files:**
- No source file changes expected.

**Interfaces:**
- Consumes: Task 1 markup and Task 2 Sass.
- Produces: final verification evidence and pushed `origin/master`.

- [ ] **Step 1: Serve the generated site locally**

Run:

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Expected: server starts and prints a local URL containing `http://127.0.0.1:4000/`.

- [ ] **Step 2: Inspect normal `/repositories/` rendering**

Open:

```text
http://127.0.0.1:4000/repositories/
```

Expected: when `github-readme-stats` works, the page shows the usual al-folio GitHub stats cards, not the local fallback cards.

- [ ] **Step 3: Inspect failure fallback rendering**

In the browser devtools Network tab, block this host:

```text
github-readme-stats.vercel.app
```

Reload:

```text
http://127.0.0.1:4000/repositories/
```

Expected: each user/repository item appears as one clean local card with GitHub icon, type label, title, and footer text. No large `shields.io` badges appear. No text overlaps. Desktop keeps two columns for repository cards. Mobile width stacks to one column.

- [ ] **Step 4: Stop the local server**

Press:

```text
Ctrl-C
```

Expected: server exits cleanly.

- [ ] **Step 5: Confirm working tree only contains intended tracked changes**

Run:

```bash
git status --short --branch
```

Expected: branch is `master...origin/master`; tracked working tree is clean after Task 1 and Task 2 commits. The existing untracked `.omc/` directory may still appear and must not be committed.

- [ ] **Step 6: Push commits**

Run:

```bash
git push origin master
```

Expected: push succeeds and updates `origin/master`.

---

## Self-Review

- Spec coverage: The plan fixes the screenshot regression, follows al-folio's existing `github-readme-stats` card pattern, preserves the repositories page structure, avoids new dependencies, and adds graceful local fallback.
- Placeholder scan: No banned placeholder phrases, vague error handling, unnamed test steps, or undefined interfaces remain.
- Type consistency: The Sass classes consumed in Task 2 exactly match the classes produced in Task 1.
