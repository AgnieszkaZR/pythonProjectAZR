def wyszukaj_naiwnie_v2(sprawdzany, szukany):
    for i in range (len(sprawdzany)-len(szukany)+1):
       znaleziono = True
       for j in range(len(szukany)):
           if not sprawdzany [i+j]==szukany [j]:
              znaleziono=True
              break
       if znaleziono:
           return i
    return None



if __name__=='__main__':
    sprawdzany = 'Ala ma tako'
    szukany = 'ko'
    print(wyszukaj_naiwnie_v2(sprawdzany,szukany))
