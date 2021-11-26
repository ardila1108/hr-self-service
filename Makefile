build:
	docker build -t hrss .

run:
	docker run --rm -p 8000:8000 --env-file .env hrss

stop:
	docker stop $$(docker ps -q --filter ancestor=hrss)

format:
	black .
