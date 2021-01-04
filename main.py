from kivy.app import App
from kivy.uix.button import Button
import config


class MindTrackerApp(App):
    def build(self):
        return Button(text='Hello World')


if __name__ == '__main__':
    config.set_config()
    MindTrackerApp().run()
