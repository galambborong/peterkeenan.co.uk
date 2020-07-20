import sys

from flask import Flask, render_template, abort, jsonify
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import jinja2


from model import *

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"


app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
pages = FlatPages(app)
freezer = Freezer(app)


@app.route("/index")
@app.route("/home")
@app.route("/")
def landing_page():
    return render_template("home.html")


@app.route("/emailme/")
def contact_page():
    return render_template("emailme.html")


@app.route("/research/")
def research_page():
    return render_template("research.html", public_db=dba, other_db=dbb)


@app.route("/music/")
def music_page():
    return render_template("music.html")


@app.route('/music/repertoire')
def rep_list():
    return render_template("replist.html", repertoire_db=dbe)

@app.route("/engraving/")
def engraving_page():
    return render_template("engraving.html", engraving_db=dbc)


@app.route("/aboutsite/")
def aboutsite_page():
    return render_template("aboutsite.html")


@app.route("/dev/")
def coding_page():
    return render_template("coding.html")


@app.route("/blog/")
def blog_page():
    return render_template("blog.html", blog_db=dbd)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)
