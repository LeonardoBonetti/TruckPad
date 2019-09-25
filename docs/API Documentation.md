### Recomendação

Recomendamos que utilize o Postman para consumir a API enquanto desenvolve e faz testes:
https://www.getpostman.com/

Após a instalação, você poderá importar a nossa coleção de requisições com toda a configuração pronta através do botão abaixo:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d72d3fa7fd6e168e69ab)

Caso não consiga ver o botão utilize este link:  https://app.getpostman.com/run-collection/d72d3fa7fd6e168e69ab


### Métodos
- **Driver**
    - [get_drivers](#get_drivers): Retorna uma lista de motoristas.
    - [get_driver](#get_driver): Retorna um motorista.
    - [register_driver](#register_driver): Cadastra um motorista.
    - [update_driver](#update_driver): Atualiza os dados do motorista.

- **Itinerarie**
    - [get_itineraries](#get_itineraries): Retorna uma lista de itinerários cadastrados.
    - [register_itinerarie](#register_itinerarie): Cadastra um itinerário.
    - [finish_itinerarie](#finish_itinerarie): Finaliza um itinerário.
    - [get_periodical_itineraries_report](#get_periodical_itineraries_report): Agrupa e contabiliza o número de itinerários.

**get_drivers**
----
  Retorna uma lista de motoristas e suas informações. Possui um parâmetro opcional `own_vehicle=[boolean]` que serve para saber quantos caminhoneiros tem veiculo próprio.

* **URL**

  /api/v1.0/drivers

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
   
   None
   
   **Optional:**
 
   `own_vehicle=[boolean]` : Veículo próprio?

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK
    
    **Content:** 
    ```
    {
      "drivers": [
        {
          "cnh_type_id": 4,
          "date_of_birth": "Mon, 04 May 1998 00:00:00 GMT",
          "gender_id": 1,
          "id": 1,
          "last_name": "Bonetti",
          "name": "Leonardo",
          "own_vehicle": 1
        },
        {
          "cnh_type_id": 4,
          "date_of_birth": "Fri, 01 Jan 1999 00:00:00 GMT",
          "gender_id": 1,
          "id": 2,
          "last_name": "Silveira",
          "name": "Jão",
          "own_vehicle": 1
        }
      ],
      "meta": {
        "total_drivers": 2
      }
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST
     
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/drivers",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**get_driver**
----
  Retorna as informações de um único motorista a partir de seu ID.

* **URL**

  /api/v1.0/drivers/<driver_id>

* **Method:**

  `GET`
  
* **URL Params**
 
   **Required:**

   `driver_id=[int]` : `ID` do motorista
   
    **Optional:**
    
    None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK
  
    **Content:** 
    ```
    {
      "driver": {
        "cnh_type_id": 4,
        "date_of_birth": "Mon, 04 May 1998 00:00:00 GMT",
        "gender_id": 1,
        "id": 1,
        "last_name": "Bonetti",
        "name": "Leonardo",
        "own_vehicle": 1
      }
    }
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND
  
    **Content:** 
    ```
    {
      "return_message": "Driver do not exist"
    }
    ```
    
  * **Code:** 400 BAD REQUEST
  
    **Content:** 
    ```
    {
      "return_message": "driver_id must be a integer number"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/drivers/<driver_id>",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**register_driver**
----
  Cadastra um motorista.

* **URL**

  /api/v1.0/drivers

* **Method:**

  `POST`
  
* **URL Params**

    **Required:**

    None
   
    **Optional:**
    
    None

* **Data Params**

  * **Data Object:** 
  ```
  {
    "cnh_type_id" : 1,
    "date_of_birth": "1998-12-14 00:00:00",
    "gender_id": 1,
    "last_name": "Bonetti",
    "name": "Leo",
    "own_vehicle": false
  }
  ```

* **Success Response:**

  * **Code:** 201 CREATED <br />
  
    **Content:** 
    ```
    {
    "driver": {
        "cnh_type_id": 4,
        "date_of_birth": "1998-04-05 00:00:00",
        "gender_id": 3,
        "id": 1,
        "last_name": "Pereira Silva",
        "name": "rapha",
        "own_vehicle": false
      },
      "return_message": "Driver Updated"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
  
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```
    
  * **Code:** 400 BAD REQUEST <br />
   
    **Content:** 
    ```
    {
      "return_message": "JSON Object not found"
    }
    ```

* **Sample Call:**

  ```javascript
  $.ajax({
      url: "localhost/api/v1.0/drivers",
      dataType: "json",
      type : "POST",
      data: JSON.stringify(data),
      success : function(r) {
        console.log(r);
      }
  });
  ```
  
**update_driver**
----
  Atualiza os dados do motorista.

* **URL**

  /api/v1.0/drivers/<driver_id>

* **Method:**

  `PUT`
  
*  **URL Params**

    **Required:**

     `driver_id=[int]` : `ID` do motorista
   
    **Optional:**
    
    None

* **Data Params**

  * **Data Object:** 
  ```
  {
    "cnh_type_id": 4,
    "date_of_birth": "1998-04-05 00:00:00",
    "gender_id": 3,
    "last_name": "Pereira Silva",
    "name": "rapha",
    "own_vehicle": false
  }
  ```

* **Success Response:**

  * **Code:** 200 OK <br />
  
    **Content:** 
    ```
    {
        "driver": {
            "cnh_type_id": 4,
            "date_of_birth": "1998-04-05 00:00:00",
            "gender_id": 3,
            "id": 1,
            "last_name": "Pereira Silva",
            "name": "rapha",
            "own_vehicle": false
        },
        "return_message": "Driver Updated"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
  
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```
    
  * **Code:** 400 BAD REQUEST <br />
   
    **Content:** 
    ```
    {
      "return_message": "JSON Object not found"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/drivers/<driver_id>"",
      dataType: "json",
      type : "PUT",
      data: JSON.stringify(data),
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**get_itineraries**
----
  Retorna os Itinerários cadastrados de acordo com os filtros passados na URL

* **URL**

  /api/v1.0/itineraries

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
   
   None
   
    **Optional:**
 
   `initial_load_period=[datetime]` : Início do itinerário
   
   `final_load_period=[datetime]` : Fim do itinerário
   
   `truck_type=[int]` : Tipo do caminhão (olhar no final da página)
   
   `loaded=[boolean]` : Caminhão carregado ?
   
   `finished=[boolean]` : Finalizado ?
   
   `origin_state=[string]` : Estado de origem
   
   `origin_city=[string]` : Cidade de origem
   
   `destination_state=[string]` : Estado de destino
   
   `destination_city=[string]` : Cidade de destino

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK
    
    **Content:** 
    ```
    {
      "itineraries": [
        {
          "destination_address": {
            "address": "Rua Parianas",
            "city": "São Paulo",
            "id": 25,
            "lat": -23.51006460,
            "lng": -46.54488690,
            "state": "SP",
            "street_number": "75"
          },
          "driver_id": 1,
          "finished": 1,
          "id": 5,
          "load_date_time": "Mon, 23 Sep 2019 00:00:00 GMT",
          "loaded": 1,
          "origin_address": {
            "address": "Rua Tenente Otávio Gomes",
            "city": "São Paulo",
            "id": 24,
            "lat": -23.56353010,
            "lng": -46.63089410,
            "state": "SP",
            "street_number": "330"
          },
          "truck_type_description": "Caminhão 3/4",
          "truck_type_id": 1,
          "unload_date_time": "Wed, 25 Sep 2019 00:00:00 GMT"
        }
      ],
      "meta": {
        "total_itineraries": 1
      }
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST
     
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/itineraries",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**register_itinerarie**
----
  Cadastra um novo itinerário.

* **URL**

  /api/v1.0/itineraries

* **Method:**

  `POST`
  
* **URL Params**

    **Required:**

    None
   
    **Optional:**
    
    None

* **Data Params**

  * **Data Object:** 
  ```
  {
    "driver_id": 2,
    "loaded": false,
    "truck_type_id": 2,
    "load_date_time": "2020-08-26 00:00:00",
    "unload_date_time": "2020-08-30 00:00:00",
    "finished":false,
    "origin_address":"Rua Tenente Otavio Gomes",
    "destination_address": "Rua Oswaldo Cruz",
    "origin_street_number":"330",
    "destination_street_number":"400"
  }
  ```

* **Success Response:**

  * **Code:** 201 CREATED <br />
  
    **Content:** 
    ```
    {
      "itinerarie": {
        "destination_address": {
          "address": "Rua Oswaldo Cruz",
          "city": "Itaperuna",
          "id": 51,
          "lat": -21.2157926,
          "lng": -41.8892951,
          "state": "RJ",
          "street_number": "400"
        },
        "driver_id": 2,
        "finished": false,
        "id": 18,
        "load_date_time": "2020-08-26 00:00:00",
        "loaded": false,
        "origin_address": {
          "address": "Rua Tenente Otávio Gomes",
          "city": "São Paulo",
          "id": 50,
          "lat": -23.5635301,
          "lng": -46.6308941,
          "state": "SP",
          "street_number": "330"
        },
        "truck_type_description": null,
        "truck_type_id": 2,
        "unload_date_time": "2020-08-30 00:00:00"
      },
      "return_message": "Itinerarie Registered"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
  
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```
    
  * **Code:** 400 BAD REQUEST <br />
   
    **Content:** 
    ```
    {
      "return_message": "JSON Object not found"
    }
    ```

* **Sample Call:**

  ```javascript
  $.ajax({
      url: "localhost/api/v1.0/drivers",
      dataType: "json",
      type : "POST",
      data: JSON.stringify(data),
      success : function(r) {
        console.log(r);
      }
  });
  ```
  
**finish_itinerarie**
----
  Finaliza o Itinerário informado através do ID, significa que o motorista chegou ao destino

* **URL**

  /api/v1.0/itineraries/finish/<itinerarie_id>

* **Method:**

  `PUT`
  
*  **URL Params**

    **Required:**

    `itinerarie_id=[int]` : `ID` do itinerário
   
    **Optional:**
    
    None

* **Data Params**

  * **Data Object:** 
  
    None

* **Success Response:**

  * **Code:** 200 OK <br />
  
    **Content:** 
    ```
    {
      "itinerarie": {
            "destination_address": {
              "address": "Rua Parianas",
              "city": "São Paulo",
              "id": 27,
              "lat": -23.51006460,
              "lng": -46.54488690,
              "state": "SP",
              "street_number": "75"
            },
            "driver_id": 2,
            "finished": true,
            "id": 6,
            "load_date_time": "Tue, 24 Sep 2019 00:00:00 GMT",
            "loaded": 0,
            "origin_address": {
              "address": "Rua Tenente Otávio Gomes",
              "city": "São Paulo",
              "id": 26,
              "lat": -23.56353010,
              "lng": -46.63089410,
              "state": "SP",
              "street_number": "330"
            },
            "truck_type_description": "Caminhão Toco",
            "truck_type_id": 2,
            "unload_date_time": "Thu, 26 Sep 2019 00:00:00 GMT"
          },
          "return_message": "Itinerarie Finished"
        }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
  
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```
    
  * **Code:** 404 BAD REQUEST <br />
   
    **Content:** 
    ```
    {
      "return_message": "Itinerarie does not exist"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/itineraries/finish/<itinerarie_id>",
      dataType: "json",
      type : "PUT",
      data: JSON.stringify(data),
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**get_periodical_itineraries_report**
----
 Retorna o número de itinerários agrupados por um tipo periódico (diário, mensal e anual), o parâmetro `periodical_type` é obrigatório e aceita os valores: `monthly`, `daily` e `yearly`, assim como o intervalo de carga do itinerário `initial_load_period` e `final_load_period`.
* **URL**

  /api/v1.0/itineraries/periodical

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
   
   `periodical_type=[string]` : Tipo periódico (`monthly`, `daily`, `yearly`)
   
   `initial_load_period=[datetime]`: Período inicial do relatório
   
   `final_load_period=[datetime]` : Período final do relatório
   
    **Optional:**
 
   `loaded=[boolean]` : Caminhão carregado ?


* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK
    
    **Content:** 
    ```
    {
      "final_period": "2021-01-01 00:00:00",
      "initial_period": "2019-01-01 00:00:00",
      "loaded": null,
      "periodic_reports": [
        {
          "count": 7,
          "period": "2019-09"
        },
        {
          "count": 1,
          "period": "2019-10"
        },
        {
          "count": 3,
          "period": "2020-08"
        },
        {
          "count": 1,
          "period": "2020-09"
        },
        {
          "count": 2,
          "period": "2020-10"
        }
      ],
      "periodical_type": "monthly"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST
     
    **Content:** 
    ```
    {
      "errors_field": {
        
      },
      "return_message": "There is some erros in your request see errors_field"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/itineraries/periodical ",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  


#### Dados estáticos:


##### Tipos de caminhão (truck_type)

| ID | Description            |
|---------------|------------------------|
| 1             | Caminhão 3/4           |
| 2             | Caminhão Toco          |
| 3             | Caminhão Truck         |
| 4             | Carreta Simples        |
| 5             | Carreta Eixo Extendido |
<br>

 ##### Tipos de CNH (cnh_type)

| ID | Description |
|---------------|-------------|
| 1             | A           |
| 2             | B           |
| 3             | C           |
| 4             | D           |
| 5             | E           |
<br>

##### Tipos de gênero (gender_type)

| ID | Description |
|---------------|-------------|
| 1             | Masculino   |
| 2             | Feminino    |
| 3             | Outro       |
<br>
  
  
