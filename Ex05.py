"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os
 seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
   depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são 
   obrigatórios."""

class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo,deposito):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo
        self.deposito = deposito
        pass

    def alterarnome(self,novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposita(self):
            self.deposito = float(input('Quanto quer depositar?: '))
            self.deposito < self.saldo
            self.saldo += self.deposito
            return self.saldo
        
    def saca(self):
            self.deposito = float(input('Quanto quer sacar?: '))
            if self.deposito < self.saldo:
                self.saldo -= self.deposito
                return self.saldo
            else:
                print('Deposito inválido!')


cliente = ContaCorrente(numero_conta=41, nome='Paula Delgado', saldo=1502,deposito=0)
print(f'Nome: {cliente.nome}')

#troca nome
novo = cliente.alterarnome(novo_nome='Paulo Delgado')
print(f'Nome atualizado: {novo}')
print(f'Número da conta: {cliente.numero_conta}')
print(f'Saldo atual: {cliente.saldo}')

#deposita e saca
print('=-'*15)
print(f'Saldo da conta atualizado depois do saque: {cliente.saca()}')
print('=-'*15)
print(f'Saldo da conta atualizado depois do deposito: {cliente.deposita()}')

