from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.app import App
import certifi
from kivy.clock import Clock
import requests
from kivy.app import App

class SearchPopupMenu(MDInputDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def open(self):
        super().open() 
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self,address):
        api_Key = "v_7BkFCLMczGJ8Y8yotrKIVTUBtm1gZkJOidraf-LL4"
        address = parse.quote(address)
        print("Second-->", address)
        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={0}&gen=9&apiKey={1}".format(address,api_Key)
        req = requests.get(url)
        if req != None:
            self.success(req)
        else:
            self.error(req)

    def success(self, req):
        print("Success: {}".format(req.json()))
        latitude = req.json()["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"]
        longitude = req.json()["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"]
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude,longitude)

    def error(self, req):
        print("error: {}".format(req.text))
