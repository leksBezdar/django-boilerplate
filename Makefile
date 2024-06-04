PC = podman-compose
STORAGES_FILE = docker_compose/storages.yaml
EXEC = podman exec -it
DB_CONTAINER = main-postgres
LOGS = podman logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
MANAGE_PY = python manage.py

.PHONY: storages
storages:
	${PC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${PC} -f ${STORAGES_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql

.PHONY: storages-logs
storages-logs:
	${LOGS} --follow ${DB_CONTAINER} 

.PHONY: app
app:
	${PC} -f ${APP_FILE} ${env} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} --follow ${APP_CONTAINER} 

.PHONY: db-logs
db-logs:
	${PC} -f ${STORAGES_FILE} logs -f


.PHONY: app-down
app-down:
	${PC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} collectstatic


.PHONY: run-test
run-test:
	${EXEC} ${APP_CONTAINER} pytest