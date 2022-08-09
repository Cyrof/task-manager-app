from random import choices
import tkinter as tk
from tkinter import ttk
from turtle import width
from tkcalendar import *
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
    
    def update_display_task(self):
        """ Update display of task to task manager window
        :return:
        """
        self.__main_c.destroy()
        self.__scroll.destroy()
        self.display_task(self.__task_list_container)
        pass

    def display_task(self, frame):
        """ Display all tasks onto task manager window
        :param frame: parent frame
        :return:
        """
        all_task = self.__db.get_all_data()

        # inner function to config scrollregion
        def on_configure(event):
            self.__main_c.configure(scrollregion=self.__main_c.bbox('all'))

        # create canvas for task list frame
        self.__main_c = tk.Canvas(frame)
        self.__main_c.place(relx=0, rely=0, relheight=1, relwidth=1)

        # frame to add stuff to screen
        canvas_frame = tk.Frame(self.__main_c)
        # resize the canvas scroll region each time the size of the frame changes
        frame.bind('<Configure>', on_configure)
        # display frame inside the canvas
        self.__main_c.create_window(0, 0, window=canvas_frame)

        # create scroll bar for task list
        self.__scroll = tk.Scrollbar(frame, command=self.__main_c.yview)
        self.__scroll.place(relx=0.95, rely=0, relheight=1)
        self.__main_c.configure(yscrollcommand=self.__scroll.set)

        # for loop to display task onto task list page
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
            task_checkbox = tk.Checkbutton(
                c, variable=var, onvalue="Completed", offvalue="Incomplete")

            # create clickable task name text
            task_name_button = tk.Button(
                c, text=task[1], relief=tk.FLAT, font=('calibri', 12, 'bold'))

            # create color box to display priority level
            pixel = tk.PhotoImage(width=1, height=1)
            color_box = tk.Button(c, bg=color, state=tk.DISABLED,
                                  height=1, relief=tk.FLAT, padx=0, pady=0, image=pixel)

            # display widget
            task_checkbox.grid(row=0, column=0)
            task_name_button.grid(row=0, column=1)
            color_box.grid(row=1, column=0, padx=0, pady=0)

            c.pack(fill=tk.BOTH, side=tk.TOP)

    def task_list_frame(self, container):
        """ Create the task list frame for the main page
        :param container: Container frame of the main page
        :return frame: return task list frame
        """
        task_list_frame = tk.Frame(container, width=325, height=500)

        self.__task_list_container = tk.Frame(task_list_frame, width=325, height=500)
        self.__task_list_container.pack()
        

        self.display_task(self.__task_list_container)

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

    def add_task_button_action(self, task_name, priority, due_date, desc=None):
        match priority:
            case "Important":
                lvl = "i"
            case "Urgent":
                lvl = "u"
            case "Normal":
                lvl = "n"

        date_time = datetime.datetime.now().strftime("%d/%M/%Y %H:%M")

        self.__db.addTask(task_name, lvl, date_time, due_date, desc)

    def side_nav_bar_frame(self, container):
        """ Create left side for the main page
        :param container: Container frame of main page
        :return frame: return left side frame
        """
        # create navbar frame
        left_main_frame = tk.Frame(
            container, width=200, height=650, highlightthickness=0, highlightcolor="white")

        # create canvas to container widget
        left_main_canvas = tk.Canvas(left_main_frame)
        left_main_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        # create name for task manager
        tk.Label(left_main_canvas, text="Name", font=(
            'Segoe Script', 12, 'bold')).pack(padx=(0, 100), pady=(10, 0))

        # seperator line
        ttk.Separator(left_main_canvas, orient="horizontal").pack(
            fill=tk.X, pady=(50, 0))

        # add task frame, configure and display onto nav frame
        add_task_frame = tk.Frame(
            left_main_canvas, width=170, height=400, bg="#f8deac")
        add_task_frame.configure(background="#F8DEAC")
        add_task_frame.pack(side=tk.BOTTOM, pady=70)
        add_task_frame.pack_propagate(0)

        # create add task label and display onto frame
        add_task_label = tk.Label(
            add_task_frame, text="Add a Task", font=('Nunito Sans', 11, 'bold'), bg="#F8DEAC")
        add_task_label.pack(padx=(0, 80), pady=(10, 40))

        # create task task name label and task name entry
        task_name_label = tk.Label(
            add_task_frame, text="Task Name", bg="#F8DEAC", font=('Nunito Sans', 9))
        task_name_entry = tk.Entry(add_task_frame, width=25)
        task_name_label.pack(padx=(0, 100))
        task_name_entry.pack()

        # create task priority label and dropdown list
        task_priority_label = tk.Label(
            add_task_frame, text="Task Piority", bg="#F8DEAC", font=('Nunito Sans', 9))
        # create string var
        dropdown_var = tk.StringVar()
        task_priority_dropdown = ttk.Combobox(
            add_task_frame, textvariable=dropdown_var, width=22, state="readonly")
        task_priority_dropdown['values'] = ('Normal', 'Urgent', 'Important')

        task_priority_label.pack(padx=(0, 100), pady=(10, 0))
        task_priority_dropdown.pack()

        # create date entry box
        task_duedate_label = tk.Label(
            add_task_frame, text="Due Date", bg="#F8DEAC", font=('Nunito Sans', 9))
        task_calendar_entry = DateEntry(
            add_task_frame, selectmode="day", width=22)
        task_duedate_label.pack(padx=(0, 110), pady=(10, 0))
        task_calendar_entry.pack()

        # create optional task description
        task_desc_label = tk.Label(
            add_task_frame, text="Task Description (Optional)", bg="#F8DEAC", font=('Nunito Sans', 9))
        task_desc_text = tk.Text(add_task_frame, width=18, height=5)
        task_desc_label.pack(padx=(0, 15), pady=(10, 0))
        task_desc_text.pack()

        # get desc if there is 
        if len(task_desc_text.get("1.0",'end-1c')) == 0:
            desc = None
        else:
            desc = task_desc_text.get()
        # create the create task button
        task_createtask_button = tk.Button(add_task_frame, text="Create Task", bg="#2F2E41",
                                           fg="white", activebackground="#52506e", activeforeground="white", relief=tk.FLAT, 
                                           command=lambda: [self.add_task_button_action(task_name_entry.get(), task_priority_dropdown.get(), task_calendar_entry.get(), desc), self.update_display_task()])
        task_createtask_button.pack(pady=(30, 0))

        return left_main_frame


class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        project_container = tk.Frame(self)

        project_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
