# Initial-Django-Project-Setup
Inital Django rest Project setup for three server like local, tests and production.

`Supports Python version 3.8` 

Setup .env file, using example.env

## Setup on local
#### First clone this repo
> git clone https://github.com/Sem31/Initial-Django-Project-Setup.git

#### Create virtaulenv
> python -m venv env

#### Instaill requirement file for local
> pip install -r requirements/local.txt

#### Migrate code
> make migrate

#### Run project
> make run

#### Run Testcases
> make test
