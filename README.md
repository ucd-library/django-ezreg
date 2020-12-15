# django-ezreg

## Docker

Converting the development version to docker was straight forward.  The only
issues were:
- The application uses an unsupported version of python
- The submodule locations needed to be modified
  - One submodule says it's deprecated.  Not sure it's used

Using a local version of postgres, you need to

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

SITE_URL='http://localhost:8000'

```

## Installation

On installation, you'll need to run `dc exec web python manage.py migrate` in order to
initialize your system.  At this point you'll have an empty database.

You can also quickly add superuser with `dc exec web python manage.py
createsuperuser` This will give you access to the `http://localhost:8000/admin'
page.  From here you can add your CAS id, and start testing the site as a user.
