FROM python:3-alpine

RUN pip install influxdb-client paho-mqtt

WORKDIR /opt/mqtt-influx/
COPY ./main.py .

ENTRYPOINT [ "/usr/local/bin/python3", "main.py" ]