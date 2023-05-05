import requests

# Set up the login credentials
payload = {
    'username': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD'
}

# Send the POST request to the login endpoint
response = requests.post('https://auth.roblox.com/v2/login', data=payload)

# Check the response status code to see if the login was successful
if response.status_code == 200:
    # Retrieve the token from the response headers
    token = response.headers['X-CSRF-TOKEN']
    print("Your Roblox token is:", token)
else:
    print("Error: Login failed. Response code:", response.status_code)
