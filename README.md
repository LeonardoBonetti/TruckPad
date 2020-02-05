# TruckPad
A API que conecta o Caminhoneiro à Carga :truck: :factory:

## Como subir o Projeto
 
 `docker-compose` possui as imagens [python 3](https://hub.docker.com/_/python), [mysql](https://hub.docker.com/_/mysql) e [adminer](https://hub.docker.com/_/adminer).

 Suba o compose: 

 `docker-compose up -d` 

 ** *Futuramente será implementado um proxy reverso para estar tratando as requisições do Flask.*

## Documentação da API
[Documentação da API](https://github.com/LeonardoBonetti/TruckPad/blob/master/docs/API%20Documentation.md)


## Testes
  1. A API possui testes que validam seus endpoints e uma vez dentro do diretório raiz do projeto, para realizar os testes basta executar o seguinte comando em seu terminal:
  
     ```
     pytest
     ```
