# Home Dashboard

Home Dashboard creates, as the name already says, a dashboard for my living room. It'll show e.g.
* Air Quality (meassured by the BME680 chip from Bosch)
* Cycling statistics (received from Strava)
* ...

## Requirements

To build the project, i assume you have the following tools installed:
* Docker
* 

## Required Environment Variables

You need to create two `.env`. At first create a `.env` file in the project root dir with the following content
```
INFLUXDB_USERNAME=<username-for-influxdb>
INFLUXDB_PASSWORD=<password-for-influxdb
INFLUXDB_TOKEN=<token-for-influxdb>
INFLUXDB_ORG=<default-org-name>
INFLUXDB_BUCKET=<default-bucket-name>

GRAFANA_USERNAME=<username-for-grafana>
GRAFANA_PASSWORD=<password-for-grafana>
```

Next, you need the file `./bicycle/.env` with the following content:
> Note: More information about the reqired Strava ID, Secret and Token can be found here: https://developers.strava.com/
```
STRAVA_CLIENT_ID=<strava-client-id>
STRAVA_CLIENT_SECRET=<strava-client-secret>
STRAVA_REFRESH_TOKEN=<strava-refresh-token>
```

## Build and Run

In the project root dir, run:
```
docker-compose up -d
```
