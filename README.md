# TruckPad
A API que conecta o Caminhoneiro à Carga

## Como rodar o Projeto
 1. [Configurar o banco de dados](https://github.com/LeonardoBonetti/TruckPad#database-configuration)
 2. Instale as dependências `pip install -r requirements.txt `
 3. Inicie o projeto `python run.py`

## Documentação da API
[Documentação das requisições](https://github.com/LeonardoBonetti/TruckPad/blob/master/API%20Documentation.md)

## Configuração do banco de dados
 1. Você irá precisar do MYSQL Server
 2. Para autenticar-se no banco, você terá duas opções:
     1. Criar um usuário e conceder acesso através dos comandos:
     
         ```
         CREATE USER 'admin'@'localhost' IDENTIFIED BY 'L1v2f3s4';
         GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
         ```
     2. Alterar a configuração contida no arquivo `config.py` na raiz do projeto
     
 3. Dentro do shell do MYSQL, rodar o script de criação que está na raiz do projeto chamado `sqldb_create.sql` com o seguinte comando:
 
     ```
     mysql -u <myuser> -p < sqldb_create.sql
     ```
    

## Dependencias
 - pip3 install flask_mysqldb==0.2.0
 - pip3 install Flask==0.12.2

## Run Project

- PYTHONPATH=. python run.py
