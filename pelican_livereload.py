from urllib.parse import urlparse

from livereload import Server
from pelican import Pelican
from pelican.settings import read_settings

settings = read_settings("pelicanconf.py")
p = Pelican(settings)


server = Server()
server.watch(p.settings["PATH"], p.run)
server.watch(p.settings["THEME"], p.run)
server.watch("./pelicanconf.py", p.run)

host_port = p.settings.get("SITEURL") or "http://localhost:5500"
details = urlparse(host_port)
host, port = details[1].split(":")

server.serve(host=host, port=int(port), root=settings["OUTPUT_PATH"])
