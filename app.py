import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        if not API_KEY:
            error = "Weather API key is not configured. Please add it to the .env file."
        else:
            city = request.form["city"]
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            try:
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    weather = {
                        "city": data["name"],
                        "temperature": data["main"]["temp"],
                        "humidity": data["main"]["humidity"],
                        "description": data["weather"][0]["description"]
                    }
                elif response.status_code == 404:
                    error = "City not found!"
                else:
                    error = "Unable to get weather data. Please check your API key and try again."
            except requests.RequestException:
                error = "Could not connect to the weather service. Please try again."

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
