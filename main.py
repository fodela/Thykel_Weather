from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from datetime import date
import requests, json


class Index(Screen):
    pass

class Weather(Screen):
    pass
    



class WeatherApp(MDApp):
    def __init__(self,*args, **kwargs):
        super().__init__()
        Window.size = (350,600)
        self.location = ''

    def build(self):
        self.sm = ScreenManager()

        self.index_page = Index()
        screen = Screen(name='index')
        screen.add_widget(self.index_page)
        self.sm.add_widget(screen)

        self.weather_page = Weather()
        screen = Screen(name='weather')
        screen.add_widget(self.weather_page)
        self.sm.add_widget(screen)

        return self.sm
        
    def change_screen(self,screen_name):
        self.sm.current = screen_name
        
        
    city_name = StringProperty()
    country_name = StringProperty()
    temp_c = StringProperty()
    weather_text = StringProperty()
    is_day = StringProperty()
    img_url = StringProperty()
    humidity = StringProperty()
    wind = StringProperty()
    pressure = StringProperty()
    feels_like = StringProperty()
    uv = StringProperty()
    Today = StringProperty()
    today = date.today()
    def search(self,instance,keycode):
        if self.sm.current == 'index':
            location = self.index_page.ids.searched_city.text
        elif self.sm.current == 'weather':
            location = self.weather_page.ids.searched_city.text
        self.Today = self.today.strftime("%a, %d %b")
        try:
            apikey = f"https://api.weatherapi.com/v1/current.json?key=a5b634c8339b46b5a60161317203110&q={location}"

            api_request = requests.get(apikey)
            api_response = json.loads(api_request.content)

            self.city_name = f"{api_response['location']['name']}"
            self.country_name = f"{api_response['location']['country']}"
            temp =f"{api_response['current']['temp_c']}" 
            self.img_url = f"http:{api_response['current']['condition']['icon']}"
            self.weather_text = f"{api_response['current']['condition']['text']}"
            self.is_day = f"{api_response['current']['is_day']}"
            self.temp_c = temp[:2]
            self.humidity = f"{api_response['current']['humidity']}"
            self.wind = f"{api_response['current']['wind_mph']}"
            self.pressure = f"{api_response['current']['pressure_in']}"
            self.feels_like = f"{api_response['current']['feelslike_c']}"
            self.uv = f"{api_response['current']['uv']}"
            self.change_screen('weather')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    WeatherApp().run()