import unittest
import api_wrapper


class MyUnitTestCase(unittest.TestCase):

    def assertNotRaises(self, code, exc):
        try:
            code()
        except exc:
            self.fail('%s did raise %s' % (code.func_name, exc))


class TestAPIFunctions(MyUnitTestCase):
    """Tests the interface with pyrest"""

    _KEY = 'thisismykey'

    def setUp(self):

        self.api = api_wrapper.Api(self._KEY)

        self._endpoint_keys = [
            'season_schedule',
            'week_projections',
            'week_injuries',
            'players',
            'player',
            'player_draft_rankings',
        ]

    def tearDown(self):
        pass

    def test_init_saves_api_key(self):
        self.assertEqual(self.api._api_key, self._KEY)

unittest.main()
