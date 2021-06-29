### A simple webhook app posting Pipedrive CRM updates to a specific Slack channel


#### App setup
Configure:
1. JSON keys in `Pipedrive JSON` section (defaults: Object + Action + Object Title)
2. Unique Slack Webhook URL (see below)

#### Slack setup
1. Create a new Slack App [here](https://api.slack.com/apps?new_app=1) 
2. Activate [Incoming Webhooks](https://api.slack.com/messaging/webhooks) feature for the app
3. Paste `Webhook URL` into `Webhook URL` section
   
A webhook requires pre-defined JSON (see [API reference](https://api.slack.com/messaging/webhooks) ) and validates JSON structure, so you need to follow Slack data model to read data.   

#### Heroku deployment
1. The app uses [gunicorn](https://gunicorn.org/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
2. Don't override `Procfile` config with a custom $PORT, it may cause Heroku deployment issues 
3. Don't forget to `heroku ps:scale web=1` to a dyno
