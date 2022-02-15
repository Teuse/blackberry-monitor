#!/usr/bin/python3

import os
from strava_client import StravaClient
from strava_stats import Stats

client_id = os.environ['STRAVA_CLIENT_ID']
client_secret = os.environ['STRAVA_CLIENT_SECRET']
refresh_token = os.environ['STRAVA_REFRESH_TOKEN']


strava = StravaClient(client_id, client_secret, refresh_token)

athlete = strava.fetch_athlete()
athlete_id = athlete['id']

stats = strava.fetch_stats(athlete_id)

rides_total = Stats(stats['all_ride_totals'])
rides_year = Stats(stats['ytd_ride_totals'])

rides_total.print_as_line_protocol("total")
rides_year.print_as_line_protocol("year")

