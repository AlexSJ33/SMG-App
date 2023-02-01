#!/usr/bin/env python3
#---------------------------------------------------------#
# Sistema MiniGestão - C.R.U.D
# Ferramentas: Python, Kivy, SQLite
# Versão: 1.0.0
#---------------------------------------------------------#
# Desenvolvedor..: Alex S Jesus <alevildark@gmail.com>
# Data...........: 04.12.2022
#---------------------------------------------------------#

from gestaocliente import GestaoCliente as gc
from gestaousuario import GestaoUsuario as gu

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


from database import ConectaBanco
from database import data as ListItems


Window.size = (680, 600)

global tela
global autenticado
tela = ScreenManager()
autenticado = []


class Inicio(Screen):
    pass

class Menu(Screen):

    def on_enter(self):
        name = autenticado[0]
        self.ids.label_menu.text = 'Olá ' + str(name)


class GestaoUsuario(Screen):

    def on_enter(self):
        self.loadItems()

    def loadItems(self):
        
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x':.5, 'center_y':.5},
            use_pagination=True,
            check=True,
            rows_num=10,
            column_data=[
                ("ID", dp(30)),
                ("Username", dp(30)),
                ("E-mail", dp(30)),
                ("Perfil", dp(30))
            
            ],
            row_data=[
                (
                i[:][0],
                i[:][1],
                i[:][2],
                i[:][4],
                )
                for i in ListItems
                ],
            )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)

        self.add_widget(self.data_tables)

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)
        pass

    def on_check_press(self, instance_table, current_row):
        print(current_row)

    def cad_usuario(self):
        self.add_widget(CadastrarUsuario())
    
   

class GestaoCliente(Screen):
    def cad_cliente(self):
        self.add_widget(CadastrarCliente())


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

            elif self.username == users[1] and self.password == users[3]:
                print(self.username)
                self.ids.label_login.text = 'Login Accept !!'
                self.ids.label_login.text_color= 'green'
                MDApp.get_running_app().root.current = 'menu'
                autenticado.append(self.username)
                break
                
            else:
                self.ids.label_login.text = 'Login Incorrect !!'
                self.ids.label_login.text_color = 'red'
    
class CadastrarCliente(MDCard):
    def get_cliente(self):
        nome = self.ids.nome.text
        cpf = self.ids.cpf.text
        email = self.ids.email.text
        email = "".join(email.split())
        telefone = self.ids.telefone.text
        telefone = "".join(telefone.split())
        cep = self.ids.cep.text
        cep = "".join(cep.split())
        cidade = self.ids.cidade.text
        uf = self.ids.uf.text
        uf = "".join(uf.split())
        endereco = self.ids.endereco.text
        numero = self.ids.numero.text
        numero = "".join(numero.split())
        bairro = self.ids.bairro.text

        if nome == '' or cpf.strip() == '' or email.strip() == '' \
            or telefone.strip() == '' or cep.strip() == '' or cidade == '' \
            or uf.strip() =='' or endereco =='' or bairro =='':

            self.dialog = MDDialog(
                text="[color=#f9f9f9]Preencha todos os campos ![/color]",
                md_bg_color='3c3c3c',
                )
            self.dialog.open()
        else:
            print('ok')


    def fechar(self):
        self.parent.remove_widget(self)   

class CadastrarUsuario(MDCard):

    dialog = None
    adminstrador = '0'

    def get_usuario(self):
        usuario = self.ids.usuario.text
        usuario = "".join(usuario.split())
        email = self.ids.email.text
        email = "".join(email.split())
        senha = self.ids.senha.text
        senha = "".join(senha.split())
        re_senha = self.ids.re_senha.text
        re_senha = "".join(re_senha.split())
        admin = self.adminstrador

        data = (usuario,email,senha,admin)
        print('get_usuario =',admin)
        
        if usuario == '' or email.strip() == '' or senha.strip() == '' or re_senha.strip() == '':
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

    def fechar(self):
        self.parent.remove_widget(self)   

    def limpar_text(self):
        self.ids.usuario.text = ''
        self.ids.email.text = ''
        self.ids.senha.text = ''
        self.ids.re_senha.text = ''

    def on_checkbox_active(self,checkbox, value):
        if value:
            self.admin = '1'
        else:
            self.admin = '0'
        self.adminstrador = ''
        self.adminstrador= self.admin

tela.add_widget(Inicio(name='inicio'))
tela.add_widget(Login(name='login'))
tela.add_widget(Menu(name='menu'))




c=ConectaBanco()
c.connect()
c.create_table()
c.listar_dados()

class MyApp(MDApp):
    

    def build(self):
        kv = Builder.load_file('app.kv')
        tela = kv
        #self.theme_cls.primary_palette = 'Purple'
        #self.theme_cls.theme_style = 'Dark'

        

        return tela


if __name__=='__main__':
    MyApp().run()
