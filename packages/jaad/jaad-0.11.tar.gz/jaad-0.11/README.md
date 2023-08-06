# Jaad

[![Build](https://github.com/AmadeusITGroup/Jaad/actions/workflows/python-package.yml/badge.svg)](https://github.com/AmadeusITGroup/Jaad/actions/workflows/python-package.yml)
[![Version](https://img.shields.io/pypi/v/jaad.svg)](https://pypi.python.org/pypi/jaad)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Overview
Jaad is an addition to Django.

It is based on Django Rest Framework and is designed to simplify
the syntax needed to expose a resilient REST API.

### Installation
To install Jaad using pip run:

```bash
pip install jaad
```

### Creating a new project
To create a new project create a project directory
and use `jaad-admin.py startproject`.

This will create the following files:
```
.
|-- server/
|     |-- apps/
|     |    |-- __init__.py
|     |    `-- index/
|     |         |-- __init__.py
|     |         |-- parameters.py
|     |         `-- view.py
|     |-- logs/
|     |-- settings/
|     |    |-- __init__.py
|     |    |-- application.py
|     |    |-- local.py
|     |    `-- __init__.py
|     `-- urls.py
`-- manage.py
```

`manage.py` is the classic Django management script hence
you can run your server using:
```bash
DJANGO_SETTINGS_MODULE=server.settings.local python manage.py runserver
```

This will launch your server and make it available here:
http://127.0.0.1:8000/

A default Index view was automatically created.

You can have a look at its definition in `server/apps/index/`
as it uses Jaad core features.

### Creating a new view
To create a view create a submodule in apps and define in it a class
inheriting from JaadView.
Then define the HTTP method you want to support:
```python
from jaad.view import JaadView

class Hello(JaadView):
    def get(self, request):
        return "Hello"

    def post(self, request):
        return "This was a POST request"
```

You can then expose it by modifying `server/urls.py`

### Defining parameters
You can define a set of parameters that a view support using a Jaad Form:
```python
from jaad.forms import fields


class HelloWorldParameters(fields.Form):
    name = fields.StringField(
        required=True,
        help_text="Enter your name :)"
    )
```

And then using it in your views:
```python
from jaad.view import JaadView, with_parameters


class Hello(JaadView):
    @with_parameters("GET", HelloWorldParameters)
    def get(self, request, parameters):
        return "Hello {}".format(parameters["name"])

    def post(self, request):
        return "This was a POST request"
```

The additional parameter used to call your method contains your
parameter values validated and converted to python objects
(int, datetime, ...).

with_parameters can be called with as many Form as you want and will
add a parameter to your method for each Form.


### Interactive documentation
You can add an interactive documentation to your API using
`jaad-admin.py add-doc`.

This will create the following files in `server/apps/`

```
documentation/
    |-- static/
    |     `-- css/
    |          `-- documentation.css
    |-- templates/
    |     `-- rest_framework_swagger/
    |          |-- base.html
    |          `-- index.html
    `-- urls.py
```

This is a Swagger UI that relies on Django Rest Framework Swagger
**and is not exposed yet**.

To expose it:
1. In `server/urls.py` import `include` from `django.conf.urls`
if not already done and add `url(r'^doc/', include('documentation.urls'))`
to urlpatterns.
2. Add `'server.apps.documentation'` to `INSTALLED_APPS`
in `server/settings/application.py`

You can now access your API documentation on http://127.0.0.1:8000/doc/

The documentation is automatically updated based on all exposed view
docstrings and parameter definitions.
