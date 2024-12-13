# Evance API Python Client

## Description
The **Evance API Python Client** is a library designed to interact with the Evance API. It simplifies authentication, resource management, and communication with the Evance platform. Perfect for developers looking to integrate their applications with Evance.

## Features
- Authentication with Evance API using client credentials flow
- Supports resource management, including products and contacts
- Error handling for common HTTP issues (e.g., 401, 403, 404)
- Pagination and querying for resources
- Extensible design for additional resources

## Installation
To install the dependencies needed for this project, run:

```bash
pip install -r requirements.txt
```

## Usage
### Authentication
Authenticate with the API using a JSON credentials file.

```python
from evance_api.auth import EvanceAuth

auth = EvanceAuth.from_json("credentials.json")
auth.authenticate()
```

### Creating the Client
Set up the Evance Client to make API requests:

```python
from evance_api.client import EvanceClient

client = EvanceClient(auth, api_version="v2")
```

### Working with Resources
#### Products
Fetch and iterate through the list of products:
```python
from evance_api.resources.products import Products

product = Products(client)
product.set("limit", 10)
product.set("page", 1)

response = product.list()

for item in response:
    print(item.title)  # Access product attributes
```

#### Contacts
Fetch and iterate through the list of contacts:
```python
from evance_api.resources.contacts import Contacts

contact = Contacts(client)
response = contact.list()

for item in response:
    print(item.email)  # Access contact attributes
```

### Error Handling
Catch specific exceptions with the built-in error classes:
```python
from evance_api.exceptions import UnauthorizedError, NotFoundError

try:
    response = client.get("nonexistent_endpoint")
except UnauthorizedError:
    print("Invalid credentials.")
except NotFoundError:
    print("Endpoint not found.")
```

## Project Structure
```
evance_api/ 
 ├── __init__.py
 ├── auth.py # Handles API authentication 
 ├── client.py # Client for making API requests 
 ├── exceptions.py # Custom exceptions for API errors 
 ├── resources/ 
 │ ├── __init__.py 
 │ ├── products.py # Products resource 
 │ └── contacts.py # Contacts resource 
 ├── response.py # Handles API response parsing and pagination 
 ├──tests/ 
 │ ├── test_auth.py # Unit tests for the authentication module 
 │ └── test_client.py # Unit tests for the client module 
 ├── requirements.txt # Project dependencies 
 └── setup.py # Project setup configuration
```

## Testing
Run unit tests with:

```bash
python -m unittest discover tests
```

## License
This project is licensed under the **MIT License**.