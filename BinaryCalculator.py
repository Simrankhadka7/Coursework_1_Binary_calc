from tkinter import *
import tkinter.messagebox
#Window 
window = Tk()

window.title("Simran's Binary Calculator")
window.geometry("480x350")
#Number get from Entry
numToConvert = IntVar()
#Ask for Decimal Number
numEntry = Entry(window, text=0, textvariable=numToConvert).grid(row=0,column=0)

#Dec To Binary

def decToBinary(decimalNumber):
    binaryNum = 0
    lastOne = 1
    while decimalNumber>0:
        binaryNum = binaryNum + ((decimalNumber%2)*lastOne)
        lastOne = lastOne*10
        decimalNumber = int(decimalNumber/2)
    return binaryNum
     
    
#Convert the Number
def convertMe():
    try:
        binaryNumber = decToBinary(int(numToConvert.get()))
        
        showNum = Label(window, text=binaryNumber).grid(row=1,column=0) 
    except Exception as e:
       tkinter.messagebox.showwarning("Value Error","Recheck Input")
        
#Convert Button
convertToBinary = Button(window, text="Convert",command=convertMe).grid(row=0,column=1)
#Add all inside window
window.mainloop()