import tkinter as tk
from tkinter import ttk

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

    