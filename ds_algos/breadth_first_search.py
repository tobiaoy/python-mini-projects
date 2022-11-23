# this is an implementation of a breadth first search on a graph
# step 1: keep a queue containing things (people) to check
# step 2: pop a person of the queue
# step 3: (in this case) check if this person is a mango seller (so some condition)
# step 4a: if yes, you're done
# step 4b: if no, add all their neighbors to the queue
# step 5: loop back and repeat from step 2
# step 6: if the queue is empty, there are no mango sellers in your network

from collections import deque # creates a new queue
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def search():
    search_queue = deque()
    search_engine += graph['name'] # adds all your neighbors to the search engine
    searched = []

    while search_engine:
        person = search_queue.popleft() # grabs the first person of the queue
        if person_is_seller(person): # checks if they're a mango seller
            print(f'{person} is a mango seller')
            return True
        else:
            search_engine += graph[person] # adds all the person's friends to the search queue
            searched.append(person)
    return False

def person_is_seller(name):
    return len(name) >= 5 # if their name ends with 'm' then they're a mango seller