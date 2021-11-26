FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y \
        locales && \
    rm -r /var/lib/apt/lists/*

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

EXPOSE 8000

COPY . /app

ENV PYTHONPATH=/app/

ENTRYPOINT ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
