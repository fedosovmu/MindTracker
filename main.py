import config
config.set_config()
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = """
Screen:
    BoxLayout:
        orientation: 'vertical'
                                        
        Image:
            source: 'data/images/360x270.png'
            allow_stretch: True
            keep_ratio: False
            height: dp(270)
            size_hint: (1, None)
   
        Label:
            text: 'Для использования приложения вы\\nдолжны принять пользовательское\\nсоглашение'
            multiline: True
            width: dp(300)
         
        Button:
            id: license_agreement_button
            text: 'Принимаю'
            height: dp(70)
            size_hint: (1, None)
            
        Button:
            id: license_agreement_button
            text: 'Не принимаю'
            height: dp(70)
            size_hint: (1, None)
"""

class MindTrackerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


if __name__ == '__main__':
    MindTrackerApp().run()
