# GalaxyHub

GalaxyHub is a Django-based web application designed to manage and explore planetary data via its app **Planet**.

## Installation

### Clone the repository:

git clone https://github.com/jibi-jn/galaxyhub.git
cd galaxyhub

Create and activate a virtual environment:

$ python3 -m venv {env_name}
$ source {env_name}/bin/activate


Install dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Configure environment variables:
Create a .env file and add your settings (e.g., SECRET_KEY, DATABASE_URL).

Run migrations:

(env)$ python3 manage.py makemigrations
(env)$ python manage.py migrate

Create a superuser (admin):

(env)$python manage.py createsuperuser
Start the development server:

(env)$python manage.py runserver
Open in browser:
Visit http://localhost:8000/
