from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.metrics import dp
from kivy.properties import NumericProperty


class MoodAssessmentScreen(Screen):
    def __init__(self, **kwargs):
        super(MoodAssessmentScreen, self).__init__(**kwargs)
        self.set_bindings()
    
    def set_bindings(self):
        mood_assessor_slider = self.ids.mood_assessor.ids.mood_assessor_slider
        mood_assessor_slider.fbind('value', self.mood_assessor_slider_on_value_changed)

    def mood_assessor_slider_on_value_changed(self, instance, value):
        print(f'Mood assessment changed {value}')
        mood_agree_button = self.ids.mood_agree_button
        mood_agree_button.current_mood = value
        #mood_assessor = self.ids.mood_assessor
        #mood_sphere_image = mood_assessor.ids.mood_sphere_image
        #mood_sphere_image.source = f'data/images/mood_spheres/{value}.png'

    def create_mood_assessor_slider_scale(self):
        slider_scale = self.ids.mood_assessor.ids.mood_assessor_slider_scale

        for i in range(7):
            pos = slider_scale.x + ((slider_scale.width - dp(10)) / 6 * i) + dp(5), slider_scale.y
            scale_line_recangle = Rectangle(pos=pos, size=(dp(2), dp(16)))
            slider_scale.canvas.add(scale_line_recangle)