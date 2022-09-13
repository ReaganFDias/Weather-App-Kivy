from kivy.app import App 
from kivy.uix.image import Image 
from kivy.uix.boxlayout import BoxLayout 

class LocationPageLayout(BoxLayout):
    pass

class Location(App):
    def build(self):
        return LocationPageLayout()

if __name__ == "__main__":
    Location().run()