# fonction qui prend en paramètre une chaîne de caractères
def encode_rle(data):
     # chaîne vide pour stocker la chaine de caractères
    encoded_data = ""
     # variable pour stocker le caractère actuel 
    gold = ""
     #variable qui compte la longeur du caractère actuel
    run_lenght = 0
     #Parcours de la chaîne de caractères
    for i in range(len(data)):
        if i == 0:
             # Pour le tout premier caractère, attribuer la valeur de ce caractère à la variable 'gold'
            gold = data[i]
             # mettre à jour 'run_length' à 1 car nous avons au moins un caractère
            run_lenght = 1
        else:
             # Pour les caractères suivants, stocker le caractère dans 'roro'
            roro = data[i]
            if roro == gold:
                 # Si le caractère actuel est identique au précédent, augmenter la valeur de run_lenght
                run_lenght += 1
            else:
                 # Si le caractère actuel est différent, ajouter la longueur du caractère et le caractère à la chaine encodé
                encoded_data += str(run_lenght) + gold
                 # Mettre à jour 'gold' avec le nouveau caractère
                gold = roro
                 # # Réinitialiser la longueur du caractère à 1 pour le nouveau caractère
                run_lenght = 1
     # Ajouter la dernière séquence encodée après la boucle          
    encoded_data += str(run_lenght) + gold
     # Retourner la chaîne de caractères encodée
    return encoded_data

    # cette fonction prend en paramètre la chaine encodé
def decode_rle(encoded_data):
     # chaine vide pour stocker les donnés encodé
    decoded_data = ''
     # chaine vide pour stocker le nombre de répétition
    count = ''
     # parcours la chaine encodé
    for i in encoded_data:
         # véréfier si le caractère est un chiffre et ajouter à count
        if i.isdigit():
            count += i
        else:
             # si c'est pas un chiffre, alors le caractère i est multiplié par le nombre de répétition contenu dans count
            decoded_data += i * int(count)
            count = ''
     # retourner la chaine décodé
    return decoded_data

