
from gestaocliente import GestaoCliente as gc
from gestaousuario import GestaoUsuario as gu

from kivymd.app import MDApp
from kivy.lang import Builder

class MyApp(MDApp):
    

    def build(self):
        kv = Builder.load_file('app.kv')
        gu.on_enter()
        tela = kv
        #self.theme_cls.primary_palette = 'Purple'
        #self.theme_cls.theme_style = 'Dark'

        

        return tela


if __name__=='__main__':
    MyApp().run()