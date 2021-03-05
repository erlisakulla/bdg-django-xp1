# se-01-team-30
SE Sprint 01, Team 30

# Implementation:
* **Frontend:** HTML, CSS, JS, Bootstrap  
* **Backend:** Python, Django

For the implementation we also reused a Bootstrap template for the instructor user pages that can be found on the [CoolAdmin](https://github.com/puikinsh/CoolAdmin) repository. You can use the several components provided by the different layouts to style the page. We do not claim ownership over the template used. We have only used the necessary components to make our implementation easier. 
Below you can find some useful resources and tutorials about Django implementation and documentation, for those who are new to the framework.
* [CRM Tutorial Playlist](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
* [Django Website](https://www.djangoproject.com)

# Description
##### What we have implemented so far:
* Instructor can register and login
* Student can register for games
* Instructor can only view registered students that have him/her as an instructor
* Instructor can create and view list of games (no game logic implemented yet)
* Instructor can delete Student from list
* Instructor can change password and delete their account

##### Further implementation ideas/aims:


# How to run

Assumming that you have ```pip``` and ```django``` installed you can run the project by moving inside the project directory and running the command  
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
