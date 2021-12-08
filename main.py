import csv
import requests
from faker import Faker
from flask import Flask, Response


class MyResponse(Response):
    pass


app = Flask(__name__)
app.response_class = MyResponse


@app.route("/requirements/")
def index():
    f = open('requirements.txt', 'r')
    g = f.read()
    return g


@app.route('/generate-users/')
def fakers():
    fake = Faker()
    lst = [fake.name() + ": " + fake.email() for _ in range(100)]
    return Response("<br>".join(lst))


@app.route('/mean/')
def param():
    height = []
    weight = []
    with open('hw.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            height += [float(row[' "Height(Inches)"']) * 2.54]
            weight += [float(row[' "Weight(Pounds)"']) * 0.454]
    mean_height = sum(height) / len(height)
    mean_weight = sum(weight) / len(weight)
    return f'Вес(кг) - = {mean_weight}, Рост(см) - = {mean_height}'


@app.route('/space/')
def cosmos():
    r = requests.get('http://api.open-notify.org/astros.json')
    x = f'Total astro : {r.json().get("number")}'
    return str(x)


if __name__ == '__main__':
    app.run(debug=True)
