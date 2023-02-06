# Blackberry Monitor

The Blackbarry Monitor is a dashboard for all the most important values I want to see on a daily basis

* Air Quality (meassured by the BME680 chip from Bosch)
* Cycling statistics (received from Strava)
* Internet Speed
* ...

This project is based on the TIG-Stack (Telegraf, InfluxDB and Grafana). Internet speed and Air Quality is measured on a rasperry pi collected by telegraf and stored the influxDB. All other data is collected by grafana datasoruces.

## Air Quality

| Air Quality | CO2 Gehalt (%) | CO2 Konzentration in ppm |
| --- | --- | --- |
| High room air quality | < 0.08% | < 800 |
| Mid room air quality  | 0.08% - 0.1% | 800 - 1000 |
| Low room air quality  | 0.1% - 0.14% | 1000 - 1400 |
| Bad room air quality  | > 0.14% | > 1400 |

## Requirements

Software

* docker
* docker-compose

Hardware

* Raspberry Pi
* MH-Z19B
* Bosch BME680

Services

* Strava

## Required Environment Variables

You need to create a `.env` in your project root dir.

```bash
INFLUXDB_USERNAME=<username-for-influxdb>
INFLUXDB_PASSWORD=<password-for-influxdb
INFLUXDB_TOKEN=<token-for-influxdb>
INFLUXDB_ORG=<default-org-name>
INFLUXDB_BUCKET=<default-bucket-name>

GRAFANA_USERNAME=<username-for-grafana>
GRAFANA_PASSWORD=<password-for-grafana>

STRAVA_CLIENT_ID=<strava-client-id>
STRAVA_CLIENT_SECRET=<strava-client-secret>
STRAVA_REFRESH_TOKEN=<strava-refresh-token>
```

> Note: More information about the reqired Strava ID, Secret and Token can be found here: <https://developers.strava.com/>

## Build and Run

In the project root dir, run:
```docker compose up -d```

### Enable Serial Port for accessing the MH-Z19

```sudo raspi-config```

Go to Advanced Options/Serial and set No to "Would you like a login shell to be accessible over serial?", and Yes to the follwong Queston. Reboot.

Also, sometimes the UART is disabled in kernel. The enable it you need to check in /boot/config.txt the line enable_uart

```bash
[all]
enable_uart=1
```
