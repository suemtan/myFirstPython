# Recursive binary search for ascending array

def binarySearch(arr, l, u, f):


    #check minimum case
    if u >= 1:
        mid = l + (u -1)/2

        # if finding element is present at the middle
        if arr[mid] == f:
            return mid
        # if finding element is at first half of the array
        elif arr[mid] > f:
            return binarySearch(arr, l, mid-1, f)
        else:
            return binarySearch(arr, mid+1, u, f)

    else:
        return -1

def main():

    arr = [3, 4, 5, 7, 9, 12]

    #finding element
    f = 12
    lower = 0
    result = binarySearch(arr, lower, len(arr)-1, f)


    if result != -1:
        print " The element is found at index of %d in the array. "% result
    else:
        print " The element is not found in the array. "


if __name__ == '__main__':
        main() # call main function

