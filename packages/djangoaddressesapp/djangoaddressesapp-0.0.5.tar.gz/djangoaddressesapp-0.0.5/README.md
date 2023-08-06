# djangoaddressesapp

**djangoaddressesapp** is a django app to register addresses.

## Features

- Complete address registration.
- Importance of regions, states and cities directly from the IBGE API.

## Installation

- Run `pip install djangoaddressesapp`
- Add `djangoauthenticationapp` to `settings.INSTALLED_APPS`

```python
INSTALLED_APPS = [
    'djangoaddressesapp',
    #...
]
```

## Upgrade

- Run `pip install djangoauthenticationapp --upgrade`
- Run `python manage.py migrate`
- Run `python manage.py collectstatic --clear`
- Restart your application server
