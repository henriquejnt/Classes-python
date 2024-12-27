"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e 
pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, 
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
 o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível 
 criar um macaco canibal?"""


class Macaco: 
    def __init__(self,nome, bucho): 
        self.nome = nome
        self.bucho = bucho 
        pass
    #Vizualiza o estomago do macaco 
    def verbucho (self): 
        return self.bucho 
    #macaco pedro come o macaco paulo 
    def macaco_canibal(self, macaco_pedro_nome,macaco_pedro_estomago):
       self.bucho.append(macaco_pedro_nome) 
       self.bucho.extend(macaco_pedro_estomago)
       return self.bucho 
    

macaco01 = Macaco(nome='Paulo', bucho=['Maçã','Banana','Sorvete'])
macaco02 = Macaco(nome='Pedro',bucho=['Pastilha','Bolacha','Morango']) 
contador = 0 
#macaco paulo come macaco pedro
canibal = macaco01.macaco_canibal(macaco_pedro_nome=macaco02.nome,macaco_pedro_estomago = macaco02.bucho)

print('=-'*5, 'MACACO PAULO', '=-'*5)
for comida in macaco01.bucho:
    print(f'O macaco {macaco01.nome} comeu {comida}')
    contador += 1
    if contador == 3:
        print(f'Vizualização do estomago do macaco {macaco01.nome}: {macaco01.bucho[0:3]}')
contador = 0
print('=-'*5, 'MACACO PEDRO', '=-'*5)
for comida in macaco02.bucho:
    print(f'O macaco {macaco02.nome} comeu {comida}')
    contador += 1
    if contador == 3:
        print(f'Vizualização do estomago do macaco {macaco02.nome}: {macaco02.bucho}')
print('=-'*5, 'MACACO PAULO COMENDO MACACO PEDRO', '=-'*5)
print('Estomâgo de macaco paulo: ',canibal)