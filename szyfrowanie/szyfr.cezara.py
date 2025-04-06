#alfabet = ""
#for i in range (ord('a'), ord('z')):
#    alfabet+=(chr(i))

alfabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
def szyfruj (napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    print(szyfr)
    wynik = ''
    for znak in napis:
        #if znak.islower():
        if ord ('a') <= ord(znak) <=ord('z'):
           #indeks = alfabet.index(znak)
           indeks = ord(znak) - ord('a')
           zaszyfrowany_znak = szyfr [indeks]
           wynik+=zaszyfrowany_znak
        else:
           wynik+=znak
    return wynik
def odszyfruj (napis,klucz):
    pass
if __name__== '__main__':
    napis = 'Ala ma kota'
    klucz=3

    zaszyfrowany_napis = szyfruj (napis, klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis= odszyfruj(zaszyfrowany_napis, klucz)
    print(odszyfrowany_napis)
