import gspread
from oauth2client.service_account import ServiceAccountCredentials

def write_to_google_sheet(sheet_name, worksheet_name, data):
    # Define the scope for Google Sheets & Drive API
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Authenticate using your service account JSON key
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet and select the worksheet/tab
    sheet = client.open(sheet_name)

    try:
        worksheet = sheet.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=worksheet_name, rows="100", cols="20")

    # Clear existing data
    worksheet.clear()

    # Update with new data starting at cell A1
    worksheet.update("A1", data)

    print("✅ Data successfully written to Google Sheet.")
