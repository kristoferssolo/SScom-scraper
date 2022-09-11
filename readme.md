# Webscraper
Webscraper of SS marketplace for GPUs

## Installation
```sh
git clone https://github.com/kristoferssolo/SScom-scraper
cd SScom-scraper
```
Create `config.json` file with following content:
```json
{
  "API_TOKEN": "<TOKEN_FROM_BOT_FATHER>"
}
```

Install required libraries:
```sh
pip install -r requirements.txt
python main.py
```

## Libraries used
- [Aiogram](https://github.com/aiogram/aiogram)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
