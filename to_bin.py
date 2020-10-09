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

def encode_file_to_bites(reading_file, out_file):
    content = read_file(reading_file)
    encoded = ""
    for char in str_to_bin(content):
        encoded += char
    write_to_file(encoded, out_file)

if __name__ in "__main__":
    encode_file_to_bites("alice.txt", "encoded_alice.txt")
