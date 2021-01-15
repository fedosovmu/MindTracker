from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.graphics import *
from kivy.metrics import dp


class MoodAssessmentScreen(Screen):
    def __init__(self, **kwargs):
        super(MoodAssessmentScreen, self).__init__(**kwargs)
        self.set_bindings()
    
    def set_bindings(self):
        mood_assessor_slider = self.ids.mood_assessor.ids.mood_assessor_slider
        mood_assessor_slider.fbind('value', self.mood_assessor_slider_on_value_changed)
        mood_assessor_slider_scale = self.ids.mood_assessor.ids.mood_assessor_slider_scale
        mood_assessor_slider_scale.bind(size=self.mood_assessor_slider_scale_changed_size_callback)

    def mood_assessor_slider_on_value_changed(self, instance, value):
        print(f'Mood assessment changed {value}')
        self.redraw_agree_button(mood=value)
        self.redraw_mood_assessor_slider_scale(mood=value)

    def redraw_agree_button(self, mood):
        mood_agree_button = self.ids.mood_agree_button
        mood_agree_button.current_mood = mood

    def mood_assessor_slider_scale_changed_size_callback(self, instance, value):
        self.redraw_mood_assessor_slider_scale()

    def redraw_mood_assessor_slider_scale(self, mood=None):
        if mood is None:
            mood = self.ids.mood_assessor.ids.mood_assessor_slider.value
        colors = App.get_running_app().colors
        neutral_color = colors.mood_assessor_slider_scale_neutral_color
        mood_color = colors.mood_assessor_slider_cursor_colors[mood]
        mood_assessor_slider_scale = self.ids.mood_assessor.ids.mood_assessor_slider_scale
        canvas = mood_assessor_slider_scale.canvas
        canvas.clear()
        with canvas:
            for i in range(1, 8):
                if i == mood:
                    Color(rgba=mood_color)
                else:
                    Color(rgba=neutral_color)
                Rectangle(pos=(mood_assessor_slider_scale.x + (mood_assessor_slider_scale.width - dp(10))/6*(i-1)+dp(4),
                               mood_assessor_slider_scale.y + dp(13)),
                          size=(dp(2), dp(16)))