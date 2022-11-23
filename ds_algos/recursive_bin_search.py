# the aim here is to use divide and conquer in binary search
# this means using binary search recursively until we get our item
# otherwise returning -1

def binary_search(l, target, start=0, end=-1):
    if start == 0:
        start = 0
    if end == -1:
        end = len(l) - 1
    
    middle = (start + end) // 2
    
    if end < start:
        return -1
    
    # our base case -> the value is in the middle
    if l[middle] == target:
        return middle
    elif l[middle] < target:
        return binary_search(l, target, middle+1, end)
    else:
        return binary_search(l, target, start, middle-1)



if __name__ == '__main__':
    sample1 = [5,3,6,2,10,14,18,3,25]
    sample2 = [2,5,3,5,1,6,7,4,1,3,4,5,6,15,9,12,4]
    
    print(binary_search(sample1, 10)) # should be 4
    print(binary_search(sample1, 15)) # should be -1
    print(binary_search(sample2, 6)) # should be 13
    print(binary_search(sample2, 10)) # should be -1
        
        
        