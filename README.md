Overview:
The Slack application program app.py under firstBoltApp directory
contains the solutions for a, b part of the assignment, and a function
that listening and responding to a message event that contains 'hello' keyword.
A greeting message and a clickable button are displayed on Slack.  In responding to 
a click, a message is returned.  The message event function was from the 
Bolt tutorial.

Create and setup a Slack app
1. create a Slack account
2. create a workspace
3. create an app and install it to the workspace
4. from Basic Information copy SIGNING_SECRET
5. from OAuth&Permissions copy Bot User OAuth Token
6. from ngrok utility, copy Forwarding URL
7. from Event Subscriptions, using the Forwarding URL to set up Request URL
       for instance: https://1b61ecf17210.ngrok.io/slack/events
8. Subscribe to bot events
    app_mention
    message.channels
    message.groups
    message.im
    message.mpim
9. from Interactivity & Shortcuts, turn on Interactivity,
   using the Forwarding URL to set up Request URL
        for instance: https://1b61ecf17210.ngrok.io/slack/events
10. from Slash Commands, Create New Commands
    assign Command = /userid
    using Forwarding URL to assign Request URL 
       for instance: https://1b61ecf17210.ngrok.io/slack/events
    provide a short description
    and save
11. from Install App, install/reinstall app to workspace

Setup local project:
# setup virtural environment
python -m venv .venv
source .venv/bin/activate
put the follow two lines in .envVariables file
    export SLACK_SIGNING_SECRET=<SIGNING_SECRET>
    export SLACK_BOT_TOKEN=<Bot User OAuth Token>
source .envVariables

# setup dependencies
pip install slack_bolt
pip install slackclient==1.3.2
pip install aiohttp
setup ngrok to create a local requests URL for development

Start servers
ngrok http 3000
python3 app.py
