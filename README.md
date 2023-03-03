![](https://img.shields.io/badge/python-3.11-green)  ![](https://img.shields.io/badge/required-PostgreSQL-blue)
# Utility Calculator    

![App Screenshot](https://i.imgur.com/FtXkIUq.jpeg)


A simple utility bill calculator written in Django, using PostgreSQL as a database.
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PGDATABASE` - The database name

`PGUSER` - Username used to authenticate to database

`PGPASSWORD` - Password used to authenticate to database

`PGHOST` - Database host address (defaults to UNIX socket if not provided)

`PGPORT` - Database connection port number (defaults to 5432 if not provided)
## Run Locally

Clone the project
```bash
git clone https://github.com/Cyero/utcalc.git
```
Go to the project directory
```bash
cd utcalc
```
Install dependencies
```bash
poetry install
```
Generate a secret key
```bash
python3 key_gen.py
```
Start Django server 
```bash
python3 manage.py runserver
```
