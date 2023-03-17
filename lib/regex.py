import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[\w\s\d\'\-]+"
name_regex = re.compile(name)

phone_number = r"\(?\d{3}\)?[-\s]?\d{3}-?\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"[\d\w]\.\w\d]+@[a-z]+.com"
email_regex = re.compile(email_address)
