import re

from View.nome import nome_usuarios
from View.users import escolher_vendedor
from View.redes import escolher_data_para_rede, escolher_rede


def form_gerente(user):
    nome_usuarios(user)
    
    print("\n\nEscolha qual operação deseja executar:")
    print("1. Pesquisar total de vendas de um vendedor")
    print("2. Exibir melhor loja")
    print("3. Exibir melhor vendedor")
    print("4. Filtrar total de vendas de uma rede\n")
     
    while True:
        opcao = input("\nEscolha uma opção: ")
        if re.match(r'^\d{1}$', opcao):
            valor = '03.' + str(opcao)
            if opcao == '1':
                vendedor = escolher_vendedor()
                return valor, vendedor[0], vendedor[1]
            if opcao == '4':
                nome_rede = escolher_rede()
                rede = escolher_data_para_rede()
                return valor, nome_rede, rede[0], rede[1]
            
            return valor
        else:
            print("digite uma opção valida.\n")
            
            