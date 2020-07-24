import tkinter
from tkinter.messagebox import askquestion
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk





class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("covid-19.jpeg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES),self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image = self.background_image)


root = Tk()


root.overrideredirect(False)

e = Example(root)
e.pack()
e.focus_set()
root.configure(background='AntiqueWhite1')

root.title(" Login successful!.     "
               " Welcome to the interface for COVID-19 Self test.")
var = ("Hey!? How are you doing?")
label = Label(root, textvariable=var, relief=RAISED, bg='yellow')




def open():
    textbox = ScrolledText()
    # textbox.grid()
    filename = askopenfilename(initialdir='c:\\python31\\', filetypes=[('Text files', '.txt'), ('All files', '*')])
    s = open('5-year-mean-1882-2014').read()
    textbox.insert(1.0, s)


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def nothing():
    from tkinter import messagebox
    msg = messagebox.showinfo("Warning", "No function assigned yet!.")


def helpline():
    from tkinter import messagebox
    msg = messagebox.showinfo("Problems with operations?", "Call OGUNJOBI Victor: +2348148918155.")


def About():
    from tkinter import messagebox
    msg = messagebox.showinfo("About this Project:",
                              'This is a self project by OGUNJOBI Victor as regards the pandemic COVID-19. ')

def submit():
    from tkinter import messagebox

    E1_short = E1.get()
    E2_short = E2.get().capitalize()
    E3_short = E3.get().capitalize()
    E4_short = E4.get().capitalize()
    E5_short = E5.get().capitalize()
    E6_short = spin.get()
    E7_short = E6.get().capitalize()
    E8_short = E7.get().capitalize()    # For Name
    E9_short = E8.get()                 # For Age
    E10_short = E9.get().capitalize()    # For Sex
    E11_short = E10.get()
    E12_short = E11.get()


    if (E8_short.isalpha()) and (E9_short.isdigit()) and (E10_short=='Male' or E10_short=='Female') and (E1_short.isdigit()) and (E2_short == 'Yes' or E2_short == 'No') and (E3_short == 'Sometimes' or E3_short == 'Very often' or E3_short == 'Not at all') and (E4_short == 'Yes' or E4_short == 'No') and (E6_short.isdigit()) and (E7_short == 'Home' or E7_short == 'Not home') and (E12_short.isdigit()):
        msg = messagebox.showinfo('Form submission successful!.', 'Check email for response/result.'
                                                                      ' Thank you ' + E8_short + ', for using this service.')

        if ((int(E1_short) > 38) and (E2_short == 'Yes') and (E3_short == 'Very often') and (E4_short == 'Yes') and (
                E5_short == 'Dry cough' or E5_short == 'Tiredness' or E5_short == 'Chest pain') and (int(E6_short)>=50) and (str(E11_short).endswith('@gmail.com'))) or (
                (int(E1_short) > 38) and (E2_short == 'Yes') and (E3_short == 'Sometimes') and (E4_short == 'Yes') and (
                E5_short == 'Dry cough' or E5_short == 'Intermittent sweats' or E5_short == 'Tiredness') and (int(E6_short)>=50) and (str(E11_short).endswith('@gmail.com'))) or ((int(E1_short) > 38) and (E2_short == 'Yes') and (E3_short == 'Sometimes') and (E4_short == 'Yes') and (
                E5_short == 'Dry cough' or E5_short == 'Tiredness' or E5_short == 'Chest pain') and (int(E6_short)>=50) and (str(E11_short).endswith('@gmail.com'))):

            msg = messagebox.showinfo('Response - ' + '( ' + E8_short + "'s test result" + ' ) .', "The result from this survey is terrible!. "
                                                   'Please stay home and put a call through NCDC: 0800 970000 10.')

        else:
            msg = messagebox.showinfo('Response - ' + '( ' + E8_short + "'s test result" + ' ) .','The result from the survey is cool. You might be sick of another illness, But you are tested negative to COVID-19. '
                                                  ' Stay safe at home or wherever you go. Thank You!.')




    else:
        msg4 = messagebox.showinfo('Error in input(s) !', 'Give all answers in appropriate formats. Thank You!.')



    return



def quit():
    answer = askquestion(title='Quit?', message='Really quit?')
    if answer == 'yes':
        root.destroy()



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0, bd=2, bg='orange')
filemenu.add_command(label="New", command=nothing)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=nothing)
filemenu.add_command(label="Save as...", command=nothing)
filemenu.add_command(label="Close", command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0, bd=2, bg='brown')
editmenu.add_command(label="Undo", command=nothing)

editmenu.add_separator()
editmenu.add_command(label="Cut", command=nothing)
editmenu.add_command(label="Copy", command=nothing)
editmenu.add_command(label="Paste", command=nothing)
editmenu.add_command(label="Delete", command=nothing)
editmenu.add_command(label="Select All", command=nothing)
menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0, bd=2, bg='purple')
helpmenu.add_command(label="Help Index", command=nothing)
helpmenu.add_command(label="About...", command=About)
helpmenu.add_command(label='Call Author?.', command=helpline)
menubar.add_cascade(label="Help", menu=helpmenu)
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label='About Project', command=About)

root.config(menu=menubar)




command1 = Label(root, text="Name :", font=('Hobo Std', 13, 'bold'), borderwidth='3', foreground='darkblue')
command1.place(x=20, y=215)

command2 = Label(root, text="Age :", font=('Hobo Std', 13, 'bold'), borderwidth='3',
                 foreground='darkblue')
command2.place(x=20, y=265)

command3 = Label(root, text="Sex :", font=('Hobo Std', 13, 'bold'), borderwidth='3', foreground='darkblue')
command3.place(x=20, y=315)

command4 = Label(root, text="Email address:", font=('Adobe Caslon Pro Bold', 10, 'bold'), borderwidth='4', foreground='darkred')
command4.place(x=50, y=635)

command5 = Label(root, text="Phone Number:", font=('Adobe Caslon Pro Bold', 10, 'bold'), borderwidth='4', foreground='darkred')
command5.place(x=450, y=635)

command6 = Label(root, text="Current Body Temperature i.e 25 :", font=('Perpetua', 10, 'bold'), borderwidth='4', foreground='darkblue')
command6.place(x=930, y=215)

command7 = Label(root, text="Had body ache in the last few days?:", font=('Perpetua', 10, 'bold'), borderwidth='3', foreground='darkblue')
command7.place(x=930, y=265)

command8 = Label(root, text="How would you rate your sweating at \n normal condition in the last few days?:", font=('Perpetua', 10, 'bold'), borderwidth='3', foreground='darkblue')
command8.place(x=930, y=315)
command9 = Label(root, text="Rapid heart rate/palpitations? :", font=('Perpetua', 10, 'bold'), borderwidth='4', foreground='darkblue')
command9.place(x=930, y=365)
command10 = Label(root, text="Others (Choose one):", font=('Perpetua', 10, 'bold'), borderwidth='4', foreground='darkblue')
command10.place(x=930, y=415)
command11 = Label(root, text="Rate the way you're feeling:", font=('Perpetua', 10, 'bold'), borderwidth='4', foreground='darkblue')
command11.place(x=1030, y=465)
command12 = Label(root, text="Where are you presently? "
                             "(Home or Not Home) :", font=('Perpetua', 10, 'bold'), borderwidth='4', foreground='darkblue')
command12.place(x=930, y=515)

E1 = StringVar()
E2 = StringVar()
E3 = StringVar()
E4 = StringVar()
E5 = StringVar()
E6 = StringVar()
E7 = StringVar()     # For Name
E8 = StringVar()    # For Age
E9 = StringVar()    # For Sex
E10 = StringVar()  # For email
E11= StringVar()   # For phone number



ent1 = Entry(root, textvariable=E7)         # For Name
ent1.place(x=101, y=219)
ent2 = Entry(root, textvariable=E8, show='*')       # For Age
ent2.place(x=90, y=269)
ent3 = Entry(root, textvariable=E9)                 # For Sex
ent3.place(x=90, y=321)
ent4 = Entry(root, textvariable=E10, show='*')        # For email address
ent4.place(x=160, y=640)
ent5 = Entry(root, textvariable=E11)        # For phone number
ent5.place(x=560, y=640)
ent6 = Entry(root, textvariable=E1)        # First enquiry
ent6.place(x=1150, y=219)
ent7 = Entry(root, textvariable=E2)        # Second enquiry
ent7.place(x=1150, y=269)
ent8 = Entry(root, textvariable=E3)        # Third enquiry
ent8.place(x=1160, y=320)
ent9 = Entry(root, textvariable=E4)        # Fourth enquiry
ent9.place(x=1150, y=370)
ent10 = ttk.Combobox(root, textvariable=E5, values= ['Dry cough',
    'Headache','Intermittent sweats','Tiredness', 'Sore throat', 'Chest pain', 'Conjuctivitis','Diarrhoea'])       # Fifth enquiry  -Entry for 'Others'

ent10.place(x=1150, y=420)
spin = Spinbox(root, from_ = 0, to_ =100)       # Sixth enquiry - Rate the way you are feeling.
spin.place(x=1200, y=468)
ent11 = Entry(root, textvariable=E6)    # Seventh enquiry - Where are you presently?.
ent11.place(x=1210, y=517)



submitButton = Button(root, text="Submit Form", font=('batang', 10, 'bold'), borderwidth='4', foreground='black',
                         command=submit)
submitButton.place(x=1100, y=655)




#if E2_short != 'Yes' or E2_short != 'No':
#    msg = messagebox.showinfo('Error in input!',
#                              'Your response in Body ache should either be YES or NO. Please try again.')

#
#while E3_short != 'Sometimes' or E3_short != 'Very often' or E4_short != 'Not at all':
#    msg = messagebox.showinfo('Error in input!',
#                              'Your response in Rapid heart rate/palpitaions should either be:'
#                              'Sometimes, Very Often, or Not at all. Please try again.')
#    break
#while E4_short != 'YES' or E4_short != 'NO':
#    msg = messagebox.showinfo('Error in input!',
#                              'Your response in Rapid heart rate/palpitaions should either be YES or NO. Please try again.')
#    break
#while E7_short != 'Home' or E7_short != 'Not home':
#    msg = messagebox.showinfo('Error in input!',
#                              'Your response in Where are you Presently? should either be:'
#                              'Home or Not home. Please try again.')
#
#    break















    
root.mainloop()