DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
EXEC = docker exec -it
DB_CONTAINER = main-postgres
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
MANAGE_PY = python manage.py
MONITORING_FILE = docker_compose/monitoring.yaml


DB_USER = $(shell grep DB_USER .env | cut -d '=' -f2)
DB_PASS = $(shell grep DB_PASS .env | cut -d '=' -f2)


.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d --force-recreate

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql -U ${DB_USER} -d ${DB_NAME} -p ${DB_PORT}

.PHONY: storages-logs
storages-logs:
	${LOGS} -f ${DB_CONTAINER}

.PHONY: app
app:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: monitoring
monitoring:
	${DC} -f ${MONITORING_FILE} ${ENV} up --build -d

.PHONY: monitoring-logs
monitoring-logs:
	${DC} -f ${MONITORING_FILE} ${ENV} logs -f

.PHONY: app-logs
app-logs:
	${LOGS} -f ${APP_CONTAINER}

.PHONY: db-logs
db-logs:
	${DC} -f ${STORAGES_FILE} logs -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

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
