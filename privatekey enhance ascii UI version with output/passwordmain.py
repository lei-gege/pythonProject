# lei is seeking for a job!!

################### THIS IS ASCII ENCRYPT PROGRAM #################

from encrpyt import *
from asciiconvert import *
from tkinter import *

mw = Tk()
mw.title("private key encryption and decryption(私钥加密解密软件)")
mw.geometry('740x440')


def click():  # encryption button function
    pass_word = passin.get()
    enhance1 = enhance1in.get()
    information_text.delete(1.0, END)  # clear table for every click
    information_text.delete(1.0, END)
    encry_text.delete(1.0, END)
    if len(pass_word) == 0:
        # print('please input your private key')
        information_text.insert(INSERT, 'please input your private key')
    elif len(pass_word) != 0:
        while len(enhance1) > len(pass_word):
            # print("please make sure password is not longer than private key")
            information_text.insert(INSERT, "please make sure password is not longer than private key")
            break

        if len(enhance1) <= len(pass_word):
            final = encode1(pass_word, enhance1) + encode2(pass_word, enhance1)
            # print("your original password:" + "  " + pass_word)
            # print("your encrypted password:" + "  " + convert(final))
            encry_text.insert(INSERT, convert(final))
            return convert(final)


def click_decry():
    encrpyted_pass_word = decry_text.get()
    enhance1 = enhance2in.get()

    if len(encrpyted_pass_word) != 0:
        definal = decode1(encrpyted_pass_word, enhance1) + decode2(encrpyted_pass_word, enhance1)
        print("your decripted password:" + "  " + deconvert(definal))
        original_text.insert(INSERT, deconvert(definal))


def output():  # button function
    with open("encrpyted private key.txt", 'a', encoding='utf-8')as enfile:
        enfile.write(encry_text.get(1.0, END))


def output1():  # button function1
    with open("original private key.txt", 'a', encoding='utf-8')as enfile:
        enfile.write(original_text.get(1.0, END))


# Private key label and function
pass_word_Lable = Label(mw, text="Private Key(私钥):").place(x=10, y=10)
passin = Entry(mw, width='50')
passin.place(x=10, y=40)

# password key label and frame
enhance1_Lable = Label(mw, text="Password(密码):").place(x=10, y=70)
enhance1in = Entry(mw, width='50')
enhance1in.place(x=10, y=100)

# encryption button
encryButton = Button(mw, text='encryption(加密)', command=click).place(x=220, y=150)

# information frame
information_Label = Label(mw, text="Information").place(x=420, y=10)
information_text = Text(mw, height='7', width='40')
information_text.place(x=430, y=50)

# encrypted private key text frame
encry_result_Label = Label(mw, text="Encrypted Private Key").place(x=10, y=180)
encry_text = Text(mw, height='3', width="43")
encry_text.place(x=10, y=200)
# output encrypted private key to local
outputButton = Button(mw, text='Output(储存)', command=output).place(x=120, y=250)

# encrypted private key for decryption text frame
decry_result_Label = Label(mw, text="Encrypted Private Key for decryption").place(x=410, y=180)
decry_text = Entry(mw, width="43")
decry_text.place(x=410, y=200)

# decryption pass_word
enhance2_Label = Label(mw, text="Password(密码) for decryption(解密）:").place(x=410, y=235)
enhance2in = Entry(mw, width='43')
enhance2in.place(x=410, y=255)
# decryption button:
decryButton = Button(mw, text='decryption(解密)', command=click_decry).place(x=570, y=280)

# original private key
original_private_key = Label(mw, text="Original_Private_Key").place(x=410, y=320)
original_text = Text(mw, height='2', width="43")
original_text.place(x=410, y=340)

# output original private key to local
output1Button = Button(mw, text='Output(储存)', command=output1).place(x=570, y=360)

mw.mainloop()
