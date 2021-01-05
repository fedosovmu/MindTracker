import config
config.set_config()
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class MindTrackerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_file('mind_tracker.kv')
        return Builder.load_file('mind_tracker.kv')


if __name__ == '__main__':
    MindTrackerApp().run()
