"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor"""
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        """Altera a cor da bola."""
        self.cor = nova_cor

    def mostraCor(self):
        """Retorna a cor atual da bola."""
        return self.cor


# Exemplo de uso
bolinha = Bola('Azul', '50cm', 'couro')

# Exibindo os atributos manualmente
print(f"Cor: {bolinha.cor}, Circunferência: {bolinha.circunferencia}, Material: {bolinha.material}")

# Alterando e mostrando a cor
bolinha.trocaCor('Preto')
print(f"Nova cor: {bolinha.mostraCor()}")
