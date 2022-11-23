states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# we use a set here 
# sets don't repeat values 
# if a set has a repeated value it will truncate here

stations = {} # we need a list of stations and use a hash to make sure they are unique
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# keys are the stations names 
# the values are the states they cover
# all the values are sets

# something to hold the final set of stations
final_stations = set()

# you need to go through every station and pick the one that covers the most uncovered states -> best_station

best_station = None
states_covered = set() # a set of all the states this station covers that haven't been covered yet
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station
    # gets an intersection of a & b
    # set of states that were in both states_needed and states_for_station
    # covered is the set of uncovered that this station covers
    # a | b -> union of a, b
    # a - b -> difference of a, b
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered

states_needed -= states_covered
final_stations.add(best_station)

print(final_stations)
    
