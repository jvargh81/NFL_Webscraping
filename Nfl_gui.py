# Importing the Libraries and packages required
from tkinter import *
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import numpy as np 

# Invoking Tkinter 
master = Tk()
# creating a icon
master.iconbitmap("nfl_TbG_icon.ico")
# title
master.title("NFL Player Stats")
# Background Image
image = Image.open('player.jpg')
photo_image = ImageTk.PhotoImage(image)
image1 = Label(master, image = photo_image)
image1.place(x=0, y=0, relwidth=1, relheight=1)
master.wm_geometry("600x400+20+40")

# Loading the csv file into a variables
ofns = pd.read_csv("nfl_offense_cleaned.csv")

ofns = ofns.dropna(how='all')

ofns = ofns.drop(ofns.columns[[0,3,4,5,8,9,11,12,13,14]], axis=1)

ofns = ofns[ofns["POS"] ==" QB"]

# Value_counts() helps to understand the count of each string in the data frame.
ofns["PLAYER"].value_counts()
# With the help of value_counts, identified 10 players who played all 11 years.
players = ["Eli Manning","Aaron Rodgers","Carson Palmer","Ben Roethlisberger","Drew Brees","Tom Brady","Kellen Clemens","Philip Rivers","Matt Cassel","Jay Cutler"]

# Creating Data frame for each player
Manning = ofns['PLAYER'].map(lambda x: x.startswith(players[0]))
manning = ofns[Manning]
manning = manning.sort_values('YEAR')

Aron = ofns['PLAYER'].map(lambda x: x.startswith(players[1]))
aron = ofns[Aron]
aron = aron.sort_values('YEAR')

Carson = ofns['PLAYER'].map(lambda x: x.startswith(players[2]))
carson = ofns[Carson]
carson = carson.sort_values('YEAR')

Ben = ofns['PLAYER'].map(lambda x: x.startswith(players[3]))
ben = ofns[Ben]
ben = ben.sort_values('YEAR')

Drew = ofns['PLAYER'].map(lambda x: x.startswith(players[4]))
drew = ofns[Drew]
drew = drew.sort_values('YEAR')

Tom = ofns['PLAYER'].map(lambda x: x.startswith(players[5]))
tom = ofns[Tom]
tom = tom.sort_values('YEAR')

Kellen = ofns['PLAYER'].map(lambda x: x.startswith(players[6]))
kellen = ofns[Kellen]
kellen = kellen.sort_values('YEAR')

Philip = ofns['PLAYER'].map(lambda x: x.startswith(players[7]))
philip = ofns[Philip]
philip = philip.sort_values('YEAR')

Matt = ofns['PLAYER'].map(lambda x: x.startswith(players[8]))
matt = ofns[Matt]
matt = matt.sort_values('YEAR')

Jay = ofns['PLAYER'].map(lambda x: x.startswith(players[9]))
jay = ofns[Jay]
jay = jay.sort_values('YEAR')

# Plots graph for 10 players based on Yards
def plot_yards(player) :
    # Ploting the graph for count of Passing yards based on Year
    objects = ("2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017")

    y_pos = np.arange(len(objects))
    performance = [manning["YDS"],aron["YDS"],carson["YDS"],ben["YDS"],drew["YDS"],tom["YDS"],kellen["YDS"],philip["YDS"],matt["YDS"],jay["YDS"]]

    colour = ['aqua','black','blue','brown','darkgreen','gold','grey','navy','plum','red']
     
    for i in range(player) :
        plt.plot(y_pos, performance[i], label = players[i],color=colour[i])


    plt.xticks(y_pos, objects,rotation=90)
    plt.xlabel('YEAR')
    plt.ylabel('Yards')
    plt.title('NFL QuaterBack analysis based on Passing yards')
    plt.legend()
    plt.show()


# Plots graph for 10 players based on TouchDowns
def plot_touchdown(player) :

    # Ploting the graph for count of Touch Down based on Year
    objects = ("2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017")

    y_pos = np.arange(len(objects))
    performance = [manning["TD"],aron["TD"],carson["TD"],ben["TD"],drew["TD"],tom["TD"],kellen["TD"],philip["TD"],matt["TD"],jay["TD"]]

    colour = ['aqua','black','blue','brown','darkgreen','gold','grey','navy','plum','red']
     
    for i in range(player) :
        plt.plot(y_pos, performance[i], label = players[i],color=colour[i])


    plt.xticks(y_pos, objects,rotation=90)
    plt.xlabel('YEAR')
    plt.ylabel('Touch Down')
    plt.title('NFL QuaterBack analysis based on Touch Down')
    plt.legend()
    plt.show()


# Plots graph for 10 players based on Percentage Completion
def plot_PCT(player) :
    # Ploting the graph for count of Percentage Completion based on Year

    objects = ("2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017")

    y_pos = np.arange(len(objects))
    performance = [manning["PCT"],aron["PCT"],carson["PCT"],ben["PCT"],drew["PCT"],tom["PCT"],kellen["PCT"],philip["PCT"],matt["PCT"],jay["PCT"]]

    colour = ['aqua','black','blue','brown','darkgreen','gold','grey','navy','plum','red']
     
    for i in range(player) :
        plt.plot(y_pos, performance[i], label = players[i],color=colour[i])


    plt.xticks(y_pos, objects,rotation=90)
    plt.xlabel('YEAR')
    plt.ylabel('Percentage Completion')
    plt.title('NFL QuaterBack analysis based on Percentage Completion')
    plt.legend()
    plt.show()
    
# Destroys the instance created when, the number of players entered is more than 10
def stop(root) :
    root.destroy()

def var_states():

   if (int(var.get())>10) :
        window = Tk()
        button = Button(window, text='Only top 10',command=lambda: stop(window),bg="red")
        button.pack()
        window.mainloop()

   if (var1.get()) :
       plot_touchdown(int(var.get()))

   if (var2.get()) :
       plot_yards(int(var.get()))

   if (var3.get()) :
       plot_PCT(int(var.get()))

def quit_me(root):
    root.destroy()

# GUI Code for the application     
label = Label(master, text="No. of Players(Top Ten)").grid(row=0,column=0, sticky=W)
var = IntVar()
Entry(master,textvariable=var).grid(row=0,column=1,sticky=W)
label = Label(master,text="Select any one Option").grid(row=1,sticky=W)
var1 = IntVar()
Checkbutton(master, text="No. of Touch downs", variable=var1).grid(row=2, sticky=W)
var2 = IntVar()
Checkbutton(master, text="No. of Yards", variable=var2).grid(row=3, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Percentage Completion", variable=var3).grid(row=4, sticky=W)
Button(master, text='Quit', command=lambda: quit_me(master)).grid(row=5, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=6, sticky=W, pady=4)


master.mainloop()

