import unittest
import api_wrapper
import api
import xml.etree.ElementTree

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

    def test_can_actually_make_request(self):
        # we use season_schedule because it should be the lightest request
        # Because of the way their api works, it will return nothing
        #    if the url+key were malformed.  This tests that :D
        server_response = self.api._make_request('season_schedule')[1]
        self.assertIn(NO_KEY_ERROR_MSG, server_response)

    def test_request_xml_parsed(self):
        response = self.api._handle_request('season_schedule')
        self.assertIsInstance(response, xml.etree.ElementTree.ElementTree)

unittest.main()
