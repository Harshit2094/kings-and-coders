from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import game


window = Tk()
window.title('Hangman')
guesses = []


photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]


def newGame():
	global the_word_withSpaces
	global numberOfGuesses
	numberOfGuesses = 0
	wurd = game.generate_phrase()
	print(wurd)
	hint = game.get_hint(wurd)
	the_word = (wurd.lower()).rstrip('.')
	the_word_withSpaces = " ".join(the_word)
	lblWord.set(' '.join("_" * len(the_word)))
	hint_label.set(f"Hint: {hint}")
	tries_label.config(text=f"Tries left: {11 - numberOfGuesses}") 
	imgLabel.config(image=photos[0])


def guess(letter):
	global numberOfGuesses
	if numberOfGuesses<11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Hangman","You guessed it!")
			guesses.append(letter)
		else:
			if letter not in guesses:
				numberOfGuesses += 1
				imgLabel.config(image=photos[numberOfGuesses])
				if numberOfGuesses==11:
						messagebox.showwarning("Hangman","Game Over")
			guesses.append(letter)
	tries_label.config(text=f"Tries left: {11 - numberOfGuesses}")


imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

tries_label = Label(window, font=('Helvetica 18'))
tries_label.grid(row=5, column=0, columnspan=9)

hint_label = StringVar()
Label(window, textvariable=hint_label, font=('Helvetica 18')).grid(row=4, column=0, columnspan=9)
  
lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c.lower()), font=('Helvetica 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8)

newGame()
window.mainloop()