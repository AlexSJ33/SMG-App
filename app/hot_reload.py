from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Window.size = (320,580)


class HotReload(MDApp):
    KV_FILES = ['app/signup.kv']
    
    DEBUG = True


    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        # screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('signup.kv'))

        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.theme_style = 'Dark'

        
        return screen_manager



HotReload().run()