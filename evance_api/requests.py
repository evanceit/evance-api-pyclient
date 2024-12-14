class QueryParams:
    def __init__(self):
        self.params = {}

    def set(self, key, value):
        """Set a new query parameter."""
        self.params[key] = value
        return self  # Allow method chaining

    def remove(self, key):
        """Remove an existing query parameter."""
        if key in self.params:
            del self.params[key]
        return self

    def to_dict(self):
        """Convert to a dictionary usable by requests."""
        return self.params


class RequestBody:
    def __init__(self):
        self.body = {"data": {}}

    def set(self, key, value):
        """Set a JSON body field."""
        self.body["data"][key] = value
        return self  # Allow method chaining

    def remove(self, key):
        """Remove an existing body field."""
        if key in self.body["data"]:
            del self.body["data"][key]
        return self

    def to_dict(self):
        """Convert to a dictionary usable by requests."""
        return self.body
