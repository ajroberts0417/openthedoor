# Open The Door!!

https://github.com/ajroberts0417/openthedoor

A simple Flask application that uses the Twilio API to play the DTMF tone for the digit 9 when receiving an incoming call.

We use this to open the door to our building.

Built w/ love by Andrew, inspired by Eric.

## Dependencies

- Python 3
- Flask
- Twilio
- Discord.py
- Gunicorn

## Deployment

For production deploys use:
`gunicorn wsgi:app`



## Installation

1. Install python 3.10.10
```sh
pyenv install 3.10.10
pyenv local 3.10.10
```


2. Install the required packages:

`pipenv install`


# Running the Application in Development
1. Start the Flask application:

`python app.py`

The application will be running on http://127.0.0.1:5000/.

2. Expose your local server using a tool like ngrok:
`ngrok http 5000`

Note the HTTPS URL provided by ngrok (e.g., https://yoursubdomain.ngrok.io).

3. Update your Twilio phone number's webhook:

Log in to your Twilio account, go to the "Phone Numbers" section, and click on your purchased number. In the "Voice & Fax" section, locate the "A Call Comes In" dropdown, select "Webhook," and enter your ngrok URL followed by the /handle_call endpoint (e.g., https://yoursubdomain.ngrok.io/handle_call). Click on the "Save" button at the bottom of the page.


Now, whenever your Twilio phone number receives a call, it will send a webhook to your Flask application, which will respond with the TwiML to play the DTMF tone for the digit 9.