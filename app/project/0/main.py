#!/usr/bin/env python3

# fmt: off
import http.server
# from pathlib import Path
# fmt: on


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    """Basic HTTP server that serves files from the current directory."""
    http.server.test(HandlerClass=Handler)
