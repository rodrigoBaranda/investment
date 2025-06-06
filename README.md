# Investment Portfolio Tracker

This is a minimal Flask-based web application used to track the state of an investment portfolio. It also supports pulling transaction data from a Google Sheet.

## Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up Google Sheets credentials (optional):
   - Create a Google Cloud service account and download the credentials JSON file.
   - Share your transactions sheet with the service account email.
   - Set the environment variables `GOOGLE_SERVICE_ACCOUNT_FILE` to the path of the JSON file and `GOOGLE_SHEET_KEY` to your sheet ID.
   - Instead of environment variables you may create a `config.py` file in the project root with `GOOGLE_SHEET_KEY` and `GOOGLE_SERVICE_ACCOUNT_FILE` defined.

3. Run the application:

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`.
Visit `/transactions` to load records from your sheet when configured.
