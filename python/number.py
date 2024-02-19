def numberSeeker ():
    addition=0
    listeNb = []
    for n in range (1,1000):
        nombre_str = str(n)
        for chiffre in nombre_str:
            listeNb.append(int(chiffre))
        if len(listeNb)>=2:
            if 1 not in listeNb and 7 not in listeNb:
                for n in range (len(listeNb)):
                    addition+=listeNb[n]
                if addition<=10:
                    if (listeNb[0]+listeNb[1])%2!=0 and listeNb[len(listeNb)-2]==4 and listeNb[len(listeNb)-1]==len(listeNb):
                        result = ''.join(map(str, listeNb))
                        return result

        listeNb=[]
        addition=0

mystery_number = numberSeeker ()

print('Le nombre mystère est le :',mystery_number)
