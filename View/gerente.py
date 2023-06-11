     
from View.users import escolher_vendedor
from View.venda import consultar_total_vendedor

def total_vendedor():
    
    vendedor_selecionado = escolher_vendedor()
    id_vendedor = vendedor_selecionado['idusuario']
    
    return consultar_total_vendedor(id_vendedor)
    
    
def melhor_loja():
    return 0


def melhor_loja():
    return "03", "loja A"


def melhor_vendedor():
    return "04", "Marcos"

def total_rede():
    return "05", "Mix"