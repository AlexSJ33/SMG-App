class ClasseA:
    def __init__(self):
        self.classe_b = ClasseB()
        
    def metodo_da_classe_a(self):
        # chama um método da ClasseB
        self.classe_b.metodo_da_classe_b()

class ClasseB:
    def metodo_da_classe_b(self):
        print("Método da ClasseB foi chamado.")

# Cria uma instância da ClasseA
objeto_a = ClasseA()

# Chama um método da ClasseA, que por sua vez chama um método da ClasseB
objeto_a.metodo_da_classe_a() # saída: "Método da ClasseB foi chamado."
