# File: sales/transform_sales.py

def transform_for_sheet(data):
    if not data:
        return []
    headers = list(data[0].keys())
    values = [list(row.values()) for row in data]
    return [headers] + values
