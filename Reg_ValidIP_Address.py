# IPv4 consists of 4 numbers ( each between 0 and 255) separated by periods

import re

regex = '^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'

def checkIP(ip):
    if(re.search(regex, ip)):
        print "This is a valid ip address"
    else:
        print "Invalid ip address"

if __name__=='__main__':
    ip = "192.168.0.3"
    checkIP(ip)

    ip1 = "10.0.0.3"
    checkIP(ip1)

    ip2 = "192.33.0.3"
    checkIP(ip2)

    ip3 = "366.33.0.3"
    checkIP(ip3)

    ip4 = "99.33.0.3"
    checkIP(ip3)