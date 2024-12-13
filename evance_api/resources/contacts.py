from .resources import Resources
from ..validator import JSONValidator


class Contacts(Resources):

    def __init__(self, client):
        """
        Initialize the Contacts module.

        :param client: An instance of the EvanceClient
        """

        # Define request parameters
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

        # Define accepted keys for POST/PUT JSON validation
        mandatory_keys = {
            "email": str,
            "type": str,
            "firstName": str,
            "lastName": str,
        }
        optional_keys = {
            "reference": str,
            "registeredNumber": str,
            "taxNumber": str,
            "username": (str, type(None)),
            "password": str,
            "title": (str, type(None)),
            "company": str,
            "position": (str, type(None)),
            "department": (str, type(None)),
            "division": (str, type(None)),
            "phone": str,
            "mobile": (str, type(None)),
            "website": str,
            "facebook": (str, type(None)),
            "flickr": (str, type(None)),
            "linkedIn": (str, type(None)),
            "pinterest": (str, type(None)),
            "instagram": (str, type(None)),
            "twitter": (str, type(None)),
            "vimeo": (str, type(None)),
            "youTube": (str, type(None)),
            "thumbnail": (str, type(None)),
            "biography": (str, type(None)),
            "startDate": (str, type(None)),
            "leaveDate": (str, type(None)),
            "consentsToEmail": bool,
            "consentsToSms": bool,
            "consentsToPost": bool,
            "consentsToPhone": bool,
        }

        super().__init__(
            client,
            "contacts",
            accepted_params,
            JSONValidator(mandatory_keys, optional_keys)
        )
