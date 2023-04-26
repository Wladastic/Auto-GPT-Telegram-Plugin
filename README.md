# Disclaimer:
Please wait until this PR is merged: https://github.com/Significant-Gravitas/Auto-GPT/pull/2929
Otherwise the plugin cannot work.
I think it should be finished until 27th of April 2023, until then feel free to test using my branch: chat_plugin_capability

If you still have any questions, feel free to ask here: https://github.com/Wladastic/Auto-GPT-Telegram-Plugin/issues/1

As much as I appreciate it, please refrain from contacting me directly, as I do not have much time, thank you! :)



## Telegram Plugin for Auto-GPT

A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal.
Making Auto-GPT a more user-friendly application to interact with.


![image](https://user-images.githubusercontent.com/11997278/233675629-fb582ab6-f89f-4837-82c4-c21744427266.png)
![image](https://user-images.githubusercontent.com/11997278/233675683-eea9dd74-1c5e-436a-b745-95dff17c4951.png)


## SETUP
First setup a telegram bot by following the instructions here: https://core.telegram.org/bots#6-botfather

Then set the following variables in your .env:

CHAT_MESSAGES_ENABLED=True
TELEGRAM_API_KEY=your-telegram-bot-token
TELEGRAM_CHAT_ID=your-telegram-bot-chat-id

to obtain your chat id, send a message to your bot and then use the following command:

curl https://api.telegram.org/bot<your-telegram-bot-token>/getUpdates



# Auto-GPT-Plugins

Plugins for Auto-GPT

Clone this repo into the plugins direcory of [Auto-GPT](https://github.dev/Significant-Gravitas/Auto-GPT)

For interactionless use, set `ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3` in your `.env`

| Plugin   | Description                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------|
| Telegram | AutoGPT is capable of asking/prompting the user via a Telegram Chat bot and also responds to commands and messages. |

