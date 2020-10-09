from typing import Dict 
from to_bin import read_file
import json

class TextParser:

    def __init__(self, content: str):
        self.content: str = content
    
    def get_occurence(self) -> Dict[str, int]:
        occurence: Dict[str, int] = {}
        for letter in self.content:
            if letter not in occurence:
                print("In")
                occurence[letter] = 1
            else:
                occurence[letter] += 1
        return occurence

    def sort_dict(self, occurence: Dict[str, int]) -> Dict[str, int]:
        sorted_dict: Dict[str, int] = {k: v for k, v in sorted(occurence.items(), key=lambda item: item[1], reverse=True)}
        return sorted_dict

    def text_to_bin(self, file: str, file_output:str) -> None:
        bin_str = read_file(file)
        dico: Dict[str, str] = json.loads(bin_str)
        print(dico)
        # with open(file_output, "r"):
            
