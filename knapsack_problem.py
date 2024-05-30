def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            # we do i -1 because the table has n + 1 rows, 
            #whereas list of values is length n
            elif wt[i-1] <= w:
                #the maximum between the addition of the value
                #of the current item in consideration + 
                #and the value in the above row for the same capacity 

                '''w-wt[i-1], tells us the remaining capacity after putting the current item in consideration
                wt[i-1] is resolved first to give the weight of the current item in consideration
                the current weight is return and subtracted from the capacity w
                so K[i-1] moves us to the above row, 
                then w - wt[i-1] moves us to the column of the remaining capacity to be filled
                this allows us to take the item with the largest value that was already calculated 
                for the remaining capacity from the above row
                if remaining capacity is 0, we move to the 0 column and pick a 0 value'''

                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            #if the current value exceeds the capacity 
            #enter the value in the above row for the same capacity 
            else:
                K[i][w] = K[i-1][w] 
    return K[n][W]



if __name__ == "__main__":
    #change wt:val to a dictionoary
    #valueweight_dictionary = {60:10, 100:20, 120:30}
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    #val = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    #       78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    #       87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    #       312]
    #wt = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    #      42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    #      3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
    #W = 850
    #n = len(val)
    print(knapSack(W, wt, val, n))