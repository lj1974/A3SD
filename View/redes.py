
from Model.queries.consultar_rede import listar_ids_e_nomes

def escolher_rede():
   
   while True:
        print("\n\nLista de Redes:\n")
        rede = listar_ids_e_nomes()
        for i, rede in enumerate(rede, start=1):
            print(f"{i}. {rede['nomerede']}")

    
        num_rede = int(input("\nDigite o número da Rede: "))
        if num_rede < 1 or num_rede > len(rede):
            print("Número da rede inválido. Tente novamente.")
        else:
            return rede[num_rede - 1]