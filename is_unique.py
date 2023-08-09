def is_unique(lst):
    # Utilisation d'un ensemble (set) pour détecter les doublons
    unique_set = set()
    for element in lst:
        if element in unique_set:
            return False
        unique_set.add(element)
    return True

# Test de la fonction is_unique
liste_sans_doublons = [1, 2, 3, 4, 5]
liste_avec_doublons = [1, 2, 2, 3, 4, 5]

print("La liste sans doublons retourne:", is_unique(liste_sans_doublons))
print("La liste avec doublons retourne:", is_unique(liste_avec_doublons))
