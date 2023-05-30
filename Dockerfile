FROM python:3.8.11-alpine3.14

WORKDIR /service/app

COPY requirements.txt /service/app
COPY application /service/app/application

RUN apk --no-cache add curl build-base npm
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8081

ENV PYTHONUNBUFFERED 1

HEALTHCHECK --timeout=30s --interval=1m30s --retries=5 \
  CMD curl -s --fail http://localhost:8081/health || exit 1

CMD ["python3", "-u", "application/app.py"]
