from flask import Flask, request, Response
import requests
import json
from jsondiff import diff


app = Flask(__name__)

# handling a /webhook route for POST


@app.route('/webhook', methods=['POST'])
def respond():

    print(request.headers)
    print(request.json)

    data = request.json

    updatesString = prepareUpdates(data)
    print(updatesString)

    if(updatesString != ''):
        # keys for parsing Pipedrive JSON
        slack_data = '{"text":"' + \
            data['meta']['object'] + ' ' + data['meta']['action'] + ': ' + data['current']['title'] + '\\n' + \
            data['meta']['host'] + '/deal/' + str(data['meta']['id']) + '\\n' + \
            updatesString.strip('{}') + '"}'

        # slack webhook URL
        # url = ''
        response = requests.post(url, slack_data)

    return Response(status=200)


def prepareUpdates(updates):

    prettify = ['"', '{', '}']

    if updates['meta']['action'] == 'updated':
        previousState = {'New Stage': decodeStageID(updates['previous']['stage_id']),
                         'New Value': updates['previous']['formatted_value'],
                         'New Status': updates['previous']['status']}
    else:
        previousState = {'New Stage': '', 'New Value': '', 'New Status': ''}

    currentState = {'New Stage': decodeStageID(updates['current']['stage_id']),
                    'New Value': updates['current']['formatted_value'],
                    'New Status': updates['current']['status']}

    diffArray = json.dumps(diff(previousState, currentState))

    for char in prettify:
        diffArray = diffArray.replace(char, '')

    return diffArray


def decodeStageID(stage):
    return {
        1:  'Intro',
        2:  'Exploration',
        3:  'Proposal',
        4:  'Negotiations',
        5:  'Won',
    }.get(stage, 'Unknown')


# handling a default route for a health check


@app.route('/')
def index():
    return "<h1>slack notifications</h1>"


if __name__ == '__main__':
    app.run(debug=False)
