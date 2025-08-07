# Evance API Python Client

## Description
The **Evance API Python Client** is a library designed to interact with the Evance API. It simplifies authentication, resource management, and communication with the Evance platform. Perfect for developers looking to integrate their applications with Evance.

## Features
- Authentication with Evance API using client credentials flow
- Supports resource management, including products and contacts
- Error handling for common HTTP issues (e.g., 401, 403, 404)
- Pagination and querying for resources
- Validation for dynamic query parameters
- Extensible design for additional resources
- Response parsing with support for JSON handling and dot notation access

## Setup
### Installation
You can install this library either locally, from a GitHub repository, or from PyPI (if published). Use one of the following methods to set it up:

#### 1. **Install Locally from Source**
   Clone the repository or download the source code, then run:
   ```bash
   pip install .
   ```

#### 2. **Install from GitHub**
   Install directly from the GitHub repository (if public):
   ```bash
   pip install git+https://github.com/evanceit/evance-api-pyclient.git
   ```

#### 3. **Install from PyPI**
   If the package is published on PyPI, use:
   ```bash
   pip install evance_api_pyclient
   ```

### Dependencies
This project uses the following dependencies as listed in `requirements.txt`. To install them manually, use:
```bash
pip install -r requirements.txt
```

### Verifying Installation
After installation, verify the package with the following command:
```bash
python -c "import evance_api_pyclient; print('Package installed successfully')"
```

## Usage
### Authentication
Authenticate with the API using a JSON credentials file. Use debug mode to disable SSL verification.

```python
from evance_api.auth import EvanceAuth

# Load credentials from a JSON file
auth = EvanceAuth.from_json("credentials.json", debug_mode=True)
auth.authenticate()
```

### Creating the Client
The API defaults to version 1 at the moment, however it is likely that v1 will not be supported going forward.
Set up the Evance Client to make API requests:

```python
from evance_api.client import EvanceClient

client = EvanceClient(auth, api_version="v2")
```

### Working with Resources
#### Products
Fetch and iterate through the list of products:

```python
from evance_api.resources.product import Products

product = Products(client)
product.set("limit", 5)
product.set("page", 1)

response = product.list()

for item in response:
    print(item.title)  # Access product attributes via dot notation
```

#### Contacts
Fetch and iterate through the list of contacts:
```python
from evance_api.resources.contacts import Contacts

contact = Contacts(client)
contact.set("email", "test@example.com")  # Query based on email address
```
It is also possible to pass parameters directly to the `list()` method. Any parameters `set()` will be merged with parameters passed in `list()`
```
response = contact.list()

# Access metadata and data
print(response.success)        # True
print(response.pagination)     # Pagination information
for contact in response:
    print(contact.email)  # Access attributes via dot notation
```

### Error Handling
Specific exceptions have been implemented to handle common HTTP errors:
```python
from evance_api.exceptions import UnauthorizedError, ForbiddenError

try:
    client.get("nonexistent_endpoint")
except UnauthorizedError:
    print("Invalid credentials. Please re-authenticate.")
except ForbiddenError:
    print("Resource access is forbidden.")
```

### API Responses
Responses are encapsulated in an `APIResponse` class for easy access:

```python
response = product.list()

# Convert response to JSON
response_json = response.to_json()

# Access pagination details
pagination = response.get_pagination()
print(pagination["totalPages"])

# Iterate through response items
for item in response:
    print(item.title)
```

## Project Structure
```aiignore
evance_api/ 
├── __init__.py 
├── auth.py # Handles API authentication 
├── client.py # Client for making API requests 
├── exceptions.py # Custom exceptions for API errors 
├── response.py # Parses API responses 
├── resources/ 
│ ├── __init__.py 
│ ├── products.py # Products resource 
│ └── contacts.py # Contacts resource 
├── tests/ 
│ ├── test_auth.py # Unit tests for authentication module 
│ └── test_client.py # Unit tests for client module 
├── setup.py # Project setup configuration 
├── requirements.txt # Project dependencies 
├── readme.md # Project documentation
└── LICENSE # Project license details
```


## Validator Utility
The library includes a `Validator` class that enforces dynamic parameter validation for API queries. Example:

```python
from evance_api.resources.product import Products

product = Products(client)

# Dynamically set and validate query parameters
product.set("sku:contains", "1234")
response = product.list()
```

## Testing
Run unit tests with `unittest`:

```bash
python -m unittest discover tests
```

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Acknowledgments
- [Requests Library](https://docs.python-requests.org) for handling HTTP requests.
- [PyJWT](https://pyjwt.readthedocs.io) for handling authentication tokens.