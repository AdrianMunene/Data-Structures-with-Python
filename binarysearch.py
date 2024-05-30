def binarysearch(arr, num):
    l = 0
    r = len(arr) -1

    while(l<r):
        mid = (l + r) // 2
        if(arr[mid] == num):
            return mid
        elif(arr[mid] < num):
            l = mid + 1
        else:
            r = mid - 1

    return -1

#def recursivebinarysearch(arr, num):


if __name__ == "__main__":
    arr = [-1,0,5,78,62,37,1,2,13]
    arr.sort()
    
    print(arr[binarysearch(arr,0)])