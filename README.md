Yatube API
===============

Project was developed as a part of **django rest framework** studying.
API was developed for **Yatube** toy social network for writers using **viewsets**`, **pagination**, **permissions**, **mixins**, **search** and **JWT authorization**


Technologies
------------

* Django
* Django Rest Framework (DRF)
* JWT based authorization (**SimpleJWT** + **Djoser** libraries)
* Swagger and ReDoc for documenting and testing API (**drf-yasg** library)
* Python


How to install and run the project
----------------------------------

1. Clone the project
2. Create virtual environment via `python3 -m venv venv` command
3. Activate the environment via `source venv/bin/activate` command
4. Upgrade pip to the latest via `python3 -m pip install --upgrade pip` command
5. Install required libraries via `pip install -r requirements.txt` command
6. Migrate db models `python3 manage.py migrate`
7. Run api via `python3 manage.py runserver`


Available API endpoints
-----------------------

* You can navigate to the `http://127.0.0.1:8000/api/swagger/` to see and try available endpoints.
* The redoc is also available at `http://127.0.0.1:8000/api/redoc/`
* You can use JWT token to issue requests that require authorization. There is are endpoints to obtain/refresh/verify JWT token.
* Admin panel is available at `http://127.0.0.1:8000/admin/`. To create superuser, `python3 manage.py createsuperuser` command can be used


Author and contacts
-------------------

* Project developer is Sergey Li who is studying "Python developer" program at Yandex.Praktikum 
* Feel free to contact me for any questions related to the project at <pincats@gmail.com>

