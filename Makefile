FKF_PASSWORD?=password
FKF_ADMIN?=admin
ALLOWED_HOSTS?=localhost
TAG?=latest
SECRET_KEY?=not_secret
DOCKER_PASSWORD?=
DOCKER_USERNAME?=

new_deploy: teardown compose_up set_admin

build:
	@docker build -t pm:latest .
.PHONY: build

test:
	@docker run --rm pm:latest python manage.py test
.PHONY: test

push:
	@docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)
	@docker tag pm:latest $(DOCKER_USERNAME)/pm:$(TAG)
	@docker push  $(DOCKER_USERNAME)/pm:$(TAG)
.PHONY: push

compose_up:
	@TAG=$(TAG) ALLOWED_HOSTS=$(ALLOWED_HOSTS) DEBUG=0 SECRET_KEY=$(SECRET_KEY) FKF_PASSWORD=$(FKF_PASSWORD) docker compose up -d
.PHONY: compose_up

set_admin:
	@docker exec pm-fkf-1 python manage.py createsuperuser --name $(FKF_ADMIN) --role admin --noinput
.PHONY: set_admin

update:
	@TAG=$(TAG) ALLOWED_HOSTS=$(ALLOWED_HOSTS) DEBUG=0 SECRET_KEY=$(SECRET_KEY) FKF_PASSWORD=$(FKF_PASSWORD) docker compose build --pull fkf
.PHONY: update

teardown:
	@docker compose down
.PHONY: teardown

reset:
	@docker compose down -v
.PHONY: reset

# example usage
## TAG=latest DEBUG=0 SECRET_KEY=test ALLOWED_HOSTS=localhost FKF_ADMIN=admin FKF_PASSWORD=admin make new_deploy
