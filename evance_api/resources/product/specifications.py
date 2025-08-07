from ..resources import Resources

class Specifications(Resources):

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
            "valueId:in": list,
            "specId:in": list
        }

        super().__init__(client, f"products/{product_id}/specifications", accepted_params)
