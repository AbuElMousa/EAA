# EAA
Embedded Acoustics API for the Third Ear project
# Running the API

Use python 3

- Clone the project
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate --run-syncdb
- python manage.py runserver (by default it will run to localhost. We can only use 192.168.7.2 on the beagle)
