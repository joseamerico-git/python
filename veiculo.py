import datetime


class Veiculo:
    def __init__(self,veiculo_modelo,veiculo_marca):
        self.veiculo_modelo = veiculo_modelo
        self.veiculo_marca = veiculo_marca
        self.numero_registro = None
          
    # Getter      
    def get_veiculo_modelo(self):
        return self.veiculo_modelo
    
    def get_veiculo_marca(self):
        return self.veiculo_marca
    
    def get_numero_registro(self):
        return self.numero_registro
    
    
    # Setter
    
    def set_veiculo_modelo(self,veiculo_modelo):
        self.get_veiculo_modelo = veiculo_modelo
        
    def set_veiculo_marca(self, veiculo_marca):
        self.get_veiculo_marca = veiculo_marca    
              
    def set_numero_registro(self, numero_registro):
        self.numero_registro = numero_registro
        
    def exibir_informacoes(self):
        print(f'Modelo: {self.veiculo_modelo}, marca: {self.veiculo_marca}.')
        
    def get_data_venda(self):
         data = input('data [d/m/Y]: ')    
         data2 = datetime.strptime(data, "%d/%m/%Y")
         return data2
        
# herança e polimorfismo        
class Carro(Veiculo):
    # init declarado em veículo
    def movimentar(self):
        print('Carro movimentando!')
    
        
class Bicicleta(Veiculo):
    pass        

if __name__ == "__main__":
    meu_veiculo = Veiculo('Corsa Classic','GM')
   
    #meu_veiculo.exibir_informacoes()
    meu_carro = Carro(meu_veiculo.veiculo_modelo,meu_veiculo.veiculo_marca)
    meu_carro.set_numero_registro('123456')
   
   
    meu_carro.exibir_informacoes()
    print(f'Nº Registro: {meu_carro.get_numero_registro()}')
    meu_carro.movimentar()
    meu_carro.get_data_venda()
           
            