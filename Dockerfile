FROM python:3.8.2

ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /src/
RUN python manage.py collectstatic --no-input
EXPOSE 8000
CMD ["gunicorn", "--timeout", "300", "--chdir", "team_management_service", "--bind", ":8000", "team_management_service.wsgi:application"]