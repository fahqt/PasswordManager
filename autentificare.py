from Tkinter import *

#Conectarea la baza de date **TREBUIE GANDIT UN ALGORITM PENTRU STOCAREA NUMELUI SI PAROLEI OFFLINE**
def Autentificare(parola,user):
	if parola == str(conectare_baza_date(user)):
        	print "Felicitari parola este corecta!"
    	else:
		print "Parola sau user gresit!"

def conectare_baza_date(user):
    	import MySQLdb

    	query = "SELECT parola from tabel WHERE nume='"+ user +"'" 
    	#selecteaza parola userului 'user'

        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "parole")
    	cursor = conn.cursor()
    	cursor.execute(query)
    	parola = cursor.fetchone()[0]
    	#print parola
    	cursor.close()
    	conn.close()
    
    	return parola

program = Tk()

Label(program, text="Username").grid(row=0) #Crearea cutiei pentru introducerea numelui
Label(program, text="Parola").grid(row=1)

input1 = Entry(program) #Afisarea cutiilor
input2 = Entry(program)

input1.grid(row=0, column=1)
input2.grid(row=1, column=1)

Button(program, text="Conectare", command=Autentificare).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
