FROM python:3.11.4-alpine
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY fkf /app/
EXPOSE 8000
RUN python manage.py migrate
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "3", "fkf.wsgi:application"]