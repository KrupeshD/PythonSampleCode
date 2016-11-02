import re

regexp = re.compile(r"(?P<matched>[-a-zA-Z]+, [-a-zA-Z]+( [-a-zA-Z]+)?: (\d\d\d-)?\d\d\d-\d\d\d\d)")


with open("phone_num.txt","r") as phonenums:
    for line in phonenums:
        result = regexp.search(line)
        if result != None:
            print(result.group('matched'))

