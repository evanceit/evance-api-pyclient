import json

class APIResponse:
    def __init__(self, data):
        """
        Initialize the APIResponse object.

        :param data: The raw JSON response from the API
        """
        self.success = data.get("success", False)
        self.status = data.get("status", None)
        self.pagination = data.get("pagination", {})
        self.links = data.get("links", {})
        self.data = [self._parse_item(item) for item in data.get("data", [])]

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
        return json.dumps({
            "success": self.success,
            "status": self.status,
            "data": [item.to_dict() for item in self.data],
            "pagination": self.pagination,
            "links": self.links
        })

    def get_pagination(self):
        """
        Retrieve pagination details.
        """
        return self.pagination

    def get_links(self):
        """
        Retrieve navigation links.
        """
        return self.links

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
    def __init__(self, client, resource_name, accepted_params=None):
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

    def list(self) -> APIResponse:
        """
        Retrieve a list of items for this resource.
        """
        response = self.client.get(f"{self.resource_name}.json", params=self.query_params)
        return APIResponse(response)

    def one(self, resource_id) -> APIResponse:
        """
        Retrieve details of a specific item by ID.

        :param resource_id: The ID of the resource
        """
        response = self.client.get(f"{self.resource_name}/{resource_id}.json")
        return APIResponse(response)
