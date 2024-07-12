FROM python:3.7-slim

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

COPY bicycle_rent/ /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1
CMD ["python3", "manage.py", "runserver", "0:8000"] 