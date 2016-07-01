import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class CustomWidget(Widget):
    pass

class mySpinnerApp(App):
    def build(self):
        return CustomWidget()

if __name__ == '__main__':
    mySpinnerApp().run()