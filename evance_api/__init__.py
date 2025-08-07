# Core components
from .auth import EvanceAuth
from .client import EvanceClient

# Resources
from .resources import Resources, Products, Contacts
from .resources.product import Downloads, Specifications

# Expose version
__version__ = '1.0.0'  # Update with your actual version