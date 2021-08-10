{{cookiecutter.project_slug}}
========

{{cookiecutter.description}}


overview
========


quickstart
==========

Moke sure you have docker_ installed to try this quickstart.

::
    # clone this repo
    $> git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git
    $> cd {{ cookiecutter.project_slug }}

    # start docker services
    $> docker-compose up
    $> docker-compose exec web python manage.py migrate
    $> docker-compose exec web python manage.py createsuperuser
    $> open http://localhost:8000/admin


unit tests
==========

::
    # from the project root dir
    $> pytest test

---eop

