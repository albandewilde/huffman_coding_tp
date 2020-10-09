from to_bin import write_to_file

class Node(object):
    def __init__(self, left, right, weight, content):
        self.weight = weight
        self.content = content
        self.left = left
        self.right = right

def sort_occurence_dico(dico):
        return sorted(dico.items(), key=lambda elem: elem[1])

def to_tree(occurence_dico):
    # occurence dico → key = lettre, value = nb_occurence
    # make list of node
    nodes = [Node(None, None, elem[1], elem[0]) for elem in occurence_dico]
    nodes.sort(key=lambda elem: elem.weight)

    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(left, right, left.weight + right.weight, None)
        for idx, node in enumerate(nodes):
            if node.weight > parent.weight:
                nodes.insert(idx, parent)
                break
        else:
            nodes.append(parent)

    return nodes[0]

def to_dict(root_node, dico={}, base_bit=""):
    if root_node.right is None:
        dico[root_node.content[0]] = base_bit

    if root_node.right is not None:
        to_dict(root_node.left, dico, base_bit+"1")

    if root_node.left is None:
        dico[root_node.content[0]] = base_bit

    if root_node.left is not None:
        to_dict(root_node.right, dico, base_bit+"0")

    return dico

def dico_to_file(dico, path):
    dico = sorted( dico.items(), key=lambda elem: elem[1] )

    content = '{\n'
    for key, value in dico:
        content += '"' + key + '":"' + value + '",\n'

    content = content + '}'

    with open(path, "w") as fle:
        fle.write( content )

if __name__ in "__main__":
    dico = {"r": 1, "t": 6, "e": 18, "4": 4, "3": 4}
    print("initial dico: ", dico)

    lst = sort_occurence_dico(dico)

    tree = to_tree(lst)

    dico = to_dict(tree)

    print("final dico: ", dico)
