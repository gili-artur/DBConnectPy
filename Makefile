#up: ##     build local environment
#	docker-compose -f ./docker/docker-compose-local.yml --env-file ./docker/env/.env.local up -d --build

up:
	docker compose -f ./docker/docker-compose.yml up -d --build

down:
	docker compose -f ./docker/docker-compose.yml down

app:
	docker exec -ti dbcp_python sh

appn:
	docker exec -ti dbcp_nginx sh

unicorn:
	docker exec -ti dbcp_python sh
	cd hanov && gunicorn --bind 0.0.0.0:7777 hanov.wsgi:application
