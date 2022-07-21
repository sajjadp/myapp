FROM python:3.8.9

WORKDIR /code

RUN pip install flask
RUN pip install Flask-SQLAlchemy

COPY . /code/app

EXPOSE 8080
CMD ["python3", "/code/app/main.py"]