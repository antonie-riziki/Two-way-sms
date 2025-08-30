from flask import Flask, request
from sms import send_two_way_sms  # import the function we defined earlier

app = Flask(__name__)


@app.route('/twowaycallback', methods=['POST'])
def twoway_callback():
    data = request.form.to_dict()

    link_id = data.get("linkId")
    text = data.get("text")
    to = data.get("to")
    sms_id = data.get("id")
    date = data.get("date")
    sender = data.get("from")

    x = {
        "message": f'This is a response to: "{text}"',
        "recipient": sender
    }

    print("Payload received:", data)
    print("Reply object:", x)

    send_two_way_sms(x["message"], x["recipient"])

    return "GOOD", 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)
