# Home Dashboard

Home Dashboard creates, as the name already says, a dashboard for my living room. It'll show e.g.
* Air Quality (meassured by the BME680 chip from Bosch)
* Cycling statistics (received from Strava)
* Internet Speed
* ...

This project is based on the TIG-Stack (Telegraf, InfluxDB and Grafana). Internet speed and Air Quality is measured on a rasperry pi collected by telegraf and stored the influxDB. All other data is collected by grafana datasoruces.

## Requirements

Software
* docker
* docker-compose

Hardware
* Raspberry Pi 
* Bosch BME680

Services
* Strava

## Required Environment Variables

You need to create a `.env` in your project root dir. 
```
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
> Note: More information about the reqired Strava ID, Secret and Token can be found here: https://developers.strava.com/

## Build and Run

In the project root dir, run:
```
docker-compose up -d
```
