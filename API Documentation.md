### Recomendation

We recomend that you use Postman to consume our API on dev environment : https://www.getpostman.com/

After Install, you can import our collection with all set up requests through the button below

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d72d3fa7fd6e168e69ab)


### Methods
- [get_drivers](#get_drivers)
- [get_driver](#get_driver)
- [register_driver](#register_driver)

**get_drivers**
----
  Return a list of all drivers.

* **URL**

  /api/v1.0/driver

* **Method:**

  `GET`
  
*  **URL Params**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ```
    {
      "drivers": [
        {
          "cnh_type_id": 2,
          "date_of_birth": "1998-05-04 00:00:00",
          "gender_id": 1,
          "id": 1,
          "last_name": "Bonetti",
          "name": "Leonardo"
        },
        ...
      ]
    }
    ```
 
* **Error Response:**

   None

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/driver",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**get_driver**
----
  Search for a driver through your ID.

* **URL**

  /api/v1.0/driver/<driver_id>

* **Method:**

  `GET`
  
*  **URL Params**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** 
    ```
    {
      "driver": {
        "cnh_type_id": 1,
        "date_of_birth": "2019-12-01 00:00:00S",
        "gender_id": 2,
        "id": 4,
        "last_name": "Last Name",
        "name": "Name"
      }
    }
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'Not found'}`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/driver/<driver_id>",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**register_driver**
----
  Register a new driver passing a Driver JSON Object.

* **URL**

  /api/v1.0/driver

* **Method:**

  `POST`
  
*  **URL Params**

   None

* **Data Params**

  * **Data Object:** 
  ```
    {
      "cnh_type_id": 1,
      "date_of_birth": "2019-12-01 00:00:00",
      "gender_id": 2,
      "id": 4,
      "last_name": "Last Name",
      "name": "Name"
    }
  ```

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:** 
    ```
    {
      "driver": {
        "cnh_type_id": 1,
        "date_of_birth": "2019-12-01 00:00:00",
        "gender_id": 2,
        "id": 4,
        "last_name": "Last Name",
        "name": "Name"
      },
      "return_message": "Driver Registered"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    ```
    {
      "driver": {
        "cnh_type_id": 1,
        "date_of_birth": "2019-12-01 00:00:00",
        "gender_id": 2,
        "id": 4,
        "last_name": "Last Name",
        "name": "Name"
      },
      "return_message": "Driver Registered"
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "localhost/api/v1.0/driver/<driver_id>",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
  
