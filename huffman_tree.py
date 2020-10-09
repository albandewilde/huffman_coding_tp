class Node(object):
    def __init__(self, left, right, content):
        self.content = content
        self.left = left
        self.right = right

def sort_occurence_list(dico):
        return sorted(dico.items(), key=lambda elem: elem[1])

def to_tree(occurence_list):
    rt_nde = Node(None, None, occurence_list[0])

    for nde in ocurence_list[1:]:
        right_nde = Node(None, None, nde)
        left_nde = rt_nde
        rt_nde = Node(left_nde, right_nde, None)

    return rt_nde

def to_dict(root_node, dico={}, base_bit=""):
    if root_node.right is None:
        dico[root_node.content[0]] = base_bit

    if root_node.right is not None:
        to_dict(root_node.left, dico, base_bit+"0"

    if root_node.left is None:
        dico[root_node.content[0]] = base_bit

    if root_node.left is not None:
        to_dict(root_node.right, dico, base_bit+"1")

    return dico

if __name__ in "__main__":
    dico = {"r": 1, "t": 6, "e": 18, "4": 4, "3": 4}
