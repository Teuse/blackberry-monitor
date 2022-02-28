FROM telegraf:latest

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 python3-pip python3-setuptools python3-wheel && \
    rm -rf /var/lib/apt/lists/*

RUN DEBIAN_FRONTEND=noninteractive pip3 install adafruit-circuitpython-bme680

