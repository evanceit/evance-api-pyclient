from ..resources import Resources
from enum import Enum

class Visibility(Enum):
    CONTACT = "contact"
    PUBLIC = "public"
    PURCHASE = "purchase"

class Downloads(Resources):

    def __init__(self, client, product_id: int):
        """
        Initialize the Product Specifications module.

        :param client: An instance of the EvanceClient
        """

        accepted_params = {
            "id:in": list,
            "id:min": int,
            "id:max": int,
            "id:before": int,
            "id:after": int,
            "file": str,
            "visibility": Visibility,
        }

        super().__init__(client, f"products/{product_id}/downloads", accepted_params)
