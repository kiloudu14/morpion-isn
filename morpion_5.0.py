#Alexandre Travers
#Joshua FlÃƒÂ©cheau
#Kilian Jospin
#TS3

from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import random

def NO(event):
    global case_NO,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_NO=Canvas(quadriage,width=95,height=110,bg="#d18412")
        case_NO.create_image(0,0,anchor=NW,image=imgmr)
        case_NO.grid(row=0,column=0,sticky=NW)
    return case_NO

def N(event):
    global case_N,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_N=Canvas(quadriage,width=95,height=110,bg='#ffc342')
        case_N.create_image(0,0,anchor=NW,image=imgmr)
        case_N.grid(row=0,column=1,sticky=NW)
    return case_N

def NE(event):
    global case_NE,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_NE=Canvas(quadriage,width=95,height=110,bg="#d18412")
        case_NE.create_image(0,0,anchor=NW,image=imgmr)
        case_NE.grid(row=0,column=2,sticky=NW)
    return case_NE

def O(event):
    global case_O,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_O=Canvas(quadriage,width=95,height=110,bg='#ffc342')
        case_O.create_image(0,0,anchor=NW,image=imgmr)
        case_O.grid(row=1,column=0,sticky=NW)
    return case_O

def C(event):
    global case_C,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_C=Canvas(quadriage,width=95,height=110,bg="#d18412")
        case_C.create_image(0,0,anchor=NW,image=imgmr)
        case_C.grid(row=1,column=1,sticky=NW)
    return case_C

def E(event):
    global case_E,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_E=Canvas(quadriage,width=95,height=110,bg='#ffc342')
        case_E.create_image(0,0,anchor=NW,image=imgmr)
        case_E.grid(row=1,column=2,sticky=NW)
    return case_E

def SO(event):
    global case_SO,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_SO=Canvas(quadriage,width=95,height=110,bg="#d18412")
        case_SO.create_image(0,0,anchor=NW,image=imgmr)
        case_SO.grid(row=2,column=0,sticky=NW)
    return case_SO

def S(event):
    global case_S,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_S=Canvas(quadriage,width=95,height=110,bg='#ffc342')
        case_S.create_image(0,0,anchor=NW,image=imgmr)
        case_S.grid(row=2,column=1,sticky=NW)
    return case_S

def SE(event):
    global case_SE,quadriage,imgmr
    souris=event.num
    if souris==1:
        case_SE=Canvas(quadriage,width=95,height=110,bg="#d18412")
        case_SE.create_image(0,0,anchor=NW,image=imgmr)
        case_SE.grid(row=2,column=2,sticky=NW)
    return case_SE

"""def jouer():
    global playerturn
    if playerturn == 0:
        case_NO=Button(quadriage,width=45,height=45)
        img = PhotoImage(file='mariorougepetit.png')
        case_NO.create_image(image=img)
        case_NO.grid(row=0,column=0)
        playerturn = 1
    elif playerturn == 1:
        img = PhotoImage(file='mariorougepetit.png')
        case_NO=Button(quadriage,state='disable',image=img)
        case_NO.grid(row=0,column=0)
        playerturn = 0"""

"""def gagnant():
    global score1
    global score2
    score1 = 0
    score2 = 0
    player1 = 15
    if player1 == 15:
        score1 = score1 + 3
    elif player2 == 3:
        score2 = score2 + 3
    else:
        score1 = score1 + 1
        score2 = score2 + 1
    Texte.set('Score : ' + str(score1) + ' - ' + str(score2))"""

def jeu():
    global case_NO,case_N,case_NE,case_O,case_C,case_E,case_SO,case_S,case_SE,playerturn,quadriage,imgmr
    playerturn = random.randint(0,1)
    fenetre.destroy()      #destruction de l'image du menu
    fenetre2=Tk()
    fenetre2.title("Tic Tac Toe")
    fenetre2.geometry('700x500+200+100')
    fenetre2.configure(bg='brown')

    quadriage=Canvas(fenetre2,width=300,height=300,bg="#ffffff")       #crÃ©ation du plateau du morpion
    quadriage.pack()
    case_NO=Canvas(quadriage, width=95, height=110, bg="#d18412")
    case_NO.focus_set()
    case_NO.bind("<Button-1>", NO)
    case_NO.grid(row=0,column=0)
    case_N=Canvas(quadriage, width=95, height=110, bg="#ffc342")
    case_N.focus_set()
    case_N.bind("<Button-1>", N)
    case_N.grid(row=0,column=1)
    case_NE=Canvas(quadriage, width=95, height=110, bg="#d18412")
    case_NE.focus_set()
    case_NE.bind("<Button-1>", NE)
    case_NE.grid(row=0,column=2)
    case_O=Canvas(quadriage, width=95, height=110, bg="#ffc342")
    case_O.focus_set()
    case_O.bind("<Button-1>", O)
    case_O.grid(row=1,column=0)
    case_C=Canvas(quadriage, width=95, height=110, bg="#d18412")
    case_C.focus_set()
    case_C.bind("<Button-1>", C)
    case_C.grid(row=1,column=1)
    case_E=Canvas(quadriage, width=95, height=110, bg="#ffc342")
    case_E.focus_set()
    case_E.bind("<Button-1>", E)
    case_E.grid(row=1,column=2)
    case_SO=Canvas(quadriage, width=95, height=110, bg="#d18412")
    case_SO.focus_set()
    case_SO.bind("<Button-1>", SO)
    case_SO.grid(row=2,column=0)
    case_S=Canvas(quadriage, width=95, height=110, bg="#ffc342")
    case_S.focus_set()
    case_S.bind("<Button-1>", S)
    case_S.grid(row=2,column=1)
    case_SE=Canvas(quadriage, width=95, height=110, bg="#d18412")
    case_SE.focus_set()
    case_SE.bind("<Button-1>", SE)
    case_SE.grid(row=2,column=2)
    """case_NO=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#d18412',activebackground='#d18412',command=jouer).grid(row=0,column=0)
    case_N=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#ffc342').grid(row=0,column=1)
    case_NE=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#d18412',activebackground='#d18412').grid(row=0,column=2)
    case_O=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#ffc342').grid(row=1,column=0)
    case_C=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#d18412',activebackground='#d18412').grid(row=1,column=1)
    case_E=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#ffc342').grid(row=1,column=2)
    case_SO=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#d18412',activebackground='#d18412').grid(row=2,column=0)
    case_S=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#ffc342').grid(row=2,column=1)
    case_SE=Button(quadriage,padx=45,pady=45,cursor ='hand2',bg='#d18412',activebackground='#d18412').grid(row=2,column=2)"""


    imgmr=PhotoImage(file="mariorougepetit.png")                      #crÃ©ation d'un canevas pour le mario rouge
    mario_rouge=Canvas(fenetre2,width=125,height=125)
    pile_mario_rouge=mario_rouge.create_image(10,0,anchor=NW,image=imgmr)
    mario_rouge.place(x=0,y=0)

    imgmv=PhotoImage(file="mariovertpetit.png")                       #crÃ©ation d'un canevas pour le mario vert
    mario_vert=Canvas(fenetre2,width=125,height=125)
    pile_mario_vert=mario_vert.create_image(10,0,anchor=NW,image=imgmv)
    mario_vert.place(x=575,y=0)

    """score = Label(fenetre2, textvariable=Texte)
    score.place(x=240,y=400)"""

    score=StringVar()                                                #crÃ©ation d'un canevas pour afficher le score
    score=Label(fenetre2, text="Score : 0 - 0",font="Arial 32")
    score.place(x=240,y=400)

    fenetre2.mainloop()


#crÃƒÂ©ation de la fenÃƒÂªtre principale avec comme nom Tic Tac Toe et comme dimension ('Lxh+x+y')
fenetre=Tk()
fenetre.title('Tic Tac Toe')
fenetre.geometry('600x500+200+100')

fenetre2=Frame(fenetre,width=600,height=500,bg='brown')
fenetre2.pack(fill=BOTH,expand=1)

widget=Frame(fenetre2,background='brown')
widget.pack(side=LEFT)
imgr=PhotoImage(file='mariorouge.png')
widget2=Canvas(fenetre2,width=400,height=500,bg='#e5bc42')
widget2.create_image(200,200,image=imgr)
widget2.create_text(200,460,text='Tic Tac Toe',font='Arial 32')
widget2.pack(side=RIGHT)

#crÃƒÂ©ation boutons
joueur1=Button(widget,text='1 Joueur',bg='#00ffff',cursor ="hand2",width=10,command=jeu)
joueur1.pack(padx=70,pady=2)
joueur2=Button(widget,text='2 Joueurs',bg='#00ffff',cursor="hand2",width=10,command=jeu)
joueur2.pack(padx=70,pady=2)

fenetre.mainloop()