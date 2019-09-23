import re
from collections import Counter

def most_occur_element(word):

    #extract all elements and make a list
    arr = re.findall(r'[0-9]+', word)

    #max frequency counter
    maxm = 0

    #store max element of most frequency
    max_elem = 0

    #counter will store all numbers with their frequencies
    c = Counter(arr)

    #store all keys of counter in a list in which first would be required element
    for x in list(c.keys()):
        if c[x] >= maxm:
            maxm = c[x]
            max_elem = int(x)

    return max_elem

 #Driver/Main program
if __name__== "__main__":
    word = 'geek55of55gee4ksabc3dr2k5vi444'
    print(most_occur_element(word))