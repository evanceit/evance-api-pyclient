import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
from .exceptions import (
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    MethodNotAllowedError,
    ServerError,
    UnexpectedError,
)

class EvanceClient:
    def __init__(self, auth, api_version=""):
        """
        Initialize the API client with authentication.

        :param auth: An instance of the EvanceAuth class
        """
        self.auth = auth
        self.api_version = api_version
        self.base_url = f"{self.auth.base_url}/api/{self.api_version}"

    def request(self, method, endpoint, params=None, data=None):
        """
        Make a request to the API.

        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint (e.g., 'products')
        :param params: Query parameters
        :param data: Request payload
        :return: JSON response from the API
        """
        headers = {"Authorization": f"Bearer {self.auth.token}"}
        url = f"{self.base_url}/{endpoint}"

        try:
            # Suppress InsecureRequestWarning when debug_mode is enabled
            if self.auth.debug_mode:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", InsecureRequestWarning)
                    response = requests.request(
                        method,
                        url,
                        params=params,
                        json=data,
                        headers=headers,
                        verify=False
                    )
            else:
                response = requests.request(
                    method,
                    url,
                    params=params,
                    json=data,
                    headers=headers,
                    verify=True
                )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            status_code = response.status_code
            if status_code == 401:
                raise UnauthorizedError() from http_err
            elif status_code == 403:
                raise ForbiddenError() from http_err
            elif status_code == 404:
                raise NotFoundError() from http_err
            elif status_code == 405:
                raise MethodNotAllowedError() from http_err
            elif 500 <= status_code < 600:
                raise ServerError() from http_err
            else:
                raise UnexpectedError(f"Unexpected HTTP error: {http_err}") from http_err

        except requests.exceptions.ConnectionError as conn_err:
            raise ConnectionError() from conn_err

        except requests.exceptions.Timeout as timeout_err:
            raise TimeoutError() from timeout_err

        except requests.exceptions.RequestException as req_err:
            raise UnexpectedError(f"An unexpected error occurred: {req_err}") from req_err

    def get(self, endpoint, params=None):
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint, data):
        return self.request("POST", endpoint, data=data)

    def put(self, endpoint, data):
        return self.request("PUT", endpoint, data=data)

    def delete(self, endpoint):
        return self.request("DELETE", endpoint)
