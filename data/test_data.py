# Test data for login tests
TEST_USERS = [
    {"username": "abc.com", "password": "abcd*88"},
    {"username": "thapasandhya1301@gmail.com", "password": "Sandhya@123"}
]

# Invalid user credentials for testing failed login
INVALID_USERS = [

    {"username": "invalid.com", "password": ""},  # Empty password
    {"username": "", "password": ""},  # Both empty
    {"username": "nonexistent@example.com", "password": "wrongpassword"}  # Invalid credentials
]

# Test data for search functionality
SEARCH_PRODUCTS = [
    {"product_name": "Cycle"},
    {"product_name": "Headphone"},
    {"product_name": "laptop"},
    {"product_name": "Hanger"}
]