import webbrowser
import tkinter as tk
from tkinter import font, END, OptionMenu, StringVar
from tkcalendar import DateEntry

from PIL import ImageTk, Image
import os
import re
import Calander_Make_event as GooCal

# General Constants
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # path to chrome browser


def main():
    def Create_Tex_Ent(texts):
        """
        Creates an label and entry of each string in texts
        :type texts: [str, str]
        :param texts: texts is an array that has all the names of entries you want to create
        :return: 2 dictionaries 1 of labels and 1 of entries
        """
        funEnts = {}
        funString = {}
        if len(texts[0]) <= 1:
            tk.Label(root, text=texts, width=25, height=1, font=FNT, relief="groove", compound=tk.TOP).pack(pady=GENERALPADDING)

            funEnts[texts] = tk.Entry(root, font="Arial")
            funEnts[texts].pack(pady=GENERALPADDING)

        else:
            for t in texts:
                tk.Label(root, text=t, width=25, height=1, font=FNT, relief="groove", compound=tk.TOP).pack(pady=GENERALPADDING)

                funString[t] = tk.StringVar()

                funEnts[t] = tk.Entry(root, textvariable=funString[t], font="Arial")
                funEnts[t].pack(pady=GENERALPADDING)

        return funEnts, funString

    def Create_Tex_DropMenu(names_types):
        """
        Creates drop down menus + a label that describes them, return 1 of the stringVar
        :param names_types:
        :return:
        """

        menu_Names_Types = {}

        for name, types in names_types.items():
            tk.Label(root, text=name, width=25, height=1, font=FNT, relief="groove",
                     compound=tk.TOP).pack(pady=1)

            menu_Names_Types[name] = StringVar(root)
            menu_Names_Types[name].set(types[0])  # default value

            # creating the drop down menu for class num
            temp = OptionMenu(root, menu_Names_Types[name], *types)
            temp.pack(pady=1)

        return menu_Names_Types

    def update_label(*args):
        """
        this function gets the class type, the num of the class(ie: first class second and so forth),
        and so on and puts them in a spasific way and then it updatest the main display_label
        :param args:
        :return:
        """
        classType = menu_Names_Types["Type of class"].get()
        classNum = menu_Names_Types["Class number"].get()
        amount = menu_Names_Types["Amount of People"].get()
        name = strings_Var["Name"].get()
        phone_Num = strings_Var["Phone Number"].get()

        display_text = GooCal.GetEverythingTogether(classType, name, phone_Num, amount, classNum)

        display_label.config(text=display_text)

    def enter_pressed():
        """
        this event happes when the enter is pressed and checks if there is only phone num or also somthing else
        :param event:
        :return:
        """
        name = ents["Name"].get()
        phone_Num = ents["Phone Number"].get()
        timeStart = ents["Time Start"].get()
        timeEnd = ents["Time End"].get()

        ents["Name"].delete(0, END)
        ents["Phone Number"].delete(0, END)
        ents["Time Start"].delete(0, END)
        ents["Time End"].delete(0, END)

        whatsappLink = OrganizePhone(phone_Num)
        date = date_cal.get()
        classNum = menu_Names_Types["Class number"].get()
        peopleAmount = menu_Names_Types["Amount of People"].get()
        if date == '' or timeStart == '':
            OpenWhatsapp(whatsappLink)
        else:
            AddMessage(whatsappLink, name, phone_Num, peopleAmount, classNum, date, timeStart, timeEnd)

    def enter_Key_Pressed(event):
        """
        this event happes when the enter is pressed and checks if there is only phone num or also somthing else
        :param event:
        :return:
        """
        t = '"'
        tt = ''
        name = ents["Name"].get()
        phone_Num = ents["Phone Number"].get()
        timeStart = ents["Time Start"].get()
        timeEnd = ents["Time End"].get()

        ents["Name"].delete(0, END)
        ents["Phone Number"].delete(0, END)
        ents["Time Start"].delete(0, END)
        ents["Time End"].delete(0, END)

        whatsappLink = OrganizePhone(phone_Num)
        date = date_cal.get()
        classNum = menu_Names_Types["Class number"].get()
        peopleAmount = menu_Names_Types["Amount of People"].get()
        if date == '' or timeStart == '':
            OpenWhatsapp(whatsappLink)
        else:
            AddMessage(whatsappLink, name, phone_Num, peopleAmount, classNum, date, timeStart, timeEnd)

    def OrganizePhone(phoneNum):
        """
        puts the phone num into a url in the way that is viable and returns that
        :param phoneNum:
        :return:
        """
        phoneNum = re.sub("[^0-9]", "", phoneNum)

        if (phoneNum[0:3] != "972"):
            phoneNum = "972" + phoneNum
        whatsappLink = "web.whatsapp.com\\send\\?phone="
        whatsappLink += phoneNum + "&text="
        return whatsappLink

    def AddMessage(whatsappLink, name, phoneNum, personAmount, classNum, date, timeStart, TimeEnd):
        """
        adds the message we want to the url, and sends a whatsapp message to the phone num,
        also sends us to a different class that adds a event to the calendar based on the entries
        :param whatsappLink:
        :param name:
        :param phoneNum:
        :param personAmount:
        :param classNum:
        :param date:
        :param timeStart:
        :param TimeEnd:
        :return:
        """
        text1 = "היי, נקבע לך שיעור בתאריך " + date
        text2 = ", בשעה " + timeStart
        text3 = ", במועדון הגלישה פרי גל בשדות ים. נתראה"
        text = text1 + text2 + text3
        whatsappLink += text
        typeOfClass = menu_Names_Types["Type of class"].get()
        GooCal.CreateTypeOfClassInCalendar(typeOfClass,
                                           GooCal.GetEverythingTogether(typeOfClass, name, phoneNum, personAmount,
                                                                        classNum),
                                           date, timeStart, TimeEnd)
        OpenWhatsapp(whatsappLink)

    def OpenWhatsapp(whatsappLink):
        """
        opens a url with chore if it exits and if not it uses explorer
        :param whatsappLink:
        :return:
        """
        if (os.path.exists(chrome_path[0:-3])):
            webbrowser.get(chrome_path).open(whatsappLink)
        else:
            webbrowser.open(whatsappLink)

    root = tk.Tk()

    # Tk Constants
    FNT = font.Font(family="Helvetica", size=10, weight=font.BOLD, slant=font.ITALIC)  # font for text ent and more
    GENERALPADDING = 1  # the padding between each text ent and more

    root.title("Send Message WhatsApp")

    root.geometry("500x900")  # Size: 300x150, Loc: 30,30

    textsToCreate = ("Name", "Phone Number", "Time Start", "Time End")
    ents: dict[str, tk.Entry]
    texs: dict[str, tk.Label]
    ents, strings_Var = Create_Tex_Ent(textsToCreate)

    # Calendar chooser
    date_Tex = tk.Label(root, text="date", width=25, height=1, font=FNT, relief="groove", compound=tk.TOP)
    date_Tex.pack(pady=1)

    date_cal = DateEntry(root, firstweekday="sunday", weekenddayslist="saturday", date_pattern="yyyy-mm-dd")
    date_cal.pack()

    # creating the menu types
    types = [
        'שיעור גלישת גלים',
        'שיעור גלישת ווינג',
        'שיעור גלישת רוח',
        'שיעור סאפ',
        'שיעור קייט סרפינג',
        'שיעור שייט על קטמרן',
        'השכרת קטמרן'
    ]

    classNumbers = [
        'נסיון',
        'ראשון',
        'שני',
        'שלישי',
        'רביעי',
    ]

    peopleAmount = [
        'פרטי',
        'זוגי',
        'רב משתתפים'
    ]

    menu_Name__menu_Type = {
        "Type of class": types,
        "Class number": classNumbers,
        "Amount of People": peopleAmount
    }

    menu_Names_Types = Create_Tex_DropMenu(menu_Name__menu_Type)

    # Creating Button
    fntForButton = font.Font(family="Helvetica", size=10, weight=font.BOLD, slant=font.ITALIC)
    Enter_button = tk.Button(root, text="Enter", font=fntForButton, command=enter_pressed)
    Enter_button.pack(pady=5)
    root.bind("<Return>", enter_Key_Pressed)

    # Getting the information on how the calendar event will look like #
    # setting traces so that the label will change if one of the entries or menus will change
    menu_Names_Types["Type of class"].trace_add("write", update_label)
    menu_Names_Types["Class number"].trace_add("write", update_label)
    menu_Names_Types["Amount of People"].trace_add("write", update_label)
    strings_Var["Name"].trace_add("write", update_label)
    strings_Var["Phone Number"].trace_add("write", update_label)

    # creating the label that will show what the calendar will write
    display_label = tk.Label(root, font=FNT, text="כאן זה יראה איך זה יראה בגוגל כאלאנדר", wraplength=300)
    display_label.pack(pady=10)

    # Putting Freegull Image
    dir_path = os.path.dirname(os.path.realpath(__file__))
    Image_WhatsApp_Link = ImageTk.PhotoImage(Image.open(dir_path + r'\Freegull_Logo.jpeg'))
    Image_WhatsApp = tk.Label(root, image=Image_WhatsApp_Link)
    Image_WhatsApp.pack(side="bottom", pady=5)

    root.mainloop()


if (__name__ == '__main__'):
    main()
