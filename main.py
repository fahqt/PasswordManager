from Tkinter import *
from tkFileDialog import askopenfilename

program = Tk()

program.geometry("600x500")

def citire_fisier(parole_manager):
    	fisier = open(parole_manager , "a+")
    	text = fisier.read()
    	file.close()
    	return text
    
def scriere_fisier(parole_manager):
    	fisier = open(parole_manager , "a+")
    	text = fisier.write(parole_manager)
    	file.close()
   	return text

def FisierNou():
	print "Fisier Nou"

def DeschideFisier():
	nume = askopenfilename()
	print nume

def Despre():
	print "Descriere descriere descriererererereeree"

meniu = Menu(program)
program.config(menu=meniu)
afisaremeniu = Menu(meniu)
meniu.add_cascade(label="Fisier", menu=afisaremeniu)
afisaremeniu.add_command(label="Nou", command=FisierNou)
afisaremeniu.add_command(label="Deschide un fisier", command=DeschideFisier)
afisaremeniu.add_separator()
afisaremeniu.add_command(label="Inchide Programul", command=program.quit)

despre = Menu(meniu)
meniu.add_cascade(label="Despre", menu=despre)
despre.add_command(label="Despre", command=Despre)

mainloop()
