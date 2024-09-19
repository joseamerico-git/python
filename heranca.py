class Animal:
    def __init__(self,altura,peso,descricao,som):
        self.__altura = altura
        self.__peso = peso
        self.__descricao = descricao
        self.som = som
    def emitir_som(self):
        print(f'{self.__descricao} fazendo barulho {self.som}')
class Cavalo(Animal):
     
    pass

class Porco(Animal):
   def __init__(self,altura, peso, descricao, som,classes):
       self.__calsse = classes
       super().__init__(altura, peso, descricao, som)     
   def get_classe(self,):
       return self.__calsse     
   
            
        
  
    
                                                             
if __name__ == "__main__":
    
    animal = Animal(60,20.50,'Animal','faz barulho!')
    animal.emitir_som()
    
    
    cavalo = Animal(1.30,200,'Cavalo','Helinchando')
    cavalo.emitir_som()
    
    porco = Porco(1.50,60,'Leitão','grunido','mamifero')
    porco.emitir_som()
    
    
    