# DYK

A simple small platform to share or record your small daily learnings.

You can currently see it in action at [https://nerdlog.herokuapp.com](https://nerdlog.herokuapp.com).

## Requirements

- Python 3.6.8+
- Virtualenv

## Setup

Initialize a virtual environment:

```bash
python3 -m venv .venv
```

Activate it before starting the server:

```bash
source .venv/bin/activate
```

Install the dependencies the first time:

```bash
pip install -r requirements.txt
```

And start a development instance with

```bash
python manage.py runserver
``` 

You might want to refer to the Django documentation for more details.
