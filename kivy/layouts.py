from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = "10dp"

        #button 1
        b1 =Button(text="Hello, ")
        b1.pos_hint = {"x":0,"y":0}
        b1.size_hint= (0.5,1)
        b1.color = (0,0.5,0.5,1)
        b1.font_size =70
        b1.font_name ="../fonts/Lcd.ttf"
        self.add_widget(b1)

        #button 2
        b2 =Button(text="World")
        b2.pos_hint = {"x":0.5,"y":0}
        b2.size_hint= (0.5,1)
        b2.color = (0,0.5,0.5,1)
        b2.font_size =70
        b2.font_name ="../fonts/Lcd.ttf"
        self.add_widget(b2)


class LayoutApp(App):
    pass


LayoutApp().run()