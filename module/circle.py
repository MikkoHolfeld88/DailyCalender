from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class CircleApp(App):

    def build(self):
        return Builder.load_file("kv\\circle.kv")

CircleApp().run()
