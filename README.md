# Jukebox

A simple appication which pulls all youtube links shared in a slack channel and provide a UI to view, play and vote those videos

### Slack configurations

Follow the steps to configure the slack workspace and channel to be monitored

* Signin to your slack work space
* Goto https://api.slack.com/apps?new_app=1
* Click on the 'create new app' button
* Choose an app name and select the work space.
* In the side bar menu, go to 'Event Subscriptions'
* Enable event subscription, you will be prompted for webhook url.
* Provide our application URL here. eg: `<domain>/incoming/`
* Once after verfiying url, add workspace event . select 'message.channels'
* Once done save the changes and you will be asked for enabling permission for app
* Select the channel and allow permissions in the continuing prompt.

You are done with the workspace and channel setup.

