## Telegram Plugin for Auto-GPT

A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal.
Making Auto-GPT a more user-friendly application to interact with.


## SETUP
First setup a telegram bot by following the instructions here: https://core.telegram.org/bots#6-botfather

Then set the following variables in your .env:

CHAT_MESSAGES_ENABLED=True
TELEGRAM_API_KEY=your-telegram-bot-token
TELEGRAM_CHAT_ID=your-telegram-bot-chat-id

to obtain your chat id, send a message to your bot and then use the following command:

curl https://api.telegram.org/bot<your-telegram-bot-token>/getUpdates```


<img src="https://user-images.githubusercontent.com/11997278/233675629-fb582ab6-f89f-4837-82c4-c21744427266.png" width="30%" height="30%"> <img src="https://user-images.githubusercontent.com/11997278/233675683-eea9dd74-1c5e-436a-b745-95dff17c4951.png" width="30%" height="30%">


# Auto-GPT-Plugins

Plugins for Auto-GPT

Clone this repo into the plugins direcory of [Auto-GPT](https://github.dev/Significant-Gravitas/Auto-GPT)

For interactionless use, set `ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3` in your `.env`

| Plugin   | Description                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------|
| Telegram | AutoGPT is capable of asking/prompting the user via a Telegram Chat bot and also responds to commands and messages. |

