# this lesson is about the implementation of a graph using hashing 
# again hash tables can be represented in dictionaries in python

# here's an example
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# it doesn't matter what order you put them in
# directed graphs -> the relationships are one way
# undirected graphs => there are no arrows and both nodes are each other's neighbors