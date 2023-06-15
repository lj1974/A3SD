
import datetime
import time

from View.lojas import escolher_loja
from View.venda import digitar_valor
from View.nome import nome_usuarios


def form_vendedor():
   
    nome_usuarios();
    
    while True:
        # Obter ID e nome da loja selecionada
        loja_selecionada = escolher_loja()
        id_loja = loja_selecionada['idloja']
        nome_loja = loja_selecionada['nomeloja']

        # Solicitar valor da venda
        valor = digitar_valor();

        # Confirmar informações
        print("Confirme as informações:")
        print("Loja selecionada:", nome_loja)
        print("Valor da venda:", valor)

        confirmacao = input("\nDeseja confirmar as informações? (s/n): ")
        if confirmacao.lower() == "s":
            data = datetime.date.today()
            return '02.0', data, id_loja, float(valor)
        else:
            print("Resetando... Tente novamente.")
            time.sleep(0.5)

    