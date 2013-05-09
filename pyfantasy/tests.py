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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_takes_api_key(self):
        my_function = lambda: api_wrapper.Api('3')
        self.assertNotRaises(my_function, Exception)

unittest.main()
