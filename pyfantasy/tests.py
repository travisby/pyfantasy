import unittest
import api_wrapper
import api
import mock
import sample_data.ffnScheduleXML as Schedule_XML
import datetime

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

        mocked.assert_called_with(
            'season_schedule',
            parameters={'apiKey': self._KEY}
        )
        self.assertIsInstance(response, api_wrapper.Season_Schedule)

    @mock.patch.object(api.Api, 'get', return_value=(None, Schedule_XML.XML))
    def test_all_players_returns_list_of_players(self, mocked):
        IS_OF_PLAYER_CLASS = lambda x: isinstance(x, api_wrapper.Player)

        self.assertNotIn(
            False,
            [IS_OF_PLAYER_CLASS(x) for x in self.api.get_all_players()],
        )
        mocked.assert_called_with('all_players')


class Season_Schedule_Tests(MyUnitTestCase):
    SEASON = '2011'
    TIMEZONE = 'Eastern'
    UNKNOWN_TIMEZONE = 'fish'
    # TODO add actual games in here
    GAMES = [None, None]

    def setUp(self):
        self.season_schedule = api_wrapper.Season_Schedule(
            self.SEASON,
            self.TIMEZONE,
            self.GAMES,
        )

    def test_season_is_int(self):
        self.assertIsInstance(self.season_schedule.season, int)

    def test_timezone_of_type_tzinfo(self):
        self.assertIsInstance(self.season_schedule.timezone, datetime.tzinfo)

    def test_games_is_list_of_games(self):
        IS_OF_GAME_CLASS = lambda x: isinstance(x, api_wrapper.Game)

        self.assertNotIn(
            False,
            [IS_OF_GAME_CLASS(x) for x in self.season_schedule.games],
        )

    def test_raise_error_on_unknown_timezone(self):
        constructor = lambda: api_wrapper.Season_Schedule(
            self.SEASON,
            self.UNKNOWN_TIMEZONE,
            self.GAMES,
        )
        self.assertRaises(api_wrapper.Unknown_Timezone, constructor)

    def tearDown(self):
        pass


class GameXML_Tests(MyUnitTestCase):

    game = None

    def setUp(self):
        self.game = api_wrapper.GameXML()

    def test_gameXML_object_is_game_object(self):
        self.assertIsInstance(self.game, api_wrapper.Game)

    def test_game_has_correct_date(self):
        """Here this test ensures correct XML parsing"""

        expected_date = datetime.date(2012, 9, 9)

        self.assertEqual(self.game.date, expected_date)
        pass

    def tearDown(self):
        pass


class Game_Tests(MyUnitTestCase):

    game = None

    def setUp(self):
        self.game = api_wrapper.Game()

    def tearDown(self):
        pass

    def test_game_has_correct_date(self):

        expected_date = datetime.date(2012, 9, 9)

        self.assertEqual(self.game.date, expected_date)

unittest.main()
