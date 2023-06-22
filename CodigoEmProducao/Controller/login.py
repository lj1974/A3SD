from View.users import leitura_cpf


def realizar_login():
    result = leitura_cpf()
    return '01.1', result
