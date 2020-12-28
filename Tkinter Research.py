from tkinter import *
import os
import time



root = Tk()




def myClick():
	myLabel= Label(root, text="Get Rick Rolled(☞ﾟヮﾟ)☞!")
	os.startfile('F:\prithviraj\COMPUTER\MY AUTOBOTS\PYBOT\dist\MisterTrollBot\MisterTrollBot.exe')
	myLabel.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick)
myButton.pack()

root.mainloop()