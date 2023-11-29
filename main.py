#1
import requests
def get_joke():
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for any errors in the response
        joke_data = response.json()  # Parse the JSON data
        joke_text = joke_data["value"]  # Extract the joke text
        return joke_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Chuck Norris joke: {e}")
        return None

def main():
    joke = get_joke()
    if joke:
        print(joke)

if __name__ == "__main__":
    main()

#2
import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_info(api_key, city_name):
    api_url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        return description, temperature_celsius
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather information: {e}")
        return None, None

def main():
    api_key = "486e354d94a859e9457d52e57ab9b11c"
    city_name = input("Enter the name of a municipality: ")

    description, temperature = get_weather_info(api_key, city_name)

    if description is not None and temperature is not None:
        print(f"{city_name}: weather is {description}, temperature is {temperature:.2f} °C")


if __name__ == "__main__":
    main()
