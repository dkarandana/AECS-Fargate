FROM python:3.6-slim

EXPOSE 80

RUN apt-get update && apt-get -y upgrade \ 
    && apt-get install -y default-libmysqlclient-dev build-essential \
    && apt-get install -y libcurl4-openssl-dev libssl-dev python3-dev \
    && pip install pipenv

WORKDIR /app

COPY Pip* /app/

RUN pipenv install --system

COPY . .

ENTRYPOINT ["/bin/bash"]

CMD [ "./run.sh" ]