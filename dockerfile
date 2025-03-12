FROM python:3-alpine AS setup

RUN pip install influxdb-client paho-mqtt

FROM setup

WORKDIR /opt/mqtt-influx/
COPY ./main.py .

ENTRYPOINT [ "/usr/local/bin/python3", "main.py" ]
