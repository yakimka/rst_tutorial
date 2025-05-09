FROM python:3.12-alpine

WORKDIR /app

COPY ./js ./js
COPY ./css ./css
COPY ./l ./l
COPY lesson.html index.html ./

RUN echo "#!/bin/sh" > /run.sh && \
    echo "cp -a /app /public" >> /run.sh && \
    chmod +x /run.sh

CMD ["/run.sh"]
