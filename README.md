
# Django RestAPIs - Movies API

In This project we use script to load data from csv files and developed RestAPIs to work with.



## Run Locally

Clone the project

```bash
  git clone git@github.com:PatilTanu/MoviesAPI.git
```

Go to the project directory

```bash
  cd MoviesAPI
```

Create Virtual Envirmonent

```bash
  pip install virtualenv 
```
```bash
  virtualenv Venv
```
```bash
  Venv/Scripts/activate 
```

Install Requirements

```bash
  pip install -r requirements.txt
```

Migrate Tables

```bash
  python manage.py migrate
```
Create Superuser

```bash
  python manage.py createsuperuse
```
Load Data From CSV

```bash
  python manage.py runscript load_movies
```
```bash
  python manage.py runscript load_rating
```

Run Server

```bash
  python manage.py runserver
```
