## Dockerized Django Project Boilerplate 🐋

a Dockerized Django Boilerplate to Starting your django Projects Productive ( also EZ as 🥧 )

## What Does this Boilerplate Includes ?

1. Both Dockerfile and docker-compose
2. Pre-Configured requirements for installing PostgreSQL and Pillow on Docker
3. Settings for Both Production and Development Environments
4. Pre Configured Security Settings
5. Flake8 for Code Quality
6. Gitignore for Git
7. Clean and Ready to use for your Project

## How to Use This Boilerplate ?

## Step 1 | Clone the Repo

```sh
git clone https://github.com/SeelpAydin/dockerized-django-project-boilerplate.git
cd dockerized-django-project-boilerplate
```

## Step 2 | Make a .env File

```sh
touch .env
```

Fill the .env file with your Project's Environment Variables

## The Minimal Credentials are :

1. ENVIROMENT (production or development)
2. SECRET_KEY
3. DOMAIN
4. DB_HOST
5. DB_NAME
6. DB_USER
7. DB_PASSWORD
8. DB_PORT
9. POSTGRES_DB
10. POSTGRES_USER
11. POSTGRES_PASSWORD

## Step 3 | Install Docker and Docker Compose

it's very easy to install Docker on your machine
simply follow the steps below

Link To the Official Docker Documentation : https://docs.docker.com/get-docker/

## Step 4 | Build The Docker Image

```sh
docker-compose build
```

it may take a while to build the image

## Step 5 | Make your First app

```sh
docker-compose run app sh -c "python manage.py startapp <app_name>"
```

## Step 6 | Run the app

For running the server simply run the following command

```sh
docker-compose up
```

Happy Coding 🥳
