# Todo App (Django)

A todo list built as a Django monolith: one project holds the URLs, the logic, the data and the HTML pages. There is no separate frontend; Django draws every page on the server.

## Folder structure

    todo-django/
    ├── manage.py                  # Django's command-line tool
    ├── config/                    # the project: settings and the root URL table
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py                # unused here
    │   └── wsgi.py
    ├── todos/                     # the app: one feature
    │   ├── models.py              # the Todo table
    │   ├── forms.py               # checks what people type
    │   ├── views.py               # list, create, toggle, delete
    │   ├── urls.py                # path → view
    │   ├── tests.py
    │   ├── admin.py               # unused here
    │   ├── migrations/            # database changes, generated from models.py
    │   ├── templates/todos/       # base.html, todo_list.html, todo_form.html
    │   └── static/todos/          # css/style.css, js/script.js
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## How the pieces connect

- models.py: what a todo is (title, completed, created_at)
- forms.py: turns what people type into a valid Todo
- views.py: the logic. Each view takes a request and returns a response
- urls.py: maps paths like /add/ to views
- templates/: the HTML. Views fill it with data
- static/: CSS and JavaScript, sent to the browser as they are

Request flow: browser → config/urls.py → todos/urls.py → view → model → database, then the view renders a template and Django sends the finished HTML back.

## Where each file comes from

Commands write some files; you write the rest. A few files are made by a command but never used by this project (marked unused). They stay in the repository, as in any real project, but you never need to open them.

    python -m venv venv
        └── venv/                                    generated, never committed
    pip freeze > requirements.txt
        └── requirements.txt
    django-admin startproject config .
        ├── manage.py
        ├── config/__init__.py
        ├── config/settings.py
        ├── config/urls.py
        ├── config/wsgi.py
        └── config/asgi.py                           unused
    python manage.py startapp todos
        ├── todos/__init__.py
        ├── todos/apps.py
        ├── todos/models.py
        ├── todos/views.py
        ├── todos/tests.py
        ├── todos/migrations/__init__.py
        └── todos/admin.py                           unused
    python manage.py makemigrations
        └── todos/migrations/0001_initial.py
    python manage.py migrate
        └── db.sqlite3                               generated, never committed
    written by you
        ├── todos/forms.py
        ├── todos/urls.py
        ├── todos/templates/todos/base.html
        ├── todos/templates/todos/todo_list.html
        ├── todos/templates/todos/todo_form.html
        ├── todos/static/todos/css/style.css
        └── todos/static/todos/js/script.js

## Run it on your computer

You need Python 3.10 or newer and Git.

### 1. Get the code

    git clone https://github.com/your-username/todo-django.git
    cd todo-django

### 2. Create the virtual environment and install Django

    python -m venv venv
    source venv/bin/activate          # Windows: venv\Scripts\activate
    pip install -r requirements.txt

### 3. Create the tables and start the server

    python manage.py migrate
    python manage.py runserver        # http://127.0.0.1:8000/

### 4. Run the tests

    python manage.py test

## Push it to GitHub

### 1. Create an empty repository

On github.com, click + → New repository. Name it todo-django and leave "Add a README file" unticked, so the repository starts empty.

### 2. Create a personal access token

GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token. Tick the repo scope, pick an expiry, then generate it and copy it: GitHub shows it only once. Git asks for it instead of your password.

### 3. Commit and push

From the todo-django folder:

    git init
    git config --global user.name "Your Name"          # once per computer
    git config --global user.email "you@example.com"   # the email on your GitHub account
    git add .
    git commit -m "feat: Django todo app"
    git remote add origin https://github.com/your-username/todo-django.git
    git branch -M main
    git push -u origin main                             # password: paste the token

After that, every change is three commands:

    git add .
    git commit -m "fix: describe the change"
    git push

Never commit venv/, db.sqlite3 or .env: .gitignore keeps them out. If a token leaks, delete it on GitHub and make a new one.
