#Classe

class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 200
        print(f"{self.modelo} acelerando. Velocidade atual: {self.velocidade} km/h")
        
#Criando Objetos

Carro1 = Carro("Lamborghini", "Amarelo")
Carro2 = Carro("Ferrari", "Vermelho")

#Metodos

print(Carro1.modelo, Carro1.cor)#Saída:  Lamborghini
Carro1.acelerar()