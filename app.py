import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/achievements')
def about():
    return render_template('achievements.html')

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

@app.route('/certification')
def certification():
    return render_template('certification.html')

@app.route('/competitions')
def competitions():
    return render_template('competitions.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()
