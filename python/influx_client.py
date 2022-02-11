import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

INTERNET_SPEED_KEY = "internet_speed"

class InfluxClient:
    __token = os.environ['INFLUXDB_TOKEN']
    __org = "org0"
    __bucket = "bucket0"

    def __init__(self, device_name):
        self.device_name = device_name

        self.client = InfluxDBClient(url='http://localhost:8086', token=self.__token, org=self.__org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_speed_measurement(self, download, upload):
        p = Point(INTERNET_SPEED_KEY).tag("location", "home").tag("device_name", self.device_name).field("download", download).field("upload", upload)
        self.write_api.write(bucket=self.__bucket, org=self.__org, record=p)
        



