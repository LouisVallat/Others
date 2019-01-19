from pokedata import CTF
POKEMON={}
for i in range(len(CTF)):
    if CTF[i]["name"] in POKEMON.keys():
        POKEMON[CTF[i]["name"]]=POKEMON[CTF[i]["name"]]+CTF[i]["dollars"]
    else:
        POKEMON[CTF[i]["name"]]=CTF[i]["dollars"]

maxi=0
nomMax=""
for nom in POKEMON.keys():
    if POKEMON[nom] > maxi:
        maxi, nomMax=POKEMON[nom], nom

print(nomMax + str(maxi))