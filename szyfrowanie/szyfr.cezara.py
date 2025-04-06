alfabet = ""
# for i in range(ord('a'), ord('z') + 1):
#     alfabet+=(chr(i))
import random

alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + list("ąćęłóźż")
random.shuffle(alfabet)
print(alfabet)


def szyfruj(napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    print(szyfr)
    wynik = ""
    for znak in napis:
        if ord('a') <= ord(znak) <= ord('z'):  # znak.islower():
            indeks = ord(znak) - ord('a')
        if znak in alfabet:
            indeks = alfabet.index(znak)
            zaszyfrowany_znak = szyfr[indeks]
            wynik += zaszyfrowany_znak
        else:
            wynik+=znak
    return wynik
