from flask import Flask, request
from sms import send_two_way_sms  
from gemini_response import autogenerate_climate_response

app = Flask(__name__)

prompt="what is the current AQI value in Mombasa"
# print(autogenerate_climate_response(prompt))



@app.route('/twowaycallback', methods=['POST'])
def twoway_callback():
    data = request.form.to_dict()

    link_id = data.get("linkId")
    text = data.get("text")
    to = data.get("to")
    sms_id = data.get("id")
    date = data.get("date")
    sender = data.get("from")

    ai_response = autogenerate_climate_response(prompt)
    x = {
        "message": ai_response,
        "recipient": sender
    }

    print("Payload received:", data)
    print("Reply object:", x)

    send_two_way_sms(x["message"], x["recipient"])

    return "GOOD", 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)
