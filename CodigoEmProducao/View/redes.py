
import datetime
import re
from Model.consultar_rede import listar_ids_e_nomes

def escolher_rede():
   
   while True:
        print("\n\nLista de Redes:\n")
        redes = listar_ids_e_nomes()
        for i, rede in enumerate(redes, start=1):
            print(f"{i}. {rede[1]}")

        num_rede = input('\nDigite o número da Rede:')
        if num_rede.isdigit():
            num_rede = int(num_rede)
            if num_rede < 1 or num_rede > len(redes):
                print("Número da rede inválido. Tente novamente.")
            else:
                return redes[num_rede - 1]
        else:
            print("digite um numero.")
        
def escolher_data_para_rede():
    
    while True:
        data_str = input("Digite a DATA INICIAL no formato dia/mês/ano sem pontuação: (Ex: 01022022)")
        if verificar_data(data_str):
            data_inicial = mudar_data_formato(data_str)
            break
        
    
    while True:
        data_str2 = input("Digite a DATA FINAL no formato dia/mês/ano sem pontuação: (Ex: 01022022)")
        if verificar_data(data_str2):
            data_final = mudar_data_formato(data_str2)
            if verificar_maior_data(data_inicial, data_final):
                break
            else:
                print('data FINAL precisa ser maior que data INICIAL')

    # Retorna as partes da data como números inteiros
    return data_inicial, data_final

def verificar_data(data_str):
    # Verifica se a string está no formato correto (DDMMYYYY)
    if not re.match(r"\d{8}$", data_str):
        print('Data no formato incorreto.')
        return False

    dia = int(data_str[:2])
    mes = int(data_str[2:4])

    # Verifica se os valores estão dentro das faixas válidas
    if dia < 1 or dia > 31:
        print('o dia precisa ser um numero de 01 a 31')
        return False
    if mes < 1 or mes > 12:
        print('o mes precisa ser um numero de 01 a 12')
        return False

    return True


def mudar_data_formato(data_str):
    dia = str(data_str[:2]).zfill(2)
    mes = str(data_str[2:4]).zfill(2)
    ano = str(data_str[4:])
    
    data = '-'.join([str(ano), str(mes), str(dia)])

    return data



def verificar_maior_data(data_inicial, data_final):
    dia_inicial, mes_inicial, ano_inicial = map(int, data_inicial.split('-'))
    dia_final, mes_final, ano_final = map(int, data_final.split('-'))
    
    if ano_final > ano_inicial:
        return True
    elif ano_final == ano_inicial and mes_final > mes_inicial:
        return True
    elif ano_final == ano_inicial and mes_final == mes_inicial and dia_final > dia_inicial:
        return True
    else:
        return False