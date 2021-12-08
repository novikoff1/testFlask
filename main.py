from flask import Flask

app = Flask(__name__)


@app.route("/requirements/")
def index():
    f = open('requirements.txt', 'r')
    g = f.read()
    return g


if __name__ == '__main__':
    app.run()
