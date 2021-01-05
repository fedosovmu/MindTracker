import config
config.set_config()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class MindTrackerApp(App):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_file('kv_lang/mind_tracker.kv')


if __name__ == '__main__':
    MindTrackerApp().run()
