### Recomendação

Recomendamos que utilize o Postman para consumir a API enquanto desenvolve e faz testes:
https://www.getpostman.com/

Após a instalação, você poderá importar a nossa coleção de requisições com toda a configuração pronta através do botão abaixo:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d72d3fa7fd6e168e69ab)

Caso não consiga ver o botão utilize este link:  https://app.getpostman.com/run-collection/d72d3fa7fd6e168e69ab


### Métodos
- **Driver**
    - [get_drivers](#get_drivers): Retorna uma lista de todos os motoristas.
    - [get_driver](#get_driver): Retorna um motorista a partir de seu ID.
    - [register_driver](#register_driver): Cadastra um motorista no sistema.
    - [update_driver](#update_driver): Atualiza os dados  de um motorista no sistema.

- **Itinerarie**
    - [get_itineraries](#get_itineraries): Retorna uma lista de itinerários cadastrados a partir de alguns filtros.
    - [register_itinerarie](#register_itinerarie): Cadastra um itinerário no sistema.
    - [finish_itinerarie](#finish_itinerarie): Finaliza um itinerári.
    - [get_grouped_itineraries](#get_grouped_itineraries): Agrupa e contabiliza o número itinerários(motoristas que passaram pelo terminal).

**get_drivers**
----
  Retorna uma lista de motoristas e suas informações, possui um parâmetro `boolean` *own_vehicle* que filtra motoristas que possuem veículo próprio ou não.

* **URL**

  /api/v1.0/drivers

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
   
   None
   
    **Optional:**
 
   `own_vehicle=[boolean]`

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK
    **Content:** 
    ```
    # WIP
    ```
 
* **Error Response:**

   None

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
  Busca um motorista e suas informações a partir de seu ID

* **URL**

  /api/v1.0/drivers/:driver_id

* **Method:**

  `GET`
  
*  **URL Params**
 
   **Required:**

   `driver_id=[int]`
   
    **Optional:**
    
    None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** 
    ```
    # WIP
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** 
    ```
    # WIP
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
  Cadastra um novo motorista no sistema a partir de informações no formato `application/json` inseridas no `request body`

* **URL**

  /api/v1.0/drivers

* **Method:**

  `POST`
  
*  **URL Params**

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
    # WIP
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    ```
    # WIP
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
  
  
