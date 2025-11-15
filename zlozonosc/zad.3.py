def znajdz_indeksy (dane, suma):
    for i in range (len(dane)):
        for j in range (len(dane)):
            if i!=j:
                if dane [i] == suma:
                    return i, j
    return None

  #0(N) = N*2

def znajdz_indeksy_v2(dane, suma):
    for i in range (len(dane)):   #N
        for j in range (len(dane)):
                if dane [i] + dane [j] == suma:
                    return i, j

# T(N) = N(N-1)/2
# O(N) = N^2gg

dane = [3,7,9,12,19,30,41,56,71]
szukane_suma = 60

print(znajdz_indeksy_v2(dane, szukane_suma))
