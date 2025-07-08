# game integration
import sause as gt
from tkinter import *

class Organizer:
    def __init__(self, lib):
        self.lib = lib
        self.description_txt = self.lib['description']
        self.goal_txt = self.lib['goal']
        self.get_choices()
        self.get_results()
        self.next = self.lib['next_lib']

    def get_choices(self):
        length = len(self.lib['choices'])
        self.ran = range(0,(length))
        self.choices = []
        for x in self.ran:
            self.choices.append(self.lib['choices'][x])
        self.dead = []
        self.alive = []
        for y in self.ran:
            if y == self.lib['right']:
                self.right = self.lib['choices'][y]
            elif y in self.lib['dead']:
                self.dead.append(self.lib['choices'][y])
            elif y in self.lib['alive']:
                self.alive.append(self.lib['choices'][y])
            else:
                print("Error")
        # creates: self.right, self.dead, and self.alive

    def get_results(self):
        self.results = self.lib['results']

class ExternalApp(Organizer):
    def __init__(self, lib):
        Organizer.__init__(self, lib)
        self.window = Tk()
        self.window.geometry("800x800")
        self.initialize_frames()
        self.read_options()
        #self.alt_frames()
        self.create_buttons()
        self.window.mainloop()

    def read_options(self):
        self.desc_mes = Message(self.topframe, text=self.description_txt)
        self.desc_mes.configure(font=("Times New Roman", 12))
        self.desc_mes.pack(fill=X)
        self.goal_mes = Message(self.midframe, text=self.goal_txt)
        self.goal_mes.configure(font=("Times New Roman", 12))
        self.goal_mes.pack(fill=X)

    def initialize_frames(self):
        # whole frame, for all internal elements
        self.mainframe = Frame(self.window)
        self.mainframe.config(highlightthickness = 1, highlightbackground = 'black')
        self.mainframe.pack()
        # topframe, for name and description
        self.topframe = Frame(self.mainframe)
        self.topframe.pack(fill=X)
        # mid frame, for goal
        self.midframe = Frame(self.mainframe)
        self.midframe.pack(fill=X)
        # lwr frame, for buttons
        self.lwrframe = Frame(self.mainframe)
        self.lwrframe.pack(fill=X)

        self.name = Label(self.topframe, text="Panic Room", borderwidth=2, relief = "raised")
        self.name.configure(font=("Times New Roman", 16, "bold"))
        self.name.pack(pady=4)


    def create_buttons(self):
        if len(self.choices) == 1:
            button1 = Button(self.lwrframe, text=self.choices[0], command= lambda: self.click_function(self.choices[0]))
            button1.configure(font=("Times New Roman", 12))
            button1.pack(fill=X, padx=4, pady=4)
        elif len(self.choices) == 2:
            button1 = Button(self.lwrframe, text=self.choices[0], command = lambda: self.click_function(self.choices[0]))
            button1.configure(font=("Times New Roman", 12))
            button1.pack(fill=X, padx=4, pady=4)
            button2 = Button(self.lwrframe, text=self.choices[1], command = lambda: self.click_function(self.choices[1]))
            button2.configure(font=("Times New Roman", 12))
            button2.pack(fill=X, padx=4, pady=4)
        elif len(self.choices) == 3:
            button1 = Button(self.lwrframe, text=self.choices[0], command = lambda: self.click_function(self.choices[0]))
            button1.configure(font=("Times New Roman", 12))
            button1.pack(fill=X, padx=4, pady=4)
            button2 = Button(self.lwrframe, text=self.choices[1], command = lambda: self.click_function(self.choices[1]))
            button2.configure(font=("Times New Roman", 12))
            button2.pack(fill=X, padx=4, pady=4)
            button3 = Button(self.lwrframe, text=self.choices[2], command = lambda: self.click_function(self.choices[2]))
            button3.configure(font=("Times New Roman", 12))
            button3.pack(fill=X, padx=4, pady=4)
        elif len(self.choices) == 4:
            button1 = Button(self.lwrframe, text=self.choices[0], command = lambda: self.click_function(self.choices[0]))
            button1.configure(font=("Times New Roman", 12))
            button1.pack(fill=X, padx=4, pady=4)
            button2 = Button(self.lwrframe, text=self.choices[1], command = lambda: self.click_function(self.choices[1]))
            button2.configure(font=("Times New Roman", 12))
            button2.pack(fill=X, padx=4, pady=4)
            button3 = Button(self.lwrframe, text=self.choices[2], command = lambda: self.click_function(self.choices[2]))
            button3.configure(font=("Times New Roman", 12))
            button3.pack(fill=X, padx=4, pady=4)
            button4 = Button(self.lwrframe, text=self.choices[3], command = lambda: self.click_function(self.choices[3]))
            button4.configure(font=("Times New Roman", 12))
            button4.pack(fill=X, padx=4, pady=4)
        elif len(self.choices) == 5:
            button1 = Button(self.lwrframe, text=self.choices[0], command = lambda: self.click_function(self.choices[0]))
            button1.configure(font=("Times New Roman", 12))
            button1.pack(fill=X, padx=4, pady=4)
            button2 = Button(self.lwrframe, text=self.choices[1], command = lambda: self.click_function(self.choices[1]))
            button2.configure(font=("Times New Roman", 12))
            button2.pack(fill=X, padx=4, pady=4)
            button3 = Button(self.lwrframe, text=self.choices[2], command = lambda: self.click_function(self.choices[2]))
            button3.configure(font=("Times New Roman", 12))
            button3.pack(fill=X, padx=4, pady=4)
            button4 = Button(self.lwrframe, text=self.choices[3], command = lambda: self.click_function(self.choices[3]))
            button4.configure(font=("Times New Roman", 12))
            button4.pack(fill=X, padx=4, pady=4)
            button5 = Button(self.lwrframe, text=self.choices[4], command = lambda: self.click_function(self.choices[4]))
            button5.configure(font=("Times New Roman", 12))
            button5.pack(fill=X, padx=4, pady=4)
        else:
            print("Import Error, no more than 5 buttons allowed.")

    def click_function(self, string):
        if string == self.right:
            self.alt_right(string)
        elif string in self.alive:
            self.alt_alive(string)
        elif string in self.dead:
            self.alt_dead(string)
        else:
            print("IDK wtf just happened.")


    def alt_dead(self, string):
        self.mainframe.pack_forget()
        alt_frame = Frame(self.window)
        alt_frame.config(highlightthickness = 1, highlightbackground = 'black')
        alt_frame.pack()
        upper = Frame(alt_frame)
        upper.pack()
        lower = Frame(alt_frame)
        lower.pack()
        mess = Message(upper, text= self.results[string])
        mess.configure(font=("Times New Roman", 12))
        mess.pack()
        mess2 = Message(upper, text="Would you like to try again?")
        mess2.configure(font=("Times New Roman", 12))
        mess2.pack()
        yes = Button(lower, text="Yes!", command = lambda : self.start_over(alt_frame))
        yes.configure(font=("Times New Roman", 12))
        yes.pack(fill=X, padx=4, pady=4)
        no = Button(lower, text="No!", command = lambda : self.window.destroy())
        no.configure(font=("Times New Roman", 12))
        no.pack(fill=X, padx=4, pady=4)
        alt_frame.tkraise()

    def start_over(self, frame):
        frame.destroy()
        self.window.destroy()
        task_1 = ExternalApp(gt.libtsk1)


    def alt_alive(self, string):
        self.mainframe.pack_forget()
        alt_frame = Frame(self.window)
        alt_frame.config(highlightthickness = 1, highlightbackground = 'black')
        alt_frame.pack()
        upper = Frame(alt_frame)
        upper.pack()
        lower = Frame(alt_frame)
        lower.pack()
        mess = Message(upper, text= self.results[string])
        mess.configure(font=("Times New Roman", 12))
        mess.pack()
        mess2 = Message(upper, text="At least you're still alive.")
        mess2.configure(font=("Times New Roman", 12))
        mess2.pack()
        button = Button(lower, text="OKAY!", command = lambda : self.return_to(alt_frame))
        button.configure(font=("Times New Roman", 12))
        button.pack(fill=X, padx=4, pady=4)
        alt_frame.tkraise()

    def return_to(self, frame):
        frame.pack_forget()
        self.mainframe.pack()

    def alt_right(self, string):
        self.mainframe.pack_forget()
        alt_frame = Frame(self.window)
        alt_frame.config(highlightthickness = 1, highlightbackground = 'black')
        alt_frame.pack()
        upper = Frame(alt_frame)
        upper.pack()
        lower = Frame(alt_frame)
        lower.pack()
        mess = Message(upper, text= self.results[string])
        mess.configure(font=("Times New Roman", 12))
        mess.pack()
        button = Button(lower, text="OKAY!", command = lambda : self.next_task())
        button.configure(font=("Times New Roman", 12))
        button.pack(fill=X, padx=4, pady=4)
        alt_frame.tkraise()

    def next_task(self):
        self.window.destroy()
        next_task = ExternalApp(self.next)


task_1 = ExternalApp(gt.libtsk1)
