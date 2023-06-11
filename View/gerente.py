     
from A3SD.View.redes import escolher_rede
from A3SD.View.users import escolher_vendedor
from A3SD.View.venda import consultar_total_vendedor
from A3SD.View.venda import consultar_vendas_rede

def total_vendedor():
    
    vendedor_selecionado = escolher_vendedor()
    id_vendedor = vendedor_selecionado['idusuario']
    
    return consultar_total_vendedor(id_vendedor)


def total_vendas_rede():
    rede_selecionada = escolher_rede()
    id_rede = rede_selecionada['idrede']
    
    return consultar_vendas_rede(id_rede)