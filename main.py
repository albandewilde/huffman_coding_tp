#!/usr/bin/env python3

from to_bin import encode_file_to_bites, read_file
from count_char import count_char
from occurence import TextParser
from huffman_tree import sort_occurence_dico, to_dict, to_tree, dico_to_file

input_file: str = 'alice.txt'

# Encode the file as a binaire
encode_file_to_bites(input_file, "output.txt")

print("char in file alice.txt: ", count_char(input_file))
print("char in file output.txt: ", count_char("output.txt"))

count_char(input_file)
texte_parser = TextParser(read_file(input_file))
sorted_dict = texte_parser.get_occurence()

lst = sort_occurence_dico(sorted_dict)

tree = to_tree(lst)

dico = to_dict(tree)

dico_to_file(dico, 'dico_output.txt')

texte_parser.text_to_bin('dico_output.txt', 'alice_huffman.txt')