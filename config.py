from kivy.config import Config


def set_config():
    Config.set('graphics', 'width', '360')
    #Config.set('graphics', 'height', '640')
    Config.set('graphics', 'height', '568')
    Config.set('kivy', 'exit_on_escape', '0')