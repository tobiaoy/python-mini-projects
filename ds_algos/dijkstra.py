# here we're going to be implementing dijkstra's algorithm
# this algorithm really only works on weighted acyclic graphs
# also note that this doesn't work with negative weights
# for that you'll need bellman-ford's algorithm
# this algorithm works by finding the shortest path (by weight)
# it updates the shortest paths to different points on the graph until it reaches the end
# once a point has been processed it doesn't repeat -> negative weights break the algorithm

# we're going to need three hash tables
# we need to represent the points and their weights

# the first hash table represents the graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')

# the second represents the costs -> how long it takes to get to a node from the start
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# the third hash table represents the parents -> the point leading to that point
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# finally an array to keep track of processed nodes
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost =  costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
