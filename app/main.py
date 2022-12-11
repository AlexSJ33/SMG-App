#!/usr/bin/env python3

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from database import ConectaBanco

class GerenciadorTelas(ScreenManager):
    pass

class Login(Screen):
    pass

class ListUser(MDCard):

    
    def exibir_dados(self):
        lista = c.listar_dados()
        for users in lista:
                    self.ids['box'].add_widget(
                        MDLabel(
                            text=f"{users[1]}",
                            halign="left",
                            
                            adaptive_height=True,
                        )
                    )
    
    def fechar(self):
        self.parent.remove_widget(self)
    

class Account(Screen,ConectaBanco,MDApp):
    dialog = None    
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
            self.dialog = MDDialog(
                text="[color=#f9f9f9]Preencha todos os campos ![/color]",
                md_bg_color='3c3c3c',
                )
            self.dialog.open()
            
        else:
            self.dialog = MDDialog(
                text="[color=#f9f9f9]Dados gravados com sucesso![/color]",
                md_bg_color='3c3c3c',
                )
        
            self.dialog.open()
            
            return c.inserir_dados(data)


    def limpar_text(self):
        self.ids.username.text = ''
        self.ids.email.text = ''
        self.ids.password.text = ''
        self.ids.password_2.text = ''

    
    def abrir_card(self):
        self.add_widget(ListUser())
        
class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('app.kv')
    

c=ConectaBanco()
c.connect()
c.create_table()
c.listar_dados()

if __name__=='__main__':
    MyApp().run()



