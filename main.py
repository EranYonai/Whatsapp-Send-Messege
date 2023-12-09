import webbrowser
import tkinter as tk
from tkinter import font

from PIL import ImageTk, Image
import os

def main():
    def Send_Phone_Num():
        user_input = entry.get()
        SendOpenWhatsapp(user_input)

    def enter_pressed(event):
        user_input = entry.get()
        SendOpenWhatsapp(user_input)

    def SendOpenWhatsapp(phoneNum):
        if (phoneNum[0:3] != "972"):
            phoneNum = "972" + phoneNum
        phoneNum = phoneNum.replace("-", "")
        whatsappLink = "wa.me\\"
        webbrowser.open(whatsappLink + phoneNum)

    root = tk.Tk()

    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    root.title("Send Message WhatsApp")
    dir_path = os.path.dirname(os.path.realpath(__file__))

    root.geometry("500x500")  # Size: 300x150, Loc: 30,30

    fnt = font.Font(family="Helvetica", size=20, weight=font.BOLD, slant=font.ITALIC)

    Entery_Lable = tk.Label(root, text="Insert Phone Number", width=25, height=1, font=fnt, relief="groove",
                            compound=tk.TOP)
    Entery_Lable.pack(pady=20)

    entry = tk.Entry(root, font="Arial")
    entry.pack(pady=15)

    fnt2 = font.Font(family="Helvetica", size=10, weight=font.BOLD, slant=font.ITALIC)
    button = tk.Button(root, text="Enter", font=fnt2, command=Send_Phone_Num)
    root.bind("<Return>", enter_pressed)

    button.pack()

    Image_Whatsapp = ImageTk.PhotoImage(Image.open(dir_path + r'\Whatsapp.jpeg'))
    label = tk.Label(root, image=Image_Whatsapp)
    label.pack(pady=20)

    root.mainloop()


if (__name__ == '__main__'):
    main()
