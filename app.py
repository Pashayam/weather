from flask import Flask, request
import requests
import os

app = Flask(__name__)


@app.route("/")
def simple():
    url_current = os.environ.get('URL_CURRENT', 'http://api.worldweatheronline.com/premium/v1/weather.ashx')
    city_ = request.args.get('city')
    dt_ = request.args.get('dt')
    try:
        res = requests.get(url_current + "?key=78c2e75b56bb470ba2c134223200310&q="
                           + city_ + "&date=" + dt_ + "&num_of_days=1&format=json")
        data = res.json()
    except Exception:
        return "No"
    return ("City: " + str(data['data']['request'][0]['query'])
            + "\tDate: " + str(data['data']['weather'][0]['date'])
            + "\tTemperature: " + str(data['data']['weather'][0]['avgtempC']))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
