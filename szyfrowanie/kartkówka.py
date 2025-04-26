alphabet = "aąbcćdeęfghijklłmnopqrsśtuvwxyzźż"

def caesar_decrypt(ciphertext, shift, alphabet):
    decrypted = ""
    n = len(alphabet)
    for char in ciphertext:
        if char.lower() in alphabet:
            # Sprawdź pozycję znaku w alfabecie
            idx = alphabet.index(char.lower())
            # Oblicz nowy indeks po przesunięciu w lewo
            new_idx = (idx - shift) % n
            # Zachowaj wielkość litery
            if char.isupper():
                decrypted += alphabet[new_idx].upper()
            else:
                decrypted += alphabet[new_idx]
        else:
            # Znaki spoza alfabetu pozostają bez zmian
            decrypted += char
    return decrypted

ciphertext = "eax toćę ksbax khlwex, fhsmws?"

print("Możliwe odszyfrowania:\n")
for shift in range(len(alphabet)):
    decrypted_text = caesar_decrypt(ciphertext, shift, alphabet)
    print(f"Przesunięcie {shift}: {decrypted_text}")











