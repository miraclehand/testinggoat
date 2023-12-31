Provisioning a new site
=======================

## Required packages;

* nginx
* Python 3.11
* Virtualenv + pip
* Git

eg, on Ubunto:
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python3.11 python3.11-venv


## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## SYstemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
|---sites
    |---DOMAIN1
    |    |--- .env
    |    |--- db.sqlite3
    |    |--- manage.py etc
    |    |--- static
    |    |--- virtualenv
    |---DOMAIN2
    |    |--- .env
    |    |--- db.sqlite3
    |    |--- etc
