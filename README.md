# ArbitrageBotV0

This bot will spot arbitrage opportunities on various DEX's and execute trades with flash loans

## Installation

Best run with docke-compose.
You can just clone the repository and run:
```bash
docker-compose up -d
```
You will also need to create a file secrets.py like this:
```
infura_project_id=""
discord_bot_token=""
```
It is also necessary to change the channel id to fit your desired discord output channel.