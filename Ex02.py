"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""
class ModelarQuadrado():
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado
        pass
    
    #método de mudar valor do lado
    def mudar_Valor_do_lado(self,novo_valor):
         self.tamanho_do_lado = novo_valor
         return self.tamanho_do_lado
    
    #calcula area
    def calcula_area(self):
        return self.tamanho_do_lado**2
        

#imprime o valor do lado
quadrado = ModelarQuadrado(100)
print(f'Tamanho do lado do quadrado: {quadrado.tamanho_do_lado} cm')
#muda o valor do lado
novo = quadrado.mudar_Valor_do_lado(50)
print('Novo valor do lado: ',novo,'cm')
#calcula area
aarea = quadrado.calcula_area(novo**2)
print('Area do novo valor: ', aarea,'cm')