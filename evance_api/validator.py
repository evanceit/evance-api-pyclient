class Validator:
    def __init__(self, accepted_params):
        """
        Initialize the parameter validator with accepted parameters.

        :param accepted_params: A dictionary of accepted parameters and their expected types
        """
        self.accepted_params = accepted_params

    def validate(self, params):
        """
        Validate the given parameters.

        :param params: Dictionary of parameters to validate
        :raises ValueError: If invalid parameters are found
        """
        for key, value in params.items():
            if key not in self.accepted_params:
                raise ValueError(f"Invalid parameter: {key}")
            expected_type = self.accepted_params[key]
            if not isinstance(value, expected_type):
                raise ValueError(f"Parameter '{key}' must be of type {expected_type.__name__}")
        return True

class JSONValidator:
    def __init__(self, mandatory_keys, optional_keys=None):
        """
        Initialize the JSON body validator with mandatory and optional keys.

        :param mandatory_keys: A dictionary of mandatory keys and their expected types (e.g., {"name": str})
        :param optional_keys: A dictionary of optional keys and their expected types (default: None)
        """
        self.mandatory_keys = mandatory_keys
        self.optional_keys = optional_keys or {}

    def validate(self, body):
        """
        Validate the given JSON body.

        :param body: Dictionary representing the JSON body to be validated
        :raises ValueError: If mandatory keys are missing or types mismatch, or if optional keys have invalid types
        """
        if not isinstance(body, dict):
            raise ValueError("The request body must be a dictionary")

        # Validate the presence of the "data" key
        if "data" not in body:
            raise ValueError("Request body must contain a 'data' key")

        data = body["data"]

        if not isinstance(data, dict):
            raise ValueError("'data' must be a dictionary")

        # Validate mandatory keys inside "data"
        for key, expected_type in self.mandatory_keys.items():
            if key not in data:
                raise ValueError(f"Missing mandatory key under 'data': {key}")
            if data[key] is not None and not isinstance(data[key], expected_type):
                raise ValueError(
                    f"Key '{key}' under 'data' must be of type {expected_type.__name__} or None"
                )

        # Validate optional keys inside "data" (if present)
        for key, expected_type in self.optional_keys.items():
            if key in data and data[key] is not None and not isinstance(data[key], expected_type):
                raise ValueError(
                    f"Optional key '{key}' under 'data' must be of type {expected_type.__name__} or None"
                )

        return True