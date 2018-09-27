import helper
import encryptation_algorithms

# Vigenere algorithm #
word = "UYINMTRMZWTRGZ"
key = "BRAVE"
correct_solution = "THISISAMESSAGE"
solution = encryptation_algorithms.vigenere_algorithm(caps_alphabet, word, key, "decrypt")
assert solution == correct_solution

word = "THISISAMESSAGE"
key = "BRAVE"
correct_solution = encryptation_algorithms.vigenere_algorithm(caps_alphabet, word, key, "encrypt")
solution = "UYINMTRMZWTRGZ"
assert solution == correct_solution
