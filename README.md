# Twilio Server Project

This project sets up a simple server using Flask to handle incoming messages from Twilio and respond to them using the Twilio API.

## Project Structure

```
twilio-server
├── src
│   ├── server.py       # Sets up Flask server and handles incoming messages
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd twilio-server
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, create a virtual environment and install the required packages:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```
   python src/server.py
   ```

5. **Set up Twilio webhook:**
   - In your Twilio console, set the webhook URL to point to your server's endpoint (e.g., `http://<your-server-url>/incoming`).

## Usage

- Send a WhatsApp message to your Twilio number.
- The server will receive the message and respond with a predefined reply using the functionality from `bot.py`. 

## License

This project is licensed under the MIT License.