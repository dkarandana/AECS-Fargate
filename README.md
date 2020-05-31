### Technologies
- django - python based web framework
- gunicorn - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.
- database - AWS RDS (mysql)
- deployment service - DOCKER & AWS ECS (Fargate Type)
- authentication - oauth strategy


### development

- install tools
```
    apt-get install -y default-libmysqlclient-dev build-essential
    apt-get install -y libcurl4-openssl-dev libssl-dev python3-dev
```

- install pipenv ( python package manager )
```
    pip --version # check pip use python3
    pip install pipenv
```
- create virtual environment
```
    git pull origin .
    pipenv shell     # use this command in root folder
```

- install dependency
```
    pipenv install
```

- setting up .env
```
    touch .env
    cp .env.example .env # change environment keys
```

- run development server
```
    python manage.py runserver
```

- migrate the database (if change the db schema we need to migrate the db)
```
    python manage.py makemigrations     # create new schema files (migration files)
    python manage.py migrate     # migrate db using schema files
```

- sync with oauth database (for the first time)
```
    python manage.py migrate oauth2_provider
```

- create django superuser
```
    python manage.py createsuperuser
```

- install aws cli
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
```
    sudo apt-get install awscli
```

- build image + push to ECR (elastic container registry) service
#### make sure virtualenvironment is active bcz aws access key + secret need to login
```
    docker build -t shipfast_service . &&     
    $(aws ecr get-login --no-include-email --region ap-southeast-1 ) &&     
    docker tag shipfast_service:latest 361704631334.dkr.ecr.ap-southeast-1.amazonaws.com/shipfast:latest &&    
    docker push 361704631334.dkr.ecr.ap-southeast-1.amazonaws.com/shipfast:latest 
```

### AUTHENTICATION SERVICE

- user authentication and get access token
#### we can find client id and client secret of oauth application using following url
http://localhost:8000/admin/oauth2_provider/application/

```
curl --location --request POST 'http://localhost:8000/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=<CLIENT ID>' \
--data-urlencode 'client_secret=<CLIENT SECRET>' \
--data-urlencode 'username=<USERNAME>' \
--data-urlencode 'password=<PASSWORD>'
```

- create new access token from refresh token

```
curl --location --request POST 'http://localhost:8000/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token=<REFRESH_TOKEN>' \
--data-urlencode 'client_id=<CLIENT ID>' \
--data-urlencode 'client_secret=<CLIENT SECRET>'
```

- view profile (test authentication)
```
curl --location --request GET 'http://localhost:8000/user/profile/' \
--header 'Authorization: Bearer <ACCESS_TOKEN>' \
```