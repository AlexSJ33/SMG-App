from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from database import data as ListItems

global autenticado
screen = ScreenManager()
autenticado = []

class Inicio(Screen):
    pass

class Login(Screen):

    def login(self):
        campo_user = self.ids.username.text
        campo_password = self.ids.password.text

        self.username = "".join(campo_user.split())
        self.password = "".join(campo_password.split())

        if self.username == '' or self.password.strip() == '':
            self.dialog = MDDialog(
                text="[color=#f9f9f9]Preencha todos os campos ![/color]",
                md_bg_color='3c3c3c',
                )
            self.dialog.open()
            
        else:
            return self.username,self.password

    def valida_login(self):
        
        for users in ListItems:

            if self.username == '' or self.password == '':
                self.ids.label_login.text = ' '

            elif self.username == users['user'] and self.password == users['password']:
                print(self.username)
                self.ids.label_login.text = 'Login Accept !!'
                self.ids.label_login.text_color= 'green'
                MDApp.get_running_app().root.current = 'menu'
                autenticado.append(self.username)
                break
                
            else:
                self.ids.label_login.text = 'Login Incorrect !!'
                self.ids.label_login.text_color = 'red'

class Menu(Screen):

    def on_enter(self):
        name = autenticado[0]
        self.ids.label_menu.text = 'Olá ' + str(name)