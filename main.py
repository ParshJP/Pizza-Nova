# Parikh, Parshva
# 2020/09/29
# ICS4U1-01
# A program that allows you to select, make and order a pizza from Pizza Nova.

from tkinter import *   #import tkinter modules to use its widgets and the corresponding functions, properties, etc.
from tkinter import ttk, messagebox
from decimal import Decimal     #import decimal module to output exact prices

def set_rads(frame):
    global rads     #set variables to global to hold rad widgets and their values
    global varSize
    t = ['Small', 'Medium', 'Large', 'Party']       #list holding property values
    for i in range(4):      #create and set rad buttons on the frame's grid
        x = Radiobutton(frame, text = t[i], anchor = 'w', width = 15, pady = 5, variable = varSize, value = i,
                        command = calc_size)        #link to function that calculates size
        x.grid(row = i, padx = 5)
        rads.append(x)          #add rad buttons to a global list

def calc_size():            #based on the value of the rad button selected, display price of according pizza size
    if varSize.get() == 0:
        size = 7.99
    elif varSize.get() == 1:
        size = 9.99
    elif varSize.get() == 2:
        size = 12.49
    else:
        size = 18.59
    insert_vals(txts[0], size)          #insert the price value into the chosen entry widget
    btns[2].config(state='disabled')        #disable the checkout button before user presses calculate

def set_chks(frame):        #set variables to global to hold chk widgets and their values
    global chks
    global bools
    t = ['Mushrooms', 'Green Peppers', 'Onions', 'Jalapenos', 'Pepperoni', 'Tomatoes', 'Olives', 'Pineapple']
    r = [0, 1, 2, 3, 0, 1, 2, 3]        #lists holding property values and grid values
    c = [0, 0, 0, 0, 1, 1, 1, 1]
    for i in range(8):                      #create and set chk buttons on the frame's grid
        b = BooleanVar()            #set each chk to a boolean variable
        x = Checkbutton(frame, text = t[i], anchor='w', width=15, pady=5, variable = b, command = calc_toppings)
        x.grid(row = r[i], column = c[i], padx=5)                            #link to function that calculates toppings
        bools.append(b)         #add chk buttons and bool vars to global lists
        chks.append(x)

def calc_toppings():        #based on the value of the chk button selected, display price of total toppings
    toppings = 0
    for i in range(7):      #for each topping selected, add a dollar
        if bools[i].get():
            toppings += 1.00
    if bools[7].get():
        messagebox.showerror('', "no")      #prevent user from committing high sin
        chks[7].deselect()
    toppings -= 3.00        #account for the 3 free toppings, minimum topping total of $0
    if toppings < 0.00:
        toppings = 0.00
    insert_vals(txts[1], toppings)          #insert the price value into the chosen entry widget
    btns[2].config(state='disabled')        #disable the checkout button before user presses calculate

def set_lbls_cbos(frame):       #set variables to global to hold combo widgets
    global cbos
    t = ['Pepsi', 'Crush (Orange)', 'Sprite', 'Mountain Dew']   #lists holding property values
    for i in range(4):      #create and set combo boxes and labels on the frame's grid
        x = Label(frame, text = t[i], width = 13, pady = 7, anchor = 'w').grid(row = i, column = 0, padx = 10)
        y = ttk.Combobox(frame, width = 1, state = 'readonly', values = (0, 1, 2, 3, 4, 5, 6))
        y.bind('<<ComboboxSelected>>', calc_bev)    #link to function that calculates beverages
        y.current(0)            #set the current values of each combo boxes to 0 (drinks)
        y.grid(row = i, column = 1, padx= 10)
        cbos.append(y)          #add combo boxes to a global list

def calc_bev(event):        #based on the value of the combo box selected, display price of total beverages
    bevs = 0
    for i in range(4):
        bevs += 0.99 * float(cbos[i].get())     #for each beverage selected, add $0.99
    insert_vals(txts[2], bevs)                  #insert the price value into the chosen entry widget
    btns[2].config(state='disabled')        #disable the checkout button before user presses calculate

def set_txts(frame):
    global txts             #set variables to global to hold entry widgets
    for i in range(3):      #create and set entry widgets on the frame's grid
        x = Entry(frame, font = 'TkDefaultFont 10 bold', justify = 'center', readonlybackground = 'white', width = 15)
        x.insert(0, '$0.00')        #set current prices to 0 for toppings and beverages
        if i == 0:
            x.delete(0, END)        #set price to 7.99 for size
            x.insert(0, '$7.99')
        x.config(state = 'readonly')
        x.grid(row = 3, column = i, ipady = 3, pady = 10)
        txts.append(x)          #add entry widgets to a global list

def set_lbls_txts(frame):
    global txts2            #set variables to global to hold entry widgets
    t = ['SUBTOTAL:', 'DELIVERY FEE:', 'HST (13%):', 'GRAND TOTAL:']    #lists holding property values
    for i in range(4):          #create and set entry widgets and labels on the frame's grid
        x = Label(frame, text = t[i], pady = 7, anchor = 'w', width = 15).grid(row = i, column = 0, padx = 10)
        y = Entry(frame, font='TkDefaultFont 10 bold', justify='center', readonlybackground='white', state = 'readonly')
        y.grid(row = i, column = 1, padx = 10, ipady = 3, pady = 5)
        txts2.append(y)         #add entry widgets to a global list

def set_btns(frame):
    global btns             #set variables to global to hold buttons
    t = ['CALCULATE', 'CLEAR', 'CHECKOUT', 'EXIT']      #lists holding property values
    c = [calc_totals, clear_all, check_out, exit_pizza]     #lists holding functions
    for i in range(4):      #create and set buttons on the frame's grid
        x = Button(frame, text = t[i], relief = 'raised', width = 15, command = c[i])   #set each to a specific function
        x.grid(row = i, pady = 5)
        btns.append(x)          #add buttons to a global list
    btns[2].config(state = 'disabled')    #disable the checkout button before user presses calculate

def insert_vals(entry, value):      #open a readonly widget, insert the calculated values and return to readonly
    entry.config(state='normal')
    entry.delete(0, END)
    value = Decimal(str(value))     #round the value to the correct amount using decimal function
    value = str(round(value, 2))
    if value[-2] == '.':            #debugging statement using string slicing for when a value ends in .0 and not .00
        value = value + '0'
    entry.insert(0, '$' + value)
    entry.config(state='readonly')

def calc_totals():          #calculate subtotal
    txts2[1].config(readonlybackground='white')     #reset entry widget if the previous delivery fee was free
    btns[2].config(state = 'active')        #activate checkout button

    size = float(txts[0].get()[1:])         #get values of size, beverages and toppings from entry widgets
    toppings = float(txts[1].get()[1:])
    bevs = float(txts[2].get()[1:])

    sub = bevs + toppings + size        #calculate and display subtotal
    insert_vals(txts2[0], sub)

    if sub < 15.00:         #if the subtotal is less than $15 there is a $5 delivery fee, fee if over $15
        delivery = 5.00
        insert_vals(txts2[1], delivery)     #insert value in entry widget
    else:
        delivery = 0.00         #change entry widget to green background if free delivery
        txts2[1].config(state='normal', readonlybackground = 'green')
        txts2[1].delete(0, END)
        txts2[1].insert(0, 'FREE')
        txts2[1].config(state='readonly')

    hst = sub * 0.13            #calculate amount of hst and display
    insert_vals(txts2[2], hst)

    grand = sub + delivery + hst        #calculate amount of grand total and display
    insert_vals(txts2[3], grand)

def clear_all():        #when user clicks clear, reset all options and entry widgets
    btns[2].config(state='disabled')    #disable checkout button
    rads[0].select()
    insert_vals(txts[0], 7.99)      #set size entry widget to the minimum amount
    for i in range(8):
        chks[i].deselect()
        insert_vals(txts[1], 0.00)      #set toppings entry widget to the minimum amount
    for i in range(4):
        cbos[i].set(0)
        insert_vals(txts[2], 0.00)      #set beverages entry widget to the minimum amount
    for i in range(4):
        txts2[i].config(state = 'normal', readonlybackground = 'white')
        txts2[i].delete(0, END)
        txts2[i].config(state = 'readonly')

def check_out():            #display order summary with messageboxes
    s = ['Small', 'Medium', 'Large', 'Party']       #hold string values for user options in lists
    t = ['Mushrooms', 'Green Peppers', 'Onions', 'Jalapenos', 'Pepperoni', 'Tomatoes', 'Olives', 'Pineapple']
    b = ['Pepsi', 'Crush (Orange)', 'Sprite', 'Mountain Dew']
    title = 'Order Summary'
    x = 'Is this order correct?\n\nPIZZA:\n'        #variable holding common string
    e = 0
    for i in range(8):      #set a variable to tell if toppings are selected or not
        if bools[i].get():
            e += 1

    if e == 0 and float(txts[2].get()[1:]) == 0.00:     #if only a pizza size is selected than display it
        answer = messagebox.askyesno(title, x + '- ' + s[varSize.get()])    #get values of widgets and convert to string
    elif float(txts[2].get()[1:]) == 0.00:          #if only a pizza size and toppings are selected than display those
        z = ''
        for i in range(8):
            if bools[i].get():
                y = '- ' + t[i] + '\n'      #get values of toppings if they are selected from global lists
                z += y                       #get values of widgets and convert to string
        answer = messagebox.askyesno(title, x + '- ' + s[varSize.get()] + '\n\nTOPPINGS:\n' + z)
    elif e == 0:                #if only a pizza size and beverages are selected than display those
        z = ''
        for i in range(4):
            if float(cbos[i].get()) > 0:            #get values of toppings if they are selected from global lists
                y = '- ' + cbos[i].get() + 'x ' + b[i] + '\n'
                z += y                                              #get values of widgets and convert to string
        answer = messagebox.askyesno(title, x + '- ' + s[varSize.get()] + '\n\nBEVERAGES:\n' + z)
    else:                   #if only all 3 are selected than display them
        z = ''
        n = ''
        for i in range(8):                  #get values of toppings if they are selected from global lists
            if bools[i].get():
                y = '- ' + t[i] + '\n'
                z += y
        for i in range(4):                  #get values of toppings if they are selected from global lists
            if float(cbos[i].get()) > 0:
                m = '- ' + cbos[i].get() + 'x ' + b[i] + '\n'
                n += m                              #get values of widgets and convert to string
        answer = messagebox.askyesno(title, x + '- ' + s[varSize.get()] + '\n\nTOPPINGS:\n' + z + '\nBEVERAGES:\n' + n)
    if answer:                                      #display order delivery message is user confirms order
        messagebox.showinfo('Pizza Nova', "Thank you for ordering from Pizza Nova!\n"
                                          "Your pizza will be delivered in 30 minutes or it's free.\n\n"
                                          "To order again, click 'CLEAR' and select your preferred choices or\n"
                                          "click 'CALCULATE' again to repeat this order.")
    btns[2].config(state='disabled')            #disable checkout button until user presses calc again

def exit_pizza():       #confirm that user wants to exit if user clicks the window X or the exit button
    answer = messagebox.askyesno('Pizza Nova', 'Are you sure you want to exit?\nAll selected options will be lost.')
    if answer:      #if user clicks yes then close the window
        exit()

root = Tk()     #create window, set title and set the window exit option to display a prompt
root.title('Pizza Nova')
root.protocol("WM_DELETE_WINDOW", exit_pizza)

rads = []
chks = []
cbos = []       #declare variables to hold values for user option widgets
txts = []         #will be set to global in their respective functions
txts2 = []
btns = []
bools = []
varSize = IntVar()

mainframe = Frame(root, padx = 10, pady = 10)   #set mainframe and add it to the window
mainframe.pack()

logo = PhotoImage(file = 'pizza_nova.png')       #set images for logo and the cards image to variables
cards = PhotoImage(file = 'PaymentOptions.png')          #put the images in a label to display
lblLogo = Label(mainframe, image = logo).grid(row = 0, column = 0, columnspan = 3)  #set mainframe's grid
lblCards = Label(mainframe, image = cards).grid(row = 4, column = 0, padx = 10, pady = 10)

frame10 = LabelFrame(mainframe, text = 'SIZE', font = 'TkDefaultFont 10 bold')
frame10.grid(row = 1, column = 0, padx = 10, pady = 10)         #create and set a labelframe in the main frame
set_rads(frame10)       #create and set radiobuttons for size using the labelframe's grid

frame11 = LabelFrame(mainframe, text = 'TOPPINGS', font = 'TkDefaultFont 10 bold')
frame11.grid(row = 1, column = 1, padx = 5, pady = 10)      #create and set a labelframe in the main frame
set_chks(frame11)       #create and set checkboxes for toppings using the labelframe's grid

frame12 = LabelFrame(mainframe, text = 'BEVERAGES', font = 'TkDefaultFont 10 bold')
frame12.grid(row = 1, column = 2,       #create and set a labelframe in the main frame
             padx = 10, pady = 10)
set_lbls_cbos(frame12)      #create and set comboboxes for beverages using the labelframe's grid

lblFree = Label(mainframe, text = 'First three (3) toppings are free!',     #create label in mainframe telling user
                font = 'TkDefaultFont 10 bold').grid(row = 2, column = 0, columnspan = 3)   #upto 3 toppings are free

set_txts(mainframe) #create and set entry widgets displaying prices of the size, toppings and beverages

frame41 = Frame(mainframe)      #create and set a frame in the main frame
frame41.grid(row = 4, column = 1, padx = 5, pady = 10)
set_lbls_txts(frame41)      #create and set entry widgets displaying total prices using the frame's grid

frame42 = Frame(mainframe)      #create and set a frame in the main frame
frame42.grid(row = 4, column = 2, padx = 5, pady = 10)
set_btns(frame42)       #create and set buttons for user options using the frame's grid

root.mainloop()     #loop the window so it can be used as many times as necessary before user selects exit
