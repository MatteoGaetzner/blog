AUTHOR = "Matteo Gätzner"
SITENAME = "Matteo Gätzner – Blog & Portfolio"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/pelican-alchemy/alchemy"
THEME_CSS_OVERRIDES = ["theme/css/oldstyle.css"]

# site header
SITESUBTITLE = "Projects, insights & thoughts"
SITEIMAGE = "/images/header.jpg"
DESCRIPTION = "The personal blog & portfolio of Matteo Gätzner"
# navigation links
LINKS = [
    ("About", "/pages/about.html"),
    ("Projects", "/categories.html"),
    ("CV", "/pages/cv.html"),
]
ICONS = [
    ("github", "https://github.com/MatteoGaetzner"),
    ("linkedin", "https://linkedin.com/in/MatteoGaetzner"),
]
# bootstrap theme (from Bootswatch)
BOOTSTRAP_CSS = (
    "https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/solar/bootstrap.min.css"
)
PYGMENTS_STYLE = "monokai"
HIDE_AUTHORS = True
