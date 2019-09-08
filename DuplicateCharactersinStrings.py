# implementation for displaying duplicate characters in two strings

from collections import Counter

def findduplicatewords(s1):
    #create dictionary with counter method
    wordcount = Counter(s1);
    key = 0;

    for i in wordcount.values():
        if(i > 1):
            print wordcount.keys()[key];
        key = key + 1;

# main function
if __name__=="__main__":
    s1="hellokgeeks";

    findduplicatewords(s1);


