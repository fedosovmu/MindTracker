import config
config.set_config()
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = """
Screen:
    GridLayout:
        rows: 2
        
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
                             
            Image:
                source: 'data/images/360x270.png'
                adaptive_width: True
        
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
        
            MDRaisedButton:
                id: license_agreement_button
                text: 'Принимаю'
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
"""

class MindTrackerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


if __name__ == '__main__':
    MindTrackerApp().run()
