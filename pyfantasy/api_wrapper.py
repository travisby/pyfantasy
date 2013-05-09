class Api(object):
    _api_key = ''
    _api = None

    def __init__(self, api_key):
        self._api = None

        self._api_key = api_key
