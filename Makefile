#up: ##     build local environment
#	docker-compose -f ./docker/docker-compose-local.yml --env-file ./docker/env/.env.local up -d --build

up:
	docker compose -f ./docker/docker-compose.yml --env-file ./docker/env/.env up -d --build

down:
	docker compose -f ./docker/docker-compose.yml --env-file ./docker/env/.env down

app:
	docker exec -ti dbcp_python sh

appn:
	docker exec -ti dbcp_nginx sh
