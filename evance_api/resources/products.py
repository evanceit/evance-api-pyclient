from .resources import Resources

class Products(Resources):

    def __init__(self, client):
        """
        Initialize the Products module.

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
            "sku:in": list,
            "sku:startsWith": str,
            "sku:endsWith": str,
            "sku:contains": str,
            "barcode:in": list,
            "partNumber:in": list,
            "type": str,
            "status": str,
            "bandId": int,
            "bandId:in": list,
            "manufacturerId": int,
            "manufacturerId:in": list
        }

        super().__init__(client, "products", accepted_params)
