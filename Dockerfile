FROM python:3.11.4-alpine
WORKDIR /app
EXPOSE 8000
COPY requirements.txt .
RUN useradd -D user && pip install -r requirements.txt --no-cache-dir
USER user
COPY fkf /app/
CMD gunicorn manager.wsgi:application -b *:8000