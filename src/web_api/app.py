from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    cont = """Some content"""

    return render_template("index.html", cont=cont)


if __name__ == "__main__":
    app.run()
