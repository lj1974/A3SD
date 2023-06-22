import re

def digitar_valor():
    
    while True:
        valor = input("\nDigite o valor da venda: ")
        if not re.match(r'^\d+(?:[.,]\d{2})?$', valor):
            print("Valor inválido. Digite um número no formato correto (ex: 10.00 ou 12,00).")
        else:
            return valor.replace(',', '.')