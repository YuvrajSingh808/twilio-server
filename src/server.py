import json
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

account_sid = 'ACb4d0869c9dc485199faf9731faf6588d'
auth_token = 'f350f80f78f42fa2964b559c2f1d96e8'
client = Client(account_sid, auth_token)

# state 1 is for classifying the disease
# state 2 is for fetching recommendations
# state 3 is for booking an appointment
users_state = {
}

def fetch_recommendations():
    pass

def book_appointment():
    pass

def generate_reply(incoming_msg, phone_number):
    # Here you would implement the logic to generate a reply based on the incoming message
    # load the user data from the file
    with open(f'users/{phone_number}.json', 'r') as f:
        user_data = json.load(f)
    
    messages = user_data['messages']

    user_state = users_state[phone_number]
    if user_state == 1:
        # Here you would implement the logic to classify the disease
        # run classifying prompt
        pass
    elif user_state == 2:
        # Here you would implement the logic to fetch recommendations
        list_of_docs = fetch_recommendations()
        # run recommendation prompt
        # and send the list of documents to the user
        pass
    elif user_state == 3:
        # Here you would implement the logic to book an appointment
        book_appointment()
        # run booking prompt
        pass

    # Here you would implement the logic to generate a reply based on the incoming message	
    reply = 'You said: ' + incoming_msg + '. You will gmesset an LLM response soon.'
    return reply

@app.route('/incoming', methods=['POST'])
def incoming_message():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()
    # open users/<phone_number>.json and get the user data
    phone_number = request.form.get('From')

    if users_state.get(phone_number) is None:
        users_state[phone_number] = 1
    else:
        users_state[phone_number] += 1
    # check if file exists, if not create it

    if users_state[phone_number] == 1:
        try:
            with open(f'users/{phone_number}.json', 'r') as f:
                user_data = json.load(f)
            
        except FileNotFoundError:
            user_data = {'phone_number': phone_number, 'messages': []}
            with open(f'users/{phone_number}.json', 'w') as f:
                json.dump(user_data, f)

        # add the incoming message to the user data
        user_data['messages'].append({
                'timestamp': request.form.get('Timestamp'),
                'message': incoming_msg
            })
        with open(f'users/{phone_number}.json', 'w') as f:
            json.dump(user_data, f)

    elif users_state[phone_number] == 2:
        fetch_recommendations()
    
    elif users_state[phone_number] == 3:
        book_appointment()


    reply = generate_reply(incoming_msg, phone_number)


    response.message(reply)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)