# Telegram Group to Twitter bot

This app will will forward messages from a user **TELEGRAM_USER_ID** posting in a channel  **TELEGRAM_CHANNEL_ID** 

**config.py** will read the os environment variables from a .env file

## env example

this examples can also be found in the .env.example file
```
TELEGRAM_USER_ID = 123456789
TELEGRAM_CHANNEL_ID = 123456789
TELEGRAM_API_ID = 2222222
TELEGRAM_API_HASH = "acbc162d62........................"
TELEGRAM_BOT_TOKEN = "1571316368:....................."

TWITTER_CONSUMER_KEY = 'v0P3SK...............'
TWITTER_CONSUMER_SECRET = 'pBHMZzo..............................................'
TWITTER_ACCESS_TOKEN = '53883286-............................................'
TWITTER_ACCESS_TOKEN_SECRET = 'z5JJ.........................................'
```
To find out the information about **TELEGRAM_USER_ID** and **TELEGRAM_CHANNEL_ID** 
the bot command `/info` can be used in the channel were the telegram bot was invited

## deploy on heroku

Procfile file for herokku is already created and the app is ready to deploy

environment varibales need to be created in heroku

## Other requirements 

### Create a Telegram bot

https://core.telegram.org/bots#3-how-do-i-create-a-bot

invite it to your cahnnel and give it admin permissions

### Create an App for Telegram 

(Most common reason for form submission ERROR while creating a app are some browser addons or a VPN connection/config)

https://my.telegram.org/apps

TELEGRAM_API_HASH = App api_id:
TELEGRAM_API_ID = App api_hash


### Twitter

create a [twitter developer app](https://developer.twitter.com/)

Under `User authentication settings` generate a `Access Token and Secret`

<img width="697" alt="Screenshot 2021-12-15 at 19 56 03" src="https://user-images.githubusercontent.com/31136147/146239766-8c3ae52d-5157-426f-b319-54b4c1a836e5.png">

with read/write permissions

TWITTER_CONSUMER_KEY = API KEY

TWITTER_CONSUMER_SECRET = API SECRET KEY 


