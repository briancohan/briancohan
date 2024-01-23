import os

from flask import Flask, render_template, request

from .config import Config

app = Flask(__name__)

if not os.environ.get("FLASK_ENV") == "development":
    from werkzeug.middleware.proxy_fix import ProxyFix

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


app.jinja_env.globals.update(
    {
        "SITE_NAV": Config.SITE_NAVIGATION,
        "REQUEST": request,
    }
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
