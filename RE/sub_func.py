import re
int_string = "1 2 987 4 5"

def int_match_to_float(match_obj):
    #return "testing"
    return (match_obj.group('num') + ".0")



pattern = r"(?P<num>[0-9]+)"
regexp = re.compile(pattern)


#result = regexp.search(int_string)
#print(result.group('num'))
#print(regexp.sub('a',int_string))

## Passing function in sub method.
# Python calls this fuction with current matched object and the returned value will be used to replace matched string.

print(regexp.sub(int_match_to_float,int_string))