def szokoz(szoveg):
    db=0
    for i in range(0,len(szoveg)-1):
        if szoveg[i]==" ":
            db+=1
    return db
def szovegfeladat(szoveg):
    szokoznelkul:str=""
    for i in range(0,len(szoveg)-1):
        if szoveg[i]!=" ":
            szokoznelkul+=szoveg[i]
    print(szokoznelkul)
def szovegfeladat2(szoveg):
    szovegkicsi:str=szoveg.lower()
    for i in range (0,len(szovegkicsi)):
        if szovegkicsi[i]=="é"or "á" or "ű" or "ő" or "ú" or "ó":
            if szovegkicsi[i]=="é":
                szovegkicsi=szovegkicsi.replace("é","e")

    print(szovegkicsi)