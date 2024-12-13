class Pagination:
    """
    Represents the pagination block of the API response.
    Provides attribute access (dot notation) for pagination information.
    """

    def __init__(self, data):
        self.page = data.get("page")
        self.limit = data.get("limit")
        self.total = data.get("total")
        self.pages = data.get("pages")

    def __repr__(self):
        return f"Pagination(page={self.page}, limit={self.limit}, total={self.total}, pages={self.pages})"


class Links:
    """
    Represents the links block of the API response.
    Provides attribute access (dot notation) for links like previous, next, self, etc.
    """

    def __init__(self, data):
        self.previous = data.get("previous")
        self.next = data.get("next")
        self.self = data.get("self")

    def __repr__(self):
        return f"Links(previous={self.previous}, next={self.next}, self={self.self})"
