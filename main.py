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
                             
        Button:
            text: 'Картинка'
   

        Label:
            text: 'Для использования приоржения вы\\nдолжны принять пользовательское\\nсоглашение'
         

        Button:
            id: license_agreement_button
            text: 'Принимаю'
            
        Button:
            id: license_agreement_button
            text: 'Не принимаю'
"""

class MindTrackerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


if __name__ == '__main__':
    MindTrackerApp().run()
