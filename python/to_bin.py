def read_file(filepath):
    """Read file content and return his string"""
    with open(filepath, "r") as fle:
        text = fle.read()
    return text

def write_to_file(content, filepath):
    with open(filepath, "w") as fle:
        fle.write(content)


def char_to_bytes(char, encoded):
    encoded += "{:08b}".format(ord(char))
    return encoded

if __name__ in "__main__":
    encode_file_to_bites("alice.txt", "encoded_alice.txt")
