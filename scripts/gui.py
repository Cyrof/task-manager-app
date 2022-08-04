import tkinter as tk

# Page class to make frames visible / hidden
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the main page")
        label.pack(side="top", fill="both", expand=True)

class ProjectFolder(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the project folders page")
        label.pack(side="top", fill="both", expand=True)

class TasksPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the tasks page")
        label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainPage(self)
        p2 = ProjectFolder(self)
        p3 = TasksPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    window = tk.Tk()
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.wm_geometry("400x400")
    window.mainloop()

# class GUI(tk.Tk):

#     # __init__ function for class GUI
#     def __init__(self, *args, **kwargs):

#         # __init__ function for class Tk
#         tk.Tk.__init__(self, *args, **kwargs)

#         # creating a container
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)

#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#         container.configure(background="#242854")

#         # initialize fraces to an empty array
#         self.frames = {}

#         # iterating through a tuple consisting 
#         # of the different page layouts
#         for F in (StartPage):
#             frame = F(container, self)

#             # initialise frame of that object from
#             # startpage, page1, page2 respectively with
#             # for loop
#             self.frames[F] = frame

#             frame.grid(row=0, column=0, sticky="nsew")
        
#         self.show_frame(StartPage)

#     # to display the current frame passed as parameter
#     def show_frame(self, cont):
#         frame= self.frames[cont]
#         frame.tkraise()

# # first window frame Startpage
# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         # label of fram layout 2
#         label = ttk.Label(self, text="StartPage")

#         # putting the grid in its place by using grid
#         label.grid(row=0, column=4, padx=10,pady=10)

#         # button1 = ttk.Button(self, text="Page 1")
#         # command = lambda : controller.show_frame(Page1)
    


    


    

# if __name__ == "__main__":
#     app = GUI()
#     app.mainloop()

    