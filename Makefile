FKF_PASSWD?=
FKF_USER?=

fkf_run:
	@docker run --name fkf -v fkf:/app \
	--network nginx \
	-e DJANGO_SUPERUSER_PASSWORD=$(FKF_PASSWD) \
	-d hawkinswinja/fkf:1.0
.PHONY: fkf_run

set_admin: fkf_run
	@docker exec fkf python manage.py createsuperuser --name $(FKF_USER) --role admin --noinput
.PHONY: set_admin

set_nginx: set_admin
	@cp fkf.conf /var/nginx-conf
	@docker restart nginx
.PHONY: set_nginx
