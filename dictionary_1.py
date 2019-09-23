# interview question Exabeam
# 1) if key is 'host', print value and if value is True or 1, print key

import re

dict = {'guido': 427, 'irv': 4127, 'jack': 4098, 'host': 345, 'Stan': True}

for key, value in dict.items():
    if key == "host":
        print value
    elif value == True or value == 1:
        print key

# 2) phone number format xxx-xxx-xxxx using regex

#regex = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
#regex = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

regex = "(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?"

string = '1234567890'
string1 ='123-345-0987'
string2 = "This is my number : 123 "

result = re.search(regex, string)
result1 = re.search(regex, string1)
result2 = re.search(regex, string2)

print result.group()
print result1.group()
print result2