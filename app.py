import os
from slack_bolt import App
import logging
from slack_bolt.async_app import AsyncApp
from datetime import datetime

# Increase debug level, and set up global app variables
logging.basicConfig(level=logging.DEBUG)
now = datetime.now()
dtString = now.strftime("%d/%m/%Y %H:%M:%S")

# Initializes app with bot_token and signing_secret
app = App(
    token = os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
)

# app_mention, subscribe to the message events that mention the bot
@app.event("app_mention")
def handle_mention(body, say, logger):
    user = body["event"]["user"]
    # logger.debug(body)
    # say() sends a message to the channel where @botName is mentioned
    say(
        text = f"date and time =  {dtString}; userId = {user}, mentioned the bot."
    )

# specify and create the slash command 'userid'
@app.command("/userid")
def userid(ack, say, command, user_id):
    user = user_id
    ack()
    say( f"userId = {user}, mentioned the bot.")

# handlng message event that contains 'hello' keyword, 
# in responding the event, a greeting message and a clickable
# button are displayed
@app.message("hello")
def message_hello(message, say):
    # say(f"Hey there <@{message['user']}>!")
    say (
        blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text = f"Hey there <@{message['user']}>!"
    )

# As user clicking on the button, a message showing user id is displayed
@app.action("button_click")
def action_button_click(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> clicked the button")


# Start the app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))