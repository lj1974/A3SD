import re

from Model.consultar_usuario import listar_ids_e_nomes_vendedores


def coletar_dados_novo_usuario():
    return 0

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
        
    
