# mqtt-influxdb-connector

## Purpose

This docker-image can be used to receive data from an mqtt-broker and write this data into an influxdb database.

The main purpose was to use this in a school project.

## Prequisites

- working docker installation
- working influxdb instance
- working mqtt_broker like mosquitto


## Setup

### Building the image localy

1. Clone the repository and cd into it

```bash
git clone https://github.com/NocDerEchte/mqtt-influxdb-connector.git
cd mqtt-influxdb-connector
```

2. Build the docker image

```bash
docker build -t mqtt-influx-connector .
```

### Running the container

#### Docker compose:

```yml
services:
  mqtt-influx-connector:
    image: mqtt-influx-connector:latest
    restart: unless-stopped
    env_file:
      - path/to/.env/file
```

Make sure to create a .env file and set the values according to your needs.
All available variables can be found at [Configuration](#Configuration).


## Configuration

Environment variables:

| Variable           | Description                                                           | Default               |
| ------------------ | --------------------------------------------------------------------- | --------------------- |
| MQTT_HOST          | Host address or IP of the MQTT broker                                 | localhost             |
| MQTT_PORT          | Port number where the MQTT broker listens on                          | 1883                  |
| MQTT_USERNAME      | Username for authenticating with the MQTT broker                      |                       |
| MQTT_PASSWORD      | Password for the specified MQTT username                              |                       |
| MQTT_TOPIC         | The topic to subscribe to for receiving messages from the MQTT broker |                       |
|                    |                                                                       |                       |
| INFLUX_TOKEN       | Access token required for authenticating with InfluxDB v2             |                       |
| INFLUX_URL         | URL of the InfluxDB instance including port                           | http://localhost:8086 |
| INFLUX_ORG         | InfluxDB organization where data will be stored                       |                       |
| INFLUX_BUCKET      | InfluxDB bucket where data will be stored                             |                       |
| INFLUX_MEASUREMENT | InfluxDB measurement where data will be stored                        |                       |


## I'd appreciate Your Feedback!

As this is my first containerized application, I’d greatly appreciate any constructive feedback you have!
