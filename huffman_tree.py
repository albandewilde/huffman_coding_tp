from to_bin import write_to_file
import json
class Node(object):
    def __init__(self, left, right, content):
        self.content = content
        self.left = left
        self.right = right

def sort_occurence_dico(dico):
        return sorted(dico.items(), key=lambda elem: elem[1])

def to_tree(occurence_dico):
    rt_nde = Node(None, None, occurence_dico[0])

    for nde in occurence_dico[1:]:
        right_nde = Node(None, None, nde)
        left_nde = rt_nde
        rt_nde = Node(left_nde, right_nde, None)

    return rt_nde

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
    dico = {k: v for k, v in sorted(dico.items(), key=lambda item: item[1])}
    with open(path, "w") as fle:
        fle.write( json.dumps(dico) )

if __name__ in "__main__":
    dico = {"r": 1, "t": 6, "e": 18, "4": 4, "3": 4}
    print("initial dico: ", dico)

    lst = sort_occurence_dico(dico)

    tree = to_tree(lst)

    dico = to_dict(tree)

    print("final dico: ", dico)