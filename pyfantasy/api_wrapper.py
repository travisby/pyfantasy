import api


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

    def _make_request(self, endpoint):
        pass
