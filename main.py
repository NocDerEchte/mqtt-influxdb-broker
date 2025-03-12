import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import os
import sys
from time import sleep

mqtt_host=os.environ.get("MQTT_HOST")
mqtt_port=int(os.environ.get("MQTT_PORT"))
mqtt_username=os.environ.get("MQTT_USERNAME")
mqtt_password=os.environ.get("MQTT_PASSWORD")
mqtt_topic=os.environ.get("MQTT_TOPIC")

influx_token=os.environ.get("INFLUX_TOKEN")
influx_url=os.environ.get("INFLUX_URL")
influx_org=os.environ.get("INFLUX_ORG")
influx_bucket=os.environ.get("INFLUX_BUCKET")
influx_measurement=os.environ.get("INFLUX_MEASUREMENT")

connected = False
connect_try_count = 1
max_connect_try_count = 3
wait_before_retry_seconds = 10

def on_connect(client, userdata, flags, reason_code, properties):
  print(f"Connected with result code {reason_code}")
  client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
  json_data = json.loads(msg.payload)
  point = Point(measurement_name=mqtt_topic)

  for field, value in json_data[influx_measurement].items():
    print(field, value)
    point.field(field=field, value=value)

  influx_write_api.write(bucket=influx_bucket, org=influx_org, record=point)


mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.username_pw_set(mqtt_username, mqtt_password)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

while not connected:
  if connect_try_count > max_connect_try_count:
    sys.exit(f'ERROR: Reached maximum amount of tries ({max_connect_try_count}). Exiting.')

  try:
    print(f'[Try {connect_try_count}] Connecting to mqtt broker...')
    mqtt_client.connect(mqtt_host, mqtt_port, 60)
    connected = True
  except:
    connect_try_count += 1
    print('Failed to connect to mqtt broker')
    print(f'Retrying in {wait_before_retry_seconds} seconds...')
    sleep(wait_before_retry_seconds)

influx_client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
influx_write_api = influx_client.write_api(write_options=SYNCHRONOUS)


mqtt_client.loop_forever()
