# mqtt-influxdb-broker

## Purpose

This docker-image can be used to receive data from an mqtt-broker and write this data into an influxdb database.

The main purpose was to use this in a school project.

## Prequisites

- working docker installation
- working influxdb instance
- working mqtt_broker such as mosquitto


## Setup

### Building the image localy

1. Clone the repository and cd into it
2. 
```bash
git clone https://github.com/NocDerEchte/mqtt-influxdb-broker.git
cd mqtt-influxdb-broker
```

1. Build the docker image
2. 
```bash
docker build -t mqtt-influx .
```

### Running the container

#### Docker compose

```yml
services:
  mqtt-influx:
    image: mqtt-influx:latest
    restart: unless-stopped
    env_file:
      - mqtt-influx.env
```

Make sure to create a .env file and set the values according to your needs.

## I'd Love Your Feedback!

As this is my first containerized application, I’d greatly appreciate any constructive feedback you have!