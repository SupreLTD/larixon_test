 MANAGE = python3 manage.py

 run:
	sudo docker-compose up --build


 back:
	${MANAGE} makemigrations
	${MANAGE} migrate
	${MANAGE} initadmin
	${MANAGE} runserver 0.0.0.0:8000

p:
	ls
