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
contact.body.set("type", "user")
contact.body.set("reference", "test-reference-123")
contact.body.set("password", "SecurePassword123!")
contact.body.set("firstName", "Jane")
contact.body.set("lastName", "Doe")
contact.body.set("email", "jane.doe@example.com")
contact.body.set("phone", "+1234567890")
# Also Supports chaining
contact.body.set("company", "Evance Inc.").set("position", "Software Engineer")

try:
    ## Can also supply a valid dict to add(), it will merge with any previously set attributes
    post_response = contact.add()
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
    # This will override previously set data
    contact.body.set("company", "Evance Tech").set("position", "Team Lead")

    try:
        put_response = contact.update(contact_id)
        print("PUT Response:")
        print(put_response.to_json())  # Output the response as JSON
    except Exception as e:
        print(f"PUT failed: {e}")
else:
    print("\nSkipping PUT test as no valid contact ID was returned from POST.")

# POST Test: Add a New Contact (Invalid Example)
print("\n---- Testing POST: Adding a new contact (Invalid Data) ----")
invalid_contact = Contacts(client)
invalid_contact.body.set("email", "invalid.user@example.com").set("phone", "12345")

try:
    post_invalid_response = invalid_contact.add()
    print("POST Invalid Response:")
    print(post_invalid_response.to_json())
except Exception as e:
    print(f"POST (invalid data) failed: {e}")

# PUT Test: Update an Existing Contact (Invalid Example)
print("\n---- Testing PUT: Updating an existing contact (Invalid Data) ----")
invalid_contact.body.set("type", "user")
invalid_contact.body.set("firstName", 123)  # Invalid type for firstName (should be str)
invalid_contact.body.set("lastName", None)  # Valid value (nullable)
invalid_contact.body.set("email", "invalid.email@example.com")

try:
    put_invalid_response = invalid_contact.update(resource_id=contact_id)
    print("PUT Invalid Response:")
    print(put_invalid_response.to_json())
except Exception as e:
    print(f"PUT (invalid data) failed: {e}")

# PUT Test: Update an Existing Contact (Invalid Example)
print("\n---- Testing DELETE: Deleting an existing contact ----")
try:
    delete = contact.delete(resource_id=contact_id)
    print("DELETE Response:")
except Exception as e:
    print(f"DELETE (invalid data) failed: {e}")
