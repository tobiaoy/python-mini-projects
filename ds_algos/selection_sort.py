import random
# first we figure out how to find the smallest value
def find_smallest(l):
    smallest = l[0]
    smallest_index = 0
    for i in range(1, len(l)):
        if l[i] < smallest:
            smallest = l[i]
            smallest_index = i
    return smallest_index

def selection_sort(l):
    sorted_list = []
    for i in range(1, len(l)):
        smallest = find_smallest(l)
        sorted_list.append(l.pop(smallest))
    return sorted_list

if __name__ == '__main__':
    sample1 = [5,3,6,2,10]
    sample2 = [2,5,3,5,1,6,7,4,1]
    print(selection_sort(sample1))
    print(selection_sort(sample2))