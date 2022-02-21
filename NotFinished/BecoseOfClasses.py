### composition

class requests:
    @staticmethod
    def get(url):
        return {
            'temp': 5,
            'wind_speed': 5.7
        }

class WeatherByProvider:
    @classmethod

    def get_weather(cls):
        response = requests.get('http://weather.by/today')
        temp = response['temp']
        wind_speed = response['wind_speed']
        return {
            'temp': temp,
            'wind': wind_speed
        }

class WeatherRuProvider:
    @classmethod

    def get_weather(cls):
        response = requests.get('http://weather.by/today')
        temp = response['temp']
        wind_speed = response['wind_speed'] * 3.6
        return {
            'temp': temp,
            'wind': wind_speed
        }

def print_to_terminal(weather):
    print(f'Today temp: {weather["temp"]}')
    print(f'Today wind speed: {weather["wind"]}')

if __name__ == '__main__':
    weather = get_weather()
    print_to_terminal(weather=weather)