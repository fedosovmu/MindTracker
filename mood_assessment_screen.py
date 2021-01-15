from kivy.uix.screenmanager import Screen


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