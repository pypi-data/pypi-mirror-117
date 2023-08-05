from NaijaBet_Api.utils.normalizer import betking_match_normalizer
from pprint import pprint
import requests
from NaijaBet_Api.id import Betid
from NaijaBet_Api.utils import jsonpaths

"""
[summary]
"""
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "referrer": "https://www.betking.com/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "method": "GET",
    "mode": "cors",
    "credentials": "include"
}


class Betking:
    """
     This class provides access to https://betking.com/sports 's odds data.

     it provides a variety of methods to query the endpoints and obtain
     odds data at a competiton and match level.

    Attributes:
        session: holds a requests session object for the class as a static variable.
    """

    session = requests.Session()
    session.get("https://betking.com/sports/s")

    def __init__(self) -> None:
        """
        Inits the class
        """
        self.site = "betking"

    def get_nations(self, nation: str):

        pass

    def get_competitions():
        pass

    def get_team(self, team):
        pass

    def get_league(self, league: Betid = Betid.PREMIERLEAGUE):
        """
        Provides access to available league level odds for unplayed matches

        Returns:
            [type]: [description]
        """
        print(league.to_endpoint(self.site))
        try:
            res = Betking.session.get(url=league.to_endpoint(self.site))
            print(res.status_code)
        except Exception as e:
            return
        else:
            self.rawdata = res.json()
            self.data = betking_match_normalizer(jsonpaths.betking_validator(self.rawdata))
            # self.data = jsonpaths.betking_validator(self.rawdata)
            return self.data

    def get_all(self):
        """
        provides odds for all 1x2 and doublechance markets for all implemented leagues

        Returns:
            Sequence[Mapping[str, str]]: A lis
        """
        self.data = []
        for league in Betid:
            self.data += self.get_league(league)
        return self.data
