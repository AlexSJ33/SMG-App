#!/usr/bin/env python3
#---------------------------------------------------------#
# Sistema MiniGestão - C.R.U.D
# Ferramentas: Python, Kivy, SQLite
# Versão: 1.0.0
#---------------------------------------------------------#
# Desenvolvedor..: Alex S Jesus <alevildark@gmail.com>
# Data...........: 04.12.2022
#---------------------------------------------------------#


from user_management import *
from client_management import *
from login_management import *

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (700, 600)

screen.add_widget(ClientManagement())
screen.add_widget(UserManagement())

class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file('app.kv')
        screen = kv

        return screen

if __name__=='__main__':
    MyApp().run()