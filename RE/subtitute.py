import re
string = "If the the problem is textual, use the the re module" # two times the. Replace this with single the using re
pattern = r"the the"
regexp = re.compile(pattern)
print(regexp.sub("the",string))
print(string)
