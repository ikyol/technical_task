# Django API Technical Task
## Installation
Clone the project

```bash
$ git@github.com:ikyol/technical_task.git
$ cd technical_task
```

Now you should make `env` file
```bash
$ touch .env
```
then, fill the fields in the `.env`
```txt
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=
SECRET_KEY=
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_USE_TLS=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

```

## Usage
To start the Django development server, run the following command:

```bash
docker-compose up -d
```

## Or 


Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then, install the required packages:

```bash
(venv)$ pip install -r requirements.txt
```

```bash
(venv)$ python manage.py runserver
```

This will start the development server at http://localhost:8000/.

To create the database tables, run the following command:

```bash
(venv)$ python manage.py migrate
```

You can access the Django admin panel at http://localhost:8000/admin/. To create a superuser account, run the following command and follow the prompts:

```bash
(venv)$ python manage.py createsuperuser
```