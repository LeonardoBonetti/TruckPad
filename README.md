# TruckPad
A API que conecta o Caminhoneiro à Carga :truck: :factory:

## Como rodar o Projeto
 1. [Configurar o banco de dados](https://github.com/LeonardoBonetti/TruckPad#configura%C3%A7%C3%A3o-do-banco-de-dados)
 2. Instale as dependências `pip install -r requirements.txt `
 3. No arquivo *`app/gmaps.py`* insira sua chave de API do Google Maps (informada no email):
    ```
    gmaps = googlemaps.Clisent(key='Add Your Key here')
    ```
 4. Inicie o projeto `python run.py`
 5. Qualquer dúvida ou ajuda, estou a disposição :iphone: 11 94937-0262

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
 
 ## Testes
  1. A API possui testes que validam seus endpoints e uma vez dentro do diretório raiz do projeto, para realizar os testes basta executar o seguinte comando em seu terminal:
  
     ```
     pytest
     ```
