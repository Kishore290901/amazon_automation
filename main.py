from sales.fetch_sales import get_mock_sales_data
from sales.transform_sales import transform_for_sheet
from sheets.google_sheets_writer import write_to_google_sheet

def main():
    print("🔄 Fetching sales data...")
    sales_data = get_mock_sales_data()

    print("🔄 Transforming data for Google Sheets...")
    sheet_data = transform_for_sheet(sales_data)

    print("📤 Writing data to Google Sheets...")
    write_to_google_sheet(
        sheet_name="Amazon Sales Dashboard",   # Change this to your actual Google Sheet name
        worksheet_name="Sales",                # Change this to your worksheet/tab name
        data=sheet_data
    )

if __name__ == "__main__":
    main()
