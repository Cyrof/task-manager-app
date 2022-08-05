import tkinter as tk
import tkinter as ttk

class window(tk.Tk):
    def __init__(self):
        super().__init__()

        # adding title to the window 
        self.wm_title("Task Manager")

        # creating a frame and assigning it to a container
        container = tk.Frame(self, height=650, width=900)
        
        # specifiying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        


#  Page class to make frames visible / hidden
# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#     def show(self):
#         self.lift()

# class MainPage(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="This is the main page")
#         # label.pack(side="top", fill="both", expand=True)

#         b_frame_right = tk.Frame(self, bg="#242854")
#         l2 = tk.Label(self, text="this is the right side frame")
#         frame_left = tk.Frame(self)
#         l3 = tk.Label(self, text="This is the left side frame")
#         b_frame_right.grid(row=0, column=1)
#         frame_left.grid(row=0, column=0)


# class ProjectFolder(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="This is the project folders page")
#         label.pack(side="top", fill="both", expand=True)

# class TasksPage(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="This is the tasks page")
#         label.pack(side="top", fill="both", expand=True)

# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = MainPage(self)
#         p2 = ProjectFolder(self)
#         p3 = TasksPage(self)

#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)

#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")

#         p1.show()

# if __name__ == "__main__":
#     window = tk.Tk()
#     main = MainView(window)
#     main.pack(side="top", fill="both", expand=True)
#     window.wm_geometry("900x650")
#     window.mainloop()
