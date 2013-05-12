import unittest
import api_wrapper
import api
import mock
import sample_data.ffnScheduleXML as Schedule_XML

NO_KEY_ERROR_MSG = "<Error>Invalid API Key.</Error>"


class MyUnitTestCase(unittest.TestCase):

    def assertNotRaises(self, code, exc):
        try:
            code()
        except exc:
            self.fail('%s did raise %s' % (code.func_name, exc))


class TestAPIFunctions(MyUnitTestCase):
    """Tests the interface with pyrest"""

    # _KEY must be a number
    _KEY = '9'
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

    @mock.patch.object(api.Api, 'get', return_value=(None, Schedule_XML.XML))
    def test_season_schedule_returns_season_schedule_object(self, mocked):
        response = self.api.get_season_schedule()
        self.assertIsInstance(response, api_wrapper.Season_Schedule)


class Season_Schedule_Tests(MyUnitTestCase):

    def setUp(self):
        self.schedule = api_wrapper.Season_Schedule()
        pass

    def test_schedule_has_season_property(self):
        func = lambda: self.schedule.season
        self.assertNotRaises(func, AttributeError)

    def tearDown(self):
        pass


unittest.main()
