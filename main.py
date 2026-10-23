from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class MayraApp(App):
def build(self):
self.title = "Mayra!"
Window.clearcolor = (0.96, 0.90, 0.96, 1)

    return Label(
        text="Mayra!\n\nYour journey starts here!",
        font_size="26sp",
        color=(0.35, 0.10, 0.35, 1),
        halign="center",
        valign="middle"
    )

if name == "main":
MayraApp().run()
