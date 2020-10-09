#!/usr/bin/env python3

from to_bin import encode_file_to_bites
from count_char import count_char

# Encode the file as a binaire
encode_file_to_bites("alice.txt", "output.txt")

print("char in file alice.txt: ", count_char("alice.txt"))
print("char in file output.txt: ", count_char("output.txt"))
