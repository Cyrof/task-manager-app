import tkinter as tk
import tkinter as ttk
from turtle import right, width

# app = tk.Tk()
# app.title("Task Manager")
# app.geometry("900x650")

# main_container = ttk.Frame(app)


# frame_left = ttk.Frame(main_container, width=200, height=650)
# frame_right = ttk.Frame(main_container, width=700, height=650, bg="#242854")

# main_container.grid_rowconfigure(1, weight=1)
# main_container.grid_columnconfigure(0, weight=1)

# frame_left.grid(row=0, sticky="w")
# frame_right.grid(row=0, sticky="e")

# main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# app.mainloop()

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Task Manager")
        self.geometry("900x650")
        container = ttk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, ProjectPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainPage)

        # frame = MainPage(container, self)
        # self.frames[MainPage] = frame

        # frame.grid(row=0, column=0, sticky="nsew")
        # self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class MainPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # main container to store left and right frame
        main_container = ttk.Frame(self)

        # create left and right frame
        frame_left = ttk.Frame(main_container, width=200, height=650)
        frame_right = ttk.Frame(
            main_container, width=700, height=650, bg="#242854")
        label1 = ttk.Label(frame_right, text="This is the main page", bg="#242854", fg="White")
        label1.place(relx=.5, rely=.5)
        button1 = ttk.Button(frame_right, text="project", command=lambda: controller.show_frame(ProjectPage))
        button1.place(relx=.2, rely=.2)

        # main container grid configuration
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        # position each frame respectively
        frame_left.grid(row=0, sticky="w")
        frame_right.grid(row=0, sticky="e")

        # pack main container and display it on window
        main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class ProjectPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # main container to store left and right frame
        project_container = ttk.Frame(self)

        # create left and right frame
        frame_left = ttk.Frame(project_container, width=200, height=650)
        frame_right = ttk.Frame(
            project_container, width=700, height=650, bg="#242854")
        label1 = ttk.Label(frame_right, text="This is the project page", bg="#242854", fg="White")
        label1.place(relx=.5, rely=.5)
        button1 = ttk.Button(frame_right, text="Main", command=lambda: controller.show_frame(MainPage))
        button1.place(relx=.2, rely=.2)

        # main container grid configuration
        project_container.grid_rowconfigure(1, weight=1)
        project_container.grid_columnconfigure(0, weight=1)

        # position each frame respectively
        frame_left.grid(row=0, sticky="w")
        frame_right.grid(row=0, sticky="e")

        # pack main container and display it on window
        project_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




if __name__ == "__main__":
    app = GUI()
    app.mainloop()
    # root = tk.Tk()
    # root.title("Task Manager")
    # root.geometry("900x650")
    # gui = GUI(root)
    # root.mainloop()
