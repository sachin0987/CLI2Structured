import requests
import json

# Define your Crosswork API endpoint and credentials
crosswork_api = "https://your-crosswork-api-endpoint"
username = "your_username"
password = "your_password"

# Function to authenticate and get the authentication token
def get_auth_token():
    auth_url = f"{crosswork_api}/v1/auth/token"
    auth_data = {
        "username": username,
        "password": password
    }
    response = requests.post(auth_url, json=auth_data)
    if response.status_code == 200:
        return response.json().get('token')
    else:
        print("Authentication failed.")
        return None

# Function to register a device
def register_device(device_info, token):
    register_url = f"{crosswork_api}/v1/devices"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(register_url, headers=headers, json=device_info)
    if response.status_code == 200:
        print("Device registered successfully.")
    else:
        print("Device registration failed.")

# Device information (example, modify as per your device details)
device_info = {
    "name": "Device_Name",
    "type": "Device_Type",
    "ipAddress": "Device_IP",
    # Add more device information as required
}

# Main execution
if __name__ == "__main__":
    token = get_auth_token()
    if token:
        register_device(device_info, token)
