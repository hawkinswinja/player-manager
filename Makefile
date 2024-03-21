FKF_PASSWORD?=
FKF_ADMIN?=
ALLOWED_HOSTS?=
TAG?=
SECRET_KEY?=

new_deploy: compose_up set_admin


compose_up:
	@TAG=$(TAG) ALLOWED_HOSTS=$(ALLOWED_HOSTS) DEBUG=$(DEBUG) SECRET_KEY=$(SECRET_KEY) FKF_PASSWORD=$(FKF_PASSWORD) docker compose up -d
.PHONY: fkf_run

set_admin:
	@docker exec pm-fkf-1 python manage.py createsuperuser --name $(FKF_ADMIN) --role admin --noinput
.PHONY: set_admin

update:
	@docker pull hawkinswinja/pm:$(TAG)
	@docker compose build --pull fkf
.PHONY: update

teardown:
	@docker compose down
.PHONY: teardown

reset:
	@docker compose down -v
.PHONY: reset

# example usage
## TAG=latest DEBUG=0 SECRET_KEY=test ALLOWED_HOSTS=localhost FKF_ADMIN=admin FKF_PASSWORD=admin make new_deploy
