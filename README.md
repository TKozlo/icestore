The iCream project is a small shop and blog about ice cream, which based on Django.

A catalog of products is presented that can be added to the user's shopping cart and paid (payment by Stripe). 
You can check the status of the order and contents.
The desktop version has a small addition (viewing the exchange rate and weather). There are a few Easter eggs for Generation Y.


Stack:

    Python
    PostgreSQL
    Redis

Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

Firstly, create and activate a new virtual environment:
     python3.10 -m venv ../venv
     ../venv/Scripts/activate
     
     
Make your changes in the .env.example file and remove ".example" from the file name
Install packages:

    pip install --upgrade pip
    pip install -r requirements.txt

Run project dependencies, migrations, fill the database with the fixture data etc.:
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py loaddata <path_to_fixture_files>
    ./manage.py runserver 

    Run Redis Server:
    redis-server

    Run Celery:
    celery -A store worker --loglevel=INFO
