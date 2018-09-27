def vigenere_algorithm(alphabet = [], message = "", key = "", method = "encrypt"):
    message_result = ""
    alphabet_len = len(alphabet)
    i = 0
    
    for character in message:
        key_idx = alphabet.index(key[i])
        if method == "decrypt":
            key_idx *= -1
            
        char_idx = alphabet.index(character) + key_idx
        
        if char_idx < 0 or char_idx >= alphabet_len:
            char_idx %= alphabet_len
        
        if i == len(key)-1:
            i = 0
        else:
            i += 1
        
        message_result += alphabet[char_idx]
    
    return message_result
