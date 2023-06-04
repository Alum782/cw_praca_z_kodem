"""
text
"""

from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    """tekst2"""
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=Damian):
    """tekst3"""
    return render_template('hello.html', name=name)
