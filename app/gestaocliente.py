from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard



class GestaoCliente(Screen):
    def cad_cliente(self):
        self.add_widget(CadastrarCliente())


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
