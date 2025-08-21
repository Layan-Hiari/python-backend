import re
from datetime import datetime
import pytz

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def display_time_in_timezones():
    timezones = [
        'UTC',
        'US/Eastern',
        'Europe/London',
        'Asia/Kolkata',
        'Asia/Tokyo'
    ]

    print("\nCurrent time in different timezones:")
    for zone in timezones:
        tz = pytz.timezone(zone)
        time_now = datetime.now(tz)
        print(f"{zone}: {time_now.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    email = input("Enter your email address: ").strip()
    if validate_email(email):
        print("Email is valid.")
    else:
        print("Email is invalid.")
    
    display_time_in_timezones()

if __name__ == "__main__":
    main()
