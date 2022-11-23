# we're going to try to define a much faster sorting algorithm
# it's called quicksort

def quicksort(l):
    # here l stands for list
    # we establish the base case
    if len(l) < 2:
        return l
    # pick a pivot 
    # partition the arrays into 2 sub arrays
    # values that are lower than pivot and 
    # values that are higher than pivot
    # call quicksort recursively on the left and right
    # so qs(left) + pivot + qs(right)
    # we do so until we get to 2 items
    # this will be easier to sort
    else:
        pivot = l[0]
        lower = [i for i in l[1:] if i <= pivot] # you'll notice that we alter the list by indexing from 1 onward
        higher = [i for i in l[1:] if i > pivot]
        return quicksort(lower) + [pivot] + quicksort(higher)
    
    
if __name__ == '__main__':
    sample1 = [5,3,6,2,10]
    sample2 = [2,5,3,5,1,6,7,4,1]
    print(quicksort(sample1))
    print(quicksort(sample2))


    