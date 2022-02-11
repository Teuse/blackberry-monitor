#!/usr/bin/python3

import speedtest
from influx_client import InfluxClient

DEVICE_NAME = "raspberry_pi_1"


def run():
    print("Run metrics.py")

    client = InfluxClient(DEVICE_NAME)

    # SPEED
    speed_test = speedtest.Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    print(" Speed: down %.2f  up %.2f" % (download, upload))
    client.write_speed_measurement(download, upload)


if __name__ == "__main__":
    run()
