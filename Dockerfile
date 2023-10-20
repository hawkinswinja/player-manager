FROM python:3.11.4-alpine
WORKDIR /app
EXPOSE 8000
ENV DJANGO_SUPERUSER_PASSWORD=admin
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY fkf /app/
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py createsuperuser --name admin --role admin --noinput
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "3", "manager.wsgi:application"]
