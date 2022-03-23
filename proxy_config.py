try:
    with open(r'C:\Users\Shubham Sharma\OneDrive - vRize India Private Ltd\Desktop\Projects\GmailCreator\proxies.txt', 'r') as file:
        proxy = [line.rstrip() for line in file.readlines()]
except FileNotFoundError:
    raise Exception('proxies.txt not found.')
