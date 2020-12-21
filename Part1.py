from tkinter import *               
import tkinter as tk
from tkinter import messagebox
import csv

window = Tk()                                # Used to create the window for the questionnaire and some features relative to it in the following 3 lines.
window.title("Innova™")            
window.geometry("440x800")
window.configure(background = "grey");

name = tk.StringVar(window)
date = tk.StringVar(window)
age = tk.StringVar(window)
dni = tk.StringVar(window)
phone = tk.StringVar(window)
email = tk.StringVar(window)
bmi = tk.StringVar(window)
city = tk.StringVar(window)
gender = tk.IntVar()
smoker = tk.IntVar()
asthma = tk.IntVar()
cancer = tk.IntVar()
chronic_renal_disease = tk.IntVar()
chronic_pulmonary_disease = tk.IntVar()
pregnant = tk.IntVar()
diabetes = tk.IntVar()
hypertension = tk.IntVar()
talassemia = tk.IntVar()
immunosuppressed = tk.IntVar()
sickle_cell_disease = tk.IntVar()

def upload():             #The function upload contains the sentences needed to get and store the information of the query into the CSV as well as to calculate the relative score for each query.
    try:
        Name = name.get()
        Date = date.get()
        Age = int(age.get())
        DNI = dni.get()
        Phone = phone.get()
        Email = email.get()
        BMI = int(bmi.get())
        City = city.get()
        Gender = gender.get()
        Smoker = smoker.get()
        Asthma = asthma.get()
        Cancer = cancer.get()
        Chronic_renal_disease = chronic_renal_disease.get()
        Chronic_pulmonary_disease = chronic_pulmonary_disease.get()
        Pregnant = pregnant.get()
        Diabetes = diabetes.get()
        Hypertension = hypertension.get()
        Talassemia = talassemia.get()
        Immunosuppressed = immunosuppressed.get()
        Sickle_cell_disease = sickle_cell_disease.get()
    except:
        messagebox.showerror("Error", "Wrong data in field")
    
    ValorAge = 0
    ValorBMI = 0
    if Age >= 65:
        ValorAge = 1
    if Age >= 75:
        ValorAge = 2
    if Age >= 85:
        ValorAge = 3
        
    if BMI < 18:
        ValorBMI = 1
    if BMI >= 30:
        ValorBMI = 1
    if BMI >= 40:
        ValorBMI = 2
        
    Score = Sickle_cell_disease+Immunosuppressed+Talassemia+Hypertension+Diabetes+Pregnant+Chronic_pulmonary_disease+Chronic_renal_disease+Cancer+Asthma+Smoker+ValorBMI+ValorAge  # Used to calculate the score.

    pacient = [DNI, Score, Name, Date, Age, Phone, Email, BMI, City, Gender, Smoker, Asthma, Cancer, Chronic_renal_disease, Chronic_pulmonary_disease, Pregnant, Diabetes, Hypertension, Talassemia, Immunosuppressed, Sickle_cell_disease]
    try:
        open("base.csv")   # Used to open the CSV file.
    except:
        with open("base.csv", "w", newline = "") as base:
            writer = csv.writer(base)
            writer.writerow(["DNI", "Score", "Name", "Date", "Age", "Phone", "Email", "BMI", "City", "Gender", "Smoker", "Asthma", "Cancer", "Chronic_renal_disease", "Chronic_pulmonary_disease", "Pregnant", "Diabetes", "Hypertension", "Talassemia", "Immunosuppressed", "Sickle_cell_disease", "Score"])
            writer.writerow(pacient)
    else:
        with open("base.csv", "a", newline = "") as base:
            writer = csv.writer(base)
            writer.writerow(pacient)
            base.close()
    finally:
         base.close()
    window.destroy()
    
Label(window, text = "Name", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 1, column = 1)   #Label is used to create the button for each entry or question.
Entry(window, textvariable = name, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 2, column = 1)  #Entry is used to relate each answer to a variable to be later processed.

Label(window, text = "Date", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 1, column = 2)
Entry(window, textvariable = date, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 2, column = 2)

Label(window, text = "Age", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 3, column = 1)
Entry(window, textvariable = age, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 4, column = 1)

Label(window, text = "DNI", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 3, column = 2)
Entry(window, textvariable = dni, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 4, column = 2)

Label(window, text = "Phone Number", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 5, column = 1)
Entry(window, textvariable = phone, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 6, column = 1)

Label(window, text = "Email", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 5, column = 2)
Entry(window, textvariable = email, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 6, column = 2)

Label(window, text = "BMI", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 13, column = 1)
Entry(window, textvariable = bmi, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 14, column = 1)

Label(window, text = "City", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 13, column = 2)
Entry(window, textvariable = city, width = 20, fg = "blue", bd = 10, selectbackground = "violet").grid(row = 14, column = 2)

Label(window, text = "Gender", bg ="grey", fg = "white", font = "none 12 bold").grid(row = 15, column = 2)
tk.Radiobutton(window, text = "Male   ", bg = "grey", padx = 20, variable = gender, value = 1).grid(row = 16, column = 2) # Radiobutton is used to create the Yes/No kind of questions from the questionnaire.
tk.Radiobutton(window, text = "Female", bg = "grey", padx = 20, variable = gender, value = 2).grid(row = 17, column = 2)

Label(window, text = "Does the patient smoke?", bg ="grey", fg = "white", font = "none 12 bold").grid(row = 15, column = 1)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = smoker, value = 1).grid(row = 16, column = 1)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = smoker, value = 0).grid(row = 17, column = 1)

Label(window, text = "Does the patient have asthma?", bg ="grey", fg = "white", font = "none 12 bold").grid(row = 18, column = 1)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = asthma, value = 1).grid(row = 19, column = 1)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = asthma, value = 0).grid(row = 20, column = 1)

Label(window ,text = "Does the patient have cancer", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 21, column = 1)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = cancer, value = 1).grid(row = 22, column = 1)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = cancer, value = 0).grid(row = 23, column = 1)

Label(window ,text = "Chronic Renal Disease", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 24, column = 1)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = chronic_renal_disease, value = 1).grid(row = 25, column = 1)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = chronic_renal_disease, value = 0).grid(row = 26, column = 1)

Label(window ,text = "Chronic Pulmonary Disease",bg = "grey", fg = "white", font = "none 12 bold").grid(row = 27, column = 1)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = chronic_pulmonary_disease, value = 1).grid(row = 28, column = 1)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = chronic_pulmonary_disease, value = 0).grid(row = 29, column = 1)

Label(window ,text = "Pregnant", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 18, column = 2)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = pregnant, value = 1).grid(row = 19, column = 2)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = pregnant, value = 0).grid(row = 20, column = 2)

Label(window ,text = "Diabetes", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 21, column = 2)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = diabetes, value = 1).grid(row = 22, column = 2)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = diabetes, value = 0).grid(row = 23, column = 2)

Label(window ,text = "Hypertension", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 24, column = 2)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = hypertension, value = 1).grid(row = 25, column = 2)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = hypertension, value = 0).grid(row = 26, column = 2)

Label(window ,text = "Talassemia", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 27, column = 2)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = talassemia, value = 1).grid(row = 28, column = 2)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = talassemia, value = 0).grid(row = 29, column = 2)

Label(window ,text = "Immunosupressed", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 30, column = 2)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = immunosuppressed, value = 1).grid(row = 31, column = 2)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = immunosuppressed, value = 0).grid(row = 32, column = 2)

Label(window ,text = "Sickle Cell Disease", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 30, column = 1)
tk.Radiobutton(window, text = "Yes", bg = "grey", padx = 20, variable = sickle_cell_disease, value = 1).grid(row = 31, column = 1)
tk.Radiobutton(window, text = "No", bg = "grey", padx = 20, variable = sickle_cell_disease, value = 0).grid(row = 32, column = 1)

Label(window, text = "", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 33, column = 1)
tk.Button(window, text = "Upload and Close", fg = "White", bg = "dark green", height = 1, width = 16, command = upload).grid(row = 34, column = 1)

window.mainloop()
