# R5. Document all endpoints for your API.

## **1. Auth routes**

### 1. `/auth/register/`  
• Methods: POST
• Arguments: None  
• Description: Return Login id and token  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:  
```
{
    "login_id": "CHANG-HA",
    "password": "1234"
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
  "msg": "Login ID: CHANG-HA registered.",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODE0MzQ4OCwianRpIjoiZDFiN2Q4MTgtMmZmYS00NzY3LWI3ZTItMTM0ZjBlNWY5ODUzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE2NjgxNDM0ODgsImV4cCI6MTY2ODIyOTg4OH0.OJaRxCzjTMT6eag6JIQc1VWmE7Q0ZHbykVqLdS4evu0"
}
```

### 2. `/auth/staffs/`  
• Methods: GET  
• Arguments: None  
• Description: Return a list of all staff  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "staff_name": null, 
    "login_id": "admin",
    "is_admin": true
  }
]
```

### 3. `/auth/staffs/<int:id>/`  
• Methods: GET  
• Arguments: id  
• Description: Return a list of staff found by id   
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  

```
{
    "id": 1,
    "staff_name": null,
    "login_id": "admin",
    "is_admin": true
}
```

### 4. `/auth/staffs/<int:id>/`  
• Methods: PUT or PATCH  
• Arguments: id  
• Description: Return the staff filtered by the id  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:

```
{
    "login_id": "lwhaus",
    "staff_name": "CHANG-HA",
    "password": "123456"
}
```

• Response HTTP Status: 200  
• Response Body:  

```
{
  "id": 2,
  "staff_name": "CHANG-HA",
  "login_id": "lwhaus",
  "is_admin": false
}

```

### 5. `/auth/staffs/<int:id>/`  
• Methods: DELETE  
• Arguments: id  
• Description: Delete the staff filtered by the id  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Staff ID: 2 deleted successfully"
}
```

### 6. `/auth/login/`  
• Methods: POST  
• Arguments: None  
• Description: Using login_id and password to login and return token  
• Authentication: None  
• Authorization: None  
• Request Body:  

```
{
    "login_id": "admin",
    "password": "lwhaus"
}
```

• Response HTTP Status: 200  
• Response Body:  

```
{
    "login_id": "admin",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODE2OTMwNSwianRpIjoiMjgwODJhMWUtMjFjYi00YTg4LWFkZWItZTczNTUwOGRhZDk1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2NjgxNjkzMDUsImV4cCI6MTY2ODI1NTcwNX0.pRxf8pfSdTm2yZsL2B0pmhDipwMum6WfXFXlIe7Pva4"
}
```


## **2. Bookings routes**

### 1. `/bookings/` 
• Methods: GET  
• Arguments: None  
• Description: Returns every bookings in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only (includes admins)  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "date": "2022-11-11",
    "time": "12:30",
    "pax": 4,
    "comment": "Test only",
    "customer": {
      "email": "test@test.com",
      "first_name": "Ryan",
      "last_name": "Evans",
      "phone": "0468426279",
      "visited": 0
    },
    "table": {
      "number": 4,
      "seats": 4
    }
  }
]
```

### 2. `/bookings/<int:id>/` 
• Methods: GET  
• Arguments: id  
• Description: Returns a booking found by id  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 1,
  "date": "2022-11-11",
  "time": "12:30",
  "pax": 4,
  "comment": "Test only",
  "customer": {
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 0
  },
  "table": {
    "number": 4,
    "seats": 4
  }
}
```

### 3. `/bookings/today/` 
• Methods: GET  
• Arguments: None  
• Description: Returns a booking found by today's date  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "date": "2022-11-11",
    "time": "12:30",
    "pax": 4,
    "comment": "Test only",
    "customer": {
      "email": "test@test.com",
      "first_name": "Ryan",
      "last_name": "Evans",
      "phone": "0468426279",
      "visited": 0
    },
    "table": {
      "number": 4,
      "seats": 4
    }
  }
]
```

### 4. `/bookings/tomorrow/` 
• Methods: GET  
• Arguments: None  
• Description: Returns a booking found by tomorrow's date  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "date": "2022-11-11",
    "time": "12:30",
    "pax": 4,
    "comment": "Test only",
    "customer": {
      "email": "test@test.com",
      "first_name": "Ryan",
      "last_name": "Evans",
      "phone": "0468426279",
      "visited": 0
    },
    "table": {
      "number": 4,
      "seats": 4
    }
  }
]
```

### 5. `/bookings/<string:year>/<string:month>/<string:day>/` 
• Methods: GET  
• Arguments: year, month, day  
• Description: Returns a booking found by specific date  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "date": "2022-11-11",
    "time": "12:30",
    "pax": 4,
    "comment": "Test only",
    "customer_id": 100,
    "customer": {
      "email": "test@test.com",
      "first_name": "Ryan",
      "last_name": "Evans",
      "phone": "0468426279",
      "visited": 0
    },
    "table": {
      "number": 4,
      "seats": 4
    }
  }
]
```

### 6. `/bookings/mybookings/` 
• Methods: POST  
• Arguments: None  
• Description: Returns all bookings a customer has and had  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Customer only (staff has no authorization)  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "date": "2022-11-11",
    "time": "12:30",
    "pax": 4,
    "comment": "Test only",
    "table": {
      "number": 4,
      "seats": 4
    }
  }
]
```

### 7. `/bookings/new/` 
• Methods: POST  
• Arguments: None  
• Description: Take json to create a new booking to the DB  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Customer only (staff has no authorization)  
• Request Body: 
```
{
    "date": "2022-11-15",
    "time": "11:30",
    "pax": 6
}
```  
• Response HTTP Status: 201  
• Response Body:  
```
{
  "id": 2,
  "date": "2022-11-15",
  "time": "11:30",
  "pax": 6,
  "comment": null,
  "customer": {
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 1
  },
  "table": {
    "number": 20,
    "seats": 8
  }
}
```

### 8. `/bookings/new/admin/`  
• Methods: POST  
• Arguments: None  
• Description: Take json to create a new booking to the DB by admin  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: 
```
{
    "date": "2022-11-16",
    "time": "11:45",
    "pax": 3,
    "customer_id": 100
}
```  
• Response HTTP Status: 201  
• Response Body:  
```
{
  "id": 8,
  "date": "2022-11-16",
  "time": "11:45",
  "pax": 3,
  "comment": null,
  "customer_id": 100,
  "customer": {
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 6
  },
  "table": {
    "number": 9,
    "seats": 4
  }
}
```

### 9. `/bookings/<int:id>/`  
• Methods: PUT or PATCH  
• Arguments: id  
• Description: modify a booking by customer  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Customer only  
• Request Body:

```
{
    "comment": "This is for test only"
}
```

• Response HTTP Status: 200  
• Response Body:  

```
{
  "id": 7,
  "date": "2022-11-15",
  "time": "11:30",
  "pax": 6,
  "comment": "This is for test only",
  "customer": {
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 6
  },
  "table": {
    "number": 20,
    "seats": 8
  }
}
```

### 10. `/bookings/<int:id>/`  
• Methods: DELETE  
• Arguments: id  
• Description: Delete the booking filtered by the id  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:   
```
{
  "msg": "Booking ID 7 deleted successfully"
}
```

## **3. Customers routes**

### 1. `/customers/` 
• Methods: GET  
• Arguments: None  
• Description: Returns all customers in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only (includes admins)  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 100,
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 6
  }
]
```

### 2. `/customers/<int:id>/` 
• Methods: GET  
• Arguments: id  
• Description: Returns a customer found by id  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only (includes admins)  
• Request Body: None   
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 100,
  "email": "test@test.com",
  "first_name": "Ryan",
  "last_name": "Evans",
  "phone": "0468426279",
  "visited": 6
}
```

### 3. `/customers/<string:f_name>/` 
• Methods: GET  
• Arguments: f_name  
• Description: Returns a customer found by first name  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only (includes admins)  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 100,
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 6
  }
]
```

### 4. `/customers/<string:f_name>/<string:l_name>/` 
• Methods: GET  
• Arguments: f_name, l_name  
• Description: Returns a customer found by full name  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only (includes admins)  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 100,
    "email": "test@test.com",
    "first_name": "Ryan",
    "last_name": "Evans",
    "phone": "0468426279",
    "visited": 6
  }
]
```

### 5. `/customers/join/` 
• Methods: POST  
• Arguments: None  
• Description: Take json to create a new customer to the DB  
• Authentication: None  
• Authorization: None
• Request Body: 
```
{
    "email": "test2@test.com",
    "password": "lwhaus",
    "first_name": "john",
    "last_name": "smiths",
    "phone": "0468426279"
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
    "msg": "test2@test.com registered. Welcome John.",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODE3NDkxNSwianRpIjoiOWNmYmJiNWMtNjMzNy00YzQ4LTgyMGQtZDczYTdjZWNiZDNiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEwMSIsIm5iZiI6MTY2ODE3NDkxNSwiZXhwIjoxNjY4MjYxMzE1fQ.-LrOUkHsvGuej4aLsljjy0iUJhJaRPlcHixYvs-woPk"
}
```

### 6. `/customers/login/` 
• Methods: GET  
• Arguments: None  
• Description: Take json and check if it matches in the db to login a new customer  
• Authentication: None  
• Authorization: None  
• Request Body: 
```
{
    "email": "test2@test.com",
    "password": "lwhaus"
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
    "msg": "Welcome. John Smiths",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODE3NTMxMCwianRpIjoiZDc0OGRlMTktNjViZS00ZTA4LWI1NjctZmIxZjcyYjNjNjNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEwMSIsIm5iZiI6MTY2ODE3NTMxMCwiZXhwIjoxNjY4MjYxNzEwfQ.rVRTc6YXtc9kVgMg-b9-v0RaZOr9daxw9PiswCOUb2I"
}
```

### 7. `/customers/<int:id>/` 
• Methods: DELETE  
• Arguments: id  
• Description: Find a customer by id then delete from the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Customer id:101 John Smiths deleted successfully"
}

```

### 8. `/customers/<int:id>/` 
• Methods: PUT or PATCH  
• Arguments: id  
• Description: Find a customer by id and take json to update   
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: 
```
{
    "email": "test2@test.com",
    "password": "lwhaus",
    "first_name": "john",
    "last_name": "smiths",
    "phone": "0468426279"
}
```  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 100,
  "email": "test2@test.com",
  "first_name": "john",
  "last_name": "smiths",
  "phone": "0468426279",
  "visited": 6
}
```


## **4. Foods routes**

### 1. `/foods/` 
• Methods: GET  
• Arguments: None  
• Description: Returns all foods in the db  
• Authentication: None  
• Authorization: None  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "name": "Steak Sandwich",
    "price": 25,
    "is_gf": false,
    "is_df": false,
    "is_v": false
  },
  {
    "id": 2,
    "name": "Fish&Chips",
    "price": 24,
    "is_gf": false,
    "is_df": true,
    "is_v": false
  },
    
  ...

  {
    "id": 12,
    "name": "Affogato",
    "price": 12,
    "is_gf": true,
    "is_df": false,
    "is_v": true
  }
]
```

### 2. `/foods/<int:id>/` 
• Methods: GET  
• Arguments: None  
• Description: Find a food with id  
• Authentication: None  
• Authorization: None  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 5,
  "name": "Mushroom Risotto",
  "price": 23,
  "is_gf": false,
  "is_df": false,
  "is_v": true
}
```

### 3. `/foods/<string:tag>/` 
• Methods: GET  
• Arguments: tag  
• Description: Find a food with tag  
• Authentication: None  
• Authorization: None  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "name": "Fish&Chips",
    "price": 24
  },
  {
    "name": "Beef Burger",
    "price": 26
  },
  {
    "name": "Pan fried Barramundi Fillet",
    "price": 29
  },
  {
    "name": "Steamed Veges",
    "price": 12
  }
]

```

### 4. `/foods/<string:tag1>/<string:tag2>` 
• Methods: GET  
• Arguments: tag1, tag2  
• Description: Find a food with 2 tags  
if 2 tags are the same, it directs to the single tag search endpoint.  
• Authentication: None  
• Authorization: None  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "name": "Pan fried Barramundi Fillet",
    "price": 29
  },
  {
    "name": "Steamed Veges",
    "price": 12
  }
]
```

### 5. `/foods/` 
• Methods: POST  
• Arguments: None  
• Description: Take json to create a food in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:   
```
{
    "name": "Ham Cheese Croissant",
    "price": 10,
    "is_gf": true
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
  "id": 13,
  "name": "Ham Cheese Croissant",
  "price": 10,
  "is_gf": true,
  "is_df": false,
  "is_v": false
}
```

### 6. `/foods/<int:id>/` 
• Methods: PUT or PATCH  
• Arguments: id  
• Description: Find a food with id and update it  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:   
```
{
    "price": 8,
    "is_gf": false
}
```
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 13,
  "name": "Ham Cheese Croissant",
  "price": 8,
  "is_gf": false,
  "is_df": false,
  "is_v": false
}
```

### 7. `/foods/<int:id>/` 
• Methods: DELETE  
• Arguments: id  
• Description: Find a food with id and delete it  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Food Ham Cheese Croissant deleted successfully"
}

```

## **4. Orders routes**

### 1. `/orders/` 
• Methods: GET  
• Arguments: None  
• Description: Returns all orders with nested related datas in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "date": "2022-11-11",
    "table": {
      "number": 10
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 3,
          "name": "Beef Burger"
        },
        "quantity": 2
      },
      {
        "food": {
          "id": 1,
          "name": "Steak Sandwich"
        },
        "quantity": 3
      }
    ],
    "total_price": 127,
    "is_paid": false
  },
  {
    "id": 2,
    "date": "2022-11-12",
    "table": {
      "number": 15
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 2
      }
    ],
    "total_price": 71,
    "is_paid": false
  },
  {
    "id": 3,
    "date": "2022-11-12",
    "table": {
      "number": 15
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 2
      }
    ],
    "total_price": 71,
    "is_paid": false
  }
]

```

### 2. `/orders/<int:id>/` 
• Methods: GET  
• Arguments: id  
• Description: Returns a order found by id  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 1,
  "date": "2022-11-11",
  "table": {
    "number": 10
  },
  "staff": {
    "id": 1,
    "staff_name": null
  },
  "order_id": [
    {
      "food": {
        "id": 3,
        "name": "Beef Burger"
      },
      "quantity": 2
    },
    {
      "food": {
        "id": 1,
        "name": "Steak Sandwich"
      },
      "quantity": 3
    }
  ],
  "total_price": 127,
  "is_paid": false
}
```

### 3. `/orders/today/` 
• Methods: GET  
• Arguments: None  
• Description: Find orders filtered by today's date  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 2,
    "date": "2022-11-12",
    "table": {
      "number": 15
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 2
      }
    ],
    "total_price": 71,
    "is_paid": false
  },
  {
    "id": 3,
    "date": "2022-11-12",
    "table": {
      "number": 15
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 2
      }
    ],
    "total_price": 71,
    "is_paid": false
  }
]
```

### 4. `/orders/<string:year>/<string:month>/<string:day>/` 
• Methods: GET  
• Arguments: year, month, day  
• Description: Find orders filtered by year, month, date  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 2,
    "date": "2022-11-12",
    "table": {
      "number": 15
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 2
      }
    ],
    "total_price": 71,
    "is_paid": false
  },
  {
    "id": 3,
    "date": "2022-11-12",
    "table": {
      "number": 15
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 2
      }
    ],
    "total_price": 71,
    "is_paid": false
  }
]

```

### 5. `/orders/<int:id>/` 
• Methods: DELETE  
• Arguments: id  
• Description: Find orders by id and delete it from the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Order id: 2 deleted successfully"
}
```


### 6. `/orders/<int:id>/` 
• Methods: PUT or PATCH  
• Arguments: id  
• Description: Find orders by id and update it from the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:  
```
{
    "table": 10,
    "food": 2,
    "quantity": 3
}
```  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 4,
  "date": "2022-11-12",
  "table": {
    "number": 10
  },
  "staff": {
    "id": 1,
    "staff_name": null
  },
  "order_id": [
    {
      "food": {
        "id": 5,
        "name": "Mushroom Risotto"
      },
      "quantity": 1
    },
    {
      "food": {
        "id": 2,
        "name": "Fish&Chips"
      },
      "quantity": 3
    }
  ],
  "total_price": 95,
  "is_paid": false
}

```

## 7. [KEY FUNCTION] `/orders/new/table<int:table_number>'/`
• Methods: POST   
• Arguments: table_number  
• Description: Take json data and send datas to each right table  
The table `Orders` has an associated table `Order_Food` connected with `Orders`'s PK and `Foods`'s PK. You can provide table number in URI, staff id from token and foods & quantities in json data.  
Food should be `f"food_{number}": integer`, Quantity should be `f"quantity_{number}": integer`.  
You can input more than one food with the above rule. 
Food id will be searched in `Foods` table, The foods data and quantities data will be stored in a list and they'll be stored in the association table through class function of `Orders`. 

The below is an example  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body:  
```
{
    "food_1": 5,
    "quantity_1": 1,
    "food_2": 2,
    "quantity_2": 2
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
  "id": 4,
  "date": "2022-11-12",
  "table": {
    "number": 11
  },
  "staff": {
    "id": 1,
    "staff_name": null
  },
  "order_id": [
    {
      "food": {
        "id": 5,
        "name": "Mushroom Risotto"
      },
      "quantity": 1
    },
    {
      "food": {
        "id": 2,
        "name": "Fish&Chips"
      },
      "quantity": 2
    }
  ],
  "total_price": 71,
  "is_paid": false
}

```


### 8. `/orders/today/table<int:table_number>/` 
• Methods: GET  
• Arguments: table_number  
• Description: Find orders by table number and today's date  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 4,
    "date": "2022-11-12",
    "table": {
      "number": 10
    },
    "staff": {
      "id": 1,
      "staff_name": null
    },
    "order_id": [
      {
        "food": {
          "id": 5,
          "name": "Mushroom Risotto"
        },
        "quantity": 1
      },
      {
        "food": {
          "id": 2,
          "name": "Fish&Chips"
        },
        "quantity": 3
      }
    ],
    "total_price": 95,
    "is_paid": false
  }
]

```

## **6. Payments routes**

### 1. `/payments/` 
• Methods: GET  
• Arguments: None  
• Description: Returns all payment methods in the db  
• Authentication: None  
• Authorization: None  
• Request Body: None   
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "method": "Cash"
  },
  {
    "id": 2,
    "method": "Card"
  },
  {
    "id": 3,
    "method": "Prepaid"
  }
]
```

### 2. `/payments/` 
• Methods: POST  
• Arguments: None  
• Description: Take json to create a new payment method in the db.  
Automatically it's added to VALID_PAYMENT list to verify the payment method  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:  
```
{
    "method": "paypal"
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
  "id": 4,
  "method": "Paypal"
}
```

### 3. `/payments/<int:id>/` 
• Methods: PUT or PATCH  
• Arguments: None  
• Description: Find a payment method by id and take json to update it  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body:  
```
{
    "method": "pay-pal"
}
```
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 4,
  "method": "pay-pal"
}
```

### 4. `/payments/<int:id>/` 
• Methods: DELETE  
• Arguments: None  
• Description: Find a payment method by id and delete it from the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None   
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Payment method: pay-pal deleted successfully"
}
```

## **7. Receipts routes**

### 1. `/receipts/` 
• Methods: GET  
• Arguments: None  
• Description: Returns all receipts in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "payments": {
      "method": "Card"
    },
    "orders": {
      "id": 1,
      "total_price": 127
    }
  }
]
```

### 2. `/receipts/<int:id>/` 
• Methods: GET  
• Arguments: id  
• Description: Find a receipt by id in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 1,
  "payments": {
    "method": "Card"
  },
  "orders": {
    "id": 1,
    "total_price": 127
  }
}
```

### 3. `/receipts/<int:id>/` 
• Methods: DELETE  
• Arguments: id  
• Description: Delete a receipt by id in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Receipt id: 1 deleted successfully"
}
```

### 4. `/receipts/table<int:number>/` 
• Methods: POST  
• Arguments: number  
• Description: Find an order by table number and `is_paid` is `False`, apply payment method from Json, verify whether the payment method from Json is valid then create new receipt in the db. Update `is_paid` attribute to `True` in `Order` after creating.  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Staff only  
• Request Body: 
```
{
    "method": "Cash"
}
```
• Response HTTP Status: 201   
• Response Body:  
```
{
  "id": 2,
  "payments": {
    "method": "Cash"
  },
  "orders": {
    "id": 1,
    "total_price": 127
  }
}

...
[In Order, is_paid is True now]
...
        "quantity": 2
      }
    ],
    "total_price": 127,
    "is_paid": true
  }
]

```

### 5. `/receipts/<int:id>/` 
• Methods: POST or PATCH  
• Arguments: id  
• Description: Find a receipt by id and update it with json  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: 
```
{
    "method": "Card"
}
```  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 2,
  "payments": {
    "method": "Cash"
  },
  "orders": {
    "id": 1,
    "total_price": 127
  }
}
```

## **8. Tables routes**

### 1. `/tables/` 
• Methods: GET  
• Arguments: None  
• Description: Returns all tables in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: None  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
[
  {
    "id": 1,
    "number": 1,
    "seats": 4
  },
  {
    "id": 2,
    "number": 2,
    "seats": 4
  },
  {
    "id": 3,
    "number": 3,
    "seats": 4
  },
  {
    "id": 4,
    "number": 4,
    "seats": 4
  },
  {
    "id": 5,
    "number": 5,
    "seats": 4
  },
  {
    "id": 6,
    "number": 6,
    "seats": 4
  },
  {
    "id": 7,
    "number": 7,
    "seats": 4
  },
  {
    "id": 8,
    "number": 8,
    "seats": 4
  },
  {
    "id": 9,
    "number": 9,
    "seats": 4
  },
  {
    "id": 10,
    "number": 10,
    "seats": 4
  },
  {
    "id": 11,
    "number": 11,
    "seats": 4
  },
  {
    "id": 12,
    "number": 12,
    "seats": 4
  },
  {
    "id": 13,
    "number": 13,
    "seats": 4
  },
  {
    "id": 14,
    "number": 14,
    "seats": 4
  },
  {
    "id": 15,
    "number": 15,
    "seats": 4
  },
  {
    "id": 16,
    "number": 16,
    "seats": 8
  },
  {
    "id": 17,
    "number": 17,
    "seats": 8
  },
  {
    "id": 18,
    "number": 18,
    "seats": 8
  },
  {
    "id": 19,
    "number": 19,
    "seats": 8
  },
  {
    "id": 20,
    "number": 20,
    "seats": 8
  }
]
```

### 2. `/tables/<int:number>/` 
• Methods: GET  
• Arguments: None  
• Description: Find a table with **table number** not id in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: None  
• Request Body: None  
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 20,
  "number": 20,
  "seats": 8
}
```

### 3. `/tables/` 
• Methods: POST  
• Arguments: None  
• Description: Take json to create new table in the db  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: 
```
{
    "number": 25,
    "seats": 6
}
```
• Response HTTP Status: 201  
• Response Body:  
```
{
  "id": 21,
  "number": 25,
  "seats": 6
}
```

### 4. `/tables/<int:id>/` 
• Methods: DELETE  
• Arguments: id  
• Description: Find a table with id and delete it  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: None   
• Response HTTP Status: 200  
• Response Body:  
```
{
  "msg": "Table ID: 21, Number: 25 deleted successfully"
}
```

### 5. `/tables/<int:number>/` 
• Methods: PUT or PATCH  
• Arguments: number  
• Description: Find a table with **table number** and update it with json  
• Authentication: @jwt_required() with Bearer token  
• Authorization: Admin only  
• Request Body: 
```
{
    "number": 35,
    "seats": 8
}
```
• Response HTTP Status: 200  
• Response Body:  
```
{
  "id": 22,
  "number": 35,
  "seats": 8
}
```

