import os
import africastalking

from dotenv import load_dotenv

load_dotenv()


# Set your app credentials
username = "EMID"   # use 'sandbox' for development in the test environment
api_key = os.getenv("AT_API_KEY")  # your API key

# Initialize the SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS


def send_two_way_sms(message: str, recipient: str):
    options = {
        "to": [recipient],    # Set the numbers you want to send to in international format
        "message": message,
        "from_": 20880      # Shortcode or sender ID
    }

    try:
        print("Sending SMS with options:", options)
        response = sms.send(message, [recipient], 20880)
        print("Response:", response)
        return response
    except Exception as e:
        print("Error:", str(e))
        return None


# Example usage
if __name__ == "__main__":
    send_two_way_sms("Hello, this is a test message!", "+254743158232")
