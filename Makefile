DJANGO_MANAGE=cd reminder_api && python manage.py

default: init run

init:
	$(DJANGO_MANAGE) makemigrations project
	$(DJANGO_MANAGE) makemigrations reminder
	$(DJANGO_MANAGE) makemigrations inventory
	$(DJANGO_MANAGE) migrate

remove_memdb:
	rm reminder_api/db.sqlite3

clean_migrations:
	rm -fr reminder_api/{project,reminder,inventory}/migrations

run:
	cd reminder_api && python manage.py runserver

dockerbuild:
	docker build -t reminder_api .

dockerrun:
	docker run -it --rm -p 8000:8000 -d reminder_api

check:
	$(DJANGO_MANAGE) test
