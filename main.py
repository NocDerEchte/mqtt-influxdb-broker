import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import os


mqtt_host=os.environ.get("MQTT_HOST")
mqtt_port=int(os.environ.get("MQTT_PORT"))
mqtt_username=os.environ.get("MQTT_USERNAME")
mqtt_password=os.environ.get("MQTT_PASSWORD")
mqtt_topic=os.environ.get("MQTT_TOPIC")

influx_token=os.environ.get("INFLUX_TOKEN")
influx_url=os.environ.get("INFLUX_URL")
influx_org=os.environ.get("INFLUX_ORG")
influx_bucket=os.environ.get("INFLUX_BUCKET")



def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(mqtt_topic)
    
def on_message(client, userdata, msg):
    # try:
        json_data = json.loads(msg.payload)
        point = Point(measurement_name=mqtt_topic)
        
        for field, value in json_data["measurements"].items():
            print(field, value)
            point.field(field=field, value=value)
            
        influx_write_api.write(bucket=influx_bucket, org=influx_org, record=point)
    # except:
    #     print("Error when writing to DB!")
    #     print("Not valid JSON!")
  
        

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.username_pw_set(mqtt_username, mqtt_password)
mqtt_client.connect(mqtt_host, mqtt_port, 60)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


influx_client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
influx_write_api = influx_client.write_api(write_options=SYNCHRONOUS)


mqtt_client.loop_forever()