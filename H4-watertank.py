#H4 tehtävä 3: Peltojen tiedot tiedostosta
pinta={}
pinnat=[]
kasvit={}
kasvikset=[]
kylvöpäivät={}
päivät=[]
pellot=[]
rivit=[]
with open("tiedosto.txt") as file:
    
    for rivi in file:
        osat=rivi.split("\t")
        if osat[0]=="Pinta-ala":
            continue
        pinta["Pinta-ala"]=pinnat
        pinnat.append(osat[0])
        if osat[1]=="Kasvi":
            continue

        kasvit["Kasvit"]=kasvikset
        kasvikset.append(osat[1].lstrip())
        if osat[2]=="Pvm":
            continue

        kylvöpäivät["Kylvöpäivä"]=päivät
        päivät.append(osat[2].strip())
    
    pellot.append(pinta)
    pellot.append(kasvit)
    pellot.append(kylvöpäivät)
    for item in pellot:
        for avain,arvo in item.items():
            item[avain]=[arvo]
            for i in arvo:
               rivi=avain+":"+i
               rivit.append(rivi)
    L1=len(pinnat)+len(kasvikset) 
    for i in range(len(pinnat)):
        row=rivit[i]+" -- "+ rivit[len(pinnat)+i]+" -- "+ rivit[L1+i]
        print(row)
    print()    
    print(f"Yhteensä {len(pinnat)} peltoa.")    
