import requests
import pandas as pd
import os
from datetime import datetime
import time

API_KEY = "a62aff81b2a622ab8182ee3376640f69"

# 🌍 Список известных городов России с координатами (lat, lon)
cities = {
    "Moscow": {"lat": 55.7558, "lon": 37.6173},
    "Saint Petersburg": {"lat": 59.9343, "lon": 30.3351},
    "Novosibirsk": {"lat": 55.0084, "lon": 82.9357},
    "Yekaterinburg": {"lat": 56.8389, "lon": 60.6057},
    "Kazan": {"lat": 55.7903, "lon": 49.1347},
    "Nizhny Novgorod": {"lat": 56.2965, "lon": 43.9361},
    "Chelyabinsk": {"lat": 55.1644, "lon": 61.4368},
    "Samara": {"lat": 53.1959, "lon": 50.1003},
    "Omsk": {"lat": 54.9893, "lon": 73.3682},
    "Rostov-on-Don": {"lat": 47.2357, "lon": 39.7015},
    "Ufa": {"lat": 54.7388, "lon": 55.9721},
    "Krasnoyarsk": {"lat": 56.0153, "lon": 92.8932},
    "Voronezh": {"lat": 51.6615, "lon": 39.2003},
    "Perm": {"lat": 58.0105, "lon": 56.2502},
    "Volgograd": {"lat": 48.7071, "lon": 44.5169},
    "Krasnodar": {"lat": 45.0393, "lon": 38.9760},
    "Saratov": {"lat": 51.5924, "lon": 45.9608},
    "Tyumen": {"lat": 57.1613, "lon": 65.5250},
    "Irkutsk": {"lat": 52.2972, "lon": 104.2966},
    "Khabarovsk": {"lat": 48.4820, "lon": 135.0830}
}

# 🌦 Функция для получения текущей погоды для одного города
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},RU&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print(f"Ошибка при получении данных для {city}: {data.get('message')}")
        return None

    # 🌐 Преобразование времени Unix в читаемый формат
    def ts_to_dt(ts):
        return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

    row = {
        "city": city,
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "wind_deg": data["wind"].get("deg"),
        "clouds": data["clouds"]["all"],
        "description": data["weather"][0]["description"],
        "datetime": ts_to_dt(data["dt"]),
        "sunrise": ts_to_dt(data["sys"]["sunrise"]),
        "sunset": ts_to_dt(data["sys"]["sunset"]),
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"]
    }
    return row

# 🔄 Функция для многократного получения данных для нескольких городов
def fetch_multiple_cities_multiple_times(cities, repetitions=3, delay=60):
    """
    repetitions: количество повторений для каждого города
    delay: задержка в секундах между измерениями
    """
    all_data = []
    for i in range(repetitions):
        print(f"\n🔄 Измерение {i+1} из {repetitions}")
        for city in cities:
            row = fetch_weather(city)
            if row:
                all_data.append(row)
        if i < repetitions - 1:
            print(f"⏳ Ждем {delay} секунд до следующего измерения...")
            time.sleep(delay)
    return pd.DataFrame(all_data)

if __name__ == "__main__":
    # 🌆 Сбор данных для всех городов 3 раза с интервалом 60 секунд
    df = fetch_multiple_cities_multiple_times(cities, repetitions=3, delay=60)

    print(df)

    # 💾 Сохранение результатов в CSV файл
    os.makedirs("api_example", exist_ok=True)
    df.to_csv("api_example/russia_weather_multiple.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Данные сохранены в api_example/russia_weather_multiple.csv")