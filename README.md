# Django-rest

Django REST Framework integrated with JWT

## How to start
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py loaddata backend/fixtures/initial_data.json
- python manage.py runserver
- login: demo / demoadmin

## API URLS
- /api 
- /api-token-auth
- /api-token-refresh

## Test
- curl -H "Content-Type: application/json" -X POST -d '{"username":"demo","password":"demoadmin"}' http://localhost:8000/api-token-auth/

    It will get something like that:
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRlbW8iLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImRlbW9AZXhhbXBsZS5jb20iLCJleHAiOjE0OTQ0Mjg1MzZ9.IrbnEEx31RJPj_x3nTlO-VUVr6yFMaISTCYFx2riQcE"}


## Version:
- Django 1.10
