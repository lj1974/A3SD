import re

from View.nome import nome_usuarios


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
            return '03.' + opcao
        else:
            print("digite uma opção valida.\n")
            
            