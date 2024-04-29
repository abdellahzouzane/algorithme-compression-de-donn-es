from algo_rle import encode_rle, decode_rle


# Exemple 2
data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 2:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
print("Données décodées:", decoded_data)
print()