# TruckPad
A API que conecta o Caminhoneiro à Carga

## Como rodar o Projeto
 1. [Configurar o banco de dados](https://github.com/LeonardoBonetti/TruckPad#configura%C3%A7%C3%A3o-do-banco-de-dados)
 2. Instale as dependências `pip install -r requirements.txt `
 3. Inicie o projeto `python run.py`

## Documentação da API
[Documentação da API](https://github.com/LeonardoBonetti/TruckPad/blob/master/docs/API%20Documentation.md)

## Configuração do banco de dados
 1. Você irá precisar do [MYSQL Server](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)
 2. Para autenticar-se no banco, você terá duas opções:
     1. Criar um usuário e conceder acesso através dos comandos dentro do shell mysql:
     
         ```
         CREATE USER 'admin'@'localhost' IDENTIFIED BY 'L1v2f3s4';
         GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
         ```
     2. Alterar a configuração contida no arquivo `config.py` na raiz do projeto
     
 3. Dentro do shell do MYSQL, rodar o script de criação que está na raiz do projeto chamado `setup.sql` com o seguinte comando:
 
     ```
     mysql -u <myuser> -p < setup.sql
     ```
