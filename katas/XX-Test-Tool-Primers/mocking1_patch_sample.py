# test with: python -m unittest mocking1_patch_sample.py


# ---------------- Productive Code --------------------------
class QueryService:  # EXTERNAL Class, which the client class uses
    def __init__(self):
        self.value = 5

    def fetch_data(self, run):
        from time import sleep
        self.value += 10
        sleep(20)
        print("Snooze ... ")
        return self.value + run


class QueryServiceClient:  # class under Test
    def __init__(self):
        self.query_service = QueryService()

    def aggregate(self, run):
        aggregated = 0
        for i in range(run):
            value = self.query_service.fetch_data(i)
            aggregated += value
        return aggregated


# ------------------- Tests ------------------------------------

# We want to test the QueryServiceClient (not! the QueryService)
#
# without mocking/patching of the external QueryService
# a) can't control the results, returned by `fetch_data(...)`
# b) would have to wait for long
#    ....
# => , let's patch the QueryService

import unittest
from unittest.mock import patch, call


class QueryServiceClientTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_aggregation_with_explicit_patch(self):
        client_under_test = QueryServiceClient()
        with patch.object(QueryService, 'fetch_data', return_value=2) as fetch_data_mock:
            agg_result = client_under_test.aggregate(3)
            self.assertEqual(agg_result, 6)

        fetch_data_mock.assert_has_calls([call(0), call(1), call(2)])

    @patch.object(QueryService, 'fetch_data')
    def test_aggregation_with_decorator_patch(self, fetch_data_mock):
        fetch_data_mock.return_value = 2

        client_under_test = QueryServiceClient()
        agg_result = client_under_test.aggregate(3)
        self.assertEqual(agg_result, 6)

        fetch_data_mock.assert_has_calls([call(0), call(1), call(2)])

# and much more: see https://docs.python.org/3/library/unittest.mock.html#quick-guide


# B u t:
#
# - @patch: requires `str`: referencing 'real' external classes/methods can be nasty, also as the namespace depends
#           on the import statement: E.g.
#           for `from time import sleep` and `import time` the `sleep` method must be handled differently!
#           @patch('<extern_module>.sleep') vs @patch('time.sleep')
# - Using patch is a CODE SMELL
#   because it means that the class under test has been COUPLED to one or more other concrete classes!!!
# - Solution: Dependency Injection => see: mocking2_mock_sample.py
