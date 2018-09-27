
def create_alphabet_list():
    alphabet = []
    
    i = ord('a')
    last_it = ord('z')
    while(i <= last_it):
        alphabet.append(chr(i))
        i += 1
    
    return alphabet
