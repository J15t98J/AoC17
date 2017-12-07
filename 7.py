import re
import copy


def populate(node):
    # recursively build the tree of children of this node
    sub_tree = {child_node: populate(child_node) for child_node in children[node]}
    # calculate the full weight of this node from its weight and the full weights of its children
    child_full_weights = [full_weights[child_node] for child_node in children[node]]
    full_weights[node] = weights[node] + sum(child_full_weights)
    # if one of the children is different
    if len(set(child_full_weights)) > 1:
        # add the correct weight for the incorrectly-weighted program to unbalanced{} at the index equal to its current
        # full weight (so that when we sort by index, the lightest i.e. nearest-the-top one will win, as all of the
        # parent nodes of the incorrectly-weighted program will also be in the list)
        target_weight = max(set(child_full_weights), key=child_full_weights.count)
        actual_weight = min(set(child_full_weights), key=child_full_weights.count)
        unbalanced[actual_weight] = \
            weights[children[node][child_full_weights.index(actual_weight)]] + (target_weight - actual_weight)
        # weight of[  child with  [            the wrong weight           ]] + (    the weight difference    )
    return sub_tree


tree, children, weights, unbalanced = {}, {}, {}, {}

for line in open("7.txt", "r"):
    # split each line into the core bits of info: parent, weight, children; store each
    parts = re.split("\s\(|\)\s->\s|\)$", line.splitlines()[0])
    weights[parts[0]] = int(parts[1])
    children[parts[0]] = [word for word in (parts[2].split(", ") if parts[2] else [])]

# deepcopy the weights list so that we can modify it later
full_weights = copy.deepcopy(weights)

# recursively build the program tree and calculate the weights
for name in list(children.keys()):
    if name not in [word for children in children.values() for word in children]:
        tree[name] = populate(name)

# first (and only) key in tree{} is the top-level program
print(list(tree.keys())[0])
# value of the smallest key in unbalanced list is the deepest unbalanced disk
print(unbalanced[min(unbalanced.keys())])
