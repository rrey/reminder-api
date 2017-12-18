DJANGO_MANAGE=cd reminder_api && python manage.py

default: init run

init:
	$(DJANGO_MANAGE) makemigrations project
	$(DJANGO_MANAGE) makemigrations reminder
	$(DJANGO_MANAGE) makemigrations inventory
	$(DJANGO_MANAGE) migrate

remove_memdb:
	rm reminder_api/db.sqlite3

run:
	cd reminder_api && python manage.py runserver

dockerbuild:
	docker build -t reminder_api .

dockerrun:
	docker run -it --rm -p 8000:8000 -d reminder_api
