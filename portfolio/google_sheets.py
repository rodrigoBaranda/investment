import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def get_transactions(sheet_key: str, credentials_file: str):
    """Return all transaction records from the first worksheet."""
    creds = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_key)
    worksheet = sheet.sheet1
    return worksheet.get_all_records()
