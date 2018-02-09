from collections import Counter
components = []

with open("inputs/electromagnetic_moat.txt") as file:
    for line in file:
        components.append([int(port) for port in line[:-1].split("/")])

entries = []
for component in components:
    entries += component

port_count = Counter(entries)

endports = {(port, port) for port in port_count if port_count[port] == 1}
allports = {(port, port) for port in entries}

# Can look for paths starting at any port, or only those at the end of branches
# of the graph. I think the longest path need not be at the end of a branch, but
# it seems to work in my case

def find_path(endport, remaining_components) :
    scores = []
    if endport[0] != 0:
        for component in remaining_components:
            if endport[0] in component:
                next_port = component[int(not component.index(endport[0]))]
                score = endport[1] + 2*next_port
                new_components = remaining_components[:]
                new_components.remove(component)
                scores += find_path((next_port,score),new_components)

    else:
        final_score = endport[1]
        scores.append(endport[1])

    return scores

overall_scores = []

for port in endports:
    overall_scores += find_path(port, components)

print(f"Highest score {max(overall_scores)}")
