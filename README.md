# CityTransport

Booking transports to move around the city.

- Clients can book a type of transport to move around the city.
- The administrators can add, modify and delete bycicles, scooters or electric scooters and mark them as available or not. They can also add routes and record them.

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

Once you are registered, you have to log in: http://127.0.0.1:8000/login/


If you want to know the information of the database inserted by the admin: http://127.0.0.1:8000

If you want to check the link of the project deployed in heroku: https://gentle-woodland-64586.herokuapp.com/
