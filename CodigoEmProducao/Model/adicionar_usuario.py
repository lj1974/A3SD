
import uuid

def cadastrar_usuario(cursor, array):
    funcionarios = [
        {'idusuario': str(uuid.uuid4()), 
         'nomeusuario': array[1], 
         'cpfusuario': array[2], 
         'anonascimento': array[3], 
         'cargousuario': array[4]},
        
    ]

    for funcionario in funcionarios:
        cursor.execute("INSERT INTO Usuarios (idusuario, nomeusuario, cpfusuario, anonascimento, cargousuario) VALUES (?, ?, ?, ?, ?)",
                       (funcionario['idusuario'], funcionario['nomeusuario'], funcionario['cpfusuario'], funcionario['anonascimento'], funcionario['cargousuario']))


    return True
   
    
    

