# TRANSITO API

This API was built with python3.10, Django 4.15 and Postgres 14.1

## Asumptions

1. For simplicity purposes, only Policia can login the webapp, overriding user with Policia class.
2. The method `cargar_infraccion`is in the POST method of the endpoint: `/api/infraciones/`
3. The method `generar_reporte` is in the GET method of the endpoint: `/api/infraciones/`
4. Since Policia class overrides User class, the method to create a new Policia is registering a new user with the endpoint `/api/register/`
5. The env variables to run the project are in the docker-compose.yml
6. In order to get the Bearer token is necessary to login with an existing user with the endpoint `api/token/`
7. This project use the django admin to manage recods in the endpoint `admin/`

## RUN PROJECT

### VirtualEnv

Use a virtualenv to run the app

```bash
virtualenv .env
pip install -r requirements.txt
python manage.py runserver
```

### Docker Compose

Use docker-compose to run the app

```bash
docker-compose up -d
```

It will build the image and run it using docker-compose
The app can be accessed using por 8000

## Create admin user

### Virtualenv

If you are running the project with virtualenv you need to execute the following command

```bash
python manage.py createsuperuser
```

### Docker Compose

First you need to open a shell inside the app's container

```bash
docker ps
docker exec -it [CONTAINER-ID] /bin/bash
python manage.py createsuperuser
```

## Run tests

```bash
python manage.py test
```

## API documentation

The API documentation is in the endpoint `/swagger/`
You can import the Postman collection to tests the API endpoints
The token is saved as a collection variable each time you run the login request.

## Docker Hub image

The docker image can be found in this [link](https://hub.docker.com/repository/docker/seethersan/transito/general)

## Proposed AWS Arquitecture

1. Amazon ECR: It can be used to store the docker images of the app.
2. Amazon ECS: With a ECS cluster we can host the Docker containers and configure it to work with the Django application and PostgreSQL database.
3. Amazon RDS: We can create a new PostgreSQL database instance using RDS and configure it to work with the Django application.
4. Elastic Load Balancer: Can be used to distribute incoming traffic across multiple instances of your Django application running in ECS. We can configure the load balancer to route traffic to the ECS service and set up health checks to ensure that your service is working correctly.
5. Amazon S3: We can configure the Django application to use S3 to store these files, and use the Django Storages library to interact with the S3 API.
6. Amazon Route 53: We can use Route 53 to manage the domain name and configure DNS records to route traffic to the Django application.
