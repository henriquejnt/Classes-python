"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
"""

class ModelarRetangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        pass

    def mudar_valor_dos_lados(self,novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB
    
    def calcular_area(self):
        return self.ladoA*self.ladoB
    
    def calcular_perimetro(self):
        return (self.ladoA+self.ladoB)*2


ladoa = float(input("Informe a primeira medida de um local: "))
ladob = float(input("Informe a segunda medida desse local: "))
retangulo = ModelarRetangulo(ladoA=ladoa, ladoB=ladob)
print(f'Medidas do local : {retangulo.ladoA} e {retangulo.ladoB} metros.')

retangulo.mudar_valor_dos_lados(novo_ladoB=10,novo_ladoA = 41)
print(f'Novos valores: {retangulo.ladoA} e {retangulo.ladoB}','metros')

print('Área do local', retangulo.calcular_area(),'metros')
print('Perímetro da área ', retangulo.calcular_perimetro(),'metros')