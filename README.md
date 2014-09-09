#Django Project Layout

Layout padrão para projetos Django

##System dependencies

* Django 1.7 (not tested on previous versions)

##Setup instructions

###Create and activate virtualenv

    virtualenv --no-site-packages {virtualenvs_path}/django-project-layout
    source {virtualenvs_path}/django-project-layout/bin/activate

###Install requirements

    cd {project_folder}
    pip install -r requirements.txt

###Create database

    createdb -U postgres -E utf-8 django-project-layout

###Create database tables

    cd {project_folder}/src
    ./manage.py migrate

###Create admin user

    cd {project_folder}/src
    ./manage.py createsuperuser

###Test it!
    
    cd {project_folder}/src
    ./manage.py runserver
    xdg-open http://localhost:8000/
