import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/build')
def build():
    return render_template('build.html')

@app.route('/think')
def think():
    return render_template('think.html')

@app.route('/share')
def share():
    return render_template('share.html')

if __name__ == "__main__":
    app.run(debug=True)
