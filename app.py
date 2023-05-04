from flask import Flask, render_template_string, request
from twilio.twiml.voice_response import VoiceResponse
import os
import requests


app = Flask(__name__)


def read_file(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        content = file.read()
    return content

readme_content = read_file('README.md')

print(readme_content)

@app.route('/handle_call', methods=['POST'])
def handle_call():
    # Get the caller's phone number
    caller_number = request.form.get('From', 'Unknown')
    msg = f'OpenTheDoor received a call from {caller_number}.'

    # Send Discord notification
    # this works locally but doesn't work on Python anywhere
    # doesn't work on render either because it's not async
    url = f'https://api.val.town/eval/@joey.sendDiscordMessage("221095018334824693851","{msg}")'
    requests.get(url)

    # Play a message to the caller
    response = VoiceResponse()
    response.play(digits='9')
    return str(response)


@app.route('/')
def index():
    print(readme_content)
    app_source_code = read_file(__file__)

    template = template = '''
    <!doctype html>
    <html>
    <head>
        <title>Flask App Info</title>
        <style>
            pre {
                background-color: #f0f0f0;
                padding: 1em;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body>
        <h1>README.md</h1>
        <pre>{{ readme_content|replace("<", "&lt;")|replace(">", "&gt;") }}</pre>
        <h1>Flask App Source Code</h1>
        <pre>{{ app_source_code }}</pre>
    </body>
    </html>
    '''

    return render_template_string(template, readme_content=readme_content, app_source_code=app_source_code)

if __name__ == '__main__':
    app.run()
