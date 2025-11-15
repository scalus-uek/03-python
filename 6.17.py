time_24 = input('Enter time (24-hour format): ')

parts = time_24.split(':')
if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
    print('Invalid time input')
else:
    hh = int(parts[0])
    mm = int(parts[1])
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        print('Invalid time input')
    else:
        suffix = 'am' if hh < 12 else 'pm'
        h12 = hh % 12
        if h12 == 0:
            h12 = 12
        print(f"Time in 12-hour format: {h12}:{mm:02d}{suffix}")
