import tkinter as tk
from tkinter import ttk
import datetime
from db import Task


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        """ Config main container to be shown on GUI window
        :instance variable self.title: set the title of the application
        :instance variable self.geometry: set the starting window size
        :instance variable self.resizable: disable resize from window
        :variable container: configure container size and grid
        :instance variable self.frames: store frames of other classes
        :return:
        """
        # configure GUI window
        self.title("Task Manager")
        self.geometry("900x650")
        self.resizable(height=False, width=False)

        # create the container to display other class frames
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create frame dictionary to store frames
        self.__frames = {}

        for F in (MainPage, ProjectPage):
            frame = F(container, self)
            self.__frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        """ Display frame onto window
        :param cont: take in class instance frame
        :return:
        """
        frame = self.__frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        """ init function for MainPage class 
        :param parent: main frame container from GUI class
        :param controller: instance of GUI class
        :return:
        """
        self.__db = Task()

        # inherit from parent
        tk.Frame.__init__(self, parent)

        # main container of MainPage class
        main_container = tk.Frame(self, bg="#242854")

        # create left and right frame
        self.__task_list_frame = self.task_list_frame(main_container)
        self.__task_detail_frame = self.task_detail_frame(main_container)
        side_navbar = self.side_nav_bar_frame(main_container)
        sep = ttk.Separator(main_container, orient="vertical")

        # config main container grid
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        # place left and right frame into container using grid
        side_navbar.grid(row=0, column=0)
        # left_frame.pack(side=tk.LEFT)
        # right_frame.pack(side=tk.RIGHT, padx=25, pady=(125, 25))
        # right_frame.grid(row=0, column=1, padx=25, pady=(125, 25))
        self.__task_list_frame.grid(
            row=0, column=1, padx=(25, 0), pady=(125, 25))
        sep.grid(row=0, column=2)
        self.__task_detail_frame.grid(
            row=0, column=3, padx=(0, 25), pady=(125, 25))

        # display container using pack
        main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # function to create canvas
    def create_canvas(self, parent, width=None, height=None, bg=None, border_width=None, border_color=None):
        """ Create canvas object
        :param parent: tkinter obj instance
        :param width: width specification for canvas obj
        :param height: height specification for canvas obj
        :param bg: background color
        :param fg: foregrounf color 
        :return canvas obj:
        """
        canvas = tk.Canvas(parent, width=width, height=height,
                           bg=bg, highlightthickness=border_width, highlightcolor=border_color)

        return canvas
    
    def display_task(self, frame):
        """ Display all tasks onto task mangaer window
        :param:
        :return:
        """
        all_task = self.__db.get_all_data()

        # ycoord = 0.02
        # for task in all_task:
            
        #     # match case to get color base on priority level
        #     color = "white"
        #     match task[2]:
        #         case 'i':
        #             color = "red"
        #         case 'u':
        #             color = "#ffbf00"
        #         case 'n':
        #             color = "#01c2ff"

        #     # create canvas frame
        #     c = self.create_canvas(frame, border_color="red", border_width=2)

        #     # create int var for checkbox
        #     var = tk.IntVar()
        #     task_checkbox = tk.Checkbutton(c, variable=var, onvalue="Completed", offvalue="Incomplete")

        #     # create clickable task name text
        #     task_name_button = tk.Button(c, text=task[1], relief=tk.FLAT, font=('calibri', 12, 'bold'))

        #     # create color box to display priority level
        #     # color_box = tk.Checkbutton(c, selectcolor=color, state=tk.DISABLED, disabledforeground=color)
        #     pixel = tk.PhotoImage(width=1, height=1)
        #     color_box = tk.Button(c, bg=color, state=tk.DISABLED, height=1, relief=tk.FLAT, padx=0, pady=0, image=pixel)

        #     task_checkbox.grid(row=0, column=0)
        #     task_name_button.grid(row=0, column=1)
        #     color_box.grid(row=1, column=0, pady=0, padx=0)

        #     c.place(relx=0.1, rely=ycoord)
        #     ycoord += 0.09


        # create canvas for task list frame
        # main_c = tk.Canvas(frame)

        # # create scroll bar for canvas
        # scroll = tk.Scrollbar(frame)
        # scroll.place(relx=0.95, rely=0, relheight=1)
        # scroll.config(command=main_c.yview)
        
        # main_c.configure()
        # # create ycoord for increment
        # ycoord = 0.02
        # # create for loop to print out all data
        # for x in range(100):
        #     # create frame to store one task 
        #     task_frame = tk.Frame(main_c)
        #     # print(f'{str(x)}')
        #     # create int var for checkbox
        #     var = tk.IntVar()
        #     task_checkbox = tk.Checkbutton(task_frame, variable=var, onvalue="Completeted", offvalue="Incomplete")

        #     # l = tk.Label(task_frame, text=f"This is a test line")
        #     # l.grid(row=0, column=1)
        #     l = tk.Label(task_frame, text=f"this is a test {str(x)}")
        #     l.grid(row=0, column=0)

        #     task_frame.pack()
        
        # def on_configure(event):
        #     main_c.configure(scrollregion=main_c.bbox("all"))
        
        # main_c.bind('<Configure>', on_configure)
        # main_c.config(height=500, width=325)
        # main_c.config(yscrollcommand=scroll.set)
        # main_c.place(relx=0, rely=0)

        # inner function to config scrollregion
        def on_configure(event):
            main_c.configure(scrollregion=main_c.bbox('all'))

        # create canvas for task list frame 
        main_c = tk.Canvas(frame)
        main_c.place(relx=0, rely=0, relheight=1, relwidth=1)

        # frame to add stuff to screen 
        canvas_frame = tk.Frame(main_c)
        # resize the canvas scroll region each time the size of the frame changes
        frame.bind('<Configure>', on_configure)
        # display frame inside the canvas
        main_c.create_window(0, 0, window=canvas_frame)

        scroll = tk.Scrollbar(frame, command=main_c.yview)
        scroll.place(relx=0.95, rely=0, relheight=1)
        main_c.configure(yscrollcommand=scroll.set)

        for task in all_task:
            # match case to get color base on priority level
            color = "white"
            match task[2]:
                case 'i':
                    color = "red"
                case 'u':
                    color = "#ffbf00"
                case 'n':
                    color = "#01c2ff"

            # tk.Label(canvas_frame, text=f"label {x}").pack()
            # create canvas to store widgets
            c = tk.Canvas(canvas_frame)
            
            # create int var for checkbox
            var = tk.IntVar()
            task_checkbox = tk.Checkbutton(c, variable=var, onvalue="Completed", offvalue="Incomplete")

            # create clickable task name text
            task_name_button = tk.Button(c, text=task[1], relief=tk.FLAT, font=('calibri', 12, 'bold'))

            # create color box to display priority level
            pixel = tk.PhotoImage(width=1, height=1)
            color_box = tk.Button(c, bg=color, state=tk.DISABLED, height=1, relief=tk.FLAT, padx=0, pady=0, image=pixel)

            # display widget
            task_checkbox.grid(row=0, column=0)
            task_name_button.grid(row=0, column=1)
            color_box.grid(row=1, column=0, padx=0, pady=0)

            c.pack(fill=tk.BOTH, side=tk.TOP)


    def add_task(self, canvas, taskName, priority):
        """ Adding tasks into db 
        :param canvas: canvas frame
        :param taskName: name of task
        :param priority: priority level of task
        """
        canvas.destroy()
        task_name = taskName
        lvl = priority

        match lvl:
            case "Important":
                lvl = "i"
            case "Urgent":
                lvl = "u"
            case "Normal":
                lvl = "n"

        date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.__db.addTask(task_name, lvl, date_time)


    def cancel_btn(self, c):
        """ Cancel button for task creation
        :param c: canvas frame
        :return:
        """
        c.destroy()

    def task_button_state(self, task, b):
        new_state = "disabled" if task == "" else "normal"
        b.configure(state=new_state)

    def create_task_button(self, frame):
        """ Create canvas to store entry for user and drop down and add task button
        :param frame: frame of where the items will b displayed
        :return:
        """

        # c = canvas, l = label, entry = entry, menu = stringVar
        c = self.create_canvas(frame, width=300)

        l1 = tk.Label(c, text="Task name: ")
        l1.grid(row=0, column=0)

        b_task = tk.Button(c, text="Add Task", state=tk.DISABLED, command=lambda: [
            self.add_task(c, self.task_entry.get(), menu.get())])
        b_task.grid(row=1, column=2)

        taskvar = tk.StringVar()
        taskvar.trace(
            "w", lambda *args: self.task_button_state(self.task_entry.get(), b_task))
        taskvar.set("")
        self.task_entry = tk.Entry(c, textvariable=taskvar)
        self.task_entry.grid(row=0, column=1)

        menu = tk.StringVar(c)
        choices = {'Normal', 'Urgent', 'Important'}
        menu.set('Normal')
        dropdown = tk.OptionMenu(c, menu, *choices)
        dropdown.grid(row=1, column=1)

        b_cancel = tk.Button(c, text="Cancel", command=lambda: [
                             self.cancel_btn(c)])
        b_cancel.grid(row=1, column=3)

        c.place(relx=.01, rely=0.2)

    def task_list_frame(self, container):
        """ Create the task list frame for the main page
        :param container: Container frame of the main page
        :return frame: return task list frame
        """
        task_list_frame = tk.Frame(container, width=325, height=500)

        self.display_task(task_list_frame)

        return task_list_frame

    def task_detail_frame(self, container):
        """ Create task detail frame for the main page
        :param container: Container frame of main page
        :return frame: return task detail frame
        """
        task_detail_frame = tk.Frame(container, width=325, height=500)
        l1 = tk.Label(task_detail_frame, text="This is the task detail frame")
        l1.place(relx=.2, rely=.5)

        return task_detail_frame

    def side_nav_bar_frame(self, container):
        """ Create left side for the main page
        :param container: Container frame of main page
        :return frame: return left side frame
        """
        left_main_frame = tk.Frame(
            container, width=200, height=650, highlightcolor="red", highlightthickness=3)
        l1 = tk.Label(left_main_frame, text="This is the left main frame")

        # Create task button
        b1 = tk.Button(left_main_frame, text="Create Task", width=20, bg="#2F2E41",
                       activebackground="#52506e", activeforeground="white", fg="white", relief=tk.FLAT, command=lambda: self.create_task_button(self.__task_list_frame))
        b1.place(bordermode=tk.INSIDE, relx=.1, rely=.1)

        # Create Project button
        # b2 = tk.Button(left_main_frame, text="Create Project", width=20,
        #                bg="#F4E8CE", activebackground="#f5ecd7", relief=tk.FLAT)
        # b2.place(bordermode=tk.INSIDE, relx=.1, rely=.17)

        l1.place(relx=.1, rely=.5)

        return left_main_frame


class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        project_container = tk.Frame(self)

        project_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
