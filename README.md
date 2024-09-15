# Telegram Bot with Uvicorn, FastAPI and Ngrok

This repository contains an example of a Telegram bot built using **FastAPI**, running with **Uvicorn**, and utilizing **ngrok** to handle the Telegram webhook in a local environment.

## Requirements

- Python 3.8+
- [Uvicorn](https://www.uvicorn.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Ngrok](https://ngrok.com/)
- A Telegram Bot API token

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vadilonga/telegram-bot-fast-api-uvicorn
   cd telegram-bot-fast-api-uvicorn
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate  # On Ubuntu use: source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root and add your Telegram Bot API token:

   ```bash
   BOT_API_TOKEN=your-telegram-bot-token
   DOMAIN_URL=https://your-ngrok-url/
   ```

2. Download or install ngrok, you can find the download here https://ngrok.com/download

3. Start ngrok to expose the local server with a public URL:

   ```bash
   ./ngrok http 8000
   ```

4. Copy the public URL provided by ngrok into the `.env` file under DOMAIN_URL

## Running the Bot

1. Start the bot using Uvicorn:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Set the webhook by accessing the `/setwebhook` endpoint in the browser. The page may ask you to confirm that you want to visit the site, click the button to confirm. Once you have set the webhook, if everything is set up correctly, you should see a response indicating "webhook setup ok".

3. Open telegram, find your bot chat and send the `/start` command. If the bot is set up properly, it should respond to your message.
