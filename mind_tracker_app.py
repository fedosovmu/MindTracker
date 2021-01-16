from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.base import EventLoop, stopTouchApp
from app_colors import AppColors
from app_content import AppContent
from mood_assessment_screen import MoodAssessmentScreen


class MindTrackerApp(App):
    def build(self):
        self.colors = AppColors
        self.content = AppContent
        Window.clearcolor = AppColors.app_background_color
        self.set_bindings()
        self.create_screen_manager()
        return self.screen_manager

    def set_bindings(self):
        Window.bind(on_keyboard=self.on_key)

    def on_key(self, window, key, *args):
        if key == 27:  # (Escape key or Back button)
            self.stop()

    def create_screen_manager(self):
        screen_manager = Builder.load_file('kv/app.kv')
        mood_assessment_screen = MoodAssessmentScreen(name='mood_assessment')
        screen_manager.add_widget(mood_assessment_screen)
        self.screen_manager = screen_manager

    def switch_screen(self, screen_name, direction='left'):
        self.screen_manager.transition.direction = direction
        self.screen_manager.current = screen_name

    def on_pause(self):
        return True

    def on_stop(self):
        pass
