def str_to_bin(text):
    """Convert a string to a binaire charactes as at least 8 bits"""
    for char in text:
        yield "{:08b}".format(ord(char))

def read_file(filepath):
    """Read file content and return his string"""
    with open(filepath, "r") as fle:
        text = fle.read()
    return text

def write_to_file(content, filepath):
    with open(filepath, "w") as fle:
        fle.write(content)

""" J'ai regroupé str_to_bin et cette methode
    pour eviter de boucler 2 fois"""
def encode_file_to_bites(txt, out_file):
    encoded = ""
    for char in txt:
        encoded += "{:08b}".format(ord(char))
    write_to_file(encoded, out_file)

def char_to_bytes(char, encoded):
    encoded += "{:08b}".format(ord(char))
    return encoded

if __name__ in "__main__":
    encode_file_to_bites("alice.txt", "encoded_alice.txt")
