import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    matches = re.search(pattern, email)
    if matches:
        return True
    return False

emails = ['yogesh@gmail.com', 'invalid-email', 'user@domain.com']

for email in emails:
    if is_valid_email(email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is not a valid email.")
