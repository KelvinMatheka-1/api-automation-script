import requests

BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}

def make_request(method, endpoint, json_data=None, token=None):
    HEADERS["Cookie"] = f"token={token}"
    url = f"{BASE_URL}{endpoint}"
    return requests.request(method, url, json=json_data, headers=HEADERS).json()

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

def get_booking(bookingid):
    return make_request("GET", f"/booking/{bookingid}")

def get_token():
    data = {"username": "admin", "password": "password123"}
    return make_request("POST", "/auth", data)['token']

def update_booking(bookingid, token):
    data = {
        "bookingdates": {"checkout": "2024-06-10"},
        "additionalneeds": "Dinner"
    }
    return make_request("PATCH", f"/booking/{bookingid}", data, token)

# invoking the functions
bookingid = create_booking()
print(f"Created booking with ID: {bookingid}")

booking_details = get_booking(bookingid)
print(f"Booking details: {booking_details}")

token = get_token()
print(f"Obtained token: {token}")

updated_booking = update_booking(bookingid, token)
print(f"Updated booking: {updated_booking}")