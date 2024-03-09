# Bitcoin Price Alert

The Bitcoin Price Alert project is a Python program designed to monitor the real-time price of Bitcoin and provide alerts when the price exceeds a predefined threshold. This project integrates with the Binance Single Symbol Price API to fetch the latest Bitcoin price in USD. Additionally, it utilizes the Bolt IoT platform to control a connected buzzer and Twilio for sending SMS alerts.

## Features

1. **Real-time Bitcoin Price Monitoring:**
   - The program regularly queries the Binance API to fetch the current price of Bitcoin.

2. **Buzzer Notification:**
   - When the current Bitcoin price exceeds a user-defined selling price, the program triggers a connected buzzer using the Bolt IoT platform. The buzzer remains active for 10 seconds, providing a noticeable alert.

3. **Twilio SMS Alerts:**
   - In addition to the audible alert, the program uses Twilio to send an SMS alert when the selling price is exceeded. Users can receive instant notifications on their mobile devices.

## Setup Instructions

1. **Clone the Repository:**
   - Clone this repository to your local machine using the provided URL.

2. **Install Dependencies:**
   - Use pip to install the required libraries: `requests`, `boltiot`, and `twilio`.

3. **Configure Credentials:**
   - Open the Python program (`bitcoin_price_alert.py`) and replace placeholder values with your actual credentials.
     - Bolt Cloud API key and device ID.
     - Selling price threshold.
     - Twilio account SID, authentication token, and phone numbers.

4. **Run the Program:**
   - Execute the program using the command: `python bitcoin_price_alert.py`.
   - Monitor the console for real-time Bitcoin price updates and alerts.

## Dependencies

- [Bolt IoT Python Library](https://github.com/Inventrom/bolt-api-python)
- [Twilio Python Library](https://github.com/twilio/twilio-python)

## License

This project is open-source and released under the [MIT License](LICENSE). Feel free to modify, distribute, or contribute to the codebase.

## Disclaimer

This project is intended for educational purposes and as a demonstration of integrating IoT devices and APIs. Use it responsibly and be aware of any API usage limits to avoid rate limiting.
