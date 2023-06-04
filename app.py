from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='Damian'):
    return render_template('hello.html', name=escape(name))

if __name__ == '__main__':
    app.run(port=5000)
