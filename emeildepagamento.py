class Caixa:
    def __init__(self, nome):
        self.nome = nome

    def processar_pagamento(self, metodo, valor):
        print(f"{self.nome} vai processar o pagamento...")
        metodo.pagar(valor)


# Classes de formas de pagamento
class CartaoCredito:
    def __init__(self, nome):
        self.nome = nome
    
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} com cartão de crédito.")


class Dinheiro:
    def __init__(self, nome):
        self.nome = nome
    
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} em dinheiro.")


class Pix:
    def __init__(self):
        pass
    
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} via Pix.")


# Criando objetos
caixa = Caixa("Caixa do Supermercado")
cartao = CartaoCredito("cartão de crédito")
dinheiro = Dinheiro("dinheiro")
pix = Pix()

# Processando pagamentos
caixa.processar_pagamento(cartao, 100)
caixa.processar_pagamento(dinheiro, 50)
caixa.processar_pagamento(pix, 200)

# Classe de cupom
class Cupom:
    def imprimir(self):
        print("Cupom de desconto de R$10,00.")

# Criando cupom e imprimindo
cupom = Cupom()
cupom.imprimir()