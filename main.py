import os
os.environ['KIVY_IMAGE'] = 'sdl2'
import config
config.set_config()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from app_colors import AppColors


class MindTrackerApp(App):
    def build(self):
        self.colors = AppColors
        Window.clearcolor = AppColors.app_background_color
        self.screen_manager = Builder.load_file('kv_lang/app.kv')
        self.set_binding()
        return self.screen_manager

    def switch_screen(self, screen_name, direction='left'):
        self.screen_manager.transition.direction = direction
        self.screen_manager.current = screen_name

    def set_binding(self):
        mood_assessor_slider = self.screen_manager.ids.mood_assessment_screen.ids.mood_assessor.ids.mood_assessor_slider
        mood_assessor_slider.fbind('value', self.mood_assessor_slider_on_value)
        print(mood_assessor_slider)

    def mood_assessor_slider_on_value(self, instance, value):
        print(f'Mood assessment changed {value}')

if __name__ == '__main__':
    MindTrackerApp().run()
