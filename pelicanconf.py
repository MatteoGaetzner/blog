# pelicanconf.py

AUTHOR = "Matteo Gätzner"
SITENAME = "Matteo Gätzner – Blog & Portfolio"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "en"

# Tell Pelican where to find “pages”
PAGE_PATHS = ["pages"]

# Ensure pretty URLs for pages:
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# …the rest of your pelicanconf.py as-is…
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

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]

RENDER_MATH = True
