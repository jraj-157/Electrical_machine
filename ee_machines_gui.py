import math
from tkinter import *

def Answer():
    parameters = getvalues()
    
    x = parameters[1]/parameters[2]
    efficiency = round((x*(parameters[0]))/((x*parameters[0])+parameters[3]+(x*x*parameters[4]))*100,2)
    max_eff = round((x)/(x+parameters[3]+(x*x*parameters[4]))*100,2)
    t1=f'The efficiency of the transformer is  {efficiency}%.'
    t2=f'The efficiency is maximum when powerfactor is unity and eficiency will be {max_eff}%'
    text1=Message(main,text=t1,bg='red',fg='black',font=('algerian',10,'bold'),width=5000)
    text2=Message(main,text=t2,bg='red',fg='black',font=('algerian',10,'bold'),width=5000)
    text1.grid(row=5,column=2)
    text2.grid(row=6,column=2)
   

def getvalues():
    p= []
    pf = float(Valuepf.get())
    load = float(Valueload.get())
    rated = float(Valuerated.get())
    pcore = float(Valuepcore.get())
    Pcufl= float(ValuePcufl.get())
    loadingdata = [pf,load,rated,pcore,Pcufl]
    for i in loadingdata:
        p.append(i)
    return p
    
main = Tk()
main['bg'] = 'orange'
main.geometry('1500x500')
main.title('###LOADNING_PARAMETERS_TRANSFORMER_PARAMETERS###')
loading_parameters = Label(main, text='LOADING PARAMETERS', borderwidth=6, relief=SUNKEN, font='comicsanms 12 bold', padx=25, pady=25,bg='orange')
# ShortCircuit_Test = Label(main, text='Short Circuit Test', borderwidth=6, relief=SUNKEN, font='comicsanms 12 bold', padx=25, pady=25,bg='orange')
power_factor = Label(main, text="POWER FACTOR ", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=8, relief=SUNKEN,bg='orange')
load_KVA = Label(main, text="LOAD KVA", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=8, relief=SUNKEN,bg='orange')
rated_kva = Label(main, text="RATED KVA", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=8, relief=SUNKEN,bg='orange')
coreloss = Label(main, text="CORE LOSS (W)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=8, relief=SUNKEN,bg='orange')
culoss_at_fullload = Label(main, text="CUFL (W)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=8, relief=SUNKEN,bg='orange')
loading_parameters.grid(row=1)
# ShortCircuit_Test.grid(row=2)
power_factor.grid(row=0,column=1)
load_KVA.grid(row=0,column=2)
rated_kva.grid(row=0,column=3)
coreloss.grid(row=0,column=4)
culoss_at_fullload.grid(row=0,column=5)

Valuepf = StringVar()
Valueload = StringVar()
Valuerated = StringVar()
Valuepcore = StringVar()
ValuePcufl = StringVar()


powerfactor = Entry(main, textvariable=Valuepf, relief=SUNKEN, borderwidth=7)
loaded_KVA = Entry(main, textvariable=Valueload, relief=SUNKEN, borderwidth=7)
rated_KVA = Entry(main, textvariable=Valuerated, relief=SUNKEN, borderwidth=7)
p_core = Entry(main, textvariable=Valuepcore, relief=SUNKEN, borderwidth=7)
p_cufl = Entry(main, textvariable=ValuePcufl, relief=SUNKEN, borderwidth=7)
# Power_At_ShortCircuit = Entry(main, textvariable=ValuePowerShortCircuit, relief=SUNKEN, borderwidth=7)
powerfactor.grid(row=1, column=1)
loaded_KVA.grid(row=1, column=2)
rated_KVA.grid(row=1, column=3)
p_core.grid(row=1, column=4)
p_cufl.grid(row=1, column=5)


submit = Button(main, text="SUBMIT", font=('comicsanms 14 bold'), borderwidth=6, command=Answer)
submit.grid(row=3, column=2)


main.mainloop()
