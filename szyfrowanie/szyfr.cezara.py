#alfabet = ""
#for i in range (ord('a'), ord('z')):
#    alfabet+=(chr(i))
import random
alfabet = [chr(i) for i in range(ord('a'), ord('z')+1)] + list("ą,ć, ę,ł,ó, ź,ż")
def szyfruj (napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    wynik = ''
    for znak in napis:
        #if znak.islower():
      #  if ord ('a') <= ord(znak) <=ord('z'):
           #indeks = alfabet.index(znak)
       #    indeks = ord(znak) - ord('a')
        if znak in alfabet:
            #zaszyfrowany_znak = szyfr [indeks]
            indeks = alfabet.index(znak)
            zaszyfrowany_znak = szyfr[indeks]
            wynik += zaszyfrowany_znak
        else:
           wynik+=znak
    return wynik
def odszyfruj (napis,klucz):
    pass
if __name__== '__main__':
    napis = "Ala ma żółć"
    klucz=3

    zaszyfrowany_napis = szyfruj(napis, klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis= odszyfruj(zaszyfrowany_napis, klucz)
    print(odszyfrowany_napis)
