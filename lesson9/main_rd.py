from flask import Flask
from flask import render_template_string
app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <html>
    <head>
        <title>Home Page</title>
        <style>
            body { max-width: 1200px; margin: auto; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Home Page!</h1>
    </body>
    </html>
    """
    return render_template_string(html)
@app.route("/name")
def myname():
    return "<h1>My name is Johnny.</h1>"
