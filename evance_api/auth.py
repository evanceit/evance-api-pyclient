import requests
import json
import warnings
from urllib3.exceptions import InsecureRequestWarning


class EvanceAuth:
    def __init__(self, account=None, client_id=None, private_key=None, algorithm="HS256", base_url="https://api.evance.com", debug_mode=False):
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

    @classmethod
    def from_json(cls, json_file_path, debug_mode=False):
        """
        Create an EvanceAuth instance from a JSON file.

        :param json_file_path: Path to the JSON file containing authentication details
        :return: An instance of EvanceAuth
        """
        with open(json_file_path, "r") as file:
            credentials = json.load(file)

        return cls(
            account=credentials["account"],
            client_id=credentials["client_id"],
            private_key=credentials["private_key"],
            algorithm=credentials.get("algorithm", "HS256"),
            base_url="https://"+credentials.get("account", "https://api.evance.com"),
            debug_mode=debug_mode,
        )

    def authenticate(self):
        """
        Authenticate with the Evance API and store the token.
        """

        url=f"{self.base_url}/oauth/token"

        data={
            "client_id": self.client_id,
            "client_secret": self.private_key,
            "grant_type": "client_credentials",
        }


        # Suppress InsecureRequestWarning when debug_mode is enabled
        if self.debug_mode:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", InsecureRequestWarning)
                response = requests.post(
                    url=url,
                    data=data,
                    verify=False
                )
        else:
            response = requests.post(
                url=url,
                data=data,
                verify=True
            )

        response.raise_for_status()
        self.token = response.json().get("access_token")

    def get_token(self):
        """
        Return the current JWT token. Generate a new one if it's not set.
        """
        if not self.token:
            self.authenticate()
        return self.token
