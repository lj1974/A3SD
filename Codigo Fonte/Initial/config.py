import subprocess

def executar_arquivo(nome_arquivo):
    try:
        subprocess.run(["python", nome_arquivo])
    except FileNotFoundError:
        print("Arquivo não encontrado: " + nome_arquivo)


executar_arquivo("onsell_schema.py")
executar_arquivo("usuarios.py")
executar_arquivo("redes.py")
executar_arquivo("lojas.py")
executar_arquivo("vendas.py")


