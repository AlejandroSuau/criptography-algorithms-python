def caesar_cipher(alphabet = [], message = "", key = 0, method = "decrypt"):
    message_result = ""
    alphabet_len = len(alphabet)
    
    for character in message:
        key_idx = key
        if method == "decrypt":
            key_idx *= -1
            
        new_char_idx = alphabet.index(character)+key_idx
        
        if new_char_idx < 0 or new_char_idx >= alphabet_len:
            new_char_idx %= alphabet_len

        message_result += alphabet[new_char_idx]
        
    return message_result

def vigenere_cipher(alphabet = [], message = "", key = "", method = "decrypt"):
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
