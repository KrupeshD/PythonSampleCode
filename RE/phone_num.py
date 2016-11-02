import re

# regexp = re.compile(r"[-a-zA-Z]+, [-a-zA-Z]+( [-a-zA-Z]+)?: (\d\d\d-)?\d\d\d-\d\d\d\d")
# Above regular expression is correct but hard to maintain and underdtand when the pattern grows.
# Example: space between : and phone is optonal
# Therefore, it's better to devide the pattern at the time of compile as shown below

regexp = re.compile(r"[-a-zA-Z]+,"                  #RE for surname and comma
                    r" [-a-zA-Z]+"                  #RE for first name
                    r"( [-a-zA-Z]+)?"               #RE for optional middle name
                    r": (\d\d\d-)?\d\d\d-\d\d\d\d"  #RE for phone number with optional area code.
                    )

with open("phone_num.txt","r") as phonenums:
    for line in phonenums:
        if regexp.search(line):
            print("found so what?")
        else:
            print("naaahhh")

