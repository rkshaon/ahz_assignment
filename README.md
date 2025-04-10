# AHZ Assignment

## Setup
### Prerequisite
- Python 3.10 or above
- PostgreSQL

### Install
Clone project
```
git clone git@github.com:rkshaon/ahz_assignment.git
```
Create and activate virtual environment [Instructions](https://github.com/rkshaon/software-engineering-preparation/tree/master/Languages/Python/environment)

Install dependencies
```
pip install -r requirements.txt
```

Create database in PostgreSQL and update in `settings.py`

Migrations
```
python manage.py makemigrations
python manage.py migrate
```


### Run server
```
python manage.py runserver
```

#### Start Celery Beat
```
celery -A AHZ_Test beat --loglevel=info
```

#### Start Celery Worker
```
celery -A AHZ_Test worker --loglevel=info
```
