import json

from evance_api.pagination import Pagination, Links


class APIResponse:
    def __init__(self, data):
        """
        Initialize the APIResponse object.

        :param data: The raw JSON response from the API
        """
        self._success = data.get("success", False)
        self._status = data.get("status", None)
        self._pagination = data.get("pagination", {})
        self._links = data.get("links", {})
        #self.data = [self._parse_item(item) for item in data.get("data", [])]

        raw_data = data.get("data", [])
        if isinstance(raw_data, list):
            self.data = [self._parse_item(item) for item in raw_data]
        elif isinstance(raw_data, dict):  # Handle a single dictionary item
            self.data = self._parse_item(raw_data)
        else:
            self.data = None  # `data` is neither a list nor a dictionary

    def _parse_item(self, item):
        """
        Parse individual data items into custom objects with attribute-style access.

        :param item: A dictionary representing a single item from the "data" array
        :return: An object representation of the item
        """

        # Dynamically create a class with an `__init__` to handle item attributes
        class APIObject:
            def __init__(self, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)

            def to_dict(self):
                """
                Convert the object back to a dictionary.
                """
                return {key: getattr(self, key) for key in self.__dict__}

            def __getattr__(self, name):
                """
                Handle missing attributes gracefully. Return None (or another default) if an attribute is missing.
                """
                return f"Attr[{name}] not available"

            def __repr__(self):
                """
                String representation for debugging.
                """
                return f"APIObject({self.__dict__})"

        return APIObject(**item)

    def to_json(self):
        """
        Convert the response object back to JSON.
        """
        if isinstance(self.data, list):
            # Data is a list of parsed items
            json_data = [item.to_dict() for item in self.data]
        elif self.data is not None:
            # Data is a single parsed item
            json_data = self.data.to_dict()
        else:
            # Data is empty or None
            json_data = None

        return json.dumps(json_data)

    @property
    def success(self):
        """
        Return the 'success' flag from the response.
        """
        return self._success

    @property
    def status(self):
        """
        Return the 'status' field from the response.
        """
        return self._status

    @property
    def pagination(self):
        """
        Returns the pagination information as a `Pagination` object.
        """
        if not hasattr(self, "_pagination_object"):
            # Convert the raw dictionary to a `Pagination` object
            self._pagination_object = Pagination(self._pagination)
        return self._pagination_object

    @property
    def links(self):
        """
        Returns the links as a `Links` object.
        """
        if not hasattr(self, "_links_object"):
            # Convert the raw dictionary to a `Links` object
            self._links_object = Links(self._links)
        return self._links_object

    def __getitem__(self, key):
        """
        Allow dictionary-like access to the underlying data.
        """
        return self.data[key]

    def __iter__(self):
        """
        Allow iteration over the data if it's a list.
        """
        if isinstance(self.data, list):
            return iter(self.data)
        raise TypeError("APIResponse is not iterable")

    def __len__(self):
        """
        Get the number of items in the "data" section.
        """
        return len(self.data)

    def __repr__(self):
        """
        Provide a string representation for debugging.
        """
        return f"APIResponse({self.data})"

class Resources:
    def __init__(
            self,
            client,
            resource_name,
            accepted_params=None,
            body_validator=None
    ):
        """
        Initialize the base Resource class.

        :param client: An instance of the EvanceClient
        :param resource_name: The name of the resource (e.g., "products", "orders")
        """
        default_params = {
            "page": int,
            "limit": int
        }

        self.client = client
        self.resource_name = resource_name
        self.accepted_params = accepted_params or {}
        self.body_validator = body_validator
        self.query_params = {}  # Store query parameters dynamically

        self.accepted_params.update(default_params)

    def set(self, key, value):
        """
        Set a query parameter dynamically after validation.

        :param key: The parameter key (e.g., "id:in")
        :param value: The parameter value (e.g., [1, 2, 3])
        """
        if key not in self.accepted_params:
            raise ValueError(f"Invalid parameter: {key}")
        expected_type = self.accepted_params[key]
        if not isinstance(value, expected_type):
            raise ValueError(f"Parameter '{key}' must be of type {expected_type.__name__}")
        self.query_params[key] = value

    def list(self, params=None) -> APIResponse:
        """
        Retrieve a list of items for this resource.
        """
        if params is None:
            params = {}

        query_params = self.query_params.copy()
        query_params.update(params)

        response = self.client.get(f"{self.resource_name}.json", params=query_params)
        return APIResponse(response)

    def one(self, resource_id) -> APIResponse:
        """
        Retrieve details of a specific item by ID.

        :param resource_id: The ID of the resource
        """
        response = self.client.get(f"{self.resource_name}/{resource_id}.json")
        return APIResponse(response)

    def add(self, body) -> APIResponse:
        """
        Add a new resource (POST).

        :param body: Dictionary representing the JSON body for the POST request
        """
        if self.body_validator:
            self.body_validator.validate(body)  # Validate structure of JSON body

        response = self.client.post(f"{self.resource_name}.json", json=body)

        return APIResponse(response)

    def update(self, resource_id, body) -> APIResponse:
        """
        Update an existing resource (PUT).

        :param resource_id: The ID of the resource to update
        :param body: Dictionary representing the JSON body for the PUT request
        """
        if self.body_validator:
            self.body_validator.validate(body)  # Validate structure of JSON body
        response = self.client.put(f"{self.resource_name}/{resource_id}.json", json=body)
        return APIResponse(response)

    def delete(self, resource_id) -> APIResponse:
        """
        Delete a resource (DELETE).

        :param resource_id: The ID of the resource to delete
        """
        response = self.client.delete(f"{self.resource_name}/{resource_id}.json")
        return APIResponse(response)