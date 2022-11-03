#!/usr/bin/env python3

# fmt: off
from decouple import config
from pathlib import Path
from sanic import Sanic
# fmt: on

# env vars (hierachy: args, env, .env)
PORT = config("APP_SERVICE_PORT", default='8000', cast=int)

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
