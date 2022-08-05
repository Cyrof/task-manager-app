import tkinter as tk
import tkinter as ttk

# # GUI class for task manager app
# class GUI(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         """ config main container to be shwon on gui window
#         :instance variable self.title: set title 
#         :instance variable self.geometry: set the starting window size
#         :variable container: configure container size and grid
#         :instance variable self.frames: store frames of other classes
#         :return:
#         """
#         self.title("Task Manager")
#         self.geometry("900x650")
#         container = ttk.Frame(self)
#         container.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}

#         for F in (MainPage, ProjectPage):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
        
#         self.show_frame(MainPage)


#     def show_frame(self, cont):
#         """ Display frame onto window
#         :param cont: take in class instance frame
#         :return:
#         """
#         frame = self.frames[cont]
#         frame.tkraise()



# class MainPage(ttk.Frame):

#     def __init__(self, parent, controller):
#         ttk.Frame.__init__(self, parent)

#         # main container to store left and right frame
#         main_container = ttk.Frame(self, highlightcolor="black", highlightthickness=2)
#         l = ttk.Label(main_container, text="Main container")
#         l.place(relx=.1, rely=.1)

#         # create left and right frame
#         frame_left = ttk.Frame(main_container, width=200, height=650, highlightthickness=2, highlightbackground="blue")
#         label2 = ttk.Label(frame_left, text="This is the main page")
#         label2.place(relx=.1, rely=.2)

#         frame_right = ttk.Frame(
#             main_container, width=700, height=650, bg="#242854")
#         label1 = ttk.Label(frame_right, text="This is the main page", bg="#242854", fg="White")
#         label1.place(relx=.5, rely=.5)
#         button1 = ttk.Button(frame_right, text="project", command=lambda: controller.show_frame(ProjectPage))
#         button1.place(relx=.2, rely=.2)

#         # main container grid configuration
#         main_container.grid_rowconfigure(1, weight=1)
#         main_container.grid_columnconfigure(0, weight=1)

#         # position each frame respectively
#         frame_left.grid(row=0, column=0)
#         frame_right.grid(row=0, column=1)

#         # pack main container and display it on window
#         main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# class ProjectPage(ttk.Frame):

#     def __init__(self, parent, controller):
#         ttk.Frame.__init__(self, parent)

#         # main container to store left and right frame
#         project_container = ttk.Frame(self)

#         # create left and right frame
#         frame_left = ttk.Frame(project_container, width=200, height=650)
#         frame_right = ttk.Frame(
#             project_container, width=700, height=650, bg="#242854")
#         label1 = ttk.Label(frame_right, text="This is the project page", bg="#242854", fg="White")
#         label1.place(relx=.5, rely=.5)
#         button1 = ttk.Button(frame_right, text="Main", command=lambda: controller.show_frame(MainPage))
#         button1.place(relx=.2, rely=.2)

#         # main container grid configuration
#         project_container.grid_rowconfigure(1, weight=1)
#         project_container.grid_columnconfigure(0, weight=1)

#         # position each frame respectively
#         frame_left.grid(row=0, sticky="w")
#         frame_right.grid(row=0, sticky="e")

#         # pack main container and display it on window
#         project_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




# if __name__ == "__main__":
#     app = GUI()
#     app.mainloop()
#     # root = tk.Tk()
#     # root.title("Task Manager")
#     # root.geometry("900x650")
#     # gui = GUI(root)
#     # root.mainloop()


class GUI:
    def __init__(self, root):
        self.__window = root
        self.__container = ttk.Frame(self.__window)
        self.mainPage()
        self.__container.pack()
        
    
    def mainPage(self):
        b1 = ttk.Button(self.__container, text="Add Tasks", command= lambda: self.createTask())
        b1.pack()
        
    
    def createCheck(self, task):
        self.check = ttk.Checkbutton(self.__container, text=task)
        self.check.pack()

    def submit(self):
        text = self.entry1.get()
        print(text)
        self.entry1.pack_forget()
        self.sub.pack_forget()
        self.createCheck(text)

    def createTask(self):
        self.entry1 = tk.Entry(self.__container)
        self.entry1.pack()
        self.sub = ttk.Button(self.__container, text="submit", command=lambda: self.submit())
        self.sub.pack()
        

if __name__ == "__main__":
    app = tk.Tk()
    gui = GUI(app)
    app.mainloop()
