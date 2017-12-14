
default: init run

init:
	cd reminder_api && python manage.py makemigrations project
	cd reminder_api && python manage.py makemigrations reminder
	cd reminder_api && python manage.py makemigrations inventory
	cd reminder_api && python manage.py migrate

remove_memdb:
	rm reminder_api/db.sqlite3

run:
	cd reminder_api && python manage.py runserver
