from to_bin import read_file

def decode_file( reading_file, out_file, dictionary ):
    content = read_file( reading_file )
    new_dict: Dict[str, str] = {}

    for k, v in dictionary.items():
        new_dict[v] = k

    result = ""
    while content:
        for k in new_dict:
            if content.startswith(k):
                result += new_dict[k]
                content = content[len(k-1):]
                break

    write_to_file(result, out_file)