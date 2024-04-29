# cette fonction prend en paramètre une chaine de caractère
def transform_bwt(data):
     # Liste de toutes les rotations possibles de la chaîne de caractères
    rotations = [data[i:] + data[:i] for i in range(len(data))]
     # Tri des rotations par ordre alphabétique
    rotations.sort()
    #prend le dernier caractère de la chaine à chaque rotation
    transformed_data = ''.join(rotation[-1] for rotation in rotations)
     # cherche où se trouve la chaîne d'origine parmi toutes les rotations triées
    key = rotations.index(data)
     #retourne la chaine de caractère transformé et la clé     
    return transformed_data, key

    #cette fonction prend en paramètre la chaine de caractère transformée et key
def inverse_bwt(transformed_data, key):
    # Crée une liste 'table' de chaînes vides de la même longueur que 'transformed_data'
    table = [''] * len(transformed_data)
    # boucle qui permet de lire chaque caractère de la chaine transformed_data 
    for i in range(len(transformed_data)):
         #permet de triée les caractères de transformed_data ordre lexicographique à l'aide de la fonction : sorted dans la liste table
        table = sorted([transformed_data[i] + table[i] for i in range(len(transformed_data))])
     # La chaîne original se trouve dans key 'key' dans la liste 'table'
    original_data = table[key]
    # on retourne la chaine original
    return original_data
