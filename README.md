# 002-python-django-by-bogdan-stashchuk

`pipenv --venv` - path to .venv `C:\Python\Django\001-project\.venv`

`pipenv shell`

---

## MVC -> MTV
- Model -> Model - Logic (work with data instances)
- View -> Template - HTML
- Controller -> View - Buttons Forms

---

# WSGI & ASGI
- WSGI - web server gateway interface (интерфейс взаимодействия между сервером и python)
- ASGI - asynchronous server gateway interface (disabled by default)

---

### `pipenv install Django`

```text
$ pipenv graph
Django==4.2.3
├── asgiref [required: >=3.6.0,<4, installed: 3.7.2]
├── sqlparse [required: >=0.3.1, installed: 0.4.4]
└── tzdata [required: Any, installed: 2023.3]
```

```text
$ pip list
Package    Version
---------- -------
asgiref    3.7.2
Django     4.2.3
pip        23.1.2
setuptools 67.8.0
sqlparse   0.4.4
tzdata     2023.3
wheel      0.40.0
```

---

## Init Django project

`django-admin startproject base .`

---

## Work with .env variables in Django
1. pip install django-environ
2. create `.env` file in the same folder with `settings.py`
```text
DB_ENGINE=django.db.backends.postgresql
DB_USER=john
DB_PASSWORD=john@#687
```
3. use vars from .env
```python
import environ
env = environ.Env()
environ.Env.read_env()
print(env.str('DB_ENGINE'))
print(env.str('DB_USER'))
print(env.str('DB_PASSWORD'))
```

---

## Start Django project

`python manage.py runserver 9000`

---

## Create application

`python manage.py startapp shop`

```python
# Application definition in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    # others default ...
]
```

---

## Database

in `settings.py`

```python
# Default is
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': 'db_name',
        'USER': 'db_username',
        'PASSWORD': 'p@$$w0rD',
        'HOST': 'db ip address',
        'PORT': '658347'
    }
}
```

## Migrations

`python manage.py migrate`