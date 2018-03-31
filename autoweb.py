import browsewebs
import Langara
import films
from threading import Thread

def callfuncs(readin,f):
    if readin == 1 :
        Langara.d2l(f)
    elif readin == 2 :
        Langara.messagelang(f)
    elif readin == 4 :
        browsewebs.browsewebss(f)
    elif readin == 3 :
        Langara.mylangara(f)
    elif readin == 6 :
        dicty = films.getFilms(f)
        films.checkfilms(dicty)
        films.watchfilms(dicty)
    elif readin == 7 :
        Langara.C3(f)


f = open("AutoData.txt", "r+")

readin = int(input("enter the number \n 1 for d2l langara \n 2 for message langara \n 3 for mylangara \n 4 for websites \n 6 for checking films \n 7 for C3 Langara "))

if (readin < 10):
    callfuncs(readin, f)
elif (readin >10 ):
    while readin >= 1:
        f = open("AutoData.txt", "r+")
        t1 = Thread(target= callfuncs, args= (int(readin % 10),f,))
        readin = int(readin / 10)
        t1.start()
