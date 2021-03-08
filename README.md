# se-01-team-30
SE Sprint 01, Team 30  
March 10th, 2021

# Implementation:
* **Frontend:** HTML, CSS, JS, Bootstrap  
* **Backend:** Python, Django

For the implementation we also reused a Bootstrap template for the instructor user pages that can be found on the [CoolAdmin](https://github.com/puikinsh/CoolAdmin) repository. You can use the several components provided by the different layouts to style the page. We do not claim ownership over the template used. We have only used the necessary components to make our implementation easier. 
Below you can find some useful resources and tutorials about Django implementation and documentation, for those who are new to the framework.
* [CRM Tutorial Playlist](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
* [Django Website](https://www.djangoproject.com)

# Requirements
1. **[Install Python](https://www.python.org/downloads/)**
2. **[Install PIP](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py)**
3. **Install Django**
```
python -m pip install Django
```

# Description
### What we have implemented in XP1:
* Instructor can register and login (we have not implemented student account registration and log in)
* Student can register for games
* Instructor can only view registered students that have him/her as an instructor
* Instructor can create and view list of games created by them (no game logic implemented yet)
* Instructor can update and delete Games
* Users can't access dashboard and other internal pages without being logged in

### Project Structure
Every Django project has a very specific file structure. It contains different 'apps' which serve a specific function in the project. In our case, our apps serve the roles of the different classes needed for the project. You can create new apps using `python manage.py startapp {appname}`. We have implemented the following apps: `instructor`, `student`, `game`. We have also created the following apps but not implemented them: `demand_pattern`, `role`. Every created app must be included in the `INSTALLED_APPS` array in `settings.py`.

##### File Structure
```
beer_game/                          # project directory
    beer_game/                      # main project default app
        mysite/
            __init__.py
            asgi.py
            settings.py             # settings/configuration for the project
            urls.py
            wsgi.py
    instructor/
        migrations/ ...             # stores migration files
        templates/                  # all html templates must be stored here
            instructor/
                # html files
        __init__.py
        admin.py
        apps.py
        filters.py                  # setting up filters from django_filters
        forms.py                    # includes forms such as the registration form
        models.py                   # setting up the classes used in the project
        tests.py                    # used for writing test cases
        urls.py                     # creates url paths from views
        views.py                    # setting up web requests and web responses
    student/ ...
    game/ ... 
    ...
    static/                         # stores static files such as css, js, images etc. 
        css/                        # write {% load static %} inside templates
        js/
        ...
    db.sqlite3                      # default Django database is SQLite
    manage.py                       # command-line utility to interact with the project
```

##### Migrations
Migrations are a way of propagating the changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They're mostly automatic, but you'll know when migrations are neccessary to make as they will appear on the terminal. You use the following commands to migrate
```
python manage.py makemigrations
python manage.py migrate
```

# How to run locally

Inside the project directory and run the command  
```
python manage.py runserver
```
If you get errors, make sure you have psycopg2 module installed: 

```
pip install psycopg2-binary
```

Then go to the address provided by the server: http://127.0.0.1:8000/. It will take you to the main home page. To access admin features and the database provided by django itself simply go to http://127.0.0.1:8000/admin/. Which will require you to enter an email and password. We created an admin user with the credentials below:   
* **Email:** manager@beergame.com	 
* **Password:** manager  

You can create another admin user by running ```python manage.py createsuperuser``` and filling the neccessary fields. You can then use these credenatials to access the admin view.  
Some pages, for example the dashboard, are only accessible after Login so in order to open them you have to be logged in. You can use the credentials provided above in the Instructor Login Form or you can register a user using the Instructor Registration Form (these users do not have admin permissions) and then login with the created data. These pages are available the whole time you are logged in.

# Testing

# Deployment
This project is deployed using Heroku and can be accessed through https://bdg-test.herokuapp.com. However this is connected to a personal account and if necessary, we could either add other members as collaborators or deactivate the current deployment, and the next team can re-deploy this project on their personal accounts. A tutorial on how to deploy to Heroku can be found [here](https://www.youtube.com/watch?v=kBwhtEIXGII&t=1145s).

Issues and errors can be seen through the Heroku logs (More > View logs). This might mean that you won't be able to run the project locally, however every change that you make to the project and commit to this repository will be automatically rebuilt by Heroku if you enable automatic deploys.
