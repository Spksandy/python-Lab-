alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet + alphabet.upper()
alphabet_dict = {}
for k in alphabet:
    alphabet_dict[k] = True
alphabet_set = set(alphabet)
print(alphabet_set)
print(alphabet_dict)