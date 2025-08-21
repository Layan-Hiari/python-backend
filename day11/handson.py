import re
from datetime import datetime
import pytz

def extract_data_from_string(text):
    print("\nExtracting data from input string...\n")
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(email_pattern, text)
    phone_pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b'
    phones = re.findall(phone_pattern, text)
    date_pattern = r'\b(?:\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b'
    dates = re.findall(date_pattern, text)
    print(f"Emails found: {emails}")
    print(f"Phone numbers found: {phones}")
    print(f"Dates found: {dates}")

def convert_timezone(dt_str, from_tz_str, to_tz_str):
    try:
        naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD HH:MM:SS")
        return
    try:
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)
    except pytz.UnknownTimeZoneError as e:
        print(e)
        return
    local_dt = from_tz.localize(naive_dt)
    converted_dt = local_dt.astimezone(to_tz)
    print("\nConverted Time:")
    print(f"{from_tz_str}: {local_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{to_tz_str}: {converted_dt.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    print("=== Regex Data Extractor & Timezone Converter ===")
    input_string = input("\nEnter a string containing emails, phone numbers, or dates: ")
    extract_data_from_string(input_string)
    print("\n--- Timezone Conversion ---")
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    from_tz = input("Enter FROM timezone (e.g., 'US/Eastern'): ")
    to_tz = input("Enter TO timezone (e.g., 'Asia/Tokyo'): ")
    convert_timezone(dt_str, from_tz, to_tz)

if __name__ == "__main__":
    main()
