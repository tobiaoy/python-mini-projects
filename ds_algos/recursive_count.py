# here we want to define a function that can recursively count the number of items in a list

def recursive_count(l):
    # first we want the base case
    if len(l) == 0:
        return 0
    # then the recursive case
    else:
        # we want to maintain a count that will reduce the array until we get to 1 or 0
        count = 0
        if len(l) > 0:
            l.pop(0)
            count += 1
        result = count + recursive_count(l)
    return result

if __name__ == '__main__':
    sample1 = [5,3,6,2,10]
    sample2 = [2,5,3,5,1,6,7,4,1,3,4,5,6]
    
    print(recursive_count(sample1)) # should be 5
    print(recursive_count(sample2)) # should be 9
        