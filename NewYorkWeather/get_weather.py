import requests
import csv
import os
from datetime import datetime

# Coordenadas de la ciudad (ejemplo para Nueva York)
latitude = "40.7128"   # Cambia esto según la ciudad que quieras
longitude = "-74.0060" # Cambia esto según la ciudad que quieras

# Tu clave de API de OpenWeatherMap
api_key = "86d6b5c0cc760093cf4e87ff6828e3cb"  # Coloca aquí tu clave API

# URL del API
url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

# Hacer la solicitud al API
response = requests.get(url)
data = response.json()

# Imprimir la respuesta completa para ver qué estamos recibiendo
print(data)

# Si la respuesta contiene la clave "name", continuamos con el procesamiento
if "name" in data:
    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_description = data["weather"][0]["description"]
    rain = data.get("rain", {}).get("1h", 0)  # Lluvia (si hay)
    snow = data.get("snow", {}).get("1h", 0)  # Nieve (si hay)

    # Definir el nombre del archivo CSV
    file_name = f"clima-{city_name.lower()}-hoy.csv"

    # Guardar los datos en el archivo CSV
    header = ['Fecha', 'Ciudad', 'Temperatura (°C)', 'Humedad (%)', 'Presión (hPa)', 'Descripción', 'Lluvia (mm)', 'Nieve (mm)']
    row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), city_name, temperature, humidity, pressure, weather_description, rain, snow]

    file_exists = os.path.exists(file_name)

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)  # Escribir el encabezado solo si el archivo no existe
        writer.writerow(row)

    print(f"Datos climatológicos guardados en {file_name}")
else:
    print("Error: La respuesta del API no contiene la clave 'name'. Esto puede deberse a un problema con la consulta.")
