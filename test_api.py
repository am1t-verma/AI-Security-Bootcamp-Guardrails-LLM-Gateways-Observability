import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env file load karo

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Sirsa"  # ya koi bhi city

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data["weather"][0]["description"])  # e.g. "clear sky"
print(data["main"]["temp"])               # e.g. 32.5 (°C)

print(f"Real Data :\n{data}")