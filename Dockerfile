FROM python:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt && chmod +x /app/gunicorn_config.sh
ENTRYPOINT ["./gunicorn_config.sh"]