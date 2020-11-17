from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
# from kivy.uix.properties import StringProperty

# Builder.load_file('weather.kv')

class HomeScreen(Screen):
    # city_name = StringProperty()
    # county_name = StringProperty()
    # temp_c = StringProperty()
    # weather_text = StringProperty()
    # is_day = StringProperty()
    # def search(self):
    #     try:
    #         apikey = f"https://api.weatherapi.com/v1/current.json?key=a5b634c8339b46b5a60161317203110&q={city.get()}"

    #         api_request = requests.get(apikey)
    #         api_response = json.loads(api_request.content)

    #         city_name = f"{api_response['location']['name']}"
    #         country_name = f"{api_response['location']['country']}"
    #         temp_c =f"{api_response['current']['temp_c']}" 
    #         img_url = f"http:{api_response['current']['condition']['icon']}"
    #         weather_text = f"{api_response['current']['condition']['text']}"
    #         is_day = f"{api_response['current']['is_day']}"
    #     except Exception as e:
    #         print(e)
    pass


class WeatherApp(MDApp):
    def __init__(self):
        super().__init__()
        Window.size = (350,600)

if __name__ == "__main__":
    WeatherApp().run()