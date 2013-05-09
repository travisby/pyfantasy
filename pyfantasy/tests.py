import unittest
import api_wrapper
import api


class MyUnitTestCase(unittest.TestCase):

    def assertNotRaises(self, code, exc):
        try:
            code()
        except exc:
            self.fail('%s did raise %s' % (code.func_name, exc))


class TestAPIFunctions(MyUnitTestCase):
    """Tests the interface with pyrest"""

    _KEY = 'thisismykey'
    _BASE_URL = 'http://api.fantasyfootballnerd.com'

    def setUp(self):

        self.api = api_wrapper.Api(self._KEY)

        self._endpoints = {
            'season_schedule': 'ffnScheduleXML.php',
            'week_projections': 'ffnSitStartXML.php',
            'week_injuries': 'ffnInjuriesXML.php',
            'players': 'ffnPlayersXML.php',
            'player': 'ffnPlayerDetailsXML.php',
            'player_draft_rankings': 'ffnRankingsXML.php',
        }

    def tearDown(self):
        pass

    def test_init_saves_api_key(self):
        self.assertEqual(self.api._api_key, self._KEY)

    def test_api_object_created(self):
        self.assertIsInstance(self.api._api, api.Api)

    def test_api_api_url_is_right(self):
        self.assertEqual(self.api._api.base_url, self._BASE_URL)

    def test_api_api_endpoints_are_right(self):
        self.assertEqual(self.api._api.endpoints, self._endpoints)

unittest.main()
