
from user_management import *
from client_management import *
from login_management import *

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (680, 600)

###################################################################
## HOT RELOAD CONFIG
###################################################################

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:
    HotReloadViewer:
    path: app.path_to_kv_file
    errors: True
    errors_text_color: 0,0,0,1
    errors_background_color: app.theme_cls.bg_dark
'''
###################################################################
## MAIN CLASS
###################################################################
class Exemple(MDApp):
    #kivy file to hot reload
    path_to_kv_file = "app.kv"
    # Build function
    def build(self):
        return Builder.load_string(KV)
###################################################################
## RUN APP 
###################################################################
Exemple().run()

