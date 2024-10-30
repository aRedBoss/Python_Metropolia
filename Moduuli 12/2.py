import requests

city = input("Enter the name of the city: ")

api_key = "785d33b81003cb7269fa3658e8e8b85f" 
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    weather = response.json()

    weather_description = weather["weather"][0]["description"]
    temperature_kelvin = weather["main"]["temp"]
    
    temperature_celsius = temperature_kelvin - 273.15
    print(f"Weather in {city}: {weather_description}")
    print(f"Temperature: {temperature_celsius:.2f}°C")
else:
    print("Failed to retrieve weather information. Please check the city name and try again.")
