FROM python:3.12-alpine

WORKDIR /app

COPY ./pyscript ./pyscript
COPY ./pyodide ./pyodide
COPY ./js ./js
COPY ./css ./css
COPY ./img ./img
COPY ./l ./l
COPY index.html lesson.html playground.html pyscript.toml main.py ./

RUN echo "#!/bin/sh" > /run.sh && \
    echo "mkdir -p /public" >> /run.sh && \
    echo "rm -rf /public/*" >> /run.sh && \
    echo "cp -a /app/. /public/" >> /run.sh && \
    chmod +x /run.sh

CMD ["/run.sh"]
