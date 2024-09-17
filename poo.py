class Animal:

    def __init__(self, nome, idade):

        self.nome = nome

        self.idade = idade

    def trotar(self):

        print(f"O {self.nome} está trotando.")
        
#Getter
    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome        
        
if __name__=='__main__':
    meu_animal = Animal('Cavalo', 30)
    meu_animal.get_nome()