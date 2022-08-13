# my_cms-team18
This is the repo of team18 project (my_cms)
Our project is bulit mainly on Python django, html, css, bootstarp and javascript.
# Overview of our project
![FORGE-PRESENTATION-1](https://user-images.githubusercontent.com/99877794/181842658-e05cc7dc-072b-4629-b44a-b260413ff532.png)

# Our objectives
![FORGE-PRESENTATION-1 (1)](https://user-images.githubusercontent.com/99877794/181843152-f28fb95d-b75a-444d-9f17-542c60abeebf.png)
# Our approach
![FORGE-PRESENTATION-1 (2)](https://user-images.githubusercontent.com/99877794/181843231-5869975c-1cb7-4439-9fcf-f0415d2e5217.png)
# How to run our project
The first thing to do is to clone the repository:

```sh
$ git clone git clone https://github.com/zuri-training/my_cms-team18.git
$ cd my_cms-team18
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -3 -m venv env
$ env\Scripts\activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment 

Once `pip` has finished downloading the dependencies:

make migrations and push the migrations

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate

```

create an admin user

```sh
(env)$ python manage.py createsuperuser
```

then run the server

```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

![FORGE-PRESENTATION-1 (3)](https://user-images.githubusercontent.com/99877794/181843303-0098c9e7-8dca-4f9b-911a-8399bc2b656c.png)

Link to our database schema
https://drive.google.com/file/d/1E4H7Ckv_2P45EUTUxayloc0C-x4AvUxZ/view

Link to our Documentation
-Developer Documentation
https://docs.google.com/document/d/14_LQ54L0qXpyRUN3glvCZCa5h3FgB0z7YmGHMV4uaQA/edit?usp=drivesdk

-User Documentation
https://docs.google.com/document/d/1pAkt-nka2xg3yS5JntEQonmNzkCWfY8ds12Nr1skM2I/edit?usp=sharing
