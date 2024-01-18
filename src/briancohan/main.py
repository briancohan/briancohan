import os

from flask import Flask, render_template

app = Flask(__name__)

if not os.environ.get("FLASK_ENV") == "development":
    from werkzeug.middleware.proxy_fix import ProxyFix

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route("/")
def index():
    return render_template("index.html", env=os.environ.get("FLASK_ENV", "dev"))


@app.route("/about")
def about():
    return render_template("about.html")
