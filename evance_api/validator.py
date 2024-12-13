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
