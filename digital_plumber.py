connections = []

with open("inputs/digital_plumber.txt") as file:
    for line in file:
        node, neighbours = line[:-1].split("<->")
        node = node.strip()
        neighbours = {int(neighbour.strip()) for neighbour in neighbours.split(",")}
        connections.append(neighbours)

def enlarge_neighbourhood(neighbours):
    new_neighbours = set({})
    for neighbour in neighbours:
        new_neighbours.update(connections[neighbour])

    return neighbours.union(new_neighbours)

def get_neighbourhood(node):

    neighbourhood = {node}
    old_size = 0
    size = 1

    while size > old_size:
        old_size = size
        neighbourhood = enlarge_neighbourhood(neighbourhood)
        size = len(neighbourhood)

    return neighbourhood

print("Size of the group containing 0: ",len(get_neighbourhood(0)))

num_groups = 0
nodes = set(range(2000))

while nodes:
    group = get_neighbourhood(nodes.pop())
    nodes.difference_update(group)
    num_groups += 1

print("Number of groups: ", num_groups)
