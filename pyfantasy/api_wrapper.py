import api


class Api(object):
    BASE_URL = 'http://api.fantasyfootballnerd.com'

    _api_key = ''
    _api = None

    def __init__(self, api_key):
        self._api = api.Api(self.BASE_URL)

        self._api_key = api_key
