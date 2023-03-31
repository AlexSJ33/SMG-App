import sqlite3

login = []

class ConectaBanco:
    
    # --- Criando a conexão com banco de dados "kivy_data.db"
    def __init__(self, name = 'kivy_data.db') -> None:
        self.name = name

    def connect(self): 
        self.connection = sqlite3.connect(self.name)
    
    def create_table(self):

        cursor = self.connection.cursor() # --- Gerando um cursor"

        # --- Criando a tabela "usuario"
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario2 (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            administrador VARCHAR(1) NOT NULL)
            """)
        self.verificar_dados()

    def verificar_dados(self):
        self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute("""SELECT COUNT(*) AS usuario FROM usuario2""")
            dados = cursor.fetchall()

            if dados[0][0] < 1:
                self.criar_admin()

                print('usuario admin criado')
            else:
                print('Total users:', dados[0][0])


        except Exception as e:
            print('não existe dados', e)
        self.close_connection()

    def criar_admin(self):
        dados = ['admin','admin@admin.com','123','1']
        campos = ('usuario','email','password','administrador')
        itens = ('?,?,?,?')

        self.connect()
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO usuario2 {campos} VALUES ({itens}) """,dados)
            self.record_data()
            
        except Exception as e:
            print('Erro, dados nao gravados\n',e)
        
        self.close_connection()


    def inserir_dados(self,dados):
        campos = ('usuario','email','password','administrador')
        itens = ('?,?,?,?')

        print(dados)
        
        self.connect()
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO usuario2 {campos} VALUES ({itens}) """, dados)
            self.record_data()
            
        except Exception as e:
            print('Erro, dados nao gravados\n',e)
        
        self.close_connection()

    def record_data(self):
        try:
            self.connection.commit() # --- Gravar dados na tabela"
        except:
            pass

    def close_connection(self): 
        try:
            self.connection.close() # --- Fecha conexão com banco"
        except:
            pass
    
    def listar_dados(self,usuarios=''):
        self.connect()
        data = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario2")
            usuarios = cursor.fetchall()

            for users in usuarios:
                #ListaItens=(users[0],users[1],users[2],users[3],users[4])
                ListaItens={'id':users[0], 'user':users[1],'email':users[2],'password':users[3],'admin':users[4]}
                data.append(ListaItens)
                login.append(ListaItens)
           
        except:
            pass
        return data
    
    def update_list(self):
        data2 =[]
        print('<<<<<UPDATE>>>>>')
        self.connect()

        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM usuario2")
        usuarios = cursor.fetchall()

        for users in usuarios:
            #ListaItens=(users[0],users[1],users[2],users[3],users[4])
            ListaItens={'id':users[0], 'user':users[1],'email':users[2],'password':users[3],'admin':users[4]}
            data2.append(ListaItens)
        

    def delete_user(self, id):
        self.connect()

        try:
            
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario2")
            usuarios = cursor.fetchall()
            
            user_deleted = False
            for users in usuarios:
                if id == str(users[0]):
                    cursor.execute("DELETE FROM usuario2 where id=?",(id,))
                    self.record_data()
                    user_deleted = True
                    print('usuario deletado com sucesso!')
                    self.update_list()
                    break

            if not user_deleted:
                print('Usuário não encontrado com ID', id)
                
            
        except Exception as e:
            print('Erro ao tentar deletar\n',e)
        
        self.close_connection()
