
## Booking API Automation Script
This Python script automates interactions with the RESTful Booker API. It demonstrates creating a booking, retrieving the created booking, obtaining an authentication token, and updating the booking. The script uses the requests library to make HTTP requests to the API.

## Prerequisites
Python 3.x
requests library
You can install the requests library using pip:

pip install requests

## Script Overview
The script is organized into several functions, each responsible for a specific API interaction:

make_request: A helper function to make HTTP requests.
create_booking: Creates a new booking.
get_booking: Retrieves the details of a booking by ID.
get_token: Obtains an authentication token.
update_booking: Updates the checkout date and additional needs of a booking by ID.

## Detailed Function Descriptions
make_request:

A generic helper function to make HTTP requests.
Takes method (HTTP method), endpoint (API endpoint), json_data (data to be sent in the request body), and token (authentication token) as parameters.
Returns the JSON response from the API.
create_booking:

Sends a POST request to create a new booking.
Returns the bookingid of the created booking.
get_booking:

Sends a GET request to retrieve the details of a booking by ID.
Returns the booking details.
get_token:

Sends a POST request to obtain an authentication token.
Returns the token.
update_booking:

Sends a PATCH request to update the checkout date and additional needs of a booking by ID.
Requires the booking ID and authentication token.
Returns the updated booking details.

## usage

Ensure you have Python and the requests library installed.
Save the script to a file .py file
Run the script using Python3 <filename>.py