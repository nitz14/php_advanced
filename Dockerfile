FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
        apt-get install -y \
        netcat \
        && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /source/
WORKDIR /source
RUN pip install -r requirements.txt
ADD . /source/

RUN chmod +x /source/docker-entrypoint.sh
EXPOSE 8000
CMD ["/source/docker-entrypoint.sh"]
