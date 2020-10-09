from typing import Dict 

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