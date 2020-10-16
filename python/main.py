#!/usr/bin/env python3

from to_bin import encode_file_to_bites, read_file, char_to_bytes, write_to_file
from count_char import count_char
from occurence import get_occurence, text_to_bin
from huffman_tree import sort_occurence_dico, to_dict, to_tree, dico_to_file

input_file: str = 'alice.txt'
alice = read_file(input_file)
nb_char_in_alice = count_char(alice)
output_classic_bytes = 'encoded_alice.txt'
output_huffman = 'alice_huffman.txt'
output_huffman_dict = 'huffman_dict.txt'

def browse_txt():
    encoded = ""
    occurence: Dict[str, int] = {}

    for char in alice:
        encoded = char_to_bytes(char, encoded)
        occurence = get_occurence(occurence, char)
    write_to_file(encoded, output_classic_bytes)
    return occurence

occurence = browse_txt()
sorted_occurence = sort_occurence_dico(occurence)
huffman = to_tree(sorted_occurence)
huffman_dict = to_dict(huffman)
dico_to_file(huffman_dict, output_huffman_dict)
text_to_bin(alice, output_huffman_dict, output_huffman)





# Just to see result
alice_in_bytes = read_file(output_classic_bytes)
alice_in_hufman = read_file(output_huffman)
nb_char_in_alice_bytes = count_char(alice_in_bytes)
nb_char_in_alice_huffman = count_char(alice_in_hufman)


print("char in file not encoded: ", nb_char_in_alice)
print("char in file classic bytes: ", nb_char_in_alice_bytes)
print("char in file huffman: ", nb_char_in_alice_huffman)
