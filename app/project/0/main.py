#!/usr/bin/env python3

# fmt: off
import os
from pathlib import Path
from sanic import Sanic
# fmt: on

# env vars
if os.getenv("APP_SERVICE_PORT") is not None:
    PORT = int(os.getenv("APP_SERVICE_PORT"))
else:
    PORT = 8000

# init app
app = Sanic(__name__)

if Path("index.html").exists():
    app.static("/", "./index.html", name="index")

app.static("/", ".")


if __name__ == "__main__":
    """
    Run the server app

    dev: debug=True, auto_reload=True
    access_log: False for performance
    motd: False to hide the banner
    """

    app.run(host="0.0.0.0", port=PORT, dev=True, access_log=False, motd=False)
