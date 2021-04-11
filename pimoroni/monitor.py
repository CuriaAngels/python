import psutil
import time
import os
import datetime
from envirophat import weather, leds, light
from influxdb import InfluxDBClient

influx_host = "192.168.1.12"
port = 8086
dbname = "environment"
user = "root"
password = "root"
host = "Shiva"

client = InfluxDBClient(influx_host, port, user, password, dbname)
#client.create_database(dbname)

def get_cpu_temp():
    path="/sys/class/thermal/thermal_zone0/temp"
    f = open(path, "r")
    temp_raw = int(f.read().strip())
    temp_cpu = float(temp_raw / 1000.0)
    return temp_cpu

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage


def get_data_points():
    temp_cpu = get_cpu_temp()
    cpu_usage = get_cpu_usage()
    temperature = weather.temperature()
    pressure = round(weather.pressure(), 2)
    light_val = light.light()
    rgb = light.rgb()


    iso = datetime.datetime.now()
    iso = iso - datetime.timedelta(hours=2)
    iso = iso.isoformat()
    json_body = [
            {
                "measurement": "ambient_celcius",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": temperature,
                    "val": float(temperature)
                    }
                },
            {
                "measurement": "cpu_celcius",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": temp_cpu,
                    }
                },
            {
                "measurement": "cpu_usage",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": cpu_usage,
                    }
                },
            {
                "measurement": "ambient_light",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": light_val,
                    }
                },
            {
                "measurement": "rgb_sensor",
                "tags": {"colour": "Red"},
                "time": iso,
                "fields": {
                    "value": rgb[0],
                    }
                },
            {
                "measurement": "rgb_sensor",
                "tags": {"colour": "Green"},
                "time": iso,
                "fields": {
                    "value": rgb[1],
                    }
                },
            {
                "measurement": "rgb_sensor",
                "tags": {"colour": "Blue"},
                "time": iso,
                "fields": {
                    "value": rgb[2],
                    }
                },
            {
                "measurement": "ambient_pressure",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": pressure,
                    }
                }

            ]

    return json_body

try:
    while True:
        json_body = get_data_points()
        client.write_points(json_body)
        print (datetime.datetime.now().isoformat())
        time.sleep(30)

except KeyboardInterrupt:
    pass
