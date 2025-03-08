
def find_min(arr, start):
    min = start;
    print(arr)
    for i in range(start + 1, len(arr)): # start+1 - len-1
        if arr[i] < arr[min]:
            min = i;
    return min


def selection(arr):
    ind = 0
    # len = arr.length - 1
    
    for ind in range (len(arr) - 1):
        #subarr = arr [ind + 1, len
        min = find_min(arr, ind)
        arr[ind], arr[min] = arr[min], arr[ind] #swap elem with min of rest
    return arr
    
arr = [0, 25, 73, 22, 11]
sorted = selection(arr)
print(sorted)







# """
# https://www.geeksforgeeks.org/insertion-sort-algorithm/?ref=lbp
# https://www.geeksforgeeks.org/bubble-sort-algorithm/?ref=lbp
# https://www.geeksforgeeks.org/quick-sort-algorithm/?ref=lbp
# https://www.geeksforgeeks.org/selection-sort-algorithm-2/?ref=lbp
# Selection Sort
# Constraints:
# length of array max(Int); [-9223372036854775808 to 9223372036854775807]
# O(n), or sort in place

# Pseudocode
# [64, 25, 73, 22, 11]
# 64, 11 -> [11, 25, 73, 22, 64]
# 25, minRest = 22, -> [11, 22, 73, 25, 64]
# 73, minRest = 25, -> [11, 22, 25, 73, 64]
# 73, minRest = 64, -> [11, 22, 25, 64, 73]

# [0, 25, 73, 22, 11]; ind = 0; min = 0
# [0, 25, 73, 22, 11]; ind = 1; min = 11 -> [0, 11, 73, 22, 25]
# [0, 11, 73, 22, 25]; ind = 2; min = 22 -> [0, 11, 22, 73, 25]
# [0, 11, 22, 73, 25]; ind = 3; min = 25 -> [0, 11, 22, 25, 73]

# iterate each ind
# subarr from ind - end; find min; swap min and arr[ind]
# ind++




# Test by hand



# """