import webbrowser
import tkinter as tk
from tkinter import font, END, OptionMenu, StringVar
from tkcalendar import DateEntry

from PIL import ImageTk, Image
import os
import re
import His_GoogleCalander_QuickStart as GooCal

# General Constants
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # path to chrome browser

i = 0


def main():
    def Create_Tex_Ent(texts):
        """
        Creates an label and entry of each string in texts
        :type texts: [str, str]
        :param texts: texts is an array that has all the names of entries you want to create
        :return: 2 dictionaries 1 of labels and 1 of entries
        """
        funTexs = {}
        funEnts = {}
        if len(texts[0]) <= 1:
            funTexs[texts] = tk.Label(root, text=texts, width=25, height=1, font=FNT, relief="groove", compound=tk.TOP)

            funTexs[texts].pack(pady=GENERALPADDING)

            funEnts[texts] = tk.Entry(root, font="Arial")
            funEnts[texts].pack(pady=GENERALPADDING)

        else:
            for t in texts:
                funTexs[t] = tk.Label(root, text=t, width=25, height=1, font=FNT, relief="groove", compound=tk.TOP)

                funTexs[t].pack(pady=GENERALPADDING)

                funEnts[t] = tk.Entry(root, font="Arial")
                funEnts[t].pack(pady=GENERALPADDING)

        return funTexs, funEnts

    def Create_Tex_DropMenu(names_types):

        names_Types = {}
        menu_Names_Types = {}

        for name, types in names_types:
            tk.Label(root, text=name, width=25, height=1, font=FNT, relief="groove",
                                    compound=tk.TOP).pack(pady=1)

            names_Types[name] = StringVar(root)
            names_Types[name].set(types[0])  # default value

            # creating the drop down menu for class num
            menu_Names_Types[name] = OptionMenu(root, names_Types[name], *types)
            menu_Names_Types[name].pack(pady=1)
            classNum_tex.pack(pady=1)

        return names_types, menu_Names_Types


    def enter_pressed(event):
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
        classNum = classNum_Men.get()
        peopleAmount = peopleAmount_Men.get()
        if date != "" or timeStart != "":
            AddMessage(whatsappLink, name, phone_Num, peopleAmount, classNum, date, timeStart, timeEnd)
        else:
            OpenWhatsapp(whatsappLink)

    def OrganizePhone(phoneNum):
        phoneNum = re.sub("[^0-9]", "", phoneNum)

        if (phoneNum[0:3] != "972"):
            phoneNum = "972" + phoneNum
        whatsappLink = "web.whatsapp.com\\send\\?phone="
        whatsappLink += phoneNum + "&text="
        return whatsappLink

    def AddMessage(whatsappLink, name, phoneNum, personAmount, classNum, date, timeStart, TimeEnd):
        text1 = "היי, נקבע לך שיעור בתאריך " + date
        text2 = ", בשעה " + timeStart
        text3 = ", במועדון הגלישה פרי גל בשדות ים. נתראה"
        text = text1 + text2 + text3
        whatsappLink += text
        typeOfClass = classTypes_Men.get()
        GooCal.CreateTypeOfClassInCalendar(typeOfClass,
                                           GooCal.GetEverythingTogether(typeOfClass, name, phoneNum, personAmount, classNum),
                                           date, timeStart, TimeEnd)
        OpenWhatsapp(whatsappLink)

    def OpenWhatsapp(whatsappLink):
        if (os.path.exists(chrome_path[0:-3])):
            webbrowser.get(chrome_path).open(whatsappLink)
        else:
            webbrowser.open(whatsappLink)


    root = tk.Tk()

    # Tk Constants
    FNT = font.Font(family="Helvetica", size=10, weight=font.BOLD, slant=font.ITALIC)  # font for text ent and more
    GENERALPADDING = 1  # the padding between each text ent and more

    root.title("Send Message WhatsApp")

    root.geometry("500x700")  # Size: 300x150, Loc: 30,30

    textsToCreate = ("Name", "Phone Number", "Time Start", "Time End")
    ents: dict[str, tk.Entry]
    texs: dict[str, tk.Label]
    texs, ents = Create_Tex_Ent(textsToCreate)

    # Calendar chooser
    date_Tex = tk.Label(root, text="date", width=25, height=1, font=FNT, relief="groove", compound=tk.TOP)
    date_Tex.pack(pady=1)

    date_cal = DateEntry(root, date_pattern="yyyy-mm-dd")
    date_cal.pack()

    #menu_Name = ()
    #menu_Type = ()

    #names_Types, menu_Names_Types =


    # Creating the Drop down menu text for class type
    classType_tex = tk.Label(root, text="Type of Class", width=25, height=1, font=FNT, relief="groove", compound=tk.TOP)
    classType_tex.pack(pady=1)

    # here is every class in the drop down
    types = [
        'שיעור גלישת גלים',
        'שיעור גלישת ווינג',
        'שיעור גלישת רוח',
        'שיעור סאפ',
        'שיעור קייט סרפינג',
        'שיעור שייט על קטמרן',
        'השכרת קטמרן'
    ]

    # Creating the Drop down menu
    classTypes_Men = StringVar(root)
    classTypes_Men.set(types[0])  # default value

    classMenu = OptionMenu(root, classTypes_Men, *types)
    classMenu.pack()

    # Creating the Drop down menu text for class num
    classNum_tex = tk.Label(root, text="Number Of Class", width=25, height=1, font=FNT, relief="groove", compound=tk.TOP)
    classNum_tex.pack(pady=1)

    # here is number in the drop down
    classNums = [
        'נסיון',
        'ראשון',
        'שני',
        'שלישי',
        'רביעי',
    ]

    # Creating the Drop down menu for class num
    classNum_Men = StringVar(root)
    classNum_Men.set(classNums[0])  # default value

    # creating the drop down menu for class
    numMenu = OptionMenu(root, classNum_Men, *classNums)
    numMenu.pack()

    # remember to change names
    # Creating the Drop down menu text for class num
    peopleAmount_tex = tk.Label(root, text="Number Of Class", width=25, height=1, font=FNT, relief="groove",
                            compound=tk.TOP)
    peopleAmount_tex.pack(pady=1)

    # here is number in the drop down
    peopleAmount = [
        'פרטי',
        'זוגי',
        'רב משתתפים'
    ]

    # Creating the Drop down menu for class num
    peopleAmount_Men = StringVar(root)
    peopleAmount_Men.set(peopleAmount[0])  # default value

    # creating the drop down menu for class num
    peopleAmountMenu = OptionMenu(root, peopleAmount_Men, *peopleAmount)
    peopleAmountMenu.pack()



    # Creating Button
    fntForButton = font.Font(family="Helvetica", size=10, weight=font.BOLD, slant=font.ITALIC)
    Enter_button = tk.Button(root, text="Enter", font=fntForButton, command=enter_pressed)
    root.bind("<Return>", enter_pressed)
    Enter_button.pack(pady=5)
    whatCalendarShow_tex: tk.Label


    name = ents["Name"].get()
    phone_Num = ents["Phone Number"].get()
    whatCalendarShow_text = GooCal.GetEverythingTogether(classTypes_Men.get(), name,
                                                         phone_Num, peopleAmount_Men.get(), classNum_Men.get())

    #whatCalendarShow_tex = CalendarShow(whatCalendarShow_tex, whatCalendarShow_text)

    #whatCalendarShow_tex = CalendarShow()

    """
    whatCalendarShow_text_length_X = len(whatCalendarShow_text)
    whatCalendarShow_text_length_Y = 0
    tempNum = whatCalendarShow_text_length_X
    while(tempNum > 20):
        whatCalendarShow_text_length_Y += 1
        tempNum -= 20
    """
    # Putting WhatsApp Image
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # Image_WhatsApp_Link = ImageTk.PhotoImage(Image.open(dir_path + r'\Freegull_Logo.jpeg'))
    # Image_WhatsApp = tk.Label(root, image=Image_WhatsApp_Link)
    # Image_WhatsApp.pack(side="bottom", pady=5)

    root.mainloop()


if (__name__ == '__main__'):
    main()
