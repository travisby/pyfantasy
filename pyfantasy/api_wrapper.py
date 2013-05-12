import api
import xml.etree.ElementTree
import pytz


class Unknown_Timezone(Exception):
    pass


class Api(object):
    BASE_URL = 'http://api.fantasyfootballnerd.com'
    ENDPOINTS = {
        'season_schedule': 'ffnScheduleXML.php',
        'week_projections': 'ffnSitStartXML.php',
        'week_injuries': 'ffnInjuriesXML.php',
        'players': 'ffnPlayersXML.php',
        'player': 'ffnPlayerDetailsXML.php',
        'player_draft_rankings': 'ffnRankingsXML.php',
    }

    _api_key = ''
    _api = None

    def __init__(self, api_key):
        self._api = api.Api(self.BASE_URL)
        self._api.update_endpoints(self.ENDPOINTS)

        self._api_key = api_key

    def get_season_schedule(self):
        result = self._handle_request('season_schedule')
        schedule = result.iterfind('Schedule').next()
        season = schedule.get('Season')
        timezone = schedule.get('Timezone')
        return Season_Schedule(season, timezone, schedule.getchildren())

    def _handle_request(self, endpoint, data=None):
        if not data:
            data = {}
        data['apiKey'] = self._api_key

        response = self._api.get(endpoint, parameters=data)[1]
        return xml.etree.ElementTree.fromstring(response)


class Season_Schedule(object):
    _season = 0
    _timezone = None
    _games = []

    def __init__(self, season, timezone, games):
        self._season = int(season)
        self._set_timezone(timezone)
        self._games = games

    @property
    def season(self):
        return self._season

    @property
    def timezone(self):
        return self._timezone

    @property
    def games(self):
        return self._games

    def _set_timezone(self, timezone_str):
        if timezone_str == 'Eastern':
            self._timezone = pytz.timezone('US/Eastern')
        else:
            raise Unknown_Timezone(timezone_str)


class Game(object):
    pass
