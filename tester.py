import helper
import encryptation_algorithms

alphabet = helper.create_english_alphabet()
caps_alphabet = helper.create_english_caps_alphabet()

# Caesar Cipher Unit Testing #
word = "HOWTOSHAREASECRET"
key = 1
correct_solution = "IPXUPTIBSFBTFDSFU"
solution = encryptation_algorithms.caesar_cipher(caps_alphabet, word, key, "encrypt")
assert correct_solution == solution

word = "IPXUPTIBSFBTFDSFU"
key = 1
correct_solution = "HOWTOSHAREASECRET"
solution = encryptation_algorithms.caesar_cipher(caps_alphabet, word, key, "decrypt")
assert correct_solution == solution
# End Caesar Ciper Unit Testing #

# Vigenere Cipher Unit Testing #
word = "UYINMTRMZWTRGZ"
key = "BRAVE"
correct_solution = "THISISAMESSAGE"
solution = encryptation_algorithms.vigenere_cipher(caps_alphabet, word, key, "decrypt")
assert solution == correct_solution

word = "THISISAMESSAGE"
key = "BRAVE"
correct_solution = encryptation_algorithms.vigenere_cipher(caps_alphabet, word, key, "encrypt")
solution = "UYINMTRMZWTRGZ"
assert solution == correct_solution
# End Vigenere Cipher Unit Testing #
