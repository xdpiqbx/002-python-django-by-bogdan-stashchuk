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
1. pipenv install django-environ
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

## PostgreSQL

[Standart!](https://pypi.org/project/psycopg2/) -> `pipenv install psycopg2`

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
import environ
env = environ.Env()
environ.Env.read_env()
DATABASES = {
    'default': {
        "ENGINE": env.str('DB_ENGINE'), # "django.db.backends.postgresql"
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT')
    }
}
```

---

## Migrations

You have 18 unapplied migration(s).
Your project may not work properly until you apply the migrations for app(s):
`admin`, `auth`, `contenttypes`, `sessions`. Run `python manage.py migrate` to apply them.

### `python manage.py migrate`

---

## Create superuser

`python manage.py createsuperuser`

---

## Crete models for DB

```python
# in shop/models.py
from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qpy = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE())
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
            return self.title
```

---

## Make migrations and migrate

`python manage.py makemigrations`

Next server start will show you next message:
```text
You have 1 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): shop.
Run 'python manage.py migrate' to apply them.
```
### `python manage.py migrate`

---

## Register `Shop` in `Installed Apps`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    #.....
    'shop.apps.ShopConfig', # <<-------------
]
```

---
## `python manage.py shell`

Working with DB objects with `manage.py` shell

```python
from shop.models import Category, Course
Course.objects.all() # <QuerySet []>
Category.objects.all() # <QuerySet []>

new_category = Category(title='Programming')
new_category.save()

Category.objects.all()  # <QuerySet [<Category: Category object (1)>]>

new_category.id  # 1
new_category.title  # 'Programming'
new_category.created_at  # datetime.datetime(2023, 7, 14, 7, 56, 57, 107130, tzinfo=datetime.timezone.utc)

Category.objects.get(pk=1)  # <Category: Category object (1)>
Category.objects.filter(pk=1)  # <QuerySet [<Category: Category object (1)>]>

category = Category.objects.get(id=1)
category.course_set.all()  # <QuerySet []>
category.course_set.create(title="Complete Python Guide", price=99.99, students_qty=100, reviews_qpy=50)  # <Course: Course object (1)>
category.course_set.create(title="Complete Java Guide", price=99.99, students_qty=80, reviews_qpy=20)  # <Course: Course object (2)>
category.course_set.all()  # <QuerySet [<Course: Course object (2)>]>
[course.title for course in category.course_set.all()]  # ['Complete Python Guide', 'Complete Java Guide']
[course.title for course in Course.objects.all()]  # ['Complete Python Guide', 'Complete Java Guide']
```

---

## Register models in `shop/admin.py`

```python
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Course)
```

---

## First Views