import config
config.set_config()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from app_colors import AppColors



class MindTrackerApp(App):
    def build(self):
        Window.clearcolor = AppColors.Dark
        self.screen_manager = Builder.load_file('kv_lang/app.kv')
        return self.screen_manager

    def switch_screen(self, screen_name, direction='left'):
        self.screen_manager.transition.direction = direction
        self.screen_manager.current = screen_name


if __name__ == '__main__':
    MindTrackerApp().run()
