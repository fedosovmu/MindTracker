import config
config.set_config()
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = """
Screen:
    MDRaisedButton:
        text: "primary_light"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
"""

class MindTrackerApp(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        return screen


if __name__ == '__main__':
    MindTrackerApp().run()
