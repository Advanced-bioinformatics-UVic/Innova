import smtplib
from tkinter import *
import tkinter as tk
from tkinter import messagebox

window = Tk()
window.title("Innova™")
window.geometry("155x300")
window.configure(background = "grey");

dni = tk.StringVar(window)
result = tk.IntVar()

def upload():
    DNI = dni.get()
    Result = result.get()
    try:
        Email = Contact[DNI]
    except:
        messagebox.showerror("Error", "Invalid DNI")
    if Result==1:
        x = 'You have tested positive for COVID-19'
    if Result==0:
        x = 'You have tested negative for COVID-19'
    gmail_user = 'innovapcr@gmail.com'
    gmail_password = 'Advanceduvic1?'

    sent_from = gmail_user
    to = [Email]
    subject = 'PCR '
    body = x

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

   
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except:
        messagebox.showerror("Error", "There was a problem sending your email")

    lines = []
    with open('base.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == DNI:
                    lines.remove(row)
    with open("base.csv", "w", newline = "") as base:
        writer = csv.writer(base)
        writer.writerows(lines)
    

Label(window, text = "DNI", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 1, column = 2)
Entry(window, textvariable = dni, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 2, column = 2)

Label(window, text = "", bg ="grey", fg = "white", font = "none 12 bold").grid(row = 3, column = 1)

Label(window, text = "Result", bg ="grey", fg = "white", font = "none 12 bold").grid(row = 4, column = 2)
tk.Radiobutton(window, text = "Positive", bg = "grey", padx = 20, variable = result, value = 1).grid(row = 5, column = 2)
tk.Radiobutton(window, text = "Negative", bg = "grey", padx = 20, variable = result, value = 0).grid(row = 6, column = 2)

Label(window, text = "", bg ="grey", fg = "white", font = "none 12 bold").grid(row = 7, column = 1)

tk.Button(window, text = "Send Result", fg = "White", bg = "dark green", height = 1, width = 10, command = upload).grid(row = 33, column = 2)

from tkinter import *
from tkinter.ttk import *
import csv

Dic = {}
Contact = {}

with open("base.csv", "r", newline = "") as base:
    reader = csv.reader(base)
    for e in reader:
        if e[0] != "DNI":
            Dic[e[0]] = int(e[1])
            Contact[e[0]] = e[6]
base.close()
sorted_dict = {}
sorted_keys = sorted(Dic, reverse = True, key=Dic.get)

for w in sorted_keys:
    sorted_dict[w] = Dic[w]

window1 = Tk()
window1.title("Innova™ Reader®©")
window1.geometry("160x200")

lb = Label(window1, text = "")

Label(window1, text = "Identification | Score").pack()
lb['text'] = '\n'.join('{} | {}'.format(k, d) for k, d in sorted_dict.items())
lb.pack()

window1.mainloop()
window.mainloop()
