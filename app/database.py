import sqlite3

global tabela

class ConectaBanco:
    
    # --- Criando a conexão com banco de dados "kivy_data.db"
    def __init__(self, name = 'kivy_data.db') -> None:
        self.name = name

    def connect(self): 
        self.connection = sqlite3.connect(self.name)
    
    def create_table(self):

        cursor = self.connection.cursor() # --- Gerando um cursor"

        # --- Criando a tabela "usuario"
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
            idUser INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL)
            """)

    def inserir_dados(self,dados):
        campos = ('username','email','password')
        itens = ('?,?,?')
        
        self.connect()
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO usuario {campos} VALUES ({itens}) """, dados)
            self.record_data()
            
        except Exception as e:
            print('Erro, dados nao gravados\n',e)
        
        self.close_connection()

    def record_data(self):
        try:
            self.connection.commit() # --- Gravar dados na tabela"
            print('Dados gravados com sucesso') 
        except:
            print('Impossivel gravar')

    def close_connection(self): 
        try:
            self.connection.close() # --- Fecha conexão com banco"
        except:
            print('Erro, não foi possivel fechar a conexão!')
    
    def listar_dados(self):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario")
            usuarios = cursor.fetchall()
            return usuarios
        except:
            pass
        

# c = ConectaBanco()
# c.connect()
# c.create_table()
# c.inserir_dados()
# c.listar_dados()
