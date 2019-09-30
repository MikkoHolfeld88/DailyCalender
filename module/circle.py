from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("kv\\circle.kv")

class Circle(Widget):
    def build(this):
        pass

class CircleApp(App):

    def build(self):
        return Circle()
    
if __name__ == "__main__":
    CircleApp().run()
