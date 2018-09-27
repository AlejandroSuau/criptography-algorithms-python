def create_alphabet_array(character_from = '', character_to = ''):
    alphabet = []
    
    i = ord(character_from)
    last_it = ord(character_to)
    while(i <= last_it):
        alphabet.append(chr(i))
        i += 1
    
    return alphabet

def create_english_alphabet():
    character_from = 'a'
    character_to = 'z'
    return create_alphabet_array(character_from, character_to)

def create_english_caps_alphabet():
    character_from = 'A'
    character_to = 'Z'
    return create_alphabet_array(character_from, character_to)
