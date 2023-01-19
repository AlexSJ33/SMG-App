import sqlite3

data = []

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

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario2")
            usuarios = cursor.fetchall()

            for users in usuarios:
                
                ListaItens={'id':users[0], 'user':users[1],'password':users[3],'admin':users[4]}
                data.append(ListaItens)
            
        except:
            pass
            return usuarios
    

  
        