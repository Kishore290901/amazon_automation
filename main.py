from sales.fetch_sales import get_mock_sales_data
from sales.transform_sales import transform_for_sheet
from sheets.google_sheets_writer import write_to_google_sheet
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email="kishore290907s@gmail.com"):
    from_email = "kishore290907s@gmail.com"
    app_password = "owfkzwdarmdiwmkf"  # Your app password - keep it safe!

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, app_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def main():
    try:
        print("🔄 Fetching sales data...")
        sales_data = get_mock_sales_data()

        print("🔄 Transforming data for Google Sheets...")
        sheet_data = transform_for_sheet(sales_data)

        print("📤 Writing data to Google Sheets...")
        write_to_google_sheet(
            sheet_name="Amazon Sales Dashboard",
            worksheet_name="Sales",
            data=sheet_data
        )

        send_email(
            subject="Amazon Automation Success",
            body="Your sales data was updated successfully in Google Sheets."
        )

    except Exception as e:
        send_email(
            subject="Amazon Automation Failure",
            body=f"Script failed with error:\n{e}"
        )
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
