from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

account_sid = 'ACb4d0869c9dc485199faf9731faf6588d'
auth_token = 'f350f80f78f42fa2964b559c2f1d96e8'
client = Client(account_sid, auth_token)

def generate_reply(incoming_msg):
    reply = 'You said: ' + incoming_msg + '. You will get an LLM response soon.'
    return reply

@app.route('/incoming', methods=['POST'])
def incoming_message():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()
    
    # Simple reply logic
    reply = generate_reply(incoming_msg)
    response.message(reply)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)