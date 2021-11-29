from flask import Flask, request, Response
import requests

app = Flask(__name__)

# handling a /webhook route for POST command
@app.route('/webhook', methods=['POST'])

def respond():
    
    print(request.json)
    print(request.headers)
    k = request.json

    # put up-to-date keys for parsing from Pipedrive JSON
    slack_data = '{"text":"' + k['meta']['object'] + ' ' + k['meta']['action'] + ': ' + k['current']['title'] + '"}'
    
    # put up-to-date slack webhook URL
    url = #slack_webhook_URL
    response = requests.post(url, slack_data)
    
    return Response(status=200)

# handling default route for a health check
@app.route('/')
def index():
    return "<h1>slack notifications here</h1>"

if __name__ == '__main__':
    app.run(debug=False)
