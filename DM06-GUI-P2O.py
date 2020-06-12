from calendar import *
from datetime import *
from tkinter import *
from tkinter import ttk


#####################################################################################################
#######################################__Programming__Part__#########################################
#####################################################################################################


#RUN__________________________________________________________________

def run():
    dec1 = {'Janvier': 1, 'Février': 2, 'Mars': 3, 'Avril': 4, 'Mai': 5, 'Juin': 6,
            'Juillet': 7, 'Aoùt': 8, 'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12}
    m = dec1[month_var.get()]
    y = year_var.get()
    d = day_var.get()

    try:
        ann = datetime(int(y), m, int(d))

    except (TypeError, ValueError):
        err_var.set('IMED')
        if err_var.get():
            err.place_forget()
            resultat.place_forget()
            res.place_forget()
            ph.place_forget()

        if not y and not d:
            err_var.set("Le champ d'année est vide.\t\t\t"
                        "      Le champ de jour est vide.")
            err.place(x = 30, y = 150)

        elif not y:
            err_var.set("Le champ d'année est vide.")
            err.place(x = 30, y = 150)

        elif not d:
            err_var.set("Le champ de jour est vide.")
            err.place(x = 394, y = 150)

        elif y == '0':
            err_var.set(f"{'Really ! '*3}")
            err.place(x = 35, y = 150)

        elif not y.isdecimal() and not d.isdecimal():
            err_var.set("Veuillez saisir un nombre.\t\t\t\t"
                        "      Veuillez saisir un nombre.")
            err.place(x = 30, y = 150)

        elif not y.isdecimal():
            err_var.set("Veuillez saisir un nombre.")
            err.place(x = 30, y = 150)

        elif not d.isdecimal():
            err_var.set("Veuillez saisir un nombre.")
            err.place(x = 394, y = 150)

        elif not 1 <= int(d) <= monthrange(int(y), m)[1]:
            err_var.set("Le jour est hors de\n porté du mois.")
            err.place(x = 420, y = 150)

    else:
        now = datetime.now()
        err.place_forget()
        delta = now - ann

        res_var.set(f"- Date d'aujourd'hui :\n\n"
                    f"- Âge en jour \t :\t\tjours.\n"
                    f"- Âge en semaine \t :\t\tsemaines.\n"
                    f"- Âge en mois \t :\t\tmois.\n"
                    f"- Âge en année \t :\t\tans.")
        resultat.place(x = 35, y = 165)

        res_var2.set(f"{now.date()}\n\n"
                     f"{delta.days}\n"
                     f"{delta.days // 7}\n"
                     f"{int(delta.days // 30.45)}\n"
                     f"{int(delta.days // 365.25)}")
        res.place(x = 220, y = 164)

        def weekday_name(yy, mm, dd):
            dec2 = {0: "lundi", 1: "mardi", 2: "mercredi", 3: "jeudi",
                    4: "vendredi", 5: "samedi", 6: "dimanche"}
            return dec2[weekday(yy, mm, dd)]

        av = now.year - (int(y) + int(delta.days // 365.25))
        ap = 4 - av
        if int(d) == 29 and m == 2 and isleap(int(y)):
            if isleap(now.year):
                if now.month < m:
                    ph_var.set(f'- Vous êtes né(e) un '
                               f'{weekday_name(int(y), m, int(d))},'
                               f' votre dernier anniverssaire\n   était un '
                               f'{weekday_name(now.year - 4, m, int(d))}'
                               f' et le prochain sera un '
                               f'{weekday_name(now.year, m, int(d))}.')

                elif now.month >= m:
                    ph_var.set(f'- Vous êtes né(e) un '
                               f'{weekday_name(int(y), m, int(d))},'
                               f' votre dernier anniverssaire\n   était un '
                               f'{weekday_name(now.year, m, int(d))}'
                               f' et le prochain sera un '
                               f'{weekday_name(now.year + 4, m, int(d))}.')
            else:
                ph_var.set(f'- Vous êtes né(e) un '
                           f'{weekday_name(int(y), m, int(d))},'
                           f' votre dernier anniverssaire\n   était un '
                           f'{weekday_name(now.year - av, m, int(d))}'
                           f' et le prochain sera un '
                           f'{weekday_name(now.year + ap, m, int(d))}.')

        else:
            if (now.month < m) or (now.month == m and now.day < int(d)):
                ph_var.set(f'- Vous êtes né(e) un '
                           f'{weekday_name(int(y), m, int(d))},'
                           f' votre dernier anniverssaire\n   était un '
                           f'{weekday_name(now.year - 1, m, int(d))}'
                           f' et le prochain sera un '
                           f'{weekday_name(now.year , m, int(d))}.')

            elif now.month > m or (now.month == m and now.day >= int(d)):
                ph_var.set(f'- Vous êtes né(e) un '
                           f'{weekday_name(int(y), m, int(d))},'
                           f' votre dernier anniverssaire\n   était un '
                           f'{weekday_name(now.year, m, int(d))}'
                           f' et le prochain sera un '
                           f'{weekday_name(now.year + 1, m, int(d))}.')

        ph.place(x = 35, y = 310)


#Clear___________________________________________________________________

def clear():
    month_var.set('Janvier')
    day_var.set('')
    err.place_forget()
    resultat.place_forget()
    res.place_forget()
    ph.place_forget()
    year_var.set('')


#Exit______________________________________________________________________

def exit_fun():
    print(f"{'':_^30}\n")
    print('الدُنيا كُلّهَا قليل            \n'
          'وَ الذِي بَقِي مِنهَا قليل        \n'
          'وَ الذِي لنا مِن البَاقي قليل      \n'
          'وَ لم يَبقى مِن قليلِنا سِوى القليل   ')
    print(f"{'':_^30}")
    exit()


######################################################################################################
#######################################__Designing__Part__############################################
######################################################################################################


#MAIN_Window___________________________________________________________

window: Tk = Tk()
window.withdraw()

top: Toplevel = Toplevel(bg = 'cornsilk4')
top.geometry('600x400+365+125')
top.title("Programmation Orienté Object (POO) - DM: 06")
top.deiconify()
top.lift()
top.resizable(0, 0)

#Inisialization_____________________________________________________

wlc = Label(top, text = f"{'Découvre votre age en jours, semaines et mois':^150}",
            bg = 'cornsilk3', fg = 'saddle brown', anchor = 's', height = 1,
            font = ('times', 16, 'bold'), bd = 3, justify = 'center')

wlc.pack(fill = 'x', ipady = 3)

fr = Frame(top, height = 3, width = 650, bg = 'light cyan')
fr.place(x = 0, y = 38)

#Input_Label______________________________________________________________

agevar = StringVar()
agevar.set('Donner votre date de naissance :')
user_age = Label(top, textvariable = agevar,
                 bg = 'cornsilk4', fg = 'light cyan',
                 font = ('arial', 11, 'bold'))

user_age.place(x = 30, y = 48)

#Year_Input_________________________________________________________

year_fr = Frame(top, bg = 'NavajoWhite1', width = 180, height = 70)
year_fr.place(x = 30, y = 75)

year_var = StringVar()
year = Entry(year_fr, bg = 'white', bd = 1,
             fg = 'gray10', width = 15,
             font = ('Arial', 12, 'bold'),
             textvariable = year_var)

year.place(x = 10, y = 30)

year_lb = Label(year_fr, text = 'Année',
                bg = 'NavajoWhite1',
                font = ('Arial', 10, 'bold'))

year_lb.place(x = 10, y = 5)

#Month_Input_________________________________________________________

month_fr = Frame(top, bg = 'NavajoWhite2', width = 180, height = 70)

month_fr.place(x = 210, y = 75)

month_var = StringVar()
month = ttk.Combobox(month_fr, font = ('Arial', 11, 'bold'), height = 6, width = 15,
                     values = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
                               'Juillet', 'Aoùt', 'Septembre', 'Octobre', 'Novembre', 'Décembre'),
                     exportselection = 0, textvariable = month_var,
                     state = 'readonly')

month_var.set('Janvier')

month.place(x = 10, y = 30)

month_lb = Label(month_fr, text = 'Mois',
                 bg = 'NavajoWhite2',
                 font = ('Arial', 10, 'bold'))

month_lb.place(x = 10, y = 5)

#Day_Input_________________________________________________________

day_fr = Frame(top, bg = 'NavajoWhite3', width = 180, height = 70)

day_fr.place(x = 390, y = 75)

day_var = StringVar()
day = Entry(day_fr, bg = 'white', bd = 1,
            fg = 'gray10', width = 15,
            font = ('Arial', 12, 'bold'),
            textvariable = day_var)

day.place(x = 10, y = 30)

day_lb = Label(day_fr, text = 'Jour',
               bg = 'NavajoWhite3',
               font = ('Arial', 10, 'bold'))

day_lb.place(x = 10, y = 5)

#RUN_Button______________________________________________________________

run_bt = Button(top, text = 'Run', bg = 'light grey', bd = 7,
                fg = 'gray15', relief = RAISED,
                activebackground = 'lawn green',
                activeforeground = 'black',
                font = ('Arial', 11, 'bold', 'underline'),
                cursor = 'hand2', width = 5, command = run)

run_bt.place(x = 510, y = 235)

#ERRER__________________________________________________________________

err_var = StringVar()
err = Label(top, textvariable = err_var,
            bg = 'cornsilk4', fg = 'red2',
            font = ('arial', 10, 'bold'))

#Clear_Button______________________________________________________________

clear_bt = Button(top, text = 'Clear', bg = 'light grey', bd = 7,
                  fg = 'gray15', relief = RAISED,
                  activebackground = 'gray',
                  activeforeground = 'black',
                  font = ('Arial', 11, 'bold', 'underline'),
                  cursor = 'hand2', width = 5, command = clear)

clear_bt.place(x = 510, y = 285)

#Résultat__________________________________________________________________

res_var = StringVar()
resultat = Label(top, textvariable = res_var,
                 bg = 'cornsilk4', fg = 'gray2',
                 font = ('times', 14), justify = 'left')


res_var2 = StringVar()
res = Label(top, textvariable = res_var2,
            bg = 'cornsilk4', fg = 'turquoise2',
            font = ('times', 14), justify = 'center')


ph_var = StringVar()
ph = Label(top, textvariable = ph_var,
           bg = 'cornsilk4', fg = 'light cyan',
           font = ('times', 14), justify = 'left')

#EXIT_#####################################################################################

#Exit_Button___________________________________________________________________________

exit_bt = Button(top, text = 'Exit', bg = 'light grey', bd = 7,
                 fg = 'gray10', relief = RAISED,
                 activebackground = 'gray',
                 activeforeground = 'black', width = 5,
                 font = ('Arial', 11, 'bold', 'underline'),
                 command = exit_fun, cursor = 'hand2')

exit_bt.place(x = 510, y = 335)

top.mainloop()

#FIN_######################################################################################
#MOUSSI_Imed_Mect
