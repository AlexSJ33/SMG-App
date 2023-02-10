from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivy.metrics import dp

from database import data as ListItems
from database import ConectaBanco



class UserManagement(Screen):
  

    def on_enter(self):
        self.loadItems()


    def loadItems(self):
        self.selected_index = None
        
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x':.5, 'center_y':.5},
            use_pagination=True,
            check=True,
            rows_num=10,
            background_color_header="#808080",
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

        self.add_widget(self.data_tables) 
        


        self.data_tables.selected_index = None
        self.selected_current_row = []

        self.data_tables.bind(on_check_press=self.on_check_press)
        self.data_tables.bind(on_row_press=self.on_row_press)

    def on_row_press(self, instance_table, instance_row):
        
        index = instance_row.index
        cols_num = len(instance_table. column_data)
        row_num = int(index/cols_num)
        col_num = index%cols_num
        cell_row = instance_table.table_data.view_adapter.get_visible_view(row_num*cols_num)
        if cell_row.ids.check.state == 'normal':
            instance_table.table_data.select_all('normal')
            cell_row.ids.check.state = 'down'
        else:
            cell_row.ids.check.state = 'normal'
        instance_table.table_data.on_mouse_select(instance_row)

    def on_check_press(self, instance_table, current_row):
        if current_row[0] in self.selected_current_row:
            self.selected_current_row.remove(current_row[0])
        else:
            self.selected_current_row.append(current_row[0])
            print('Item selecionado', current_row)            

    def edit_user(self):
        self.add_widget(EditUser(MDCard))
        
        
    def cad_usuario(self):

        self.add_widget(RegisterUser())

class RegisterUser(MDCard):

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

class EditUser(MDCard):


    def fechar(self):
        self.parent.remove_widget(self)   


c=ConectaBanco()
c.connect()
c.create_table()
c.listar_dados()    
   
