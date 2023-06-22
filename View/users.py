import re

from Model.consultar_usuario import listar_ids_e_nomes_vendedores


def coletar_dados_novo_usuario(cpf):
    nome = input("\n\nEscreva seu nome completo: ")
    ano = digitar_ano()
    cargo = escolher_cargo()
    
    return '04.0', nome, cpf, ano, cargo


def digitar_ano():
    
    while True:
        valor = input("\nEscreva seu ano de nascimento: (Ex: 1990) ")
        if not re.match(r'^\d+(?:[.,]\d{2})?$', valor):
            print("Valor inválido. Digite um número no formato correto (ex: 2010).")
        else:
            return valor.replace(',', '.')
        
def escolher_cargo():
    print("Escolha o seu cargo: ")
    print('1. VENDEDOR')
    print('2. GERENTE\n')
    
    while True:
        escolha = int(input('\nDigite o número do seu cargo: '))
        if escolha < 1 or escolha > 2:
            print("Número inválido. Tente novamente.")
        else:
            if escolha == 1:
                return 'VENDEDOR'
            elif escolha == 2:
                return 'GERENTE'
        

def leitura_cpf():
    while True:
        cpf = input("\nDigite o seu CPF (ex: 68719287600): ")
        cpf = cpf.strip()  

        if re.match(r'^\d{11}$', cpf):
            return cpf
        else:
            print("CPF inválido. Digite apenas 11 dígitos numéricos.")
            

def escolher_vendedor():
   
   while True:
        while True:
            print("\n\nLista de Vendedores:\n")
            vendedores = listar_ids_e_nomes_vendedores()
            for i, vendedor in enumerate(vendedores, start=1):
                print(f"{i}. {vendedor[1]}")

            num_vendedor = int(input("\nDigite o número do Vendedor: "))
            if num_vendedor < 1 or num_vendedor > len(vendedores):
                print("Número do vendedor inválido. Tente novamente.")
            else:
                escolha_vendedor = vendedores[num_vendedor - 1]
                return escolha_vendedor
        
    
