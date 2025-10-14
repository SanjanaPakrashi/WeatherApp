from flask import Flask, render_template, request
import requests

app = Flask(__name__)

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def fetch_weather(city):
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city}&units=metric"
    response = requests.get(complete_url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = fetch_weather(city)
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
