import os
os.environ['KIVY_IMAGE'] = 'sdl2'
import config
config.set_config()
from mind_tracker_app import MindTrackerApp


if __name__ == '__main__':
    MindTrackerApp().run()
