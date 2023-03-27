import random
import  json
import unicodedata

#load word file
liste_mots=[]
f=open("C:\\Users\Formation\python\pendu\Mots.json","r" ,encoding="utf-8-sig")
file=json.load(f)
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

#choose word type
for i in file["test"]:
    if i["type"]=="subst." or i["type"]=="adj." or i["type"]=="verbe":
        liste_mots.append(strip_accents(i["label"]))

#start again
relance=True
while relance==True:

    #set random word form word file
    selec_mot=random.randint(0,len(liste_mots))
    mot=liste_mots[selec_mot]

    tiret=""
    gagne=False
    tirets=[]
    life=6
    pendu=[["|","-","-","-","|",""],["|"," "," "," "," "," "],["|"," "," "," "," "," "],["|"," "," "," "," "," "],["|","_","_","_","_","_"]]
    affichage=""


    #show board
    for tab in pendu:
        affichage=""
        for char in tab:
            affichage+=char
        print(affichage)

    #show _ for each letter in random word
    for i in range(len(mot)):
        tirets.append("_")
        tiret+="_"
    print(tiret)


    #game loop
    while gagne==False and life!=0:
        print(f"entrez une lettre")
        letter_user=input()
        count=0

    #checking if letter in word
        for i in range(len(mot)):
            if letter_user=="cheat":
                print(mot)
            if len(letter_user)<1:
                print("pas assez de lettre")
                break
            elif len(letter_user)>1:
                print("trop de lettres")
                break

            if  (letter_user==mot[i] and letter_user!=tirets[i]):
                tirets[i]=mot[i]
                tiret=""
                for i in range(len(tirets)):
                    tiret+=tirets[i]
                    #tiret=tiret.replace(tiret[mot.index(mot[i])][2], mot_user[i],mot.count(mot_user[i]))
                    #tiret = tiret[:i] + mot_user[i] + tiret[i+1:]
            else:
                count+=1

        #error count and board update 
        if count==len(mot):
            print(life)
            life-=1
            match life:
                case 5:
                    pendu[1][4]="o"
                case 4:
                    pendu[2][4]="|"
                case 3:
                    pendu[2][3]="/"
                case 2:
                    pendu[2][5]="\\"
                case 1:
                    pendu[3][3]="/"
                case 0:
                    pendu[3][5]="\\"
                    print("perdu")
                    print(mot)
        
        for tab in pendu:
            affichage=""
            for char in tab:
                affichage+=char
            print(affichage)
        print(tiret)

        #win condition
        if tiret==mot or life==0:
            print("rejouer? oui/non")
            rejouer=input()
            if rejouer=="oui":
                relance=True
            else:
                relance=False
            gagne=True