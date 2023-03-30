
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.clock import Clock

from database import ConectaBanco

c=ConectaBanco()
c.connect()
c.create_table()
c.listar_dados()


class UserManagement(Screen):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
 
    row_edit = []
    check = False
    maior_q_um = False
    
    def sayhello(self):
        
        print("hello world")


    def on_enter(self):
        self.create_datatable()
        self.reload_datatable()
        print('ok')

    

##################### CRIA UM DATATABLE DE USUARIOS #########################

    def create_datatable(self):

        

        self.selected_index = None

        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x':.5, 'center_y':.5},
            use_pagination=True,
            check=True,
            #rows_num=10,
            background_color_header="#808080",
            #background_color_cell="#451938",
            #background_color_selected_cell="e4514f",

            column_data=[
                ("ID", dp(30)),
                ("Username", dp(30)),
                ("E-mail", dp(50)),
                ("Administrador", dp(46)),
            ],
            row_data=[],
        )        

        self.data_tables.selected_index = None
        self.selected_current_row = []

        self.data_tables.bind(on_check_press=self.on_check_press)
        self.data_tables.bind(on_row_press=self.on_row_press)

        self.add_widget(self.data_tables)


############# FORNECE OS DADOS DE USUARIOS PARA DATATABLE ###################

    def get_data(self):
        dados = c.listar_dados()
             

        for item in dados:
            if item['admin'] == '1':
                item['admin'] = ("check-circle", [0, 1, 0, 1],"")
            elif item['admin'] == '0':
                item['admin'] = ("close-circle", [1, 0, 0, 1],"")
            else:
                pass
        
            self.data_tables.add_row((item['id'], item['user'], item['email'], item['admin']))
###########################################################################


################### VERIFICA LINHA SELECIONADA ###################
    def on_row_press(self, instance_table, instance_row):
        
        
        index = instance_row.index
        cols_num = len(instance_table. column_data)
        row_num = int(index/cols_num)
        col_num = index%cols_num
        cell_row = instance_table.table_data.view_adapter.get_visible_view(row_num*cols_num)
        if cell_row.ids.check.state == 'normal':
            instance_table.table_data.select_all('normal')
            self.check = True
            cell_row.ids.check.state = 'down'
            
            
        else:
            self.check = False
            cell_row.ids.check.state = 'normal'
            
        instance_table.table_data.on_mouse_select(instance_row)


    def on_check_press(self, instance_table, current_row):
        if current_row[0] in self.selected_current_row:
            self.selected_current_row.remove(current_row[0])

        else:
            self.selected_current_row.append(current_row[0])
            print('Item selecionado', current_row)            
            self.row_edit.insert(0,current_row)
##############################################################

############### ATUALIZA DATATABLE USUARIO #################
    def reload_datatable(self):
        self.remove_datatable()
        self.create_datatable()
        self.get_data()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def remove_datatable(self):
       self.remove_widget(self.data_tables)
##############################################################

##################### EDITAR USUARIO #########################

    def edit_user(self):
        self.add_widget(EditUser(MDCard))
        

        if self.check == False:
            print('check = ',self.check)
            print('Maior que Um = ',self.maior_q_um)
        else:
            print('check = ',self.check)
            print('Maior que Um = ',self.maior_q_um)
            print(self.row_edit[0])
###############################################################

##################### DELETAR USUARIO #########################    
    def delete_user(self):
        def deselect_rows(*args):
            self.data_tables.table_data.select_all("normal")


        for data in self.data_tables.get_row_checks():
            c.delete_user(data[0])
            self.reload_datatable()
        
        Clock.schedule_once(deselect_rows)
##############################################################

class RegisterUser(Screen):
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

    

    def cancelar(self):
        self.limpar_text()
                

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

class EditUser(Screen):
    pass

    # def cancelar(self):      
    #     self.parent.remove_widget(self)

