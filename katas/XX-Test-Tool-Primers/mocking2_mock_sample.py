# test with: python -m unittest mocking2_mock_sample.py


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


class QueryServiceClient:  # class under Test, now with DEPENDENCY INJECTION
    def __init__(self, query_service):
        self.query_service = query_service

    def aggregate(self, run):
        try:
            aggregated = 0
            for i in range(run):
                value = self.query_service.fetch_data(i)
                aggregated += value
            return aggregated
        except Exception as detail:
            print('Ouch: {}'.format(detail))
            return -1


# ------------------- Tests ------------------------------------

# We want to test the QueryServiceClient (not! the QueryService)
#
# without mocking/patching of the external QueryService
# a) can't control the results, returned by `fetch_data(...)`
# b) would have to wait for long
#    ....
# => , let's mock the QueryService

import unittest
from unittest.mock import Mock, call


class QueryServiceClientTest(unittest.TestCase):
    def setUp(self):
        self.query_service_mock = Mock()

    def test_aggregation(self):
        # given
        self.query_service_mock.fetch_data.return_value = 2
        client_under_test = QueryServiceClient(self.query_service_mock)

        # when
        agg_result = client_under_test.aggregate(3)

        # then
        self.assertEqual(agg_result, 6)
        self.query_service_mock.fetch_data.assert_has_calls([call(0), call(1), call(2)])

    def test_failing_aggregation(self):
        # given
        self.query_service_mock.fetch_data.side_effect = Exception('Unexpected')
        client_under_test = QueryServiceClient(self.query_service_mock)

        # when
        agg_result = client_under_test.aggregate(3)

        # then
        self.assertEqual(agg_result, -1)
        self.query_service_mock.fetch_data.assert_called_once_with(0)

