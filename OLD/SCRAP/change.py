from tkinter import *
# import other necessery modules
import random
import time
import datetime
# creating root object
root = Tk()
# defining size of window
# root.geometry("1300x6200")
root.geometry("1920x1080")
# setting up the title of window
root.title("Message Encryption and Decryption")
root.configure(bg='#b3acf2')
Tops = Frame(root, width = 2600, relief = SUNKEN)
Tops.pack(side = TOP)
f1 = Frame(root, width = 800, height = 700, relief = SUNKEN, bg='#b3acf2')
# f1 = Frame(root, width = 1000, height = 1400, relief = SUNKEN)
f1.pack(side = BOTTOM)
# ==============================================
# TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), text = "Caesar Cipher", fg = "Black", bd = 10, anchor='w')
lblInfo.grid(row = 0, column = 0)
# lblInfo.config(bg="#b3acf2")
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text = localtime, fg = "black", bd = 10, anchor = 'w')
lblInfo.grid(row = 7, column = 0)
# lblInfo.config(bg="#b3acf2")
rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
# exit function
def qExit():
    root.destroy()
# Function to reset the window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
# reference
lblReference = Label(f1, font = ('arial', 16, 'bold'), text = "Name :",width=7, bd = 16, anchor = "w")
lblReference.grid(row = 0, column = 0)
lblReference.configure(bg='#b3acf2')
txtReference = Entry(f1, font = ('arial', 16, 'bold'), textvariable = rand, bd = 10, insertwidth = 4, bg = "white", justify = 'left')
txtReference.grid(row = 0, column = 1)
# txtReference.configure(bg='#b3acf2')
# labels
lblmode = Label(f1, font = ('arial', 16, 'bold'), text = "Mode :\n(e = encrypt, d = decrypt)", bd = 16, anchor = "w")
lblmode.grid(row = 0, column = 4)
lblmode.configure(bg='#b3acf2')
txtmode = Entry(f1, font = ('arial', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, width=5, bg = "white", justify = 'center')
txtmode.grid(row = 0, column = 5)
# txtmode.configure(bg='#b3acf2')

lblkey = Label(f1, font = ('arial', 16, 'bold'), text = "Key :", width=10, bd = 16, anchor = "w")
lblkey.grid(row = 1, column = 2)
lblkey.configure(bg='#b3acf2')
txtkey = Entry(f1, font = ('arial', 16, 'bold'), textvariable = key, bd = 10 , insertwidth = 4, bg = "white", justify = 'center')
txtkey.grid(row = 1, column = 3)

lblMsg = Label(f1, font = ('arial', 16, 'bold'), text = "Message :", bd = 16,width=10, anchor = "w")
lblMsg.grid(row = 2,columnspan=2, column = 0)
lblMsg.configure(bg='#b3acf2')
txtMsg = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Msg, bd = 10, insertwidth = 4, width=30, bg = "white", justify = 'left')
# txtMsg.grid(row = 2, column = 1)
txtMsg.grid(row = 3, rowspan=2, columnspan=2,column = 0)

lblService = Label(f1, font = ('arial', 16, 'bold'), text = "The Result :", bd = 16, anchor = "w")
lblService.grid(row = 2,columnspan=2, column = 4)
lblService.configure(bg='#b3acf2')
txtService = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4, width=30, bg = "white", justify = 'left')
txtService.grid(row = 3,columnspan=2, column = 4)
# Vigenère cipher
import base64
# Function to encode
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
# Function to decode
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)

    return "".join(dec)

def Ref():
    print("Message= ", (Msg.get()))
    clear = Msg.get()
    k = key.get()
    m = mode.get()
    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
fg = "black", font = ('arial', 16, 'bold'),
width = 10, text = "Reset", bg = "green",
command = Reset).grid(row = 8,  columnspan=2, column = 0)

# Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
font = ('arial', 16, 'bold'), width = 10,
text = "Show Message", bg = "yellow",
command = Ref).grid(row = 7, columnspan=2, column = 2)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
fg = "black", font = ('arial', 16, 'bold'),
width = 10, text = "Exit", bg = "red",
command = qExit).grid(row = 8,  columnspan=2, column = 4)


# keeps window alive
root.mainloop()
