# pelicanconf.py

AUTHOR = "Matteo Gätzner"
SITENAME = "Matteo Gätzner – Blog & Portfolio"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "en"

# Tell Pelican where to find “pages”
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["articles"]

# Ensure pretty URLs for pages:
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DEFAULT_PAGINATION = 10
THEME = "themes/pelican-alchemy/alchemy"
THEME_CSS_OVERRIDES = ["theme/css/oldstyle.css"]
SITESUBTITLE = "Projects, insights & thoughts"
SITEIMAGE = "/images/header.jpg"
DESCRIPTION = "The personal blog & portfolio of Matteo Gätzner"

ICONS = [
    ("github", "https://github.com/MatteoGaetzner"),
    ("linkedin", "https://linkedin.com/in/matteo-g"),
]

BOOTSTRAP_CSS = (
    "https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/solar/bootstrap.min.css"
)
PYGMENTS_STYLE = "monokai"
HIDE_AUTHORS = True

# Math
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]
RENDER_MATH = True

MATH_JAX = {
    "responsive": True,
    "process_summary": True,
    "tex_extensions": ["AMSmath.js", "AMSsymbols.js"],
}

MARKDOWN = {
    "extensions": [
        "codehilite",
        "extra",
        "mdx_math",  # ← this preserves $…$ and \(...\) math blocks
        "toc",
    ],
    "extension_configs": {
        "mdx_math": {},  # no extra options needed
    },
    "output_format": "html5",
}

STATIC_PATHS = ["files", "images"]
