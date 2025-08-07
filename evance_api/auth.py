import requests
import json
import warnings
from urllib3.exceptions import InsecureRequestWarning


class EvanceAuth:
    def __init__(self, base_url, account=None, client_id=None, private_key=None, algorithm="HS256", debug_mode=False):
        """
        Initialize the authentication module.

        :param debug_mode: Enable debug mode
        :param account: Account identifier (e.g., "akiba.kai-dev.xyz")
        :param client_id: Client ID provided by Evance
        :param private_key: Private key for signing the JWT
        :param algorithm: Algorithm for signing the JWT (default: HS256)
        :param base_url: Base URL for the API
        """
        self.debug_mode = debug_mode
        self.account = account
        self.client_id = client_id
        self.private_key = private_key
        self.algorithm = algorithm
        self.base_url = base_url
        self.token = None

    def from_json(self, json_file_path):
        """
        Create an EvanceAuth instance from a JSON file.


        :param json_file_path: Path to the JSON file containing authentication details
        :return: An instance of EvanceAuth
        """
        with open(json_file_path, "r") as file:
            credentials = json.load(file)


        self.account=credentials["account"],
        self.client_id=credentials["client_id"],
        self.private_key=credentials["private_key"],
        self.algorithm=credentials.get("algorithm", "HS256")

    def authenticate(self):
        """
        Authenticate with the Evance API and store the token.
        """
        url = f"{self.base_url}/admin/oauth/token"

        data = {
            "client_id": self.client_id,
            "client_secret": self.private_key,
            "grant_type": "client_credentials",
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # Create a Prepared Request to inspect headers
        session = requests.Session()
        req = requests.Request("POST", url, data=data, headers=headers)
        prepared_request = session.prepare_request(req)

        # Suppress InsecureRequestWarning when debug_mode is enabled
        if self.debug_mode:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", InsecureRequestWarning)
                response = session.send(prepared_request, verify=False)
        else:
            response = session.send(prepared_request, verify=True)

        response.raise_for_status()
        self.token = response.json().get("access_token")

    def get_token(self):
        """
        Return the current JWT token. Generate a new one if it's not set.
        """
        if not self.token:
            self.authenticate()
        return self.token
