import requests
from requests import Response


class APIClient:

    def __init__(self, base_url = "https://jsonplaceholder.typicode.com/"):
        self.base_url = base_url


    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", verify=False)


    def post(self, endpoint, data):
        return requests.post(f"{self.base_url}{endpoint}", json=data, verify=False)


    def put(self, endpoint, data):
        return requests.put(f"{self.base_url}{endpoint}", json=data, verify=False)


    def patch(self, endpoint, data):
        return requests.patch(f"{self.base_url}{endpoint}", json=data, verify=False)


    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", verify=False)


    def status_code(self, response: Response, expected_status_code):
        return response.status_code == expected_status_code