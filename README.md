# kaspi-backend
## Architecture and technology

## Used technology stack

#### Programming language
* paython 3.9

#### Frameworks and libraries
* Django 4.2.4
* djangorestframework 3.14.0
* daphne 4.0.0
* gunicorn 21.2.0
* celery 5.3.6

> The full list of dependencies can be found in the file '/requirements.txt'

#### Database
* mariadb 10.9.3

#### Tools and technologies
* Docker 
* Dokcer compose 
* Git
* REST API

## Project

### kaspi_backend

**Description**: This is the main directory containing your Django project.

**Contains**:
```sh
- kaspi_backend/
 -- settings.py
 -- urls.py
 -- celery.py
```

#### settings.py

* Is the main settings file for Django project. It contains all the settings required for your Django application to work.

* The settings.py file defines settings such as database, authentication settings, static file settings, security keys, and more.

* This file defines the configuration of your project, and changes here affect the entire application in the project.

#### urls.py

* Defines URL routes for your Django application.

* This file defines matches between URLs and Django views.

* When a client request comes in, Django looks for a match in the urls.py file and calls the corresponding view.

#### celery.py

* Is used to customize the Celery framework in your Django project.

* Celery is an asynchronous task queue that allows you to run long-running operations in the background. In this project it is used for parsing data from the marketplace

* The celery.py file is used to set up and configure Celery for your project, including connecting to a message broker (such as Redis or RabbitMQ), setting up task queues, and other parameters.

## Applications
**Description**: Each application in Django is an independent component that provides some functionality.

**All applications use the same structure**

```sh
- application_name/
 -- migrations/
  -- migration_file.py
 -- admin.py
 -- models.py
 -- apps.py
 -- serializers.py
 -- tests.py
 -- urls.py
 -- views.py
```

#### 1. migrations/:

**Responsibility**: The migrations directory contains Django migration files, which are used for automatically updating the database schema when changes are made to data models.

**Description**:

* Each migration file (migration_file.py) is a Python script that defines changes to the database structure, such as creating new tables, adding new fields, etc.

* Migrations are created automatically when you run the python manage.py makemigrations command and applied to the database using the python manage.py migrate command.

#### 2. admin.py:

**Responsibility**: The admin.py file is used to configure the Django admin interface.

**Description**:

* In this file, you register data models to make them available for editing in the Django admin panel.

* You can customize which fields are displayed and editable in the admin panel, as well as define relationships between different models.

#### 3. models.py:

**Responsibility**: The models.py file contains Django data model definitions, which represent the structure of the database.

**Description**:

* In this file, you define Python classes that correspond to tables in the database.

* Each model class defines fields of the table and their data types, as well as additional parameters such as uniqueness constraints, etc.

#### 4. apps.py:

**Responsibility**: The apps.py file is used to configure a Django application.

**Description**:

* In this file, you can configure application-specific settings such as the application name and other metadata.

* While this file is not required for all applications, it can be used to define additional application settings.

#### 5. serializers.py:

**Responsibility**: The serializers.py file contains Django REST Framework serializers, which are used to convert Python objects to and from JSON format.

**Description**:

* Serializers are used in the Django REST Framework to work with data transmitted via APIs.

* In this file, you define serializer classes that specify which model fields should be included in JSON responses and what validation rules should be applied.

#### 6. tests.py:

**Responsibility**: The tests.py file contains unit tests for your Django application.

**Description**:

* In this file, you can define tests that verify the functionality of various parts of your application.

* Unit tests in tests.py can be used to automatically check the correctness of your code when it changes or is updated.

#### 7. urls.py:

**Responsibility**: The urls.py file defines URL routes for your Django application.

**Description**:

* In this file, you define mappings between URL addresses and Django views.

* When a request comes from the client, Django looks for a match in the urls.py file and calls the corresponding view.

#### 8. views.py:

**Responsibility**: The views.py file contains Django views, which handle requests from clients and return responses.

**Description**:

* In this file, you define functions or classes of views that handle various types of requests (e.g., GET, POST).

* Views can work with data from models and pass it to templates or return it as JSON responses.

### 1. landing

**Description**:
The "landing" module is responsible for managing models and API endpoints related to the landing page of the application. It handles the data and functionalities necessary for displaying tariffs, reviews, footer information, and FAQs on the landing page.

#### Models:

  - **Tariff**:
    -  Represents the different pricing plans or tariffs available for the service or product.
    
    -  Contains fields such as tariff name, price, features, etc.

  - **Review**:

    - Represents user reviews or testimonials about the service or product.

    - Includes fields like user name, review text, rating, etc.

  - **Footer**:

    - Contains information displayed in the footer section of the landing page, such as contact details, links to social media, etc.

    - Fields may include company address, phone number, email, etc.

  - **Faq**:

    - Represents frequently asked questions and their corresponding answers.

    - Fields might include question text and answer text.

### 2. stores

**Description**:
The "stores" module is responsible for managing models and functionalities related to the management of stores, orders, products, and competition analysis within the application. It handles various aspects such as store information, product inventory, order management, competitor analysis, and notifications.

#### Models:

  - **Store**:

    - Represents individual stores or outlets managed within the application.

    - Contains details such as store name, address, contact information, etc.

  - **Orders**:

    - Represents orders placed by customers.
  
    - Includes fields like order date, customer information, order status, etc.

  - **Products**:

    - Represents the products available for sale.

    - Contains details such as product name, description, price, etc.

  - **OrderItem**:

    - Represents individual items within an order.

    - Relates to the products ordered, quantity, and associated order.

  - **SalesPoint**:

    - Represents sales points or locations where products are sold.

    - Contains details similar to the Store model.

  - **CompetitorsProducts**:

    - Stores information about products offered by competitors.

    - May include details such as competitor product name, description, price, etc.

  - **Competitors**:

    - Represents competitor businesses.

    - Contains details like competitor name, contact information, etc.

  - **ProductPriceUpdated**:

    - Tracks updates to product prices over time.

    - Records changes in product prices and related metadata.

  - **Notifications**:

    - Stores notification messages or alerts for users.

    - Includes fields such as notification content, recipient, timestamp, etc.

  - **UploadProducts**:

    - Used for uploading product data into the system.

    - May contain fields for uploaded file, upload date, status, etc.

  - **Clients**:

    - Represents clients or customers of the application.

    - Contains client details like name, contact information, etc.

  - **CompetitorStore**:

    - Represents competitor stores or outlets.

    - Similar to the Store model but specific to competitors.

  - **CompetitorsProductMonitoring**:

    - Used for monitoring competitor products and pricing.

    - Tracks changes and updates related to competitor products.

  - **AllCompetitorProducts**:

    - Stores information about all competitor products.

    - May contain aggregated data about competitor product offerings.

Also in this module the following files were added:
```sh
 - consumers.py
 - routing.py
 - signals.py
 - tasks.py
 - tg_send_message.py
```
### consumers.py:

**Purpose**: The consumers.py file is used for handling WebSocket connections in Django using the Channels library.

**Description**:

* This file defines WebSocket consumers, which handle incoming messages and manage sending data to clients over WebSocket connections.

* WebSocket consumers can handle various events such as connection, disconnection, message sending, and other custom actions.

### routing.py

**Purpose**: The routing.py file is also used for working with WebSockets in Django through Channels.

**Description**:

* In this file, routes for WebSocket connections are defined. They specify which WebSocket consumers should handle different types of messages and events.

* Routing WebSocket connections helps efficiently manage the handling of incoming messages and simplifies code organization.

### signals.py:

**Purpose**: The signals.py file is used for defining signals in Django.

**Description**:

* Signals in Django are a mechanism that allows sending signals when certain events occur in the application.

* In the signals.py file, signal handlers are defined, which are automatically executed when the corresponding events occur. For example, signals can be used to perform additional actions when a data model is saved or when a user is authenticated.

### tasks.py:

**Purpose**: The tasks.py file is used for defining asynchronous tasks in Django using Celery.

**Description**:

* In this file, tasks are defined that should be executed asynchronously. These tasks may involve long-running operations that should not block the main application thread.

* Tasks defined in tasks.py can be run in the background using Celery, allowing workload distribution and improving the performance of the application.

### tg_send_message.py**:

**Purpose**: The tg_send_message.py file is responsible for sending messages via the Telegram Bot API.

**Description**:

* In this file, functions or classes can be defined to send messages through a Telegram bot.

* It's commonly used for sending notifications, alerts, or other messages to users via the Telegram messenger.


### 3. users

**Description**:
The "users" module handles user-related functionalities within the application. It manages user accounts, their subscriptions or tariffs, and their purchase history.

#### Models:

  - **User**:

    - Represents individual users registered within the application.

    - Contains fields such as username, email, password, etc.

  - **UserTariff**:

    - Represents the subscription or tariff plans chosen by users.

    - Contains details such as tariff name, subscription start/end dates, etc.

  - **UserPurchases**:

    - Represents the purchase history of users.

    - Includes information about products or services purchased by users, purchase dates, prices, etc.


## Initial Setup
1. **Clone the project**
```sh
  git clone https://github.com/EvaDigital/Leadsdoit-test.git](https://github.com/EvaDigital/kaspi-backend.git)
```
2. **Go to project derictory**
```sh
  cd kaspi-backend/
```

3. **Create .env file**
```sh
  FRONT_URL = '<frontend url>'
  BATCH_SIZE = 2
  REDIS_HOST = Redis host
  DB_HOST = DB host
  DB_PORT = DB post
```

## Local
1.  **Run this command to start project**
```sh
  docker-compose up --build
```

2. **Run this commands to create migrations**
```sh
  docker exec -it kaspi_backend-web-1 python3 manage.py makemigrations
  docker exec -it kaspi_backend-web-1 python3 manage.py migrate
```

3. **Run this commands to create admin users**
```sh
  docker exec -it kaspi_backend-web-1 python3 manage.py createsuperuser
```

### Urls
1. **Base url**
```sh
  http://0.0.0.0:8000/api
```

2. **Admin panel**
```sh
  http://0.0.0.0:8000/api/admin
```

3. ***Flower url*
```sh
  http://0.0.0.0:5555
```

4. **Api documantation**
```sh
  https://kaspi.hopto.org/api/docs/
```

## Deploy
### Installing and run MariaDb and Redis:
#### MariaDb
Download the MariaDb installer from the [official website](https://mariadb.org/)

Run the installer and follow the installation instructions.

#### Redis
Download the Redis installer from the [official website](https://redis.io/)

Run the installer and follow the installation instructions.

1.  **Run this command to create vitrual environment**
```sh
  python3 -m venv env
```
2. **Run vitrual environment**
```sh
  source env/bin/activate
```
3. **Install requirements**
```sh
(env)  pip install -r requirements.txt
```
4. **Use this command to start your project**
```sh
(env)  python3 manage.py runserver 0.0.0.0:8000
```
5. **Use this commands to start migrations**
```sh
(env)  python3 manage.py makemigrations
(env)  python3 manage.py migrate
```
6. **Run this commands to create admin users**
```sh
(env)  python3 manage.py createsuperuser
```
7. **Use this command to start celery**
```sh
(env)  celery -A kaspi_backend.celery:app worker  --loglevel=info
```
8. **Use this command to start celery beat**
```sh
(env)  celery -A kaspi_backend.celery:app beat
```
9. **Use this command to start telegram bot**
```sh
(env)  python3 tgbot.py
```





