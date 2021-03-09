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

**Notes (for further implementation):** The main idea is that students register for games by submitting their name, email and instructor, and the interested students will then appear on the specified instructor's dashboard.

The instructor creates and monitors games. He can create several games either through the 'Create Game' button or in the Setup Games page (not implemented) and then view all games in the All Games page. Then, the instructor can assign students to one or multiple games by selecting 2-4 students in the dashboard list and then clicking 'Assign Selected'. Students can also be assigned through writing their ids in the Game Creation Form. The roles and passwords can be assigned either using a random algorithm or just by order of selection, or even manually assigned. Maybe if there are too many students on the list, there could be an option to automatically create multiple games at a time and automatically assign a maximum of 4 students per game. 

We have not implemented the student assignment to a game on this project but our implementation idea was as stated above. 

Instructors could then see what games the students are assigned to (or not) and what students are assigned to a game (or not). After assigning students to games, instructors can then click on the 'Send Email' button on each student which will send an automatic email to them with the link to the game, the game number, the role and password. 

Proper error checking should also be implemented to avoid issues. For example checking that a student has an assigned game before sending an email, not assigning more than 4 students to a game and so on.  

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
        tests/                      # stores test cases
            test_models.py          # test cases for models
            test_views.py           # test cases for views(endpoints)
            test_forms.py           # test cases for custom validators in forms
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
Migrations are a way of propagating the changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They're mostly automatic, but you'll know when migrations are necessary to make as they will appear on the terminal. You use the following commands to migrate
```
python manage.py makemigrations
python manage.py migrate
```

# How to run locally

Inside the project directory and run the command  
```
python manage.py runserver
```
Then go to the address provided by the server: http://127.0.0.1:8000/. It will take you to the main home page. To access admin features and the database provided by django itself simply go to http://127.0.0.1:8000/admin/. Which will require you to enter an email and password. We created an admin user with the credentials below:   
* **Email:** manager@beergame.com	 
* **Password:** manager  

You can create another admin user by running ```python manage.py createsuperuser``` and filling the necessary fields. You can then use these credentials to access the admin view.  
Some pages, for example the dashboard, are only accessible after Login so in order to open them you have to be logged in. You can use the credentials provided above in the Instructor Login Form or you can register a user using the Instructor Registration Form (these users do not have admin permissions) and then login with the created data. These pages are available the whole time you are logged in.

# Testing
Inside the project directory and run the command.  
```
python manage.py test
```
If you want to run a subset of your tests you can do so by specifying the full dot path to the package(s), module, TestCase subclass:

Run the specified module
```
python3 manage.py test instructor.tests
```
Run the specified module
```
python3 manage.py test instructor.tests.test_models
```
Run the specified class
```
python3 manage.py test instructor.tests.test_models.YourTestClass
```
You might find this [guide](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing) on testing Django projects helpful.

# Deployment
This project is deployed using Heroku and can be accessed through https://bdg-test.herokuapp.com. However this is the deployment of the forked repository and it is connected to a personal account. Other teams, could also deploy it by connecting Heroku to this repository or another forked one. A tutorial on how to deploy to Heroku can be found [here](https://www.youtube.com/watch?v=kBwhtEIXGII&t=1145s).

Issues and errors can be seen through the Heroku logs (More > View logs). This might mean that you won't be able to run the project locally, however every change that you make to the project and commit to the repository will be automatically rebuilt by Heroku if you enable automatic deploys.
