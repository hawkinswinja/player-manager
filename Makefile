FKF_PASSWD?=
FKF_USER?=

all: fkf_run set_admin set_nginx
crashed: fkf_run set_nginx

fkf_run:
	@docker run --name fkf -v fkf:/app \
	--network nginx \
	-e DJANGO_SUPERUSER_PASSWORD=$(FKF_PASSWD) \
	-d hawkinswinja/fkf:1.1
.PHONY: fkf_run

set_admin:
	@docker exec fkf python manage.py createsuperuser --name $(FKF_USER) --role admin --noinput
.PHONY: set_admin

set_nginx:
	@cp fkf.conf /var/nginx-conf
	@docker restart nginx
.PHONY: set_nginx

stop_fkf:
	@docker rm -f fkf
	@docker rmi hawkinswinja/fkf:1.1
