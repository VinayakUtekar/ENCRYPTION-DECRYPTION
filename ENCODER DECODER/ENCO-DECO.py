from cProfile import label
from cgitb import text
from tkinter import *
# import other necessery modules
import random
import time
import datetime
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from numpy import char, chararray
from tkinter import messagebox
from tkinter.filedialog import *
#from new import Encode

# creating root object
root = Tk()
# defining size of window
root.geometry("1920x1080")
# setting up the title of window
root.title("Encryption and Decryption")
root.config(bg='#b3acf2')

Tops = Frame(root, width = 2600, relief = SUNKEN, bg='#b3acf2')
Tops.pack(side = TOP)
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), bg='#b3acf2', text = "", fg = "Black", bd = 10, anchor='w')
lblInfo.grid(row = 0, column = 0)
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), text = "Encoder - Decoder", fg = "Black", bd = 10, anchor='w')
lblInfo.grid(row = 1, column = 0)


def windowForTextCipher():
     # Destroying optional window
     root.destroy()
     # Creating new window for text ciphering
     Screen = Tk()
     Screen.geometry("1920x1080")
     Screen.title("Encryption and Decryption | Caesar Cipher")
     Screen.config(bg='#b3acf2')

     # Creating table frame to contain rows and columns
     Tops = Frame(Screen, width = 2600, relief = SUNKEN)
     Tops.pack(side = TOP)
     f1 = Frame(Screen, width = 800, height = 700, relief = SUNKEN, bg='#b3acf2')
     f1.pack(side = BOTTOM)

     # ==============================================
     # TIME
     # ==============================================
     localtime = time.asctime(time.localtime(time.time()))
     lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), text = "Caesar Cipher", fg = "Black", bd = 10, anchor='w')
     lblInfo.grid(row = 0, column = 0)
     lblInfo = Label(Tops, font=('arial', 20, 'bold'), text = localtime, fg = "black", bd = 10, anchor = 'w')
     lblInfo.grid(row = 7, column = 0)
     rand = StringVar()
     Msg = StringVar()
     key = StringVar()
     mode = StringVar()
     Result = StringVar()

     # exit function
     def qExit():
          Screen.destroy()

     # Function to reset the window
     def Reset():
          rand.set("")
          Msg.set("")
          key.set("")
          mode.set("")
          Result.set("")

     # Column for Name 
     lblReference = Label(f1, font = ('arial', 16, 'bold'), text = "Name :",width=7, bd = 16, anchor = "w")
     lblReference.grid(row = 0, column = 0)
     lblReference.configure(bg='#b3acf2')
     # Column for Name input
     txtReference = Entry(f1, font = ('arial', 16, 'bold'), textvariable = rand, bd = 10, insertwidth = 4, bg = "white", justify = 'left')
     txtReference.grid(row = 0, column = 1)

     # Column for mode
     lblmode = Label(f1, font = ('arial', 16, 'bold'), text = "Mode :\n(e = encrypt, d = decrypt)", bd = 16, anchor = "w")
     lblmode.grid(row = 0, column = 4)
     lblmode.configure(bg='#b3acf2')
     # Column for mode input
     txtmode = Entry(f1, font = ('arial', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, width=5, bg = "white", justify = 'center')
     txtmode.grid(row = 0, column = 5)

     #  Column for key   
     lblkey = Label(f1, font = ('arial', 16, 'bold'), text = "Key :", width=10, bd = 16, anchor = "w")
     lblkey.grid(row = 1, column = 2)
     lblkey.configure(bg='#b3acf2')
     #  Column for key input
     txtkey = Entry(f1, font = ('arial', 16, 'bold'), textvariable = key, bd = 10 , insertwidth = 4, bg = "white", justify = 'center')
     txtkey.grid(row = 1, column = 3)

     #  Column for message
     lblMsg = Label(f1, font = ('arial', 16, 'bold'), text = "Message :", bd = 16,width=10, anchor = "w")
     lblMsg.grid(row = 2,columnspan=2, column = 0)
     lblMsg.configure(bg='#b3acf2')
     #  Column for message input
     txtMsg = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Msg, bd = 10, insertwidth = 4, width=30, bg = "white", justify = 'left')
     txtMsg.grid(row = 3, columnspan=2,column = 0)

     #  Column for result 
     lblService = Label(f1, font = ('arial', 16, 'bold'), text = "The Result :", bd = 16, anchor = "w")
     lblService.grid(row = 2, columnspan=2, column = 4)
     lblService.configure(bg='#b3acf2')
     #  Column for result output
     txtService = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4, width=30, bg = "white", justify = 'left')
     txtService.grid(row = 3,columnspan=2, column = 4)

     # Function for encrypting message
     def encrypt(key, text):
          specialChar = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
          result = ""
          for i in range(len(text)):
               ch = text[i]
               # Encrypt uppercase characters
               if (ch.isupper()):
                    result += chr((ord(ch) + key-65) % 26 + 65)
               #Numerical values
               elif (ord(ch) >= 48 and ord(ch) <= 57):
                    result += chr((ord(ch) + key+10) % 10 + 48)
               # Encrypt special characters
               elif(ch in specialChar):
                    newChar = (specialChar.index(ch)+key)%33
                    result += specialChar[newChar]
               # Encrypt lowercase characters
               elif (ch.islower()):
                    result += chr((ord(ch) + key-97) % 26 + 97)    
          return result

     # Function for decrypting message
     def decrypt(key,text):
          specialChar = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
          result = ""
          # traverse text
          for i in range(len(text)):
               ch = text[i]
               # Decrypt uppercase characters
               if (ch.isupper()):
                    result += chr((ord(ch) - key-65) % 26 + 65)
               # Decrypt Numerical  values
               elif (ord(ch) >= 48 and ord(ch) <= 57):
                    result += chr(((ord(ch) - key+10) % 10 + 48)-6)
               # Decrypt special characters
               elif(ch in specialChar):
                    newChar = (specialChar.index(ch)-key)%33
                    result += specialChar[newChar]
               # Decrypt lowercase characters
               elif(ch.islower()):
                    result += chr((ord(ch) - key-97) % 26 + 97)

          return result

     # Function to check whether to encrypt or decrypt text based on 'mode' input
     def Ref():
          clear = Msg.get()
          k = int(key.get())
          m = mode.get()
          if (m == 'e'):
               Result.set(encrypt(k, clear))
          else:
               Result.set(decrypt(k, clear))
          
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


def windowForImageCipher():
     # Deleting optional window
     root.destroy()
     # Creating new window
     Screen = Tk()
     Screen.geometry("1920x1080")
     Screen.title("Encryption and Decryption | Image Steganography")
     Screen.config(bg='#b3acf2')

     # Creating frames 
     Tops = Frame(Screen, width = 2600, relief = SUNKEN,  bg='#b3acf2')
     Tops.pack(side = TOP)
     f1 = Frame(Screen, width = 800, height = 700, relief = SUNKEN, bg='#b3acf2')
     f1.pack(side = BOTTOM)
     Msg = StringVar()
     addr = StringVar()
     mode = StringVar()
     Result = StringVar()

     # Function to check whether to encrypt or decrypt text based on 'mode' input
     def Ref():
          userMessage = Msg.get()
          fileAddr = addr.get()
          m = mode.get()
          if (m == 'e'): 
               Encode(userMessage, fileAddr)
          else:
               Result.set(Decode(fileAddr))

     #  Function to browse file and store it's into a variable as string
     def OpenFile():
          global FileOpen
          FileOpen=StringVar()
          FileOpen = askopenfilename(initialdir ="/Desktop",title="SelectFile",filetypes=(("only jpeg files","jpg"),("all type of files",".*")))
          addr.set(FileOpen)

     # Function to encode text into image
     def Encode(userMessge, fileAddr):
          Response = messagebox.askyesno("PopUp","Do you want to encode the image?")
          if Response == 1:
               stg.hide(FileOpen,fileAddr+".jpg",userMessge)
               messagebox.showinfo("Pop Up","Successfully Encoded")
          else:
               messagebox.showwarning("Pop Up","Unsuccessful, please try again")

     # Function to decode image into text
     def Decode(fileAddr):
          Message=stg.reveal(fileAddr)
          return Message      

     # Column for Heading
     lblInfo = Label(Tops, font = ('helvetica', 45, 'bold'), bg='#b3acf2', text = "", fg = "Black", bd = 10, anchor='w')
     lblInfo.grid(row = 0, column = 0)
     lblInfo = Label(Tops, font = ('helvetica', 45, 'bold'), text = "Image Steganography", fg = "Black", bd = 10, anchor='w')
     lblInfo.grid(row = 1, column = 0)
 
     # Column for Message
     lblReference = Label(f1, font = ('arial', 16, 'bold'), text = "Message :", width=7, bd = 16, anchor = "w")
     lblReference.grid(row = 0, column = 0)
     lblReference.configure(bg='#b3acf2')

     # Column for Message Input
     txtReference = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Msg, bd = 10, insertwidth = 4, bg = "white", justify = 'left')
     txtReference.grid(row = 0, column = 1)

     # Column for Mode
     lblmode = Label(f1, font = ('arial', 16, 'bold'), text = "Mode :\n(e = encrypt, d = decrypt)", bd = 16, anchor = "w")
     lblmode.grid(row = 0, column = 5)
     lblmode.configure(bg='#b3acf2')
     # Column for Mode Input
     txtmode = Entry(f1, font = ('arial', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, width=5, bg = "white", justify = 'center')
     txtmode.grid(row = 0, column = 6)

     searchFile = Button(f1, padx = 5, pady = 3, bd = 5, fg = "black",
     font = ('arial', 16, 'bold'), width = 10,
     text = "Search file", bg = "yellow",
     command = OpenFile).grid(row = 1, column = 0)

     # 2 Empty columns for blank spaces
     emptylabel = Label(f1, font = ('arial', 16, 'bold'), text = "",width=10,  bd = 16, anchor = "w")
     emptylabel.grid(row = 0, column = 3)
     emptylabel.configure(bg='#b3acf2')
     emptylabel1 = Label(f1, font = ('arial', 16, 'bold'), text = "", bd = 16, anchor = "w")
     emptylabel1.grid(row = 0, column = 4)
     emptylabel1.configure(bg='#b3acf2')                    

     # Column for file name display
     addrReference = Entry(f1, font = ('arial', 16, 'bold'), textvariable = addr, justify = 'left')
     addrReference.grid(row = 1, column = 1)

     # Empty column for blank spaces
     emptylabel2 = Label(f1, font = ('arial', 16, 'bold'), text = "", bd = 16, anchor = "w")
     emptylabel2.grid(row = 2, column = 0)
     emptylabel2.configure(bg='#b3acf2')
     emptylabel3 = Label(f1, font = ('arial', 16, 'bold'), text = "",width=10,  bd = 16, anchor = "w")
     emptylabel3.grid(row = 3, column = 0)
     emptylabel3.configure(bg='#b3acf2')

     processIntr = Button(f1, padx = 5, pady = 3, bd = 5, fg = "black",
     font = ('arial', 16, 'bold'), width = 10,
     text = "Go", bg = "green",
     command = Ref).grid(row = 4, column = 0)

     # Column for show result
     showResult = Label(f1, font = ('arial', 16, 'bold'), text = "Result :", bd = 16, anchor = "w")
     showResult.grid(row = 4,  column = 4)
     showResult.configure(bg='#b3acf2')

     # Column for show result output
     resultMessage = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4, width=30, bg = "white", justify = 'left')
     resultMessage.grid(row = 4, columnspan= 2, column = 5)

     # Empty column for blank spaces
     emptylabel2 = Label(f1, font = ('arial', 16, 'bold'), text = "", bd = 16, anchor = "w")
     emptylabel2.grid(row = 5, column = 0)
     emptylabel2.configure(bg='#b3acf2')






textCiphering = Button(text="Text Cipher",padx = 20, pady = 12, font = ('arial', 12, 'bold'), command=windowForTextCipher)
textCiphering.place(relx=0.3,rely=0.5)

textCiphering = Button(text="Image Segano",padx = 20, pady = 12,font = ('arial', 12, 'bold'), command=windowForImageCipher)
textCiphering.place(relx=0.6,rely=0.5)

root.mainloop()