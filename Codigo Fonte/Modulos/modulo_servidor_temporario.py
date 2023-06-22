

connections = []
servidor_conectado = 0
is_servidor_ativo = True


def iniciar_eleicao():

    i = 0
    while True:
        servidor_escolhido = connections[i]
        
        if(servidor_conectado == servidor_escolhido):
            i+=1
        else:
            servidor_conectado = servidor_escolhido
            break
    
    return servidor_escolhido

def atribuir_id_processo():
    return len(connections) + 1

    