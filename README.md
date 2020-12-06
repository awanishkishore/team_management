# Team Member Project


### How to set it up?
<br/>

#### Method 1: Normal setup
**Prequisites**
Following dependencies must be installed in your system:
- Postgres
- Python 3.8 or above

**Steps**
1. Clone this repository.
2. Create .env file in root directory. (Contents of .env is present below.)
3. Install requirements.txt using command `pip install -r requirements.txt`
4. Migrate migration files using `python manage.py migrate`
5. (Optional) To access admin panel, run `python manage.py createsuperuser`
6. Start web server with `python manage.py runserver`
<br/><br/>

#### Method 2: Docker setup
**Prequisites**
Following dependencies must be installed in your system:
- Docker & Docker Compose

**Steps**
1. Clone this repository.
2. Create .env file in root directory. (Contents of .env is present below.)
3. Set `IS_DOCKERIZED=1` in .env file.
4. Run `docker-compose up --build -d`
5. Run `docker exec -it team_service /bin/bash`
6. Now migrate migration files using `python manage.py migrate`
7. (Optional) To access admin panel, run `python manage.py createsuperuser`
<br/><br/>

### How to test this project?
All the endpoints with CURL command & example are publised [here](https://documenter.getpostman.com/view/11856231/TVmQdvYm)
<br/><br/>

#### .env example
```yaml
SECRET_KEY=whatever_secret_you_want_to_keep

### DB Settings ###
POSTGRES_DB=team_members
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_PORT=5432

IS_DOCKERIZED=0
```