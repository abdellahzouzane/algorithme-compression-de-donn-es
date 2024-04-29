README - Projet d'Algorithmes de Compression de Données

La compression de données est une technique essentielle pour réduire la taille des fichiers et optimiser la transmission et le stockage. Dans ce projet, vous trouverez des algorithmes permettant de transformer, compresser, et décompresser des données.

Description des Fichiers :
-burrows.py : Implémente les fonctions de transformation Burrows-Wheeler (BWT) et d'inversion BWT.
-transform_bwt(data): Effectue la transformation Burrows-Wheeler sur une chaîne de caractères donnée.
-inverse_bwt(transformed_data, key): Inverse la transformation Burrows-Wheeler pour récupérer la chaîne d'origine.

algo_rle.py : Fournit les fonctions d'encodage et de décodage utilisant Run-Length Encoding (RLE).
encode_rle(data): Encode une chaîne de caractères en utilisant RLE.
decode_rle(encoded_data): Décodage de la chaîne encodée avec RLE.
test.py : Contient des exemples de tests pour valider le bon fonctionnement des algorithmes.

Utilisation :
Pour utiliser les fonctions de ce projet, suivez ces étapes :
-Clonez le dépôt ou téléchargez les fichiers.
-Importez les modules requis (burrows.py ou algo_rle.py) dans votre script Python.
-Utilisez les fonctions correspondantes pour compresser et décompresser vos données.
