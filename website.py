from flask import Flask, render_template, abort, jsonify
from model import dba, dbb, dbc

app = Flask(__name__)


@app.route('/index')
@app.route('/home')
@app.route('/')
def landing_page():
    return render_template(
            'home.html'
            )

@app.route('/emailme')
def contact_page():
    return render_template(
            'emailme.html'
            )

@app.route('/research')
def research_page():
    return render_template(
            'research.html',
            public_db=dba,
            other_db=dbb
            )

@app.route('/music')
def music_page():
    return render_template(
            'music.html'
            )

@app.route('/engraving')
def engraving_page():
    return render_template(
            'engraving.html',
            engraving_db=dbc
            )

@app.route('/aboutsite')
def aboutsite_page():
    return render_template(
            'aboutsite.html'
            )
