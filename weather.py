# python_test.py
import requests

# Enter l'api provenant de mon compte
api_key = "f49211bbdd9e7a0f88b82613fd5c8e5c"  
complete_url = "https://openweathermap.org/api"

# completer la base url
Nom_ville = input("Bordeaux")
complete_url = base_url + "appid=" + 'f49211bbdd9e7a0f88b82613fd5c8e5c' + "&q=" + Nom_ville 
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")