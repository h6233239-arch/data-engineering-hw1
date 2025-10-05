import pandas as pd

# 📄 Чтение CSV файла, собранного в первой части
df = pd.read_csv("api_example/russia_weather_multiple.csv")

# 🌡 Средняя температура по каждому городу
print("\nСредняя температура по городам:")
print(df.groupby("city")["temperature"].mean())

# 💧 Город с максимальной влажностью
max_humidity = df.loc[df["humidity"].idxmax()]
print("\nГород с максимальной влажностью:")
print(max_humidity[["city", "humidity"]])

# 🌬 Города, отсортированные по скорости ветра (по убыванию)
print("\nГорода по скорости ветра (по убыванию):")
print(df[["city", "wind_speed"]].sort_values(by="wind_speed", ascending=False))
