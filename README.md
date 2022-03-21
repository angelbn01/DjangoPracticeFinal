# CityTransport

Booking transports to move around the city.

- Clients can book a type of transport to move around the city.
- The administrators can add, modify and delete bycicles, scooters or electric scooters and mark them as available or not. They can also add routes and record them.

# Run locally

To test the admin

```bash
python manage.py createsuperuser

Username: admin
Email address: admin@admin.com
Password: admin
Password(again): admin


python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

To access to the admin page, insert /admin/ at the url and insert the credentials:
http://127.0.0.1:8000/admin/
