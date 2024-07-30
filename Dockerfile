FROM python:3.10.0
RUN apt-get update && \
    apt-get install -y build-essential python vim net-tools && \
    pip install uwsgi

WORKDIR /code
COPY ./ /code
RUN pip install  --default-timeout=1000 -r /code/requirements.txt
RUN python /code/manage.py collectstatic --noinput
CMD [ "uwsgi", "--ini", "/code/archiveAPI.uwsgi.ini" ]
