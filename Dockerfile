FROM python:3.11

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY req.txt /app/

RUN pip install -r req.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]