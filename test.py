from evance_api.auth import EvanceAuth
from evance_api.client import EvanceClient
from evance_api.resources.products import Products
from evance_api.resources.contacts import Contacts

# Load authentication details from the JSON file
auth = EvanceAuth.from_json("akiba.json", True)

# Authenticate and create the client
auth.authenticate()
client = EvanceClient(auth, "v2")
product = Products(client)
contact = Contacts(client)

# Example: Fetch a list of products
product.set("limit",5)
product.set("page", 2)

response = product.list()

# Access metadata
print(response.success)  # True
print(response.status)   # 200
print(response.pagination)  # {'page': 1, 'limit': 100, 'total': 77, 'totalPages': 1}

# Iterate over the data items
for data in response:
    print(data.title)  # Access via dot notation


# Convert the response back to JSON
response_json = response.to_json()
print(response_json)

# Work with pagination
next_link = response.get_links().get("previous")
if next_link:
    print(f"Next page link: {next_link}")

## Contacts
response = contact.list()

# Access metadata
print(response.success)  # True
print(response.status)   # 200
print(response.pagination)  # {'page': 1, 'limit': 100, 'total': 77, 'totalPages': 1}

# Iterate over the data items
for data in response:
    print(data.email)  # Access via dot notation


# Convert the response back to JSON
response_json = response.to_json()
#print(response_json)

# Work with pagination
next_link = response.get_links().get("previous")
if next_link:
    print(f"Next page link: {next_link}")