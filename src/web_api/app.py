from flask import Flask, render_template
from flask_bootstrap import Bootstrap

"""This program is base flask application."""

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    """This function is running when user access index.html"""
    cont = """Some content"""

    return render_template("index.html", cont=cont)


if __name__ == "__main__":
    """This programs entry point"""
    app.run()
