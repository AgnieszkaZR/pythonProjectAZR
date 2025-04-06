import math

def szyfruj(napis, klucz):
    kolumny = len(klucz)
    wiersze=math.ceil(len(napis)/len(klucz))
    rozmiar=kolumny*wiersze
    wiadomosc= napis + '_'* (rozmiar-len(napis))
    print(wiadomosc)

def odszyfruj(napis,klucz):
    pass

if __name__=='__main__':
    napis="Ala ma kota"
    klucz="pies"

    zaszyfrowany_napis= szyfruj(napis,klucz)

    odszyfrowany_napis= odszyfruj(napis,klucz)
