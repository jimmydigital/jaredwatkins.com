# The Infinite Unknown — Site Setup

Personal blog of Jared Watkins. Built with Hugo and deployed to jaredwatkins.com.

---

## System Dependencies

Install these once on a fresh Mac before anything else.

### Hugo Extended

Hugo Extended is required (the standard build does not support Sass compilation).

```bash
brew install hugo
```

Verify you have the extended build:

```bash
hugo version
# Should show "extended" in the output
```

### Go

Required for Hugo's module system.

```bash
brew install go
```

### Dart Sass

Required by the TeXify3 theme for SCSS compilation.

```bash
brew install sass/sass/sass
```

### Node.js

Required for PostCSS (used by TeXify3).

```bash
brew install node
```

---

## Project Setup

After cloning the repo, run these from the site root:

### Install Node dependencies

PostCSS, autoprefixer, and postcss-import are required by the TeXify3 theme's `postcss.config.js`:

```bash
npm install
```

### Download Hugo modules

```bash
hugo mod download
```

This pulls all Go module dependencies listed in `go.mod`:

| Module | Purpose |
|--------|---------|
| `github.com/michaelneuper/hugo-texify3` | Active theme (TeXify3) |
| `github.com/rootwork/hugo-module-gallery-grid` | Gallery grid shortcode (used in Projects) |

---

## Local Preview Server

### TeXify3 theme — port 1313

```bash
hugo server --configDir config-texify3
```

Uses `config-texify3/_default/hugo.toml`.

---

## Project Structure

```
.
├── config-texify3/          # Active theme config (TeXify3)
├── archetypes/
│   └── default.md           # Hugo archetype with standard frontmatter
├── assets/
│   └── css/
│       └── custom.css       # Site-wide custom CSS (loaded via baseof.html asset pipeline)
├── content/
│   ├── _index.md            # Homepage body content
│   ├── posts/               # Blog posts
│   ├── projects/            # Project pages (uses gallery shortcode)
│   └── pages/               # Static pages (about, market-info, etc.)
├── layouts-texify3/         # TeXify3 layout overrides (all theme customizations go here)
│   ├── index.html           # Homepage: recent posts + categories/tags sidebar
│   ├── _default/
│   │   ├── _markup/
│   │   │   └── render-image.html  # Goldmark image hook: resizing + float CSS classes
│   │   ├── baseof.html      # Fixes .Site.Author (removed Hugo 0.124); loads custom.css
│   │   ├── list.html        # Removes posts-only section filter so all sections work
│   │   └── rss.xml          # Fixes .Site.Author in RSS; corrects XML declaration escaping
│   ├── partials/
│   │   └── footer.html      # Fixes .Site.Author removed in Hugo 0.124
│   └── shortcodes/
│       ├── email.html       # Obfuscated mailto link (base64, JS decode on click)
│       ├── gallery.html     # Gallery override: css.Sass + page bundle resource lookup
│       └── linkcard.html    # OG preview card fetched at build time
├── static/
│   ├── .well-known/
│   │   └── openpgpkey/      # WKD (Web Key Directory) for PGP key auto-discovery
│   ├── css/                 # Static CSS (legacy; prefer assets/css/ for new styles)
│   ├── images/              # Favicons and site icons
│   └── pics/                # Header/background images
├── Templates/
│   └── Post Template.md     # Obsidian post template with Hugo frontmatter
├── go.mod                   # Hugo module dependencies
├── go.sum                   # Module checksums
└── package.json             # Node dependencies (PostCSS, autoprefixer, postcss-import)
```

---

## Known Theme Quirks & Workarounds

### TeXify3: `.Site.Author` removed in Hugo 0.124

TeXify3's templates reference `.Site.Author.name` and `.Site.Author.email` which were removed in Hugo 0.124. Overrides in `layouts-texify3/` replace all references with `.Site.Params.author`.

Affected files: `baseof.html`, `footer.html`, `rss.xml`.

### TeXify3: RSS XML declaration escaping

Go's `html/template` engine escapes the `<?xml` processing instruction to `&lt;?xml`. Fixed in `layouts-texify3/_default/rss.xml` by outputting the declaration via `safeHTML` rather than as literal text.

### TeXify3: layout isolation

The TeXify3 config mounts only `layouts-texify3/` as the layouts directory — the main `layouts/` directory is not mounted. This prevents site-wide partials from other themes from breaking the TeXify3 build.

Shared shortcodes (e.g. `email.html`, `gallery.html`, `linkcard.html`) live in `layouts-texify3/shortcodes/` so they are available under this config.

### TeXify3: Dart Sass `@import` deprecation warnings

TeXify3's own Sass files use `@import` which is deprecated in Dart Sass and will be removed in Dart Sass 3.0. These warnings come from the theme source and are not actionable. Suppressed in config via:

```toml
ignoreLogs = ['warning-goldmark-raw-html']
```

When Dart Sass 3.0 drops `@import` support, the theme author will need to update the Sass files.

### Gallery shortcode: `resources.ToCSS` removed in Hugo 0.128

The `hugo-module-gallery-grid` shortcode used `resources.ToCSS` which was removed in Hugo 0.128. Fixed in `layouts-texify3/shortcodes/gallery.html` by using `css.Sass` instead.

### TeXify3: list pages show all sections

TeXify3's default `list.html` filters `where .Data.Pages "Type" "posts"` which hides all non-blog sections. Overridden in `layouts-texify3/_default/list.html` to use `.Pages` directly so projects and other sections render correctly.

### custom.css not loaded via `customCSS` param

TeXify3 loads extra CSS via `params.customCSS = []`. Rather than listing paths there, `custom.css` is loaded directly in `baseof.html` via Hugo's asset pipeline (minified + fingerprinted):

```html
{{ with resources.Get "css/custom.css" | minify | fingerprint }}
<link rel="stylesheet" href="{{ .RelPermalink }}" ...>
{{ end }}
```

---

## Shortcodes

| Shortcode                                  | Usage                 | Notes                                                   |
| ------------------------------------------ | --------------------- | ------------------------------------------------------- |
| `{{< email "addr@example.com" "label" >}}` | Obfuscated email link | Base64-encoded, decoded on click via JS                 |
| `{{< linkcard "https://..." >}}`           | OG preview card       | Fetches OG tags at build time; cached by Hugo           |
| `{{< gallery >}}`                          | Image gallery grid    | Page bundle images; requires `hugo-module-gallery-grid` |


---

## Rebuilding After a Fresh Clone

```bash
# 1. Install system deps (Hugo Extended, Go, Dart Sass, Node) — see above
# 2. Clone the repo
git clone <repo-url> jaredwatkins-site
cd jaredwatkins-site

# 3. Install Node packages
npm install

# 4. Download Hugo modules
hugo mod download

# 5. Start the preview server
hugo server --configDir config-texify3
```
