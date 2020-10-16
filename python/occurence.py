from typing import Dict 
from to_bin import read_file, write_to_file
import json

def get_occurence(occurence, letter):
    if letter not in occurence:
        occurence[letter] = 1
    else:
        occurence[letter] += 1  
    return occurence

def text_to_bin(content: str, file: str, file_output:str) -> None:
    bin_str = read_file(file)
    dico: Dict[str, str] = json.loads(bin_str)
    file_content: str = ''
    for letter in content:
        file_content += dico[letter]
    write_to_file(file_content, file_output)
