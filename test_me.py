from evance_api.auth import EvanceAuth
from evance_api.client import EvanceClient
from evance_api.resources.contacts import Contacts

# Load authentication details from the JSON file
auth = EvanceAuth.from_json("akiba.json", True)

# Authenticate and create the client
auth.authenticate()
client = EvanceClient(auth, "v2")
contact = Contacts(client)

# POST Test: Add a New Contact (Valid Example)
print("---- Testing POST: Adding a new contact (Valid Data) ----")
valid_contact_data = {
    "data": {
        "type": "user",
        "reference": "test-reference-123",
        "password": "SecurePassword123!",
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@example.com",
        "phone": "+1234567890",
        "company": "Evance Inc.",
        "position": "Software Engineer"
    }
}

try:
    post_response = contact.add(valid_contact_data)
    print("POST Response:")
    print(post_response.to_json())  # Output the response as JSON

    # Extract the ID from the POST response
    contact_id = post_response.data.id  # Adjusted to access `id` via "data"
    print(f"New contact ID: {contact_id}")

except Exception as e:
    print(f"POST failed: {e}")
    contact_id = None

if contact_id:
    # PUT Test: Update an Existing Contact (Valid Example)
    print("\n---- Testing PUT: Updating an existing contact (Valid Data) ----")
    valid_update_data = {
        "data": {
            "type": "user",
            "firstName": "John",
            "lastName": "Smith",
            "email": "john.smith@example.com",
            "phone": "+0987654321",
            "company": "Evance Tech",
            "position": "Team Lead"
        }
    }

    try:
        put_response = contact.update(
            resource_id=contact_id,
            body=valid_update_data)  # Replace `6` with an actual contact ID
        print("PUT Response:")
        print(put_response.to_json())  # Output the response as JSON
    except Exception as e:
        print(f"PUT failed: {e}")
else:
    print("\nSkipping PUT test as no valid contact ID was returned from POST.")

# POST Test: Add a New Contact (Invalid Example)
print("\n---- Testing POST: Adding a new contact (Invalid Data) ----")
invalid_contact_data = {
    "data": {
        # Missing mandatory fields like `type`, `firstName`, `lastName`, etc.
        "email": "invalid.user@example.com",
        "phone": "12345"
    }
}

try:
    post_invalid_response = contact.add(invalid_contact_data)
    print("POST Invalid Response:")
    print(post_invalid_response.to_json())
except Exception as e:
    print(f"POST (invalid data) failed: {e}")

# PUT Test: Update an Existing Contact (Invalid Example)
print("\n---- Testing PUT: Updating an existing contact (Invalid Data) ----")
invalid_update_data = {
    "data": {
        "type": "user",
        "firstName": 123,  # Invalid type for firstName (should be str)
        "lastName": None,  # Valid value (nullable)
        "email": "invalid.email@example.com"
    }
}

try:
    put_invalid_response = contact.update(
        resource_id=contact_id,
        body=invalid_update_data)
    print("PUT Invalid Response:")
    print(put_invalid_response.to_json())
except Exception as e:
    print(f"PUT (invalid data) failed: {e}")
