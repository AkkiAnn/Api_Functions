import requests
import json

class APIFunctions:
    """
    A class to interact with a RESTful API using GET, POST, and DELETE methods.
    """

    def __init__(self, url):
        # Initialize the class with the base URL of the API
        self.url = url

    def api_status_code(self):
        """
        Sends a GET request to the API and returns the HTTP status code.
        """
        request = requests.get(self.url)
        return request.status_code

    def fetch_api_data(self):
        """
        Fetches and returns the data from the API in JSON format if the status code is 200.
        Returns an error message if the API call fails.
        """
        if self.api_status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "Error - 404"

    def fetch_header(self):
        """
        Retrieves and returns the HTTP response headers from the API as a dictionary.
        Returns an empty dictionary if the API call fails.
        """
        if self.api_status_code() == 200:
            data = requests.get(self.url)
            return dict(data.headers)  # Convert headers to a dictionary
        else:
            return {}

    def fetch_data(self, user_id):
        """
        Fetches specific user data if a user_id is provided.
        If no user_id is provided, returns a list of all users with selected fields.
        """
        if self.api_status_code() == 200:
            if user_id:  # If a specific ID is provided
                for d in self.fetch_api_data():
                    if d["id"] == str(user_id):  # Match ID as a string
                        return json.dumps(
                            {"id": d["id"], "name": d["name"], "avatar": d["avatar"]},
                            indent=4
                        )
                return f"No user found with id {user_id}"  # If no match is found
            else:
                # Return all users with selected fields
                data = [
                    {"id": d["id"], "name": d["name"], "avatar": d["avatar"]}
                    for d in self.fetch_api_data()
                ]
                return json.dumps(data, indent=4)
        return "Error fetching data"

    def insert_data(self, data):
        """
        Inserts a new user record into the API using POST method.
        Returns True if data is inserted successfully (HTTP 201), otherwise False.
        """
        if self.api_status_code() == 200:
            response = requests.post(self.url, json=data)
            return response.status_code == 201
        else:
            return "False"

    def delete_data(self, id):
        """
        Deletes a specific user record from the API based on the given ID.
        Returns True if the record is successfully deleted (HTTP 200), otherwise False.
        """
        if self.api_status_code() == 200:
            delete_url = f"{self.url}/{id}"
            response = requests.delete(delete_url)
            return response.status_code == 200
        return "False"


# Example usage (commented out for testing purposes):
# data = {"name" : "Optimus Prime", "avatar" : "Autobot"}
# link = "https://67f6456b42d6c71cca61454e.mockapi.io/api/v1/restfulapi"
# myapi = APIFunctions(link)
# print(myapi.api_status_code())
# print(myapi.fetch_api_data())
# print(myapi.fetch_header())
# print(myapi.insert_data(data))
# print(myapi.delete_data(53))
