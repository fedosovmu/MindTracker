import os
os.environ['KIVY_IMAGE'] = 'sdl2'
import config
config.set_config()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from app_colors import AppColors
from content import Content
from mood_assessment_screen import MoodAssessmentScreen


class LicenseAgreementScreen(Screen):
    pass


class MindTrackerApp(App):
    def build(self):
        self.colors = AppColors
        self.content = Content
        Window.clearcolor = AppColors.app_background_color
        self.screen_manager = Builder.load_file('kv_lang/app.kv')
        self.add_screens()
        return self.screen_manager

    def add_screens(self):
        license_agreement_screen = LicenseAgreementScreen(name='license_agreement')
        #self.screen_manager.add_widget(license_agreement_screen)
        mood_assessment_screen = MoodAssessmentScreen(name='mood_assessment')
        self.screen_manager.add_widget(mood_assessment_screen)

    def switch_screen(self, screen_name, direction='left'):
        self.screen_manager.transition.direction = direction
        self.screen_manager.current = screen_name

if __name__ == '__main__':
    MindTrackerApp().run()
