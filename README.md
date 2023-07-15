# 002-python-django-by-bogdan-stashchuk

---

## Short. How to start project

### Setup environment

- `pip list`
- `pip install pipenv` - one time globally
- Create `.venv` in Django project folder

### Setup Django project

- `pipenv install Django`
- `django-admin startproject config .`
- `.env`
    1. pipenv install django-environ
    2. create `.env` file in the same folder with `settings.py`
- Сonnect database (PostgreSQL)
    1. `pipenv install psycopg2`
    2. config in `settings.py` `DATABASES = { ... }`
- Makemigrations `python manage.py makemigrations`
- Migrate `python manage.py migrate`
- Create superuser`python manage.py createsuperuser`
- Create application `python manage.py startapp shop`
- Crete models for DB
- `Makemigrations` and `Migrate`
- Register `Shop` in `settings.py` `INSTALLED_APPS = [..., 'shop.apps.ShopConfig']`
- Register models in `shop/admin.py`
- Create Views
- `pipenv install django-tastypie`
- Create application `python manage.py startapp api`

---

`pipenv --venv` - path to .venv `C:\Python\Django\001-project\.venv`

`pipenv shell`

---

## MVC -> MTV

- Model -> Model - Logic (work with data instances)
- View -> Template - HTML
- Controller -> View - Buttons Forms

---

## WSGI & ASGI

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

## `python manage.py migrate`

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

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from .models import Course, Category
def index(request: WSGIRequest) -> HttpResponse:
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
```

```emmet
table>(thead>tr>th*5)(tbody>tr>td*5)
```

---

## Change templates destination

now template in the root of project

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': { ... },
    },
]
```

---

## Create REST

- [`pipenv install django-tastypie`](https://pypi.org/project/django-tastypie/)
- `pipenv shell`
- Create application `python manage.py startapp api`
- Add to `INSTALLED_APPS = [..., 'api.apps.ApiConfig',]`
- [Create models](./api/models.py)
- Add url patterns in `base` -> [`urls.py`](./base/urls.py)

```python
from api.models import CategoryResource, CourseResource
from tastypie.api import Api

api = Api(api_name='v1')
category_resource = CategoryResource()
course_resource = CourseResource()
api.register(category_resource)
api.register(course_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('api/', include(api.urls)),
]
```

- `http://localhost:9000/api/v1/`

## REST Auth

- [`authentication.py`](./api/authentication.py)
  - create `CustomAuthentication` if you need
- in models create instances of:
    1. `authentication = CustomAuthentication()`
    2. `authorization = Authorization()`

## Create `API_KEY`

- Add `tastypie` to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'tastypie' # And now -> You have 2 unapplied migration(s).
]
```

- Apply migrations `python manage.py migrate`
- Save an API key via the web interface for specific user

## `POST` `DELETE` Authorization

- For action set header `Authorization: ApiKey username:api_key`
- For `POST` (create record to db)
    1. `def hydrate(self, bundle): ...` how to send data to server
    2. `def dehydrate(self, bundle): ...` its how to send data to client
