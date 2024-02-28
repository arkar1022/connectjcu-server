FROM python:3.11.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for mysqlclient
# RUN apt-get update && apt-get install -y \
#     gcc \
#     libc-dev \
#     libssl-dev \
#     libffi-dev \
#     libmariadb-dev \
#     pkg-config \
#     default-libmysqlclient-dev

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev

WORKDIR /app
COPY ./connectjcuServer ./

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "connectjcuServer.wsgi:app","--bind","0.0.0.0:8000"]