def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def filter_by_voyel(word_list, N):
    filtered_list = []
    for word in word_list:
        if count_vowels(word) >= N:
            filtered_list.append(word)
    return filtered_list

words = []
a=0
while True:
    word= str(input("Entrez une liste de chaîne de caractères : "))
    if word == "":
        break
    words.append(word)

N = int(input("Entrez un nombre N : "))

filtered_words = filter_by_voyel(words, N)
print("Mots avec au moins", N, "voyelle(s) :", filtered_words)
