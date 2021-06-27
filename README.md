# Dgraph-django-boilerplate

## Installation

Requirements:

- Default requirements mentioned below.
Follow these steps:
  
Create Virtual Environment
```sh
pip install virtualenv
virtualenv dgraphBase
source dgraphBase/bin/activate
```

Make env file
- Copy `.env.example` file to `.env`

Install Requirement
```sh
pip install -r requirements.txt
```

- Sync Dgraph db
```sh
python db_sync.py
```
 
- Run Project
```sh
python manage.py runserver
```

