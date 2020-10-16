#!/usr/bin/env python3

import datetime

from to_bin import read_file, char_to_bytes, write_to_file
from count_char import count_char
from occurence import get_occurence, text_to_bin
from huffman_tree import sort_occurence_dico, to_dict, to_tree, dico_to_file

input_file: str = 'alice.txt'
output_classic_bytes = 'py_encoded_alice.txt'
output_huffman = 'py_alice_huffman.txt'
output_huffman_dict = 'py_huffman_dict.txt'

def browse_txt():
    encoded = ""
    occurence: Dict[str, int] = {}

    for char in alice:
        encoded = char_to_bytes(char, encoded)
        occurence = get_occurence(occurence, char)
    write_to_file(encoded, output_classic_bytes)
    return occurence

begin = datetime.datetime.now()
alice = read_file(input_file)
print("Reading file: ", datetime.datetime.now() - begin)

begin = datetime.datetime.now()
nb_char_in_alice = count_char(alice)
occurence = browse_txt()
print("Counting occurence: ", datetime.datetime.now() - begin)

begin = datetime.datetime.now()
sorted_occurence = sort_occurence_dico(occurence)
huffman = to_tree(sorted_occurence)
print("Making huffman tree: ", datetime.datetime.now() - begin)

begin = datetime.datetime.now()
huffman_dict = to_dict(huffman)
print("Encoding the text: ", datetime.datetime.now() - begin)

begin = datetime.datetime.now()
dico_to_file(huffman_dict, output_huffman_dict)
print("Writing to file: ", datetime.datetime.now() - begin)

text_to_bin(alice, output_huffman_dict, output_huffman)


# Just to see result
alice_in_bytes = read_file(output_classic_bytes)
alice_in_hufman = read_file(output_huffman)
nb_char_in_alice_bytes = count_char(alice_in_bytes)
nb_char_in_alice_huffman = count_char(alice_in_hufman)


print("char in file not encoded: ", nb_char_in_alice)
print("char in file classic bytes: ", nb_char_in_alice_bytes)
print("char in file huffman: ", nb_char_in_alice_huffman)
