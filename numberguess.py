from tkinter import  *
import random  
number = random.randint(0, 10)
tries = 0
root = Tk()
root.geometry("700x500")
root.title("Guess The Number")
Label(root , text = "Welcome to Guess The Number \n have fun! " , font = "arial 20 bold").pack()

name = Label(root , text = "Enter your name", font = "arial 13 bold").place(x = 130 , y = 200)

#Tkinter variable for storing value
namevalue = StringVar()

#Entries
nameentry = Entry(root , textvariable = namevalue , font = "arial 13 bold")

#packing the entry
nameentry.place(x = 280 , y = 200)

def first():

    #new window
    fir = Tk()
    fir.geometry("600x300")
    fir.title("Welcome")
    Label(fir , text = ('Hello! '+ str(nameentry.get()) +' \n \n \nWould you like to Play?' ) , font = "arial 15 bold").place(x = 180 , y = 40)
    

    def yes(): # if user choose yes

        ys = Tk()
        ys.geometry("700x500")
        ys.title("Let\'s Play..")
        
        Label(ys , text = ("I\'m thinking a number between 1 and 10" ), font = "arial 11 bold").place(x = 180 , y = 50)
        Label(ys , text = ("You have to guess a number in three tries") , font = "arial 11 bold").place(x = 180 , y = 100)

        guess = Label(ys , text = "Guess a number", font = "arial 12 bold").place(x = 130 , y = 200)

        #Enter variable for storing value
        guessvalue = IntVar()

        #Entries
        guessentry = Entry(ys , textvariable = guessvalue , font = "arial 10 bold")

        #packing the entry
        guessentry.place(x = 280 , y = 200)

        def cont():

            ct = Tk()
            ct.geometry("700x500")
            ct.title("continue...")
            global tries
            global number
            
        
                  
            tries = tries + 1

            if int(guessentry.get()) > number:
                Label(ct , text = ("Enter number is: " + str(guessentry.get()) + " and Tries: "+ str(tries)) , font = "arial 14 bold").place(x = 130 , y = 150)
                Label(ct , text = ("Guess Lower....") , font = "arial 11 bold").place(x = 130 , y = 200)
                Button(ct , text = "Try Again.." , command = lambda:[yes() , ct.destroy()] , font = "arial 12 bold").place(x = 200 , y = 270 )

            if int(guessentry.get()) < number :
                Label(ct , text = ("Enter number is: " + str(guessentry.get()) + " and Tries: "+ str(tries)) , font = "arial 14 bold").place(x = 130 , y = 150)
                Label(ct , text = ("Guess Higher....") , font = "arial 11 bold").place(x = 130 , y = 200)
                Button(ct , text = "Try Again.." , command = lambda:[yes() , ct.destroy()] , font = "arial 12 bold").place(x = 200 , y = 270 )

            if int(guessentry.get()) == number:
                Label(ct , text = ("Congratulations! You won!! \n Number of tries : "+str(tries)) , font = "arial 11 bold").place(x = 130 , y = 200)
                tries = 0
                number = random.randint(0, 10)
                Button(ct , text = "Play Again.." , command = lambda:[yes() , ct.destroy()] , font = "arial 12 bold").place(x = 200 , y = 270 )
                Button(ct , text = "Quit...." , command = lambda: ct.destroy() , font = "arial 12 bold").place(x = 350 , y = 270 )
            
            if tries >= 3:
                Label(ct , text = ("OOPPSSS ! You Lost..." ), font = "arial 11 bold").place(x = 130 , y = 200)
                tries = 0
                number = random.randint(0, 10)
                Button(ct , text = "Play Again.." , command = lambda:[yes() , ct.destroy()] , font = "arial 12 bold").place(x = 200 , y = 270 )
                Button(ct , text = "Quit...." , command = lambda: ct.destroy() , font = "arial 12 bold").place(x = 350 , y = 270 )

            
        Button(ys , text = "Enter" , command = lambda:[cont() , ys.destroy()] , font = "arial 12 bold").place(x = 200 , y = 270 )

    def no(): #if user choose no

        no = Tk()
        no.geometry("400x200")
        no.title("Thank you")
        Label(no , text = "Thank You!" , font = "arial 16 bold" ).place(x = 150  ,  y = 50)
        Button(no , text = "CLOSE" , command = lambda: no.destroy() , font = "arial 12 bold").place(x = 180 , y = 150 )



    Button(fir , text = "YES" , command = lambda:[yes() , fir.destroy()] , font = "arial 12 bold").place(x = 180 , y = 240 )

    Button(fir , text = "NO" , command = lambda:[no() , fir.destroy()] , font = "arial 12 bold").place(x = 350 , y = 240 )



Button(root , text = "Enter" , command = lambda:[first() , root.destroy()] , font = "arial 12 bold").place(x = 260 , y = 290)
root.mainloop()