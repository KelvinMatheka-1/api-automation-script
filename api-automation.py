import requests
# Base URL for the RESTful Booker API
BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}

#Helper function to handle repetitive HTTP requests.
def make_request(method, endpoint, json_data=None, token=None):
    HEADERS["Cookie"] = f"token={token}"
    url = f"{BASE_URL}{endpoint}"
    return requests.request(method, url, json=json_data, headers=HEADERS).json()
#Creates a new booking. and returns the ID of the booking
def create_booking():
    data = {
        "firstname": "kelvin",
        "lastname": "matheka",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-06-01",
            "checkout": "2024-06-05"
        },
        "additionalneeds": "Breakfast"
    }
    return make_request("POST", "/booking", data)['bookingid']
#Retrieve a booking by ID.
def get_booking(bookingid):
    return make_request("GET", f"/booking/{bookingid}")

#Obtain and return an authentication token.
def get_token():
    data = {"username": "admin", "password": "password123"}
    return make_request("POST", "/auth", data)['token']

#Use patch to partialy update the checkout date and additionalneeds of a booking by ID.
def update_booking(bookingid, token):
    data = {
        "bookingdates": {"checkout": "2024-06-10"},
        "additionalneeds": "Dinner"
    }
    return make_request("PATCH", f"/booking/{bookingid}", data, token)

# invoking the functions
# Create a new booking and print the booking ID
bookingid = create_booking()
print(f"Created booking with ID: {bookingid}")

# Retrieve and print the details of the created booking
booking_details = get_booking(bookingid)
print(f"Booking details: {booking_details}")

# Obtains an authentication token and print it
token = get_token()
print(f"Obtained token: {token}")

# Updating the booking and print the updated details
updated_booking = update_booking(bookingid, token)
print(f"Updated booking: {updated_booking}")