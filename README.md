# Webscraper

Webscraper of SS marketplace for GPUs

## Installation

```sh
git clone https://github.com/kristoferssolo/SScom-scraper
cd SScom-scraper
pip install .
```

Add [Telegram bot API token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) to the `config.json` file.
```json
{
  "API_TOKEN": "<TOKEN_FROM_BOT_FATHER>"
}
```

Run the bot.
```sh
python main.py
```
