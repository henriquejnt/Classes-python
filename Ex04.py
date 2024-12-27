"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que passa,nossa pessoa envelhece,
 sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""

class ModelarPessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        pass

    def envelhecer(self):
        if  self.idade < 21:
            self.altura += 0.5
        self.idade += 1
        
pessoa = ModelarPessoa('Jullya',3 ,15, 50)
for _ in range(22):
    pessoa.envelhecer()
    print(f'Nome {pessoa.nome}, idade {pessoa.idade}, altura {pessoa.altura}')