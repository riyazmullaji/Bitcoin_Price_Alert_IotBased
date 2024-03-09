import requests
import time
from boltiot import Bolt
from twilio.rest import Client

# Replace 'YOUR_API_KEY' and 'YOUR_DEVICE_ID' with your Bolt Cloud API key and device ID
api_key = 'YOUR_API_KEY'
device_id = 'YOUR_DEVICE_ID'

# Replace 'SELLING_PRICE' with the price at which you want to trigger the buzzer
selling_price = 50000

# Twilio credentials
twilio_account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
twilio_auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_from_number = 'YOUR_TWILIO_FROM_NUMBER'
twilio_to_number = 'YOUR_TWILIO_TO_NUMBER'

# Function to fetch the current Bitcoin price using Single Symbol Price API
def get_bitcoin_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {'symbol': 'BTCUSDT'}
    response = requests.get(url, params=params)
    data = response.json()
    return float(data['price'])

# Function to control the Bolt module and trigger the buzzer
def control_buzzer(on_duration=10):
    mybolt = Bolt(api_key, device_id)
    mybolt.digitalWrite('0', 'HIGH')  # Switch on the buzzer
    time.sleep(on_duration)  # Wait for on_duration seconds
    mybolt.digitalWrite('0', 'LOW')   # Switch off the buzzer

# Function to send alert message using Twilio
def send_twilio_alert():
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body="Bitcoin price exceeded the selling price!",
        from_=twilio_from_number,
        to=twilio_to_number
    )
    print(f"Twilio Alert Sent: {message.sid}")

# Main program loop
while True:
    try:
        current_price = get_bitcoin_price()
        print(f"Current Bitcoin Price: ${current_price}")

        if current_price > selling_price:
            print("Bitcoin price exceeded the selling price! Triggering the buzzer and sending Twilio alert...")
            control_buzzer()
            send_twilio_alert()

        time.sleep(30)  # Wait for 30 seconds before the next iteration

    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(30)  # Wait for 30 seconds in case of an error
