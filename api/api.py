import flask
from forecast.rain import minutes_to_rain

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    minutes = minutes_to_rain()
    if minutes > 0:
        return "<h1 style='color: red'>Pluie dans " + str(minutes) + " minutes</h1>"
    else:
        return "<h1 style='color: green'>Pas de pluie pendant 1 heure</h1>"


app.run()
