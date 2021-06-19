from tkinter import *
import random
import json
from timeit import default_timer as timer


root = Tk()
root.title("Key press")
root.geometry("1600x500")

global start, end

data = []
take_input = True
var = StringVar()
var.set('Press tab key,you can type now!!')
var2 = StringVar()
var2.set("You have not started the game yet")

# -----------------------------OPEN----------------------------------------#


with open("data.json") as file:
    contents = json.load(file)
    sentence = contents["sentence"]

givenString = random.choice(sentence)


# -------------------------------------------------CODE--------------------------#


def clicker(event):
    global take_input, data, start, end
    start = timer()
    print(event.char)
    if '\r' == event.char:
        take_input = False

    elif '\x08' == event.char:
        if len(data) == 0:
            pass
        else:
            data.pop()
            print(data)
            strings = "".join(data)
            var.set(strings)

    else:
        print(event.char)
        print(data)
        data.append(event.char)
        strings = "".join(data)
        var.set(strings)

    if not take_input:
        print("Comming out of for")
        string = "".join(data)
        print(f"The string is::{string}")
        print(f"The string is::{givenString}")
        if givenString == string:
            mylabel = Label(root, text="You were right without errors", font=("Arial", 20))
            mylabel.pack(padx=10, pady=10)
        else:
            mylabel = Label(root, text="There was an error", font=("Arial", 20))
            mylabel.pack()

    end = timer()
    return 0


def Timer():
    global start, end
    try:
        time_taken = end - start
        print(end)
        print(start)
        print(time_taken)
        time_taken = time_taken*100000
        label_x88 = Label(text=f"Your speed is {time_taken} seconds", font=("courier", 18, "bold"), fg="#064420")
        label_x88.pack()
    except NameError:
        label_x88 = Label(textvariable=var2, font=("courier", 18, "bold"), fg="#F54748")
        label_x88.pack()


# --------------------------------------------------UI-----------------------------------------------#

label_x2 = Label(text="Hi there..Let's play a speed test Game start with Tab key", font=("Arial", 20, "bold"), fg="#343A40" )
label_x2.pack(padx=10, pady=10)

label_x77 = Label(text="Rules\n 1.Don't enter backspace\n 2.No Cheating\n 3.Press enter when done", font=("Arial", 18, "italic"), fg="#D83A56")
label_x77.pack(padx=10, pady=10)

label_x78 = Label(text=givenString, font=("courier", 18, "bold"))
label_x78.pack(padx=10, pady=10, anchor=CENTER)

myButton = Button(root, text="Click ME")
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)

mylabel2 = Label(root, textvariable=var, font=("Arial", 20), fg="#7952B3")
mylabel2.pack()

myButton3 = Button(root, text="Check my speed", fg="#DA0037", command=Timer)
myButton3.pack()

root.mainloop()