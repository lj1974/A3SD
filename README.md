# A3 - Sistemas distribuídos

 A proposta deste trabalho é desenvolver uma aplicação utilizando sockets para capturar dados relacionados às vendas em uma rede de lojas. A principal finalidade é criar uma solução eficiente que permita aos vendedores registrarem suas vendas e aos gerentes consultarem as informações registradas.
A aplicação foi projetada de acordo com os seguintes requisitos: existem dois tipos de clientes, os gerentes e os vendedores. Os vendedores têm a responsabilidade de informar ao sistema o valor de cada venda realizada, enquanto os gerentes podem consultar as informações de vendas registradas. O servidor atua como hospedeiro das informações fornecidas pelos vendedores e responde às consultas dos gerentes.
Uma funcionalidade importante da aplicação é a capacidade de eleger um servidor coordenador temporário na ausência do servidor principal. Esse coordenador temporário assume temporariamente as responsabilidades do coordenador principal até que este retorne.
A aplicação foi desenvolvida em Python, utilizando a arquitetura MVC (Model-View-Controller), um modelo que divide a aplicação em três camadas: Model, Controller e View. Não foi utilizada uma interface gráfica na aplicação, apenas uma interface textual, com o intuito de demonstrar os processos que estão ocorrendo.



### 🔧 Instalação

O tutorial descrito abaixo irá te direcionar na instalação de todas as tecnologias usadas, para que você possa testá-las em seu próprio ambiente. 

Clonar Repositório:

```
	   git clone https://github.com/lj1974/A3SD
```

Após copiar, executar os comandos abaixo no terminal, na pasta raiz:
```
    	Python socket_servidor_thread.py
```
E depois:
```
    	Python socket_cliente.py
```

### 🔧 Utilização

Para fazer login, basta apenas digitar um CPF. Se gostaria de criar uma conta propria, digite o seu CPF e logo após entrará na tela de cadastro caso não possua um cadastro já feito para o seu CPF.

O banco de dados possue dados que podem ser visualizados assim que rodar o codigo pela primeira vez, para testar, tente entrar com um dos usuarios previamente cadastrados:
LOGIN DE VENDEDOR: 12345678901
LOGIN DE GERENTE: 56789012345

Caso não funcione significa que os dados iniciais do banco de dados não foram cadastrados imediatamente! Nesse caso, siga as instruções a seguir:

Navegue até a pasta "Initial" e execute o comando abaixo:
```
   python config.py
```

Pronto! 


## 🛠️  Bibliotecas utilizadas 🚀🚀

Em sequência iremos citar as bibliotecas utilizadas na aplicação, e seus comandos para a importação, junto com uma breve descrição de sua funcionalidade:

```
* SQlite3 - Uma biblioteca em linguagem C que implementa uma base de dados SQL embutida, com todas as funcionalidades, incorporado diretamente ao programa , o que permite acesso ao banco de dados sem a necessidade de um SGBD. Não requer uma instalação separada, nem precisa de um servidor dedicado.
	‘import sqlite3’
      	 
* Biblioteca OS Python - Biblioteca padrão para interagir com o sistema operacional em que o python está sendo executado.
‘import os’
        	
* Biblioteca ‘datetime’ - Biblioteca utilizada para formatação de data e hora.
        	‘import datetime’

* Biblioteca ‘sockets’ -  Biblioteca que permite que ocorra a comunicação entre os processos.
	‘import socket’
        	
* Biblioteca ‘load_dotenv’ - Biblioteca utilizada para acessar as variáveis do arquivo .env. Ela busca automaticamente as variáveis definidas no arquivo .env e as adiciona ao ambiente de execução do programa.
	‘import load_dotenv’
        	
* Biblioteca ‘re’ - Biblioteca que verifica se a condição foi cumprida, o regex.
        	‘import re’
* Biblioteca ‘threading’ - Biblioteca que permite a utilização de múltiplos processos no servidor.
        	‘import threading’

* Biblioteca ‘uuid’ - Biblioteca utilizada para gerar id’s únicas e universais com valor de 128 bits.
	‘import uuid’

```



## 🛠️ Construído em :


* Python


## Conclusão

Nossa equipe tentou nesse projeto, e em partes conseguimos, desenvolver uma aplicação utilizando os sockets, com a finalidade de gerenciar a captura dos dados referente às vendas de uma loja. Nossa intenção aqui foi projetar uma aplicação que atenda tanto a necessidades do gerente, na consulta das informações registradas, mas também que atenda aos vendedores, no registro dessas informações. Infelizmente, não conseguimos finalizar a parte do algoritmo de eleição, e pedimos desculpas.




 
