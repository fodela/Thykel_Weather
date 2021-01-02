from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy.properties import StringProperty, ObjectProperty
from datetime import date
import requests, json


# class Index(Screen):
#     pass

class Weather(Screen):
    pass
    
class LocationGetter(Screen):
    pass



class Thykel_WeatherApp(MDApp):
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
    current_city = StringProperty('Ho')
    current_country = StringProperty('Ghana')
    background_pic = StringProperty('images/bgpic.jpg' )

    def __init__(self,*args, **kwargs):
        super().__init__()
        Window.size = (350,600)
        self.location = ''
        self.icon = '/home/fodela/Project/Python Projects/Kivy Projects/Thykel_Weather/images/weather_icon.png'
        self.ask_current_location_dialog = None
        self.err_dialog = None
  
    def on_start(self):
        location = f"{self.current_city}, {self.current_country} "
        self.get_data(location)
        self.background_pic = 'images/bgpic.jpg'

    def ask_current_location(self):
        
        if not self.ask_current_location_dialog: 
            
            self.ask_current_location_dialog = MDDialog(
                                            title = 'Add Current Location:',
                                            type = 'custom',
                                            content_cls=LocationGetter(),
                                            size_hint = (.8,.3),
                                            buttons=[
                                                MDFlatButton(
                                                    text = 'Cancel',
                                                    on_press = lambda x: self.cancel()
                                                ),
                                                MDRaisedButton(
                                                    text = 'Add',
                                                     on_press= lambda a:self.add_location()
                                                )
                                            ]
                                            )
        self.ask_current_location_dialog.open()
        
    def search(self,instance,keycode):
        location = self.root.ids.searched_city.text
        self.get_data(location)
        
    def get_data(self,location):
        self.Today = self.today.strftime("%a, %d %b")
        try:
            apikey = f"https://api.weatherapi.com/v1/current.json?key=a5b634c8339b46b5a60161317203110&q={location}"

            api_request = requests.get(apikey)
            api_response = json.loads(api_request.content)

            self.city_name = f"{api_response['location']['name']}"
            self.country_name = f"{api_response['location']['country']}"
            self.temp_c =f"{int(api_response['current']['temp_c'])}" 
            self.img_url = f"http:{api_response['current']['condition']['icon']}"
            self.weather_text = f"{api_response['current']['condition']['text']}"
            self.is_day = f"{api_response['current']['is_day']}"
            self.humidity = f"{api_response['current']['humidity']}"
            self.wind = f"{api_response['current']['wind_mph']}"
            self.pressure = f"{api_response['current']['pressure_in']}"
            self.feels_like = f"{api_response['current']['feelslike_c']}"
            self.uv = f"{api_response['current']['uv']}"
            
        except Exception as e:
            self.error_dialog(str(e))
            print(e)
    
    def close_dialog(self):
        try:
            self.ask_current_location_dialog.dismiss(force=True)
        except Exception as e:
            print(e)

    def add_location(self):
        location = f"{self.current_city}, {self.current_country} "
        self.get_data(location)
        self.close_dialog()

    def cancel(self):
        self.close_dialog()

    def error_dialog(self,err):
        self.err_dialog = MDDialog(
                                            title = 'Error!',
                                            type = 'custom',
                                            text = err,
                                            size_hint = (.8,.3)
                                            )
        self.err_dialog.open()

if __name__ == "__main__":
    Thykel_WeatherApp().run()