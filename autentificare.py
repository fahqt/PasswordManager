from Tkinter import *

#Conectarea la baza de date **TREBUIE GANDIT UN ALGORITM PENTRU STOCAREA NUMELUI SI PAROLEI OFFLINE**
def Autentificare():
	print "Nume: " + input1.get() + "\nParola: " + input2.get()

program = Tk()

Label(program, text="Username").grid(row=0) #Crearea cutiei pentru introducerea numelui
Label(program, text="Parola").grid(row=1)

input1 = Entry(program) #Afisarea cutiilor
input2 = Entry(program)

input1.grid(row=0, column=1)
input2.grid(row=1, column=1)

Button(program, text="Conectare", command=Autentificare).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
