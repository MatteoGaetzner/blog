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
# THEME = "themes/pelican-alchemy/alchemy"
THEME = "theme"
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
# PLUGIN_PATHS = ["pelican-plugins"]
# PLUGINS = ["render_math"]
# RENDER_MATH = False

# MATH_JAX = {
#     "responsive": True,
#     "process_summary": True,
#     "tex_extensions": ["AMSmath.js", "AMSsymbols.js"],
#     "MathJax_font": "sanserif",
# }
STATIC_PATHS = ["images", "files", "extras"]

EXTRA_PATH_METADATA = {
    "extras/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extras/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extras/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extras/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extras/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extras/favicon.ico": {"path": "favicon.ico"},
    "extras/manifest.json": {"path": "manifest.json"},
    "extras/CNAME": {"path": "CNAME"},
}
RFG_FAVICONS = True

# Code
PYGMENTS_STYLE = "default"
