def longest_string(words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet + alphabet.upper()
    alphabet_dict = {}
    for k in alphabet:
        alphabet_dict[k] = True
    alphabet_set = set(alphabet)
    max_word = words[0]
    for el in words:
        if not((set(el)<=alphabet_set)and(set(el) == set(el).intersection(alphabet_dict.keys()))):
            continue
        if len(el)>=len(max_word):
            max_word = el
    return max_word
strs =  ['cat', 'car', 'fear', 'center']
print("Original string:",strs)
print("Longest string of the said list of strings:",longest_string(strs))