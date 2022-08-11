from platform import release
import tkinter as tk
from tkinter import ttk
from turtle import width
from tkcalendar import *
from tkfontawesome import icon_to_image
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
        # create dictionary for dynamic var
        self.__canvas_var = {}

        # db instance
        self.__db = Task()

        # get id of first element
        datas = self.__db.get_all_data()
        for data in datas:
            first_id = data[0]

        # check if task detail function ran
        self.__task_detail_bool = False

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
        self.__task_list_frame.grid(
            row=0, column=1, padx=(25, 0), pady=(125, 25))
        sep.grid(row=0, column=2)
        self.__task_detail_frame.grid(
            row=0, column=3, padx=(0, 25), pady=(125, 25))

        self.display_task(self.__task_list_frame)

        if self.__db.check_table():
            self.display_task_detail(self.__task_detail_frame, first_id)
            self.__task_detail_bool = True

        # display container using pack
        main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def task_detail_edit(self, frame, id):
        pass

    def display_task_detail(self, frame, id):
        """ display tast details
        :param frame: parent frame
        :param id: id of task
        :return:
        """
        # get task
        task = self.__db.get_data_by_id(id)

        # format date for due date text
        task_due_date = task[0][4].split("/")
        date = datetime.datetime(int(task_due_date[2]), int(
            task_due_date[1]), int(task_due_date[0]))
        date = date.strftime("%d %b %Y")

        # match case to get color and priority level
        color = "white"
        priority_tag_text = "Low"
        match task[0][2]:
            case 'i':
                color = "red"
                priority_tag_text = "High"
            case 'u':
                color = "#ffbf00"
                priority_tag_text = "Medium"
            case 'n':
                color = "#01c2ff"
                priority_tag_text = "Low"

        # create second container frame
        self.__detail_container = tk.Frame(frame, width=325, height=500)
        self.__detail_container.pack()

        # create canvas for task details
        self.__detail_c = tk.Canvas(self.__detail_container)
        self.__detail_c.place(relx=0, rely=0, relheight=1, relwidth=1)

        # create frame to put widgets
        self._detail_c_frame = tk.Frame(self.__detail_c)

        # display frame onto canvas
        self._detail_c_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        # create task detail label
        task_detail_label = tk.Label(
            self._detail_c_frame, text="Task details", fg="#2F80ED", font=('segoe ui', 12, 'bold'))

        # create status label
        task_status_label = tk.Label(
            self._detail_c_frame, text=f"{task[0][6]}", bg="#e0e0e0", fg="black", font=('segoe ui', 12))

        # create table for task name
        task_name = tk.Label(
            self._detail_c_frame, text=f"{task[0][1]}", font=('segoe ui', 15, 'bold'))

        # create priority level color widget
        priority_tag = tk.Label(
            self._detail_c_frame, text=priority_tag_text, bg=color, fg="white", width=7)

        # create task desc label
        task_desc_label = tk.Label(self._detail_c_frame, text="Task description", font=(
            'segoe ui', 8, 'bold'), fg="#6D6D6D")

        # create text area to for desc
        desc_box = tk.Text(self._detail_c_frame, height=10, width=30,
                           highlightthickness=0, borderwidth=0, bg="#f0f0f0", state=tk.DISABLED)
        desc_box.insert(tk.END, f"{task[0][5]}")

        # create due date label and date widget
        due_date_label = tk.Label(self._detail_c_frame, text="Due Date", font=(
            'segoe ui', 8, 'bold'), fg="#6d6d6d")
        due_date = tk.Label(self._detail_c_frame,
                            text=f"{date}", bg="#e0e0e0", font=('segoe ui', 12))

        # create seperater line 1
        sep1 = ttk.Separator(self._detail_c_frame, orient="horizontal")

        # create date created
        date_time = task[0][3].split(' ')
        date_created = date_time[0].split('/')
        x = datetime.datetime(int(date_created[2]), int(
            date_created[1]), int(date_created[0]))
        date_created = x.strftime("%d %b %Y %B")
        date_created = f"{str(date_created)} {date_time[1]}"
        task_date_created = tk.Label(
            self._detail_c_frame, text=f"Created on {date_created}", font=('segoe ui', 7), fg="#6d6d6d")

        # create seperater line 2
        sep2 = ttk.Separator(self._detail_c_frame, orient="horizontal")

        # create delete task button
        delete_button = tk.Button(
            self._detail_c_frame, text="Delete Task", font=('segoe ui', 10, 'bold'), relief=tk.FLAT, fg="red", activeforeground="red", command=lambda: self.delete_task(task[0][0]))

        # create edit button
        pen = icon_to_image("pen", scale_to_width=20, fill="#black")
        edit_button = tk.Button(self._detail_c_frame,
                                image=pen, relief=tk.FLAT)
        edit_button.image = pen

        # create mark complete button
        complete_button = tk.Button(
            self._detail_c_frame, text="Mark as Completed", font=('segoe ui', 10, 'bold'), relief=tk.FLAT, fg="#2F80ED", activeforeground="#2F80ED")

        task_detail_label.grid(row=0, column=0, pady=(10, 0))
        task_status_label.grid(row=0, column=1, pady=(10, 0), sticky="w")
        edit_button.grid(row=0, column=2, pady=(10, 0), sticky="w")
        task_name.grid(row=1, column=0, columnspan=3, sticky="w", padx=(15, 0))
        priority_tag.grid(row=2, column=0, pady=(
            5, 10), sticky="w", padx=(20, 0))
        task_desc_label.grid(row=3, column=0)
        desc_box.grid(row=4, column=0, columnspan=3, padx=(20, 0))
        due_date_label.grid(row=5, column=0, sticky="w", padx=(20, 0))
        due_date.grid(row=6, column=0, padx=(20, 0))
        sep1.grid(row=7, column=0, ipadx=150, pady=(
            10, 0), padx=(10, 0), columnspan=5)
        task_date_created.grid(row=8, column=0, columnspan=2)
        sep2.grid(row=9, column=0, ipadx=150, padx=(
            10, 0), pady=(80, 0), columnspan=5)
        delete_button.grid(row=10, column=0, pady=(10, 0))
        # edit_button.grid(row=10, column=1, pady=(20,0), sticky="w")
        complete_button.grid(row=10, column=1, pady=(
            10, 0), padx=(50, 0), sticky="e")

    def delete_task(self, id):
        """ Delete task from db
        :param id: id of task
        :return:
        """
        task = self.__db.get_data_by_id(id)
        self.__canvas_var[id].destroy()
        self.__db.delete_task(id)

        # self.__canvas_var[task[0]].destroy()
        self.__main_c.update_idletasks()

    def update_display_task_detail(self, frame, id):
        """ Update display task detail
        :param frame: parent frame
        :param id: id of task
        :return:
        """
        self.__detail_container.destroy()
        self.display_task_detail(frame, id)

    def display_task_detail_check(self, id):
        """ Check which function to run 
        :param id: id of task
        :return:
        """
        if self.__task_detail_bool:
            self.update_display_task_detail(self.__task_detail_frame, id)
        else:
            self.display_task_detail(self.__task_detail_frame, id)
            self.__task_detail_bool = True
        

    def update_display_task(self):
        """ Update display of task to task manager window
        :return:
        """
        # get all task from db
        all_task = self.__db.get_all_data()
        task = all_task[-1]

        # inner function to config scrollregion
        def on_configure(event):
            self.__main_c.configure(scrollregion=self.__main_c.bbox('all'))

        # resize the canvas scroll region each time the size of the frame changes
        self.__frame_container.bind('<Configure>', on_configure)

        # match case to get color base on priority level
        color = "white"
        match task[2]:
            case 'i':
                color = "red"
            case 'u':
                color = "#ffbf00"
            case 'n':
                color = "#01c2ff"

        v_name = f"c{task[0]}"        
        # create canvas to store widgets
        v_name = tk.Canvas(self._canvas_frame)

        # create int var for checkbox
        var = tk.IntVar()
        task_checkbox = tk.Checkbutton(
            v_name, variable=var, onvalue="Completed", offvalue="Incomplete")

        # create clickable task name text
        task_name_button = tk.Button(
            v_name, text=task[1], relief=tk.FLAT, font=('segoe ui', 12, 'bold'),
            command=lambda id=task[0]: [self.display_task_detail_check(id)])

        # create color box to display priority level
        pixel = tk.PhotoImage(width=1, height=1)
        color_box = tk.Button(v_name, bg=color, state=tk.DISABLED,
                              height=1, relief=tk.FLAT, padx=0, pady=0, image=pixel)

        # create due date label
        due_date = tk.Label(v_name, text=f"Due {task[4]}", height=1)

        # display widget
        task_checkbox.grid(row=0, column=0)
        task_name_button.grid(row=0, column=1, sticky=tk.W)
        color_box.grid(row=1, column=0, padx=0, pady=0)
        due_date.grid(row=1, column=1, padx=0, pady=0)

        self.__canvas_var[task[0]] = v_name

        v_name.pack(fill=tk.BOTH, side=tk.TOP)
        self.__main_c.update_idletasks()
        self.__main_c.configure(scrollregion=self.__main_c.bbox('all'))
    
    # def new_display_task(self, frame):
    #     """  Display all task onto task manager window
    #     :param frame: parent frame
    #     :return: 
    #     """
    #     # get all task from db
    #     all_task = self.__db.get_all_data()

    #     # create secondary frame container
    #     self.__display_frame_container = tk.Frame(frame, width=325, height=500)
    #     self.__display_frame_container.pack()

    #     # inner function to config scrollregion
    #     def on_configure(event):
    #         self._display_task_c.configure(scrollregion=self._display_task_c.bbox('all'))

    #     # create canvas for task list frame
    #     self._display_task_c = tk.Canvas(self.__display_frame_container)
    #     self._display_task_c.place(relx=0, rely=0, relheight=1, relwidth=1)

    #     # frame to add stuff to screen
    #     self._canvas_frame = tk.Frame(self._display_task_c)

    #     # resize the canvas scroll region each time the size of the frame changes
    #     self.__display_frame_container.bind('<Configure>', on_configure)

    #     # display frame inside the canvas
    #     self._display_task_c.create_window(0, 0, window=self._canvas_frame)

    #     # create scroll bar for task list
    #     self._scroll = tk.Scrollbar(self.__display_frame_container, command=self._display_task_c.yview)
    #     self._scroll.place(relx=0.95, rely=0, relheight=1)
    #     self._display_task_c.configure(yscrollcommand=self._scroll.set)

    #     # for loop to display task onto task list page
    #     for task in all_task:
    #         tk.Label(self._canvas_frame, text=f"{task[1]}").pack(side=tk.TOP)
    
    # def update_task_list(self, frame):
    #     """ Update task list 
    #     :param frame: parent frame
    #     :return:
    #     """
    #     self.__display_frame_container.destroy()
    #     self.new_display_task(frame)


    def display_task(self, frame):
        """ Display all tasks onto task manager window
        :param frame: parent frame
        :return:
        """
        all_task = self.__db.get_all_data()

        self.__frame_container = tk.Frame(frame, width=325, height=500)
        self.__frame_container.pack()

        # inner function to config scrollregion
        def on_configure(event):
            self.__main_c.configure(scrollregion=self.__main_c.bbox('all'))

        # create canvas for task list frame
        self.__main_c = tk.Canvas(self.__frame_container)
        self.__main_c.place(relx=0, rely=0, relheight=1, relwidth=1)

        # frame to add stuff to screen
        self._canvas_frame = tk.Frame(self.__main_c)
        # resize the canvas scroll region each time the size of the frame changes
        self.__frame_container.bind('<Configure>', on_configure)
        # display frame inside the canvas
        self.__main_c.create_window(0, 0, window=self._canvas_frame)
        # canvas_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        # create scroll bar for task list
        self.__scroll = tk.Scrollbar(
            self.__frame_container, command=self.__main_c.yview)
        self.__scroll.place(relx=0.95, rely=0, relheight=1)
        self.__main_c.configure(yscrollcommand=self.__scroll.set)

        # for loop to display task onto task list page
        for task in all_task:
            v_name = f"c{task[0]}"
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
            v_name = tk.Canvas(self._canvas_frame)

            # create int var for checkbox
            var = tk.IntVar()
            task_checkbox = tk.Checkbutton(
                v_name, variable=var, onvalue="Completed", offvalue="Incomplete")

            # create clickable task name text
            task_name_button = tk.Button(
                v_name, text=task[1], relief=tk.FLAT, font=('segoe ui', 12, 'bold'),
                command=lambda id=task[0]: [self.display_task_detail_check(id)])

            # create color box to display priority level
            pixel = tk.PhotoImage(width=1, height=1)
            color_box = tk.Button(v_name, bg=color, state=tk.DISABLED,
                                  height=1, relief=tk.FLAT, padx=0, pady=0, image=pixel)

            # create due date label
            due_date = tk.Label(v_name, text=f"Due {task[4]}", height=1)

           # display widget
            task_checkbox.grid(row=0, column=0)
            task_name_button.grid(row=0, column=1, sticky=tk.W)
            color_box.grid(row=1, column=0, padx=0, pady=0)
            due_date.grid(row=1, column=1, padx=0, pady=0)

            self.__canvas_var[task[0]] = v_name

            v_name.pack(fill=tk.BOTH, side=tk.TOP)

    def task_list_frame(self, container):
        """ Create the task list frame for the main page
        :param container: Container frame of the main page
        :return frame: return task list frame
        """
        task_list_frame = tk.Frame(container, width=325, height=500)

        return task_list_frame

    def task_detail_frame(self, container):
        """ Create task detail frame for the main page
        :param container: Container frame of main page
        :return frame: return task detail frame
        """
        task_detail_frame = tk.Frame(container, width=325, height=500)

        return task_detail_frame

    def add_task_button_action(self, task_name, priority, due_date, desc=None, status="Incomplete"):
        match priority:
            case "Important":
                lvl = "i"
            case "Urgent":
                lvl = "u"
            case "Normal":
                lvl = "n"

        date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        self.__db.addTask(task_name, lvl, date_time, due_date, desc, status)

    def side_nav_bar_frame(self, container):
        """ Create left nav bar for the main page
        :param container: Container frame of main page
        :return frame: return nav bar frame
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
            add_task_frame, text="Add a Task", font=('segoe ui', 11, 'bold'), bg="#F8DEAC")
        add_task_label.pack(padx=(0, 80), pady=(10, 40))

        # create task task name label and task name entry
        task_name_label = tk.Label(
            add_task_frame, text="Task Name", bg="#F8DEAC", font=('segoe ui', 9))
        task_name_entry = tk.Entry(add_task_frame, width=25)
        task_name_label.pack(padx=(0, 100))
        task_name_entry.pack()

        # create task priority label and dropdown list
        task_priority_label = tk.Label(
            add_task_frame, text="Task Piority", bg="#F8DEAC", font=('segoe ui', 9))
        # create string var
        dropdown_var = tk.StringVar()
        task_priority_dropdown = ttk.Combobox(
            add_task_frame, textvariable=dropdown_var, width=22, state="readonly")
        task_priority_dropdown['values'] = ('Normal', 'Urgent', 'Important')

        task_priority_label.pack(padx=(0, 100), pady=(10, 0))
        task_priority_dropdown.pack()

        # create date entry box
        task_duedate_label = tk.Label(
            add_task_frame, text="Due Date", bg="#F8DEAC", font=('segoe ui', 9))
        task_calendar_entry = DateEntry(
            add_task_frame, selectmode="day", width=22)
        task_duedate_label.pack(padx=(0, 110), pady=(10, 0))
        task_calendar_entry.pack()

        # create optional task description
        task_desc_label = tk.Label(
            add_task_frame, text="Task Description (Optional)", bg="#F8DEAC", font=('segoe ui', 9))
        task_desc_text = tk.Text(add_task_frame, width=18, height=5)
        task_desc_label.pack(padx=(0, 15), pady=(10, 0))
        task_desc_text.pack()

        def clear():
            task_name_entry.delete(0, tk.END)
            task_priority_dropdown.set("")
            task_calendar_entry.set_date(datetime.date.today())
            task_desc_text.delete(1.0, tk.END)

        def get_desc():
            desc = task_desc_text.get("1.0", "end")
            return desc
        # create the create task button
        task_createtask_button = tk.Button(add_task_frame, text="Create Task", bg="#2F2E41",
                                           fg="white", activebackground="#52506e", activeforeground="white", relief=tk.FLAT,
                                           command=lambda: [self.add_task_button_action(task_name_entry.get(), task_priority_dropdown.get(), task_calendar_entry.get(), get_desc()),
                                                            self.update_display_task(), clear()])
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
