import pytest
import json
import requests
from api_functions.functions import APIFunctions
from api_functions.mock_data import TestData

# Test class for verifying API functionality using pytest
class TestApiFunctions:

    @pytest.fixture()
    def setup(self):
        """
        Fixture to create an instance of APIFunctions with a base URL.
        This setup is reused across multiple tests.
        """
        url = "https://67f6456b42d6c71cca61454e.mockapi.io/api/v1/restfulapi"
        api_functions = APIFunctions(url)
        return api_functions

    def test_api_status_code(self, setup):
        """
        Test to verify that the API returns HTTP 200 status code.
        """
        assert setup.api_status_code() == 200

    def test_fetch_api_data(self, setup):
        """
        Test to verify that the data fetched from the API matches expected mock data.
        """
        assert setup.fetch_api_data() == TestData.mock_data

    def test_fetch_header(self, setup):
        """
        Test to verify that the 'Report-To' field in the response header contains 'heroku-nel'.
        This ensures the correct response headers are being received.
        """
        headers = setup.fetch_header()
        report_to = headers.get("Report-To", "")
        assert "heroku-nel" in report_to

    def test_fetch_data(self, setup):
        """
        Test to verify data retrieval for a specific ID.
        The returned JSON should match the expected data.
        """
        expected_result = {"id": "51", "name": "Optimus Prime", "avatar": "Autobot"}
        result = json.loads(setup.fetch_data(51))
        assert result == expected_result

    def test_insert_data(self, setup):
        """
        Test to verify that new data can be successfully inserted into the API.
        Assumes the API returns True upon successful insertion.
        """
        new_data = {"name": "Megatron", "avatar": "Decepticon"}
        assert setup.insert_data(new_data) == True

    def test_delete_data(self, setup):
        """
        Test to verify that data with a specific ID can be deleted successfully.
        Assumes the API returns True upon successful deletion.
        """
        assert setup.delete_data(52) == True
