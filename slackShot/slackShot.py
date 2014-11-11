
# pyslack
# A Python wrapper for Slack's API
# 
# https://api.slack.com
# 
# Installation
# 
# pip install git+git://github.com/loisaidasam/pyslack.git
# 
# from pyslack import SlackClient
# 

client = SlackClient('xoxp-2870308576-2870308582-2918153085-a165ac')
client.chat_post_message('#general', "testing, testing... Slack <-> Shotgun integration", username='slackbot')
