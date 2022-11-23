# we want to write a function that can help us find the max number in a list
def recursive_max(l):
    # first the base case
    if len(l) <= 0:
        return -1
    elif len(l) == 1:
        return l[0]
    # then we have the recursive case
    else:
        if l[1] > l[0]:
            l.pop(0)
        else:
            l.pop(1)
        recursive_max(l)
        return l[0]

if __name__ == '__main__':
    sample1 = [5,3,6,2,10,14,18,3,25]
    sample2 = [2,5,3,5,1,6,7,4,1,3,4,5,6,15,9,12,4]
    
    print(recursive_max(sample1)) # should be 10
    print(recursive_max(sample2)) # should be 7