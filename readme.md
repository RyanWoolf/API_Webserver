# T2A2 API WebServer Project
### 13410 CHANG-HA LEE

------------------------
<h1 align="center"> <br><b>LionWolf Haus <br>
POS system</b> <br><br></h1>


### Welcome back to LionWolf Haus project. The owner got impressed your task at the last time which is to solve new staffs get work and he wants you give another task. 
--------------------------------

### Before run the program, please check this page. [Click Here](.docs/../docs/before_to_run.md)
-----------
**Link to Github repo**

https://github.com/RyanWoolf/ChanghaLee_T2A2

----------------------------------------------------------------

### <br>**R1. Identification of the problem you are trying to solve by building this particular app.**

Recently, the POS system service provider that LionWolf Haus's been using has been informed that the service fee will increase, There are so many functions in the system but the restaurant uses only not even half of them but only basic things such as adding/deleting staff, taking orders from a table, storing/printing receipts, taking a booking from customers and admin etc. 

The owner of the restaurant used to think that the previous service fee was understandable but it is not clear whether the restaurant would use full functions in future and paying the increased fee every month is a loss to the business. Moreover, it does not show such fast performance either possibly because it provides too many functions with not powerful server computer from the service company. Also, sometimes they have been troubled by the app that frequently frozen, stopped and terminated. This is not a small issue from a business standpoint and the owner thinks it'll be difficult to guarantee quick and accurate service to customers. 

For the replacement service, The owner mentioned a few key functions below that are essential to the program.

1. Add/delete staff using Authentication & Authorization.
   - As POS system should be related to budget, it's mandatory to have a strong authentication mechanism. URL might be exposed to the public depending on where the server'd be based, but to access to the Orders or Payments needs to be protected. 
2. Admin can make/delete Menu with price, ingredients, etc
   - By implementing Authorization, Admin can control the details of menu items. Ingredients will indicate simple details (due to the full ingredients will be displayed on the actual menu), what needs to be implemented in DB is `is_GF` and `is_DF` so that the waiting staff can guarantee it to customers before they put the order through.
3. Managing previous receipts
   - Storing previous transactions is important for the business in case of lots of other situations. The history is better to be stored in DBs rather than the app itself.
4. History of taking orders with staff id
   - Logging the history can make the process of transactions easier. It makes it quick to identify what happened during the service.
5. Reservation system
   - Most of reservation in restaurants need simple details from customers such as name, email, date and time. This can be implemented by a third party app, such as `NowBookit`, `Square`, `Opentable`, `The fork` and else.
6. and possibly more

The owner believes that this will suffice for the business. However, he also asked to leave possibility for adding features that might be needed in the future. He hopes there's no heavy requirements to run this program so that one of the computer the restaurant has can be the main server computer and if possible, it's to be make by Open source too.

The client asked to complete the project within two weeks and has promised a substantial commission fee upon completion.


### <br>**R2. Why is it a problem that need solving?**

As mentioned above, the current POS server is not implemented in the restaurant itself, but connects to another server computer remotely through the internet and runs the app there to execute. It seems like very normal why the app got frozen or stopped occasionally. 

At first, the previous company started the service with moderate prices and it was a good choice for the new start business. But every time the restaurant needed problem solutions, they had to wait long for it to be solved. The owner believes that if they have a new, lightweight POS system from this project and operate it inside the restaurant, there will be much faster reactions or solutions to solve issues and moreover, they don't have to pay a service fee. He believe it's so much better choice than continuing to use the previous service, which will be more expensive.


### <br>**R3. Why have you chosen this database system. What are the drawbacks compared to others?**

<center><img src="./docs/dbms_rank.png"  width="450"><br><sup>[Image from 'DB-ENGINES'(https://db-engines.com/en/ranking)]</sup></center>

The client requested that the database system used in this project be open source. He wants it that's trustful to the most basic functions and fast. Based on experience, I've concluded that PostgreSQL is the right database system for this project. 

First, as requested by the client, it's open source, so there are no restrictions on usability, no license fees, so the operation cost is low. Also it's good on security through host-based access control, object-level authority, and data encryption between the client and the network through communication. 

Second, In order to add more complex functions later, he requested to make it flexible so that it'd be easy to respond. PostgreSQL, unlike other relational database system, provides various data such as operators, complex data types, aggregate functions, data type converters, and extension functions. Thanks to this functions that allows users to create DB objects arbitrarily at the SQL level, it is possible to quickly solve future problems. In addition, it is compatible with various programming languages ​​and platforms, and it is highly recoverable, enabling point-in-time recovery with archiving and hot backup devices even if previous history is accidentally lost. 

Finally, PostgreSQL can create a table like Java or C++ programming language create and inherit a table to create sub-tables. It seems useful when you need an inherited table, such as when a receipt needs to be linked to an order in a restaurant.

But that doesn't mean everything is perfect, it has chosen scalability and compatibility at the expense of speed compared to our competitors. It may not be the best choice if you need the fastest read operations.

Second, its many features and adherence to standard SQL syntax might make it a lot of work even for a simple database setup. So, if speed is important and you have a lot of read work, MySQL could be a more viable choice. 

Finally, it's also not suitable if you just want a simple cloning operation mainly. PostgreSQL also has strong support for cloning, but it's still a relatively new feature, and MySQL might be a better option for this too.


### <br>**R4. Identify and discuss the key functionalities and benefits of an ORM**

One of the important parts of the program in which the database is built is the persistence of persistence, which refers to the characteristics of data that does not disappear even when the program that created it is terminated. Data without this only exists in memory and is lost when the program terminates. However, persistence is given to data by permanently storing it to memory using a file system, relational database.

ORM is an short word of **Object Relational Mapping** and means configuration mapping between objects and relational databases. This is a tool used to describe models in the MVC pattern. Object-Oriented Programming uses classes and relational databases use tables, and this is where the inconsistency arises. In other words, when an object is stored in a relational database, a problem arises when you want to retrieve and manipulate the data in the relational database as an object, and this problem will cause spending more time and money if the developer does not have ORM. ORM solves these inconsistencies by automatically generating SQL based on the relationship between objects.

The advantages we can get from ORM are:

1. By manipulating the db through the method of the class rather than the SQL statement, the readability of the code is increased as it is much shorter and more concise than SQL embedded. It also eliminates or drastically reduces the use of ancillary code such as declarations, assignments, and terminations, helping developers to consider only object-oriented approaches rather than the mixed approach of object-oriented and SQLs procedural-sequential approaches.

2. When changing the data structure, only the object needs to be changed, so maintainability is better. Because ORM is written independently and the objects can be reused, it is advantageous to solidify the design pattern in the form of merging the data processed in the model with the view by the controller.

3. Most of ORMs are not dependent on DBMS, but not only the implementation methods but also the data types, which allows programmers to focus on objects, so even the huge task of replacing DBMS takes relatively little risk and time.

The OOP language we will use is Python and RDBMS is PostgreSQL. The ORM we will be using requires Flask-SQLAlchemy and Psycopg2, an adapter that will help connect to the database. It's a kind of dependency that will help us do our job mostly in the invisible area.

### **Below we look at some of the functionality features of SQLAlchemy.**

The most important part of SQLAlchemy is Core and ORM.
Core is the internal part of SQLAlchemy. It manages how the querying works or connection to the database and more for the structure of itself.

ORM is the main functionality part of SQLAlchemy. It builds upon Core to provide a means of working with a domain object model mapped to a database schema.

![SQLAlchemy](docs/sqla_arch.png) . 



1. Connecting database
   - Engine is the starting point of SQLAlchemy. This approaches to the database connected in DBAPI(DataBase Application Programming Interface) through Pool or Dialect. Pool is an abstract class of DB Connection pool, it creates a connection through `connect()`. Dialect is the system SQLAlchemy uses to communicate with various types of DBAPI implementations and databases.
  
   - `SQLALCHEMY_DATABASE_URI` : The database URI that should be used for the connection. 

    ```python
    # ex)
    app.config['SQLALCHEMY_DATABASE_URI']='DMBS+Adapter://username:password@localhost/mydatabase'
    ```

2. Table mapping by declaring Models
   - Make an instance from SQLAlchemy class with `app` in it that we can interact using SQLAlchemy. the instance's generally named as `db`. db has another class called `Model` that's a declarative base which can be used to declare models.
   - By declaring a class inheriting db.Model, we wound up linking and connection to SQLAlchemy's mappings between python classes and tables.
  
   - `__tablename__` : If you don't set the table name, SQLAlchemy will use the lowercase same name from the class name
   - `db.Column` : for easy understanding, it literally means setting a column in the table.
   - `db.String`, `db.Date`, `db.Integer`, `db.Boolean` etc : datatypes that can be used in flask-SQLAlchemy. For more details, visit [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) 

    ```python
    # ex)
    db = SQLAlchemy(app)

    class Customer(db.Model): 
        __tablename__ = 'customers' 
        # Set the table name. If not set, SQLAlchemy will use the lowercase name from the class name

        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(), nullable=False)
        last_name = db.Column(db.String(), nullable=False)
        # Column will declare the column in the database
        # Datatyps (String, Integer and elses)
    ```

3. Create Schema
   - `db.create_all()` detects meta datas in models and creates a new schema in the db
   - `db.drop_all()` deletes all meta datas stored in the db. Once it's dropped, never can be restored.
   - Good way to use them is in CLI commands

    ```python
    # ex)
    @app.cli.command('create')
    def create_db():
        db.create_all()

    @app.cli.command('drop')
    def drop_db():
        db.drop_all()
    ```

4. Querying

   To query SQL statement and execute in Python is not easy and efficient. That's the reason ORM comes to the best idea to implement DBAPI. The basic concept is Creating a statement using `db.select()` or `db.query()` which is a legacy method.
   
   it lets you write SELECT statements but it means just CREATE the statement not execute it. You can add conditions such as `filter_by(condition)`, `order_by(condition)`, `where(condition)`, etc.
   


   ```python
   # ex)
   stmt = db.select(Table).order_by(Table.number)
   print(stmt)

   # it's the same as the below in SQL statement 
   SELECT tables.id, tables.number, tables.seats 
   FROM tables ORDER BY tables.number
   ```




5. Session
   - **This is the ORM mapping functions.**
   - `db.session` object lets you manage your database changes
   1. `db.session.add(object)` to insert data and `db.session.commit()` method to commit new thing or the change.
      1) Create the Python object
      2) Add it to the session
      3) Commit the session
   2. `db.session.delete(object)` to delete data. 
   3. `db.session.commit()` to apply the changes includes added or deleted data to the database.  If you miss this step after any changes, it's only left in the memory part and not applying to the actual database.

    ```python
    # ex)
    customer1 = Customer(
        first_name = 'CHANG-HA',
        last_name = 'Lee'
    )

    db.session.add(customer1)
    db.session.commit() # customer1 is added and committed

    db.session.delete(customer1)
    db.session.commit() # customer1 is removed
    ```
    4. `db.session.execute()` to execute the statement you created. It returns SQLAlchemy class but you can jasonify using `JSONIFY` from Flask. Using `db.session.execute(statement)` or `db.session.scalar(statement)` or `db.session.scalars(statement)` depending on what you want back in the result. `Execute` is for literally executing a statement. It'll return a tuple. `Scalar` which is for when you expect only one result, otherwise `Scalars`, returns in iterator. You'll have to choose between them on the circumstances.

6. Relationships
   
   Relationships can be expressed with the `db.relationship()` function. It returns a new property that can do multiple things. but the foreign key has to be separately declared with the `ForeignKey` class. 

   It consists of 

   `foreign key = db.Column(db.datatype, db.ForeignKey(TABLE.attribute), nullable=False)`

   Since the subject of the ForeignKey shouldn't be empty, so `nullable=False` is required. 

   Then you set `back_populates` on the other model, it goes like

   `tablename_plural = db.relationship(Table_you_want_to_connect_to, back_populates=the_attribute_you_connect_with)`

   Note that, this back_populates should be set on both tables.

   let's have a look in the example for better understanding.

   ```python
    class Customer(db.Model): 
        __tablename__ = 'customers'
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(), nullable=False)
        last_name = db.Column(db.String(), nullable=False)

        booking = db.relationship('Booking', back_populates='customers')

    class Booking(db.Model):
        __tablename__ = 'bookings'
        id = db.Column(db.Integer, primary_key=True)
        date = db.Column(db.Date(), nullable=False)
        time = db.Column(db.Date(), nullable=False)
        Pax = db.Column(db.Integer, nullable=False)

        customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
        customers = db.relationship('Customer', back_populates='bookings')
    ```

    In the example above, Booking table needs Customer ids as a ForeignKey. Set db.ForeignKey() then set back_populates to each other so that they can access to each other.

    You can add `cascade` which means when the data used as a foreign key is deleted, all the connected data is also deleted.


Most of implementations consists of using the above functions. Create a custom statement to filter the records that you want to find or create a new data and save it to the database using `session`


### <br>**R5. Document all endpoints for your API.**

This is a very long page, so click the link to see the all list

# **[CLICK HERE](./docs/endpoint_document.md)**





### <br>**R6. An ERD for your app.**


![ERD](docs/T2A2_ERD.png)




### <br>**R7. Detail any third party services that your app will use**


## 1. bcrypt

 - 'bcrypt' itself is a password-hashing function designed by Niels Provos and David Mazières, based on the Blowfish cipher and presented at USENIX in 1999.  
 `Bcrypt` package is a python library that encodes password to encrypted result which is only one-way hashing so that anyone can't figure out what the password was originally. `Bcrypt` checks the password from input is matched against the hashed password stored in the database. It doesn't really decode the hashed password back not only because for safety reasons but also because Hash function iterates certain times and added with `SALT` which is a random value which makes this hashed password more complicated.
 
 ![bcrypt](docs/bcrypt_hashing.png)

 - ### **Used functions in the program**
 - `generate_password_hash(password)`:
 it generate hashed password from the given password

 - `check_password_hash(password, password2)`: 
 it returns boolean after check the 2 passwords given are match. 

 - generate_password_hash(password).`decode('utf-8')`:  
 Before storing the hashed password in the database, you have to decode it to `utf-8` Unicode regulation because the hashed password is a `bytes` which has an error when you try to store it in the database because the database takes this as a simple `string` which is different type of data with `bytes`. When `Bcrypt` tries to check the password, it can't compare it against the password in the database. 

 ![decode](docs/bcrypt_encode_decode.png)

## 2. click

- Click is a Python package for creating command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.  
It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

- `@click.command`: Click is built as decorator to declare command lines using in the terminal.

```python
# ex)
@db_commands.cli.command('create')
                # by typing 'create' in the terminal, it executes the below through db_commands
def create_db():
    db.create_all()
    print("Initial tables created")
```

## 3. Flask
-Flask is a micro Web framework of Python comes with very good flexibility to associate with web engines and works in simple & light codes. The biggest websites using Flask include Pinterest and LinkedIn.

```python
from flask import Flask
...
# import packages or mudules that you need to run the program

# As the app is built on MVC which builds models, schemas and controllers in separate moduels.
def create_app():
    app = Flask(__name__)

    # set up error handling decorators as many as you need
    @app.errorhandler(400)
    def bad_request(err):
    return {'error': str(err)}, 400
    ...

    # config such things like the database connection and JWT, JSON SORTING
    app.config['SQLALCHEMY_DATABASE_URI'] = 
    app.config['JWT_SECRET_KEY'] = 
    app.config['JSON_SORT_KEYS'] = 
    ...

    # Initiating core packages for the app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints for using and connecting controllers
    app.register_blueprint(customers_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(db_commands)
    ...

    # Finally execute app
    return app
```

1) &nbsp;As Flask is a third party module, what you need to do is download Flask through pip in virtual environment then declare it so that you can add the source to Python. Import `Flask` class from `flask` module to do this. In some cases you have to relate with relational databases and send it to the web browser, you'll have to import `jsonify` function too. 

2) &nbsp;Now, we make an instance of Flask. You might wonder why we put `__name__` in as a parameter. `__name__` is a special variable only in Python which represents the name of module. In the basic structure which is with only one package that means the current python package itself, we want this current file(`__main__` which is represented by `__name__`) to be executed as a Flask instance. When you modulised the project, you'd put the package(or entry point in other languages)you want to execute  name here.<br>
   
    ``` py
    app = Flask(__name__) # as a single module
    app = Flask('the name of package') # as modulized packages
    ```


3) As the app is built followed **MVC**, the rest of parts such as
   - configs for preventing circular importing 
   - models coded using SQLAlchemy and Marshmallow
   - schemas coded using SQLAlchemy and Marshmallow 
   - controllers for setting endpoints or executing queryies <br><br>
  
    are built in separate packages and imported in the main python file.


## 4. Flask-Bcrypt  
   
  - Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application. Due to the recent increased prevalence of powerful hardware, such as modern GPUs, hashes have become increasingly easy to crack. A proactive solution to this is to use a hash that was designed to be “de-optimized”. Bcrypt is such a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are optimized for speed, bcrypt is intentionally structured to be slow.

  - For sensitive data that must be protected, such as passwords, bcrypt is an advisable choice.


## 5. Flask-JWT-Extended, PyJWT
   - JWT is short word of JSON Web Token. Token is an encrypted packet data. JWT has 3 parts that are Header which is algorithm to encrypt detail of Token Payload that's the essential information such as User's unique id you're verifying and signature that's a proof of the token is inspected. Thanks to the server or both side inspects validity of the token, it can be detected if someone trying to manipulate information. 
   - For exmaple
   - 1. User send a ID/PW data to the server for login, then server checks whether the PW is correct.
   - 2. After the server confirms the PW is correct, then it sends back a certificate, Token with signature about the user and expire date) to the user side.
   - 3. When the user tries to use things only for verified users, the user show the server the token that proves the user is verified.
   - 4. The server can't know who is this user before the token, but by checking the token anytime it needs to, the server can determine who is this user. 
    ```python
    create_access_token(identity= ,expires_delta= ) 
    # Create the token from the information and give expire date.

    get_jwt_identity()
    # Bring the identity information from the token

    @jwt_required()
    # Decorator. must be placed after endpoint declare
    # Check this user is authenticated from the token and user's unique id and expire date.
    ```


## 6. SQLAlchemy, Flask-SQLAlchemy
   - ORM of this app. SQLAlchemy is for creating the part of Model in MVC. 
   - ORM is an short word of **Object Relational Mapping** and means configuration mapping between objects and relational databases. This is a tool used to describe models in the MVC pattern. Object-Oriented Programming uses classes and relational databases use tables, and this is where the inconsistency arises. In other words, when an object is stored in a relational database, a problem arises when you want to retrieve and manipulate the data in the relational database as an object, and this problem will cause spending more time and money if the developer does not have ORM. ORM solves these inconsistencies by automatically generating SQL based on the relationship between objects.
   - For more detail, please see R4

## 7. psycopg2
   - It's a driver to connect SQLAlchemy to the actual database.
   - Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). 
   - It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.
   - Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being both efficient and secure. It features client-side and server-side cursors, asynchronous communication and notifications, “COPY TO/COPY FROM” support. Many Python types are supported out-of-the-box and adapted to matching PostgreSQL data types; adaptation can be extended and customized thanks to a flexible objects adaptation system.
   - Psycopg 2 is both Unicode and Python 3 friendly.
   


## 8. Marshmallow, Flask-marshmallow, Marshmallow-SQLAlchemy
   
   - Marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
  
   - Flask-Marshmallow is a thin integration layer for Flask and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs. It also optionally integrates with Flask-SQLAlchemy.
   - Because the query results are not serialized, it can't be Json in order to show the result in the app. Marshmallow can basically serialize the results so we can get proper output
  
```python
class BookingSchema(ma.Schema): 
    customer = fields.Nested('CustomerSchema', exclude=['id', 'password'])
    table = fields.Nested('TableSchema', exclude=['id'])
    # Setting nested fields which is for when returns the fields returning have related fields with other schema.  

    pax = fields.Integer(validate=(
        Range(1,8, error='It\'s over max 8 pax. Please contact the manager for group booking')))
    date = fields.Date()
    time = fields.Time('%H:%M')
    customer_id = fields.Integer()
    comment = fields.String(validate=(
        Length(max=150, error='Comment must be less than 150 letters')))
    # Setting datatypes through fields.Datatypes. You can add validate option, 
    
    class Meta:
        fields = ('id', 'date', 'time', 'pax', 'comment', 'customer_id', 'customer', 'table')
        ordered = True
    # Setting metadata when you have fields to expose
```

## 9. python-dotenv

   - Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.
  
   - **When the sensitive codes such as database address, database user id and password etc are implemented in a package, it's risky to get exposed on someone else which might lead to serious data-leaks breach. dotenv make python can save evironment variables to hidden seperate file and prevent them from being exposed.**


### <br>**R8. Describe your projects models in terms of the relationships they have with each other**

There two main part of this app; `Orders` and `Bookings`  
The rest of the tables are to assist to create or describe datas such as food, table, payment etc. 

 1. `Orders` 
    - It's one of the main part of Staff aspect. It starts with `Staffs` table which you register a staff in the db. After login, when an Order creates, it adds new data or datas in the associated table `Order_Food`. 
  
    - As `Order_Food` is to describe details of the order, one Order can have multiple order_food instances. Each instances will have the order_id from Orders as FK, food_id from Foods as FK and its quantity. 
    - So 

    - For example, One order creates with 2 burgers and 1 fish and chips, order_food will create 2 instances due to the order has 2 different foods. To make this happen with one endpoints, i built a class function in order class so when new order's been through, automatically creates a instance of order_food. With similar way, it calculates the total price too.

```python
    def generate_order_food(self, items):
        for food, qty in items:
            self.order_food.append(Order_Food(order=self, food=food, quantity=qty))
            
    def calc_total_price(self, items):
        for food, qty in items:
            self.total_price += food.price * qty
```

2. `Bookings`
   - This is the main part for customers. Customer can register in a certain endpoint, then create a booking by sending json. Take customer id from token and date, time, pax and comment from JSON. Finally the custom function will decide which table is good to be assigned to this booking. After added successfully, it'll update customers `visited` data.

```python
def create_booking():
    is_customer()
    data_booking = BookingSchema().load(request.json)
    booking = Booking(
        date = data_booking['date'], 
        time = data_booking['time'],
        pax = data_booking['pax'],
        table_id = assign_table(data_booking['pax']),
        comment = data_booking.get('comment'),
        customer_id = get_jwt_identity()
    )
    db.session.add(booking)
    customer = query_by_id(Customer, get_jwt_identity())
    customer.visited += 1 # Visited records
    db.session.commit()
    return BookingSchema(exclude=['customer_id']).dump(booking), 201
```

3. The rest
   - As i mentioned above, Most of the rest tables are for assistance with main tables. 
   - They take a JSON to create or modify data or search a data by variable in endpoints.

```python
# ex)
#search foods with two tags(GF, DF, V)
tags = ('gf', 'df', 'v')

@foods_bp.route('/<string:tag1>/<string:tag2>')
def search_food_tags(tag1, tag2):
    tag1, tag2 = tag1.lower(), tag2.lower()
    if tag1 not in tags or tag2 not in tags:
        return {'error': 'Failed to search. Please check the tag and try again.'}, 404
    elif tag1 == tag2: # If you put two same tags, it redirects to search_food
        return redirect(url_for('foods.search_food', tag = tag1))
    rest = list(tags)
    rest.remove(tag1)
    rest.remove(tag2)
    if 'v' in rest:
        stmt = db.select(Food).filter_by(is_gf=True, is_df=True)
        food = db.session.scalars(stmt)
    elif 'gf' in rest:
        stmt = db.select(Food).filter_by(is_df=True, is_v=True)
        food = db.session.scalars(stmt)
    elif 'df' in rest:
        stmt = db.select(Food).filter_by(is_v=True, is_gf=True)
        food = db.session.scalars(stmt)
    return FoodSchema(many=True, only=['name', 'price']).dump(food)

``` 


### <br>**R9. Discuss the database relations to be implemented in your application**


As mentioned in the ERD, This program consists of lots of tables and associate to each other.

Staffs has a relationship with Orders as One-to-Many(or 0) which means one staff can relate with none or lots of orders but one order must have one staff.

Foods has a relationship with Order_Food table. One food can be associated with lots of Order_Food instances or none, but one instance of Order_Food which is association table, should have only one food.

Payments has One-to-Many(or 0) relationship with Receipts. One payment can be used multiple times or none in Receipts, One receipt have to have only one payment method because the restaurant does not want to take split bill.

Customers has also One-to-Many(or 0) relationship with Bookings which means one customer can have multiple or none booking but one booking must have one customer.

Bookings has another relationship with Tables which is One-to-Many(or 0). One table can be used multiple times in Orders but one booking has only one table.

Orders is the most related table.  
First it has one-to-many(or 0) relationship with Staffs means one order should have one staff but one staff can be used multiple times in Orders.  
Second Tables. It has one-to-many(or 0) relationship too, for the same reason of Staff.  
Third is Receipts. One-to-one in this case because One order has it's own receipt and the receipt should be connected only one order.  
The last is Order_Food table. Due to Order_Food is an association table, it has a little complicated relationship. 
In real life, it's not often that one order has only one food in a restaurant. Most of us orders several dishes at once. However, in terms of data relationships, it is against data integrity to have two or more values ​​for any attribute in one order instead of one. We need this association table to solve that.


One Order_Food uses a primary key from orders and a primary key from foods as foreign key and primary key at the same time in Order_Food. One order can be used multiple times in order_food, and one order_food row brings only one order key. The same goes for our relationship with food.

For example, when an order comes in two foods and different numbers of quantity come together, two rows are created in the order_food table. Because two different types of food came in. Each row will store an individual quantity.



### <br>**R10. Describe the way tasks are allocated and tracked in your project**



![trello](./docs/trello.png)

### To visit the Trello page ; **[CLICK HERE](https://trello.com/invite/b/50BFlPvV/ATTI0bf23d0fdedcfd05777f3dd363c2990e841F964D/lionwolf-pos-project)**

