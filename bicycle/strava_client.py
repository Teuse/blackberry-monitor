import requests


class StravaClient:
    __access_token = ""

    def __init__(self, client_id, client_secret, refresh_token):
        self.__access_token = self.__fetch_access_token(client_id, client_secret, refresh_token)


    def fetch_activities(self):
        url = "https://www.strava.com/api/v3/athlete/activities"
        param = {'per_page': 200, 'page': 1}
        return requests.get(url, headers=self.__headers(), params=param).json()


    def fetch_athlete(self):
        url = "https://www.strava.com/api/v3/athlete"
        return requests.get(url, headers=self.__headers()).json()


    def fetch_stats(self, athlete_id):
        id_str = str(athlete_id)
        url = "https://www.strava.com/api/v3/athletes/" + id_str + "/stats"
        return requests.get(url, headers=self.__headers()).json()


    def __headers(self):
        if self.__access_token == "":
            print("Access Token not available")
        return {'Authorization': 'Bearer ' + self.__access_token}


    def __fetch_access_token(self, client_id, client_secret, refresh_token):
        auth_url = "https://www.strava.com/oauth/token"

        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token,
            'grant_type': "refresh_token",
            'f': 'json'
        }
        res = requests.post(auth_url, data=payload, verify=False)
        return res.json()['access_token']

