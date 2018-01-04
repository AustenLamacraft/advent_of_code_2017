import re
from collections import Counter


nodes = {}
weights = {}
weights_above = {}

with open("inputs/recursive_circus.txt") as file:
    for line in file:
        line_parts = line.split("->")
        parent = re.search(r"[a-z]+", line_parts[0]).group()
        weight = int(re.search(r"[0-9]+", line_parts[0]).group())
        if len(line_parts) == 2:
            children = re.findall(r"[a-z]+", line_parts[1])
        else:
            children = []

        nodes[parent] = set(children)
        weights[parent] = weight


def prune_tree(kid):
    "Recursively prune the tree"
    try:
        grandkids = nodes.pop(kid)
        for grandkid in grandkids:
            prune_tree(grandkid)
    except KeyError:
        pass



def sum_weights(kid):
    "Recursively sum the weights"
    grandkids = nodes[kid]
    total_weight = weights[kid]
    for grandkid in grandkids:
        total_weight += sum_weights(grandkid)

    weights_above[kid] = total_weight
    return total_weight


def find_root():

    while nodes:
        parent, children = nodes.popitem()
        for child in children:
            prune_tree(child)

        if nodes == {}:
            print(parent)

def find_unbalanced_node(root):
    kids = nodes[root]
    kid_weights = {weights_above[kid]: kid for kid in kids}
    if len(kid_weights) > 1:
        counter = Counter([weights_above[kid] for kid in kids])
        odd_kid = kid_weights[min(counter, key=counter.get)] # Find the kid with the unique weight above
        find_unbalanced_node(odd_kid)
        print(odd_kid)
