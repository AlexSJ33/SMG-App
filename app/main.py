#!/usr/bin/env python3

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from database import ConectaBanco

Window.size = (320,580)



class GerenciadorTelas(ScreenManager):
    pass

class Login(Screen):
    pass



class Account(Screen,ConectaBanco):
        
    def pega_valor(self):
        username = self.ids.username.text
        username = "".join(username.split())
        email = self.ids.email.text
        email = "".join(email.split())
        password = self.ids.password.text
        password = "".join(password.split())
        password_2 = self.ids.password_2.text
        password_2 = "".join(password_2.split())
        data = (username,email,password)
        
        if username == '' or email.strip() == '' or password.strip() == '' or password_2.strip() == '':
            print('Necessario prencher todos os dados')
        else:
            print(data)
        #return c.inserir_dados(data)

class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('app.kv')

c=ConectaBanco()
c.connect()
c.create_table()


MyApp().run()