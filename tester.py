import helper
import encryptation_algorithms

alphabet = helper.create_english_alphabet()
caps_alphabet = helper.create_english_caps_alphabet()

# Vigenere algorithm #
word = "UYINMTRMZWTRGZ"
key = "BRAVE"
correct_solution = "THISISAMESSAGE"
solution = encryptation_algorithms.vigenere_algorithm(caps_alphabet, word, key, "decrypt")
assert correct_solution == solution

word = "THISISAMESSAGE"
key = "BRAVE"
correct_solution = "UYINMTRMZWTRGZ"
solution = encryptation_algorithms.vigenere_algorithm(caps_alphabet, word, key, "encrypt")
assert correct_solution == solution
