# here we want to define a function that can add recursively
# we want to add the number at the beginning to the rest of the array

def recursive_add(l):
    # first the base case
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    # now the recursive case
    else:
        first = l.pop(0)
        result = first + recursive_add(l)
    return result

if __name__ == '__main__':
    sample1 = [5,3,6,2,10]
    sample2 = [2,5,3,5,1,6,7,4,1]
    
    print(recursive_add(sample1)) # should be 26 
    print(recursive_add(sample2)) # should be 34