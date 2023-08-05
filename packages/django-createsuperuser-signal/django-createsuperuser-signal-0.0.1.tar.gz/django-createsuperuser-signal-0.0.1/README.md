# django-createsuperuser
Django app that implements a signal to create super user from environment
variables on migration. Useful for Docker, Kubernetes etc. If the user already
exists it will do nothing.

## Installation

Simply download from Pypi:
```bash
pip install django_superuser
```

## Usage

This app needs to register in the `INSTALLED_APPS` list in your Django settings:

```python
INSTALLED_APPS = [
    ...
    "createsuperuser",
    ...
]
```

As it is, it will do nothing. You need to define 4 environment variables through
which the superuser will be created during the migration stage (uses the
post_migrate signal).

| Environment Variable | Description |
| -------------------- | ----------- |
| DJANGO_SUPERUSER_CREATE | Enables the process of creating the superuser. Must be true or false (case insensitive) |
| DJANGO_SUPERUSER_USERNAME | The username of the superuser account to create |
| DJANGO_SUPERUSER_EMAIL | The email of the superuser account |
| DJANGO_SUPERUSER_PASSWORD | The password of the superuser account |

After defining these variables, the superuser will be created the next time you
perform a migration (even if no migrations are applied)

```bash
export DJANGO_SUPERUSER_CREATE=true
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=admin
python manage.py migrate
```

You can use this to create the user when launching your django project in Docker
by passing the variables in the command. Or if you are using Kuberenetes you can
add them in a `Secret` and pass them in the pod via `envFrom`. Or however the
environment variables fit in your workflow.