# demonstrate working re.search, match, and group function
# finding date string
import re

# month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

    print "Match as index %s, %s " % (match.start(), match.end())

    #return fully matched string
    print "Full match : %s " % (match.group(0))

    #return the capture of June
    print "Month : %s " % (match.group(1))

    #return day
    print "Day: %s " % (match.group(2))

else:
    print "The regex pattern does not match"

#findall()
print "Findall Function : "
#string1 = """"Hello My number is 5102345698 and my friend's number is 54321987"""
string1 = "Hello My number is 5102345698 and my friend's number is 54321987"
regex1 = '\d+'

match1 = re.findall(regex1, string1)
print (match1)

#find email
r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+]+\.[a-z]+"
text = "Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
regex2 = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+]+\.[a-z]+"

#extract all emails and add them into resulting set
emails = set(re.findall(regex2, text, re.I))

print("emails : ")
print(emails)
