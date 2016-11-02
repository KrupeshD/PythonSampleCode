import re

# regexp = re.compile(r"[-a-zA-Z]+, [-a-zA-Z]+( [-a-zA-Z]+)?: (\d\d\d-)?\d\d\d-\d\d\d\d")
# Above regular expression is correct but hard to maintain and underdtand when the pattern grows.
# Example: space between : and phone is optonal
# Therefore, it's better to devide the pattern at the time of compile as shown below

regexp = re.compile(r"(?P<sname>[-a-zA-Z]+,)"                  #RE for surname and comma
                    r"(?P<fname> [-a-zA-Z]+)"                  #RE for first name
                    r"(?P<mname>( [-a-zA-Z]+)?)"               #RE for optional middle name
                    r"(?P<phone>: (\d\d\d-)?\d\d\d-\d\d\d\d)"  #RE for phone number with optional area code.
                    )

with open("phone_num.txt","r") as phonenums:
    for line in phonenums:
        result = regexp.search(line)
        if result == None:
            print("Not Found")
        else:
            print('Name:',result.group('fname'),' Phone',result.group('phone'))

