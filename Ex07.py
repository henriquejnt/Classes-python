class BombaCombustível:
    def __init__(self, tipocombustivel,valorlitro,quantidadecombustivel):
        self.tipocomsbutivel = tipocombustivel
        self.valorlitro = valorlitro
        self.quantidadecombustivel = quantidadecombustivel
        pass

    #mostra a quantidade de litros que foi colocada no veículo
    def abastecerporvalor(self, valor:float):
        litros_abastecidos = valor/self.valorlitro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def _apresentar_abastecimento_se_possivel(self, litros_abastecidos:float, valor:float):
        if litros_abastecidos > self.quantidadecombustivel:
            print(f'Não é possível, abastecer.Faltam {litros_abastecidos - self.quantidadecombustivel:.2f} litros.')
        else:
            self.quantidadecombustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros de um valor de R${valor:.2f} reais')
            print(f'Sobraram {self.quantidadecombustivel:.2f} litros na bomba.')
    
    #mostra o valor a ser pago pelo cliente.
    def abastecerporlitro(self,litros_abastecidos:float):
        valor = litros_abastecidos*self.valorlitro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)
    
abastecimento = BombaCombustível('Diesel', 4.59, 100)
print('=-'*6,'BOMBA','=-'*6)
print('Tipo de combustivel: ',abastecimento.tipocomsbutivel)
print('Valor por litro: ', abastecimento.valorlitro)
abastecimento.abastecerporvalor(100)
abastecimento.abastecerporlitro(50)

abastecimento.valorlitro = 5.59
abastecimento.abastecerporlitro(50)