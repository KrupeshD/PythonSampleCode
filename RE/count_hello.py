import re
#regexp = re.compile('hello') # Always compile the pattern for faster execution.
regexp = re.compile("[hH]ello")

## Other options
## ("hello|Hello") OR ("(h|H)ello")

count = 0
with open("hello.txt",'r') as hellofile:
    for line in hellofile.readlines(): # Careful with realine() and readlines()
        if regexp.search(line):
            count = count + 1
print(count)


