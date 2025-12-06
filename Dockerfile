FROM python:3.12-slim

WORKDIR /app

# first copy only requirements.txt to run pip install, later copy rest of the project
COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5556

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5556

CMD ["flask", "run", "--host=0.0.0.0", "--port=5556"]
