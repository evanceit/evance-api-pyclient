from .resources import Resources

class Contacts(Resources):

    def __init__(self, client):
        """
        Initialize the Contacts module.

        :param client: An instance of the EvanceClient
        """

        accepted_params = {
            "id:in": list,
            "id:min": int,
            "id:max": int,
            "id:before": int,
            "id:after": int,
            "quickfind:in": list,
            "quickfind:min": int,
            "quickfind:max": int,
            "quickfind:before": int,
            "quickfind:after": int,
            "createdOn:min": str,
            "createdOn:max": str,
            "createdOn:before": str,
            "createdOn:after": str,
            "modifiedOn:min": str,
            "modifiedOn:max": str,
            "modifiedOn:before": str,
            "modifiedOn:after": str,
            "reference": str,
            "reference:in": list,
            "email": str
        }

        super().__init__(client, "contacts", accepted_params)
