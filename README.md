# CityTransport

Booking transports to move around the city.

- Clients can book a type of transport to move around the city.
- The administrators can add, modify and delete bycicles, scooters or electric scooters and mark them as available or not. They can also add routes and record them.
- Clients can create a new route or edit/delete routes already created by them. The fact of creating a route for a client, simulates the action of taking a certain vehicle in a location (start point) and leaving it in another location (end point).

# Run locally

To test the admin:
```bash
python manage.py createsuperuser

Username: admin
Email address: admin@admin.com
Password: admin
Password(again): admin

```
Then:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# When the server is running:

To access to the admin page, insert /admin/ at the url and insert the credentials:
http://127.0.0.1:8000/admin/

If you are a new user and you want to register: http://127.0.0.1:8000/register/


If you want to know the information of the database inserted by the admin: http://127.0.0.1:8000

# Heroku

If you want to check the link of the project deployed in heroku: https://city-transports-django.herokuapp.com/
