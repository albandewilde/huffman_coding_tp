from to_bin import read_file

def count_char( path ):
    content = read_file( path )
    
    count = 0
    for char in content:
        count += 1
    
    print(count)