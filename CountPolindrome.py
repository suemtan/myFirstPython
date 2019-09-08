# count and print all palindrome numbers in a list
def Is_palindrome(a):

    start = 0
    end = len(a) - 1

    #loop
    while start < end:
        if a[start] != a[end]:
            return 0
        start += 1
        end -= 1
    return 1

def main():
    a_list = [11, 102, 131,609, 525, 101, 200, 909]
    count = 0

    print " Here is the list : ["
    for i in a_list:
        print i,
    print " ]"

    print " Here is the Palindrome list : ["

    for i in a_list:
        cstring = str(i)
        if Is_palindrome(cstring) == 1:
            count += 1
            print i ,

    print "]"
    print "Total number of Palindrome in the list is : ", count

if __name__=="__main__":
    main()





