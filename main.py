from tkinter import *
from fpdf import*
from tkinter.messagebox import *


def senddata():
    Dicoidentite = {
        "Nameschool" : "Campus RIERA",
        "prénom": txt_prénom.get(), "nom": txt_nom.get(), "classe": txt_classe.get(), "période": txt_période.get()
    }
    addpdf(Dicoidentite, ajoutnote)

def addpdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, text="période" )
    pdf.output('Pronote.pdf','F')
#----------------------------------------------------------------
window = Tk()
#Set up de la page
window.title("Création de bulletin")
window.geometry("1280x720")
window.minsize(1280,720)
window.maxsize(1280,720)
window.configure(bg="green")

listenote = [] #Création de la liste

#------------------------------------------------------------------

def alert():
    showinfo("Info","Cette application sert a créer un bulletin de note facilement et créer un pdf de ce bulletin !")

menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Enregistrer", command=alert)
menu1.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

window.config(menu=menubar)
#-----------------------------------------------------------
txt_prénom = StringVar()  #StringVar permet d'enregistrer le contenu qui est écrit dans texte dans une variable
prénom = Label(window, text = "Prénom : ")
prénom.place(x = 10, y = 10)
prénom.configure(bg="green")
i_prénom = Entry(window, bd = 5, textvariable=txt_prénom) #Toujours ajoutez le nom de la variable dans un texte variable
i_prénom.place(x = 70, y = 10)

#--------------------------------------------------------------------

txt_nom = StringVar()
nom = Label(window, text = "Nom : ")
nom.configure(bg="green")
nom.place(x = 225, y = 10)
i_nom = Entry(window, bd = 5, textvariable=txt_nom)
i_nom.place(x = 270, y = 10)

#-------------------------------------------------------

txt_classe = StringVar()
classe = Label(window, text = "Classe : ")
classe.configure(bg="green")
classe.place(x = 10, y = 70)
i_classe = Entry(window, bd = 5, textvariable=txt_classe)
i_classe.place(x = 70, y = 70)

#--------------------------------------------------------

txt_période = StringVar()
période = Label(window, text = "Période : ")
période.configure(bg="green")
période.place(x = 225, y = 70)
classe.configure(bg="green")
i_période= Entry(window, bd = 5, textvariable=txt_période)
i_période.place(x = 280, y = 70)

#-------------------------------------------------------------

txt_matière = StringVar()
matière = Label(window, text = "Matière : ")
matière.place(x = 425, y = 70)
matière.configure(bg="green")
i_matière = Entry(window, bd = 5, textvariable=txt_matière)
i_matière.place(x = 475, y = 70)

#-----------------------------------------------------------------

txt_professeur = StringVar()
professeur = Label(window, text = "Professeur : ")
professeur.place(x = 10, y = 125)
professeur.configure(bg="green")
i_prof = Entry(window, bd = 5, textvariable=txt_professeur)
i_prof.place(x = 80, y = 125)

#----------------------------------------------------------------

txt_moyenne = StringVar()
moyenne = Label(window, text = "Moyenne : ")
moyenne.place(x = 10, y = 180)
moyenne.configure(bg="green")
i_moyenne = Entry(window, bd = 5, textvariable=txt_moyenne)
i_moyenne.place(x = 70, y = 180)

#---------------------------------------------------------------

txt_apréciation = StringVar()
apréciation = Label(window, text = "Apréciation : ")
apréciation.place(x = 225, y = 180)
apréciation.configure(bg="green")
i_apréc = Entry(window, bd = 5, textvariable=txt_apréciation)
i_apréc.place(x = 300, y = 180)

#-------------------------------------------------------

photo = PhotoImage(file="Logo-pronote-menu.png")    #Création d'une image via Canvas pour le coup c'est une image Pronote mais il reste quelque soucis que je n'ai pas corriger

canvas = Canvas(window,width=900, height=900)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.place(x = 1000, y = 10)
canvas.configure(bg="green")

#---------------------------------------------------------


def ajoutnote(): #Nous déffinisson notre fonction en créant un dictionnaire et en y insérant nos variable avec get, après cela il faut insérez via le .append le dictionnaire dans la liste qui a était créer en début de code
    Dico = {
        "matière":txt_matière.get(),"professeur":txt_professeur.get(),"appréciation":txt_apréciation.get()
    }
    listenote.append(Dico)
    print(listenote)

Bouton_print = Button(text="Ajoutez une note !", command=ajoutnote) #On créer un bouton et on lui ajoute notre fonction créer au dessus
Bouton_print.place(x = 600, y = 300)

Bouton_PFD = Button (text="Créez le PDF !", command=senddata)
Bouton_PFD.place(x = 1000, y = 500)

window.mainloop()