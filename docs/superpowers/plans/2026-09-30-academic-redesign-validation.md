# Academic redesign validation

The first draft is isolated on `junghyunJJ/academic-redesign`. The original `master` HEAD, modified-file hashes, and working-tree status were verified unchanged.

## Implemented

- Research-first homepage, three research themes, four selected publications, three software cards, recent news, and background.
- Research and Software pages; original Publications, Repositories and CV PDF remain available.
- Complete bibliography: all 29 entries, dynamically grouped by year.
- Accessible native abstract buttons with synchronized expanded state and a skip-to-content link.
- Conceptual SVG illustrations explain research themes; they are not reproduced paper figures or quantitative results.
- Existing user badge-color changes were carried into the draft.

## Evidence

- Jekyll build passes with the existing Ruby 3.2.2 environment and lockfile.
- Six rendered-site tests pass at the root URL and with `/preview` as baseurl.
- JavaScript syntax and `git diff --check` pass.
- Browser checks: desktop and mobile show no horizontal overflow; mobile menu opens; abstract buttons open and close with correct expanded state; year headings use the intended style.
- Browser console contains no messages.
- Independent code review found no blocking draft-specific issue. Its year-heading style finding was corrected; visual review also corrected badge contrast.
- Original checkout remains intact; no push, merge, or deployment was performed.

## Reproduce the local build

The local machine has a different `convert` executable and no ImageMagick. Create an untracked override outside the repo:

```yaml
imagemagick:
  enabled: false
```

Then run:

```sh
RBENV_VERSION=3.2.2 /opt/homebrew/bin/rbenv exec bundle exec jekyll build --config _config.yml,/path/to/local.yml
python3 -m unittest discover -s tests -v
python3 -m http.server 4001 --bind 127.0.0.1 --directory _site
```

## Limits retained from the existing site

- ImageMagick optimization was excluded from local validation; the product configuration is preserved.
- Existing Sass deprecation and empty-slug warnings remain.
- An existing publication references a missing local PDF: `Text-78246-3-10-20220830.pdf`.
- Native keyboard input could not be fully exercised because the embedded browser reported no window focus. Native button semantics, mouse activation, expanded state, and the skip link were verified.
