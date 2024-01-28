import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from ttkbootstrap.constants import *
import ttkbootstrap as tb

import flight_DB
# import pywhatkit
from PIL import ImageTk, Image
#import random as rd

back = "#f5ded6"
front = "#672c18"
active_ID = 0
user_ID = 0





def createacct():
    def new_acct():
        #serial = serial_Entry.get()
        name = Name_Entry.get()
        Password = pword_Entry.get()
        confirm = confirm_pword_Entry.get()
        # seat = "No Flight Booked"
        if Password != "" and name != "":
            id = flight_DB.get_user_ID()
            mb.showinfo("Success Message", flight_DB.user_entry(id, name, Password, seat_number='None', plane_name="None", next_destination="None"))

        elif name == "Admin":
            mb.showerror("Error Message", "username cannot be used")
        elif Password != confirm:
            mb.showerror("Error", "password must match")
        elif Password == "AdminLogin":
            mb.showerror("Error", "This Password can not be used")
        elif Password != confirm:
            mb.showerror("Error", "Password do not match")
        else:
            mb.showinfo("INFO", "Enter a name and password")
        new_window.destroy()


    new_window = Toplevel()
    new_window.title("Create account")
    new_window.geometry("1000x600")
    new_window.config(bg="white")

    # Labels
    Name_Label = tb.Label(new_window, text="Enter name",  font=("segoe ui semibold", 14))
    pword_label = tb.Label(new_window, text="Enter password",  font=("segoe ui semibold", 14))
    confirm_pword_label = tb.Label(new_window, text="comfirm password", font=("segoe ui semibold", 14))

    # Entries
    Name_Entry = tb.Entry(new_window, font=('segoe ui semibold', 14), bootstyle="primary")
    pword_Entry = tb.Entry(new_window, font=('segoe ui semibold', 14), bootstyle="primary")
    confirm_pword_Entry = tb.Entry(new_window, font=('segoe ui semibold', 14), bootstyle="primary")
    serial_Entry = tb.Entry(new_window, font=('segoe ui semibold', 14),  state=DISABLED, width=2)
    # Buttons
    done_Button = tb.Button(new_window, text="create", bootstyle="primary", command=new_acct, )

    # packing
    Name_Label.pack()
    Name_Entry.pack(pady=10)
    pword_label.pack(pady=10)
    pword_Entry.pack(pady=10)
    confirm_pword_label.pack(pady=10)
    confirm_pword_Entry.pack(pady=10)

    done_Button.pack(pady=10)
    #serial_Entry.pack()


def login():

    name = name_entry.get()
    password = Password_entry.get()
    if name and password:
        id1 = name
        id2 = password
        result1 = flight_DB.view_name(id1)
        result2 = flight_DB.view_pass(id2)
        if password == "AdminLogin" and name == "Admin":
            mb.showinfo("Welcome message", "welcome admin")


            def admin_users():
                window.destroy()
                window_9 = Tk()
                window_9.geometry("1200x700")
                window_9.title("Users info")
                window_9.config(bg=back)

                def clear_users():
                    user_serial_entry.delete(0, END)
                    user_name_entry.delete(0, END)
                    user_password_entry.delete(0, END)
                    active_seat_entry.delete(0, END)
                    active_plane_entry.delete(0, END)
                    active_destination_entry.delete(0, END)

                def add_users():
                    serial = user_serial_entry.get()
                    name = user_name_entry.get()
                    password = user_password_entry.get()
                    seats = active_seat_entry.get()
                    flight_name = active_plane_entry.get()
                    destination = active_destination_entry.get()
                    if name != "" and password != "":
                        #id = flight_DB.get_user_ID()
                        mb.showinfo("data entered", flight_DB.user_entry(serial, name, password, seats, flight_name, destination))
                    view_users()



                def single_user():
                    id = user_serial_entry.get()
                    results = flight_DB.view_user(id)
                    if results is None:
                        mb.showerror("Error Message", "Invalid S/N")
                    else:
                        clear_users()
                        user_name_entry.insert(0, results[1])
                        user_password_entry.insert(0, results[2])
                        active_seat_entry.insert(0, results[3])
                        active_plane_entry.insert(0, results[4])
                        active_destination_entry.insert(0, results[5])
                        global user_ID
                        user_ID = id



                def update_users():
                    if int(user_ID) > 0:
                        # serial = serial_entry.get()
                        user_name = user_name_entry.get()
                        user_password = user_password_entry.get()
                        user_seat = active_seat_entry.get()
                        flight_name = active_plane_entry.get()
                        destination = active_destination_entry.get()
                        mb.showinfo("Success Message", flight_DB.update_user(user_ID, user_name, user_password, user_seat, flight_name, destination))
                        view_users()
                        clear_users()
                    else:
                        mb.showerror("Error Message", "Error: Serial number is invalid")

                def delete_user():
                    if int(user_ID) > 0:
                        serial = user_serial_entry.get()
                        mb.showinfo("Success message", flight_DB.delete_user(serial))
                        view_users()
                        clear_users()
                    else:
                        mb.showerror("Error Message", "Error: Invalid serial number")

                def view_users():
                    user = flight_DB.view_users()
                    text_box1.delete(1.0, END)
                    text_box1.insert(INSERT,
                                     f"| S/N |  Name\t\t| Password\t | Seat Number \t| Flight Name\t\t| Flight Destination |\n")
                    for i in user:
                        text_box1.insert(INSERT,
                                         f"|{i[0]}| {i[1]} \t\t | {i[2]} \t| {i[3]} \t | {i[4]} \t\t| \t {i[5]} \t|\n")

                #  Frames
                left_frame = Frame(window_9, bg=back, height=650, width=546, highlightcolor="Black",
                                   highlightthickness=2)
                middle_frame = Frame(window_9, bg=front, height=650, width=2)
                right_frame = Frame(window_9, bg=back, height=650, width=556, highlightcolor="Black",
                                    highlightthickness=2)
                # Labels
                users_title_label = tb.Label(left_frame, text="Users information", font=("segoe ui semibold", 17))
                users_serial_label = tb.Label(left_frame, text="Serial number", font=("segoe ui semibold", 17))
                users_name_label = tb.Label(left_frame, text="user name", font=("segoe ui semibold", 17))
                users_password_label = tb.Label(left_frame, text="user password", font=("segoe ui semibold", 17))
                users_seatno_label = tb.Label(left_frame, text="current seat", font=("segoe ui semibold", 17))
                users_plane_label =tb. Label(left_frame, text="Plane name", font=("segoe ui semibold", 17))
                users_destination_label = tb.Label(left_frame, text="Destination", font=("segoe ui semibold", 17), bootstyle="dark")
                
                registered_user = tb.Label(right_frame, text="registered users:", font=('Lucida calligraphy', 20))
                # Entries
                user_serial_entry = tb.Entry(left_frame, font=("segoe ui semibold", 14), bootstyle="Dark", width="2")
                user_name_entry = tb.Entry(left_frame, font=("segoe ui semibold", 14), bootstyle="Dark")
                user_password_entry = tb.Entry(left_frame, font=("segoe ui semibold", 14), bootstyle="Dark")
                active_seat_entry = tb.Entry(left_frame,  font=("segoe ui semibold", 14), bootstyle="Dark")
                active_plane_entry = tb.Entry(left_frame, font=("segoe ui semibold", 14), bootstyle="Dark")
                active_destination_entry = tb.Entry(left_frame,  font=("segoe ui semibold", 14), bootstyle="Dark")

                # Scrollbars
                scrollbar_1 = tb.Scrollbar(right_frame, bootstyle="dark round")
                scrollbar_2 = tb.Scrollbar(right_frame, orient=HORIZONTAL, bootstyle="dark round")
                # Text BOX
                text_box1 = Text(right_frame, xscrollcommand=scrollbar_2.set, yscrollcommand=scrollbar_1.set, width=48,
                                 height=13, font=('segoe ui semibold', 14), wrap=NONE)
                # Buttons
                add_button = tb.Button(left_frame, text='add', command=add_users, bootstyle="Dark")
                view_button = tb.Button(left_frame, text='view',command=view_users, bootstyle="Dark")
                clear_button = tb.Button(left_frame, text='clear',command=clear_users, bootstyle="Dark")
                delete_button = tb.Button(left_frame, text='delete', command=delete_user, bootstyle="Dark")
                update_button = tb.Button(left_frame, text='update', command=update_users, bootstyle="Dark")
                                       
                select_button = tb.Button(left_frame, text='select',command=single_user, bootstyle="Dark")
                                       
                # FRAME PROPAGATION
                left_frame.propagate(TRUE)
                middle_frame.propagate(TRUE)
                right_frame.propagate(False)
                # FRAME PACKING
                left_frame.place(x=20, y=10)
                middle_frame.place(x=548, y=10)
                right_frame.place(x=600, y=10)
                # placement
                users_title_label.place(x=130, y=15)
                registered_user.place(x=100, y=15)
                users_name_label.place(x=15, y=100)
                user_name_entry.place(x=260, y=100)
                users_password_label.place(x=15, y=160)
                user_password_entry.place(x=260, y=160)
                users_seatno_label.place(x=15, y=220)
                active_seat_entry.place(x=260, y=220)
                users_plane_label.place(x=15, y=280)
                active_plane_entry.place(x=260, y=280)
                users_destination_label.place(x=15, y=340)
                active_destination_entry.place(x=260, y=340)
                add_button.place(x=15, y=420)
                view_button.place(x=85, y=420)
                update_button.place(x=155, y=420)
                delete_button.place(x=245, y=420)
                clear_button.place(x=335, y=420)
                select_button.place(x=415, y=420)
                users_serial_label.place(x=15, y=500)
                user_serial_entry.place(x=200, y=500)
                scrollbar_1.pack(side="right", fill=Y)
                text_box1.pack(pady=50)
                scrollbar_1.config(command=text_box1.yview)
                scrollbar_2.pack(side="bottom", fill=X)
                scrollbar_2.config(command=text_box1.xview)

            def admin_planes():
                def clear():
                    serial_entry.delete(0, END)
                    plane_entry.delete(0, END)
                    destination_entry.delete(0, END)
                    business_seats_entry.delete(0, END)
                    first_seats_entry.delete(0, END)
                    second_seats_entry.delete(0, END)
                    business_entry.delete(0, END)
                    first_entry.delete(0, END)
                    second_entry.delete(0, END)
                    type_entry.delete(0, END)
                    dept_date_entry.delete(0, END)
                    dept_time_entry.delete(0, END)

                def add_plane():
                    # serial = serial_entry.get()
                    plane = plane_entry.get()
                    arrival = destination_entry.get()
                    business_seats = business_seats_entry.get()
                    first_seats = first_seats_entry.get()
                    second_seats = second_seats_entry.get()
                    business_price = business_entry.get()
                    first_price = first_entry.get()
                    second_price = second_entry.get()
                    f_type = type_entry.get()
                    time = dept_time_entry.get()
                    date = dept_date_entry.get()
                    if plane != "" and date != "":
                        id = flight_DB.get_plane_ID()
                        mb.showinfo("data entered", flight_DB.plane_entry(id, plane, arrival, business_seats,
                                                                          first_seats, second_seats, business_price,
                                                                          first_price, second_price, f_type, date,
                                                                          time))
                    view_planes()

                def single_plane():
                    id = serial_entry.get()
                    results = flight_DB.view_plane(id)
                    if results is None:
                        mb.showerror("Error Message", "Invalid S/N")
                    else:
                        clear()
                        plane_entry.insert(0, results[1])
                        destination_entry.insert(0, results[2])
                        business_seats_entry.insert(0, results[3])
                        first_seats_entry.insert(0, results[4])
                        second_seats_entry.insert(0, results[5])
                        business_entry.insert(0, results[6])
                        first_entry.insert(0, results[7])
                        second_entry.insert(0, results[8])
                        type_entry.insert(0, results[9])
                        dept_date_entry.insert(0, results[10])
                        dept_time_entry.insert(0, results[11])
                    global active_ID
                    active_ID = id

                def update_plane():
                    if int(active_ID) > 0:
                        # serial = serial_entry.get()
                        plane = plane_entry.get()
                        arrival = destination_entry.get()
                        business_seats = business_seats_entry.get()
                        first_seats = first_seats_entry.get()
                        second_seats = second_seats_entry.get()
                        business_price = business_entry.get()
                        first_price = first_entry.get()
                        second_price = second_entry.get()
                        f_type = type_entry.get()
                        time = dept_time_entry.get()
                        date = dept_date_entry.get()
                        mb.showinfo("Success Message", flight_DB.update(active_ID, plane, arrival, business_seats,
                                                                        first_seats, second_seats, business_price,
                                                                        first_price, second_price, f_type, date, time))
                        view_planes()
                        clear()
                    else:
                        mb.showerror("Error Message", "Error: Serial number is invalid")

                def delete_plane():
                    if int(active_ID) > 0:
                        serial = serial_entry.get()
                        mb.showinfo("Success message", flight_DB.delete_plane(serial))
                        view_planes()
                        clear()
                    else:
                        mb.showerror("Error Message", "Error: Invalid serial number")

                def view_planes():
                    plane = flight_DB.view_planes()
                    text_box1.delete(1.0, END)
                    text_box1.insert(INSERT,
                                     f"|S/N   | NAME\t\t  | DESTINATION   | Business class Seats |First class seats|Second Class Seats| business class price ($)|First class ice($)| second class price ($)| Flight Type |Departure date| Departure time |\n")
                    for i in plane:
                        text_box1.insert(INSERT,
                                         f"|{i[0]} |{i[1]} \t\t| {i[2]}  \t\t|   {i[3]}   \t\t   |  {i[4]}   \t    |   {i[5]}    \t\t |   {i[6]}   \t\t|   {i[7]}    \t\t  |    {i[8]}   \t\t|     {i[9]}   \t   |    {i[10]}  |    {i[11]}   |\n")

                window.destroy()
                window_4 = Tk()
                window_4.title("Shamzi Airways")
                window_4.config(bg="white")
                window_4.geometry("1200x700")
                # FRAMES
                left_frame = Frame(window_4, height=650, width=546, highlightcolor="black", highlightthickness=2 )
                middle_frame = Frame(window_4, height=650, width=2) 
                right_frame = Frame(window_4, height=650, width=556, highlightcolor="black", highlightthickness=2)
                # LABELS
                title = Label(left_frame, text="Plane registration", font=('Lucida calligraphy', 20))
                serial_label = Label(right_frame, text="S/N:", font=("segoe ui semibold", 17))
                plane_name = Label(left_frame, text="Name:", font=("segoe ui semibold", 17))
                destination = Label(left_frame, text="Destination:", font=("segoe ui semibold", 17))
                business_seats_no = Label(left_frame, text="Business Seats NO:", font=("segoe ui semibold", 17))
                first_seats_no = Label(left_frame, text="First Seats NO:", font=("segoe ui semibold", 17))
                second_seats_no =Label(left_frame, text="Second Seats NO:", font=("segoe ui semibold", 17))
                business = Label(left_frame, text="Business Class Price($):", font=("segoe ui semibold", 17))
                first = Label(left_frame, text="First Class Price($):", font=("segoe ui semibold", 17))
                second = Label(left_frame, text="Second class Price($):", font=("segoe ui semibold", 17))
                flight_type = Label(left_frame, text="Flight Type:", font=("segoe ui semibold", 17))
                departure_date = Label(left_frame, text="Departure date:", font=("segoe ui semibold", 17))
                departure_time = Label(left_frame, text="Departure time:", font=("segoe ui semibold", 17))
                available = Label(right_frame, text=" Available Flights:", font=('Lucida calligraphy', 20))
                # ENTRIES
                serial_entry = tb.Entry(right_frame,bootstyle="dark", font=("segoe ui semibold", 14), width=4 )
                plane_entry = tb.Entry(left_frame, bootstyle="dark", font=("segoe ui semibold", 14))
                destination_entry = tb.Entry(left_frame, bootstyle="dark",  font=("segoe ui semibold", 14))
                business_seats_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                first_seats_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                second_seats_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                business_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                first_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                second_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                type_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                dept_date_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                dept_time_entry = tb.Entry(left_frame, bootstyle="dark",font=("segoe ui semibold", 14))
                # Scrollbars
                scrollbar_1 = tb.Scrollbar(right_frame, bootstyle="dark rounded")
                scrollbar_2 = tb.Scrollbar(right_frame, orient=HORIZONTAL, bootstyle="dark rounded")
                # Text BOX
                text_box1 = Text(right_frame, xscrollcommand=scrollbar_2.set, yscrollcommand=scrollbar_1.set, width=48,
                                 height=13, font=('segoe ui semibold', 14), wrap=NONE)

                # Buttons
                add_button = tb.Button(right_frame, text='add', command=add_plane, bootstyle="Dark ")
                view_button = tb.Button(right_frame, text='view', command=view_planes, bootstyle="Dark ")
                clear_button = tb.Button(right_frame, text='clear', command=clear, bootstyle="Dark ")
                delete_button = tb.Button(right_frame, text='delete', command=delete_plane, bootstyle="Dark ")
                update_button = tb.Button(right_frame, text='update', command=update_plane, bootstyle="Dark ")
                select_button = tb.Button(right_frame, text='select', command=single_plane, bootstyle="Dark ")
                # FRAME PROPAGATION
                left_frame.propagate(TRUE)
                middle_frame.propagate(TRUE)
                right_frame.propagate(False)
                # FRAME PACKING
                left_frame.place(x=20, y=10)
                middle_frame.place(x=548, y=10)
                right_frame.place(x=600, y=10)
                # placement
                title.place(x=130, y=15)
                plane_name.place(x=15, y=70)
                plane_entry.place(x=260, y=70)
                destination.place(x=15, y=110)
                destination_entry.place(x=260, y=110)
                business_seats_no.place(x=15, y=150)
                business_seats_entry.place(x=260, y=150)
                first_seats_no.place(x=15, y=190)
                first_seats_entry.place(x=260, y=190)
                second_seats_no.place(x=15, y=230)
                second_seats_entry.place(x=260, y=230)
                business.place(x=15, y=270)
                business_entry.place(x=260, y=270)
                first.place(x=15, y=310)
                first_entry.place(x=260, y=310)
                second.place(x=15, y=350)
                second_entry.place(x=260, y=350)
                flight_type.place(x=15, y=390)
                type_entry.place(x=260, y=390)
                departure_date.place(x=15, y=430)
                dept_date_entry.place(x=260, y=430)
                departure_time.place(x=15, y=470)
                dept_time_entry.place(x=260, y=470)
                available.place(x=110, y=10)
                add_button.place(x=15, y=480)
                view_button.place(x=85, y=480)
                update_button.place(x=155, y=480)
                delete_button.place(x=245, y=480)
                clear_button.place(x=335, y=480)
                select_button.place(x=415, y=480)
                serial_label.place(x=15, y=530)
                serial_entry.place(x=100, y=530)
                scrollbar_1.pack(side="right", fill=Y)
                text_box1.pack(pady=50)
                scrollbar_1.config(command=text_box1.yview)
                scrollbar_2.pack(side="bottom", fill=X)
                scrollbar_2.config(command=text_box1.xview)
            window_8 = Tk()
            window_8.title("Admin")
            window_8.geometry("1000x600")
            window_8.config(bg="white")
            Button_1 = Button(window_8, text="Planes", bg=front, fg="white", font=("segoe ui semibold", 12), command=admin_planes)
            Button_2 = Button(window_8, text="users", bg=front, fg="white", font=("segoe ui semibold", 12), command=admin_users)
            Button_1.pack(pady=10)
            Button_2.pack(pady=15)




        elif result1 is None or result2 is None:
            mb.showerror("Error", "Wrong username or password")
        elif result1 == "":
            mb.showerror("info", "please enter username")
        elif result2 == "":
            mb.showinfo("info", "please enter password")

        else:
            def view_upcoming():
                def plane1():
                    def book_flight():
                        # value = business_class_radio.getint(1)
                        flight_serial = r1[0]
                        busines = r1[3]
                        firsts = r1[4]
                        seconds = r1[5]
                        user_seat = flight_DB.view_user(1)
                        seat = preferred_seat_entry.get()
                        plane1_info = flight_DB.view_plane(1)
                        name = plane1_info[1]
                        destination = plane1_info[2]

                        if c1.get() == 1:
                            if user_seat[3] == 'None':
                                if busines > 0:
                                    if '1' <= seat <= '50':
                                        mb.showinfo("Flight Booked", flight_DB.book_business(flight_serial, busines))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        #flight_DB.update_user_plane_name(1, name)
                                        #flight_DB.update_user_destination(1, destination)
                                    elif seat >= '51':
                                        mb.showerror("Error", "Seat number is not  available for business class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 2:
                            if user_seat[3] == "None": 
                                if firsts > 0:
                                    if seat >= '51':
                                        mb.showinfo("Flight Booked", flight_DB.book_first(flight_serial, firsts))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    
                                    elif seat >= '151' or seat <= '50':
                                        mb.showerror("Error", "Seat number is not  available for first class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 3:
                            if user_seat[3] == "None":
                                if seconds > 0:
                                    if'151' <= seat <= '300':
                                        mb.showinfo("Flight booked", flight_DB.book_second(flight_serial, seconds))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat <= '151':
                                        mb.showerror("Error", "seat not available for this class")
                                    elif seat >= '301':
                                        mb.showerror("Error", "This seat does not exist")

                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat available!")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    else:
                                        mb.showerror("Error", 'input not understood')
                                else:
                                    mb.showerror("error", "flight fully booked")
                            else:
                                mb.showerror("error", "You have already booked a flight")
                        else:
                            mb.showinfo("Info", "Please choose your desired class ")
                        window_6.destroy()

                    r1 = flight_DB.view_plane(1)
                    window_6 = Toplevel()
                    window_6.title("flight details")
                    window_6.config(bg="white")
                    window_6.geometry("1000x600")
                    #serial_number = Label(window_6, text="Enter your serial number", fg="black", bg="white", font=("segoe ui semibold", 12))
                    prefered_seat_label = Label(window_6, text="Choose your preferred seat", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_1 = Label(window_6, text=f"Name: {r1[1]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_2 = Label(window_6, text=f"Destination: {r1[2]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_3 = Label(window_6, text=f"Business Seats: {r1[3]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_4 = Label(window_6, text=f"First class Seats: {r1[4]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_5 = Label(window_6, text=f"Second class seats: {r1[5]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_6 = Label(window_6, text=f"Business class price ($): {r1[6]}", fg="black", bg="white", font=("segoe ui semibold",                                                                                                                     12))
                    label_7 = Label(window_6, text=f"First class price($): {r1[7]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_8 = Label(window_6, text=f"Second class price($): {r1[8]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_9 = Label(window_6, text=f"Flight type:{r1[9]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_10 = Label(window_6, text=f"Departure time: {r1[10]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    label_11 = Label(window_6, text=f"Departure time: {r1[11]}", fg="black", bg="white", font=("segoe ui semibold", 12))
                    #serial_number_entry = Entry(window_6, width=3, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=1)
                    preferred_seat_entry = Entry(window_6, width=5, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=1)

                    book_1_button = Button(window_6, bg=front, fg=back, text="book", font=("segoe ui semibold", 12),
                                           activebackground=front, activeforeground=back, command=book_flight)
                    c1 = IntVar()
                    # x = c1.get()

                    business_class_radio = Radiobutton(window_6, variable=c1, value=1)
                    First_class_radio = Radiobutton(window_6, variable=c1, value=2)
                    Second_class_radio = Radiobutton(window_6, variable=c1, value=3)

                    prefered_seat_label.pack(expand=True)
                    preferred_seat_entry.pack(expand=True)
                    label_1.pack(pady=5, expand=True)
                    label_2.pack(pady=5, expand=True)
                    label_3.pack(pady=5, expand=True)
                    label_4.pack(pady=5, expand=True)
                    label_5.pack(pady=5, expand=True)
                    label_6.pack(pady=5, expand=True)
                    business_class_radio.pack(expand=True)
                    label_7.pack(pady=5, expand=True)
                    First_class_radio.pack(expand=True)
                    label_8.pack(pady=5, expand=True)
                    Second_class_radio.pack(expand=True)
                    label_9.pack(pady=5, expand=True)
                    label_10.pack(pady=5, expand=True)
                    label_11.pack(pady=5, expand=True)
                    book_1_button.pack(pady=5, expand=True)
                    window_5.destroy()

                window_5 = Toplevel()
                window_5.title("Upcoming flights")
                window_5.config(bg="white")
                window_5.geometry("1000x600")
                # global final_pane_1
                d1 = flight_DB.view_plane(1)
                plane_1 = Image.open("1200px-A6-EDY_A380_Emirates_31_jan_2013_jfk_(8442269364)_(cropped).png", mode="r")
                resize_plane_1 = plane_1.resize((160, 160))
                final_plane_1 = ImageTk.PhotoImage(resize_plane_1)
                flight_1 = Button(window_5,  image=final_plane_1, command=plane1)
                d_1label = Label(window_5, text=f"{d1[2]}", bg="white", fg="black", font=("segoe ui semibold", 12))
                flight_1.image = final_plane_1
                flight_1.place(x=10, y=20)
                d_1label.place(x=35, y=200)
                # global final_pane_2

                def plane2():
                    def book_flight():
                        # value = business_class_radio.getint(1)
                        flight_serial = r1[0]
                        busines = r1[3]
                        firsts = r1[4]
                        seconds = r1[5]
                        user_seat = flight_DB.view_user(3)
                        seat = preferred_seat_entry.get()
                        plane1_info= flight_DB.view_plane(2)
                        name = plane1_info[1]
                        destination = plane1_info[2]
                        if c1.get() == 1:
                            if user_seat[3] == 'None':
                                if busines > 0:
                                    if '1' <= seat <= '70':
                                        mb.showinfo("Flight Booked", flight_DB.book_business(flight_serial, busines))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat >= '71':
                                        mb.showerror("Error", "Seat number is not  available for business class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 2:
                            if user_seat[3] == "None": 
                                if firsts > 0:
                                    if seat >= '71' :
                                        mb.showinfo("Flight Booked", flight_DB.book_first(flight_serial, firsts))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    
                                    elif seat >= '191' or seat <= '70':
                                        mb.showerror("Error", "Seat number is not  available for first class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 3:
                            if user_seat[3] == "None":
                                if seconds > 0:
                                    if'191' <= seat <= '350':
                                        mb.showinfo("Flight booked", flight_DB.book_second(flight_serial, seconds))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat <= '151':
                                        mb.showerror("Error", "seat not available for this class")
                                    elif seat >= '351':
                                        mb.showerror("Error", "This chosen seat is not available")

                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat available!")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    else:
                                        mb.showerror("Error", 'input not understood')
                                else:
                                    mb.showerror("error", "flight fully booked")
                            else:
                                mb.showerror("error", "You have already booked a flight")
                        else:
                            mb.showinfo("Info", "Please choose your desired class ")
                        window_6.destroy()
                    r1 = flight_DB.view_plane(2)
                    window_6 = Toplevel()
                    window_6.title("flight details")
                    window_6.config(bg="white")
                    window_6.geometry("1000x600")
                    seat_number = Label(window_6, text="Choose Your Preferred seat", fg="black", bg="white",
                                        font=("segoe ui semibold", 12))
                    label_1 = Label(window_6, text=f"Name: {r1[1]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_2 = Label(window_6, text=f"Destination: {r1[2]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_3 = Label(window_6, text=f"Business Seats: {r1[3]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_4 = Label(window_6, text=f"First class Seats: {r1[4]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_5 = Label(window_6, text=f"Second class seats: {r1[5]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_6 = Label(window_6, text=f"Business class price ($): {r1[6]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_7 = Label(window_6, text=f"First class price($): {r1[7]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_8 = Label(window_6, text=f"Second class price($): {r1[8]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_9 = Label(window_6, text=f"Flight type:{r1[9]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_10 = Label(window_6, text=f"Departure time: {r1[10]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    label_11 = Label(window_6, text=f"Departure time: {r1[11]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    preferred_seat_entry = Entry(window_6, width=3, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=1)

                    book_1_button = Button(window_6, bg=front, fg=back, text="book", font=("segoe ui semibold", 12),
                                           activebackground=front, activeforeground=back, command=book_flight)
                    c1 = IntVar()
                    # x = c1.get()

                    business_class_radio = Radiobutton(window_6, variable=c1, value=1)
                    First_class_radio = Radiobutton(window_6, variable=c1, value=2)
                    Second_class_radio = Radiobutton(window_6, variable=c1, value=3)

                    seat_number.pack(pady=5, expand=True)
                    preferred_seat_entry.pack(expand=True)
                    label_1.pack(pady=5, expand=True)
                    label_2.pack(pady=5, expand=True)
                    label_3.pack(pady=5, expand=True)
                    label_4.pack(pady=5, expand=True)
                    label_5.pack(pady=5, expand=True)
                    label_6.pack(pady=5, expand=True)
                    business_class_radio.pack(expand=True)
                    label_7.pack(pady=5, expand=True)
                    First_class_radio.pack(expand=True)
                    label_8.pack(pady=5, expand=True)
                    Second_class_radio.pack(expand=True)
                    label_9.pack(pady=5, expand=True)
                    label_10.pack(pady=5, expand=True)
                    label_11.pack(pady=5, expand=True)
                    book_1_button.pack(pady=5, expand=True)
                    window_5.destroy()
                d2 = flight_DB.view_plane(2)
                plane_2 = Image.open("civil-wide-body-plane-flight-aircraft-flying-high-civil-wide-body-plane-flight-aircraft-flying-high-altitude-above-131219454.jpg", mode="r")
                resize_plane_2 = plane_2.resize((160, 160))
                final_plane_2 = ImageTk.PhotoImage(resize_plane_2)
                flight_2 = Button(window_5, image=final_plane_2, command=plane2)
                d_2label = Label(window_5,  text=f"{d2[2]}", bg="white", fg="black", font=("segoe ui semibold", 12))
                flight_2.image = final_plane_2
                flight_2.place(x=190, y=20)
                d_2label.place(x=215, y=200)

                # global final_pane_3
                def plane3():
                    def book_flight():
                        # value = business_class_radio.getint(1)
                        flight_serial = r1[0]
                        busines = r1[3]
                        firsts = r1[4]
                        seconds = r1[5]
                        user_seat = flight_DB.view_user(3)
                        seat = preferred_seat_entry.get()
                        plane1_info = flight_DB.view_plane(3)
                        name = plane1_info[1]
                        destination = plane1_info[2]

                        if c1.get() == 1:
                            if user_seat[3] == 'None':
                                if busines > 0:
                                    if '1' <= seat <= '50':
                                        mb.showinfo("Flight Booked", flight_DB.book_business(flight_serial, busines))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat >= '51':
                                        mb.showerror("Error", "Seat number is not available for business class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 2:
                            if user_seat[3] == "None": 
                                if firsts > 0:
                                    if seat <= '150' :
                                        mb.showinfo("Flight Booked", flight_DB.book_first(flight_serial, firsts))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)

                                    elif seat > '150':
                                        mb.showerror("Error", "Seat number is not available for first class")
                                    elif seat < '51':
                                         mb.showerror("Error", "Seat number is not available for first class")

                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 3:
                            if user_seat[3] == "None":
                                if seconds > 0:
                                    if'151' <= seat <= '300':
                                        mb.showinfo("Flight booked", flight_DB.book_second(flight_serial, seconds))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)

                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat available!")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat <= '151':
                                        mb.showerror("Error", "seat not available for this class")
                                    elif seat > '300':
                                        mb.showerror("Error", "This Plane has only 300 seats")
                                    else:
                                        mb.showerror("Error", 'input not understood')
                                else:
                                    mb.showerror("error", "flight fully booked")
                            else:
                                mb.showerror("error", "You have already booked a flight")
                        else:
                            mb.showinfo("Info", "Please choose your desired class ")
                        window_6.destroy()
                    r1 = flight_DB.view_plane(3)
                    window_6 = Toplevel()
                    window_6.title("flight details")
                    window_6.config(bg="white")
                    window_6.geometry("1000x600")
                    seat_number = Label(window_6, text="Enter your serial number", fg="black", bg="white",
                                          font=("segoe ui semibold", 12))
                    label_1 = Label(window_6, text=f"Name: {r1[1]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_2 = Label(window_6, text=f"Destination: {r1[2]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_3 = Label(window_6, text=f"Business Seats: {r1[3]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_4 = Label(window_6, text=f"First class Seats: {r1[4]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_5 = Label(window_6, text=f"Second class seats: {r1[5]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_6 = Label(window_6, text=f"Business class price ($): {r1[6]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_7 = Label(window_6, text=f"First class price($): {r1[7]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_8 = Label(window_6, text=f"Second class price($): {r1[8]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_9 = Label(window_6, text=f"Flight type:{r1[9]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_10 = Label(window_6, text=f"Departure time: {r1[10]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    label_11 = Label(window_6, text=f"Departure time: {r1[11]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    preferred_seat_entry = Entry(window_6, width=3, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=1)

                    book_1_button = Button(window_6, bg=front, fg=back, text="book", font=("segoe ui semibold", 12),
                                           activebackground=front, activeforeground=back, command=book_flight)
                    c1 = IntVar()
                    # x = c1.get()

                    business_class_radio = Radiobutton(window_6, variable=c1, value=1)
                    First_class_radio = Radiobutton(window_6, variable=c1, value=2)
                    Second_class_radio = Radiobutton(window_6, variable=c1, value=3)

                    seat_number.pack(pady=5, expand=True)
                    preferred_seat_entry.pack(expand=True)
                    label_1.pack(pady=5, expand=True)
                    label_2.pack(pady=5, expand=True)
                    label_3.pack(pady=5, expand=True)
                    label_4.pack(pady=5, expand=True)
                    label_5.pack(pady=5, expand=True)
                    label_6.pack(pady=5, expand=True)
                    business_class_radio.pack(expand=True)
                    label_7.pack(pady=5, expand=True)
                    First_class_radio.pack(expand=True)
                    label_8.pack(pady=5, expand=True)
                    Second_class_radio.pack(expand=True)
                    label_9.pack(pady=5, expand=True)
                    label_10.pack(pady=5, expand=True)
                    label_11.pack(pady=5, expand=True)
                    book_1_button.pack(pady=5, expand=True)
                    window_5.destroy()
                d3 = flight_DB.view_plane(3)
                plane_3 = Image.open("B-747_Iberia.jpg", mode="r")
                resize_plane_3 = plane_3.resize((160, 160))
                final_plane_3 = ImageTk.PhotoImage(resize_plane_3)
                flight_3 = Button(window_5, image=final_plane_3, command=plane3)
                d_3label = Label(window_5, text=f"{d3[2]}", bg="white", fg="black", font=("segoe ui semibold", 12))
                flight_3.image = final_plane_3
                flight_3.place(x=380, y=20)
                d_3label.place(x=405, y=200)

                # global final_pane_4
                def plane4():
                    def book_flight():
                        # value = business_class_radio.getint(1)
                        flight_serial = r1[0]
                        busines = r1[3]
                        firsts = r1[4]
                        seconds = r1[5]
                        user_seat = flight_DB.view_user(3)
                        seat = preferred_seat_entry.get()
                        plane1_info= flight_DB.view_plane(4)
                        name = plane1_info[1]
                        destination = plane1_info[2]

                        if c1.get() == 1:
                            if user_seat[3] == 'None':
                                if busines > 0:
                                    if '1' <= seat <= '70':
                                        mb.showinfo("Flight Booked", flight_DB.book_business(flight_serial, busines))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat >= '71':
                                        mb.showerror("Error", "Seat number is not available for business class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 2:
                            if user_seat[3] == "None": 
                                if firsts > 0:
                                    if seat >= '71':
                                        mb.showinfo("Flight Booked", flight_DB.book_first(flight_serial, firsts))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat >= '191' or seat <= '70':
                                        mb.showerror("Error", "Seat number is not available for first class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 3:
                            if user_seat[3] == "None":
                                if seconds > 0:
                                    if'191' <= seat <= '350':
                                        mb.showinfo("Flight booked", flight_DB.book_second(flight_serial, seconds))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)

                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat available!")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat <= '191':
                                        mb.showerror("Error", "seat not available for this class")
                                    elif seat > '350':
                                        mb.showerror("Error", "This Plane has only 350 seats")
                                    else:
                                        mb.showerror("Error", 'input not understood')
                                else:
                                    mb.showerror("error", "flight fully booked")
                            else:
                                mb.showerror("error", "You have already booked a flight")
                        else:
                            mb.showinfo("Info", "Please choose your desired class ")
                        window_6.destroy()

                    r1 = flight_DB.view_plane(4)
                    window_6 = Toplevel()
                    window_6.title("flight details")
                    window_6.config(bg="white")
                    window_6.geometry("1000x600")
                    seat_number = Label(window_6, text="Enter your serial number", fg="black", bg="white",
                                        font=("segoe ui semibold", 12))
                    label_1 = Label(window_6, text=f"Name: {r1[1]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_2 = Label(window_6, text=f"Destination: {r1[2]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_3 = Label(window_6, text=f"Business Seats: {r1[3]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_4 = Label(window_6, text=f"First class Seats: {r1[4]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_5 = Label(window_6, text=f"Second class seats: {r1[5]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_6 = Label(window_6, text=f"Business class price ($): {r1[6]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_7 = Label(window_6, text=f"First class price($): {r1[7]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_8 = Label(window_6, text=f"Second class price($): {r1[8]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_9 = Label(window_6, text=f"Flight type:{r1[9]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_10 = Label(window_6, text=f"Departure time: {r1[10]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    label_11 = Label(window_6, text=f"Departure time: {r1[11]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    preferred_seat_entry = Entry(window_6, width=3, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=1)

                    book_1_button = Button(window_6, bg=front, fg=back, text="book", font=("segoe ui semibold", 12),
                                           activebackground=front, activeforeground=back, command=book_flight)
                    c1 = IntVar()
                    # x = c1.get()

                    business_class_radio = Radiobutton(window_6, variable=c1, value=1)
                    First_class_radio = Radiobutton(window_6, variable=c1, value=2)
                    Second_class_radio = Radiobutton(window_6, variable=c1, value=3)

                    seat_number.pack(pady=5, expand=True)
                    preferred_seat_entry.pack(expand=True)
                    label_1.pack(pady=5, expand=True)
                    label_2.pack(pady=5, expand=True)
                    label_3.pack(pady=5, expand=True)
                    label_4.pack(pady=5, expand=True)
                    label_5.pack(pady=5, expand=True)
                    label_6.pack(pady=5, expand=True)
                    business_class_radio.pack(expand=True)
                    label_7.pack(pady=5, expand=True)
                    First_class_radio.pack(expand=True)
                    label_8.pack(pady=5, expand=True)
                    Second_class_radio.pack(expand=True)
                    label_9.pack(pady=5, expand=True)
                    label_10.pack(pady=5, expand=True)
                    label_11.pack(pady=5, expand=True)
                    book_1_button.pack(pady=5, expand=True)
                    window_5.destroy()
                d4 = flight_DB.view_plane(4)
                plane_4 = Image.open("airplane-flying-clouds-front-view-260nw-1297294231.jpg", mode="r")
                resize_plane_4 = plane_4.resize((160, 160))
                final_plane_4 = ImageTk.PhotoImage(resize_plane_4)
                flight_4 = Button(window_5, image=final_plane_4, command=plane4)
                d_4label = Label(window_5, text=f"{d4[2]}", bg="white", fg="black", font=("segoe ui semibold", 12))
                flight_4.image = final_plane_4
                flight_4.place(x=570, y=20)
                d_4label.place(x=595, y=200)
                # Plane 5

                def plane5():
                    def book_flight():
                        # value = business_class_radio.getint(1)
                        flight_serial = r1[0]
                        busines = r1[3]
                        firsts = r1[4]
                        seconds = r1[5]
                        user_seat = flight_DB.view_user(3)
                        seat = preferred_seat_entry.get()
                        plane1_info= flight_DB.view_plane(4)
                        name = plane1_info[1]
                        destination = plane1_info[2]

                        if c1.get() == 1:
                            if user_seat[3] == 'None':
                                if busines > 0:
                                    if '1' <= seat <= '50':
                                        mb.showinfo("Flight Booked", flight_DB.book_business(flight_serial, busines))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)
                                    elif seat >= '51':
                                        mb.showerror("Error", "Seat number is not available for business class")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat Available!")
                                    elif seat == "":
                                        mb.showerror("Error", "Choose a seat Number")
                                    else:
                                        mb.showerror("ERROR", "Input not understood")
                                else:
                                    mb.showerror("Error", "flight fully booked")
                            else:
                                mb.showerror("Error", "You already Have a Flight Booked, cancel it to book again")
                        elif c1.get() == 2:
                            if user_seat[3] == "None":
                                if firsts > 0:
                                    if seat >= '50':
                                        mb.showinfo("Flight booked", flight_DB.book_second(flight_serial, seconds))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)

                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat available!")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat <= '50' >= '151':
                                        mb.showerror("Error", "Seat not available for this class")
                                    else:
                                        mb.showerror("Error", 'Input not understood')
                                else:
                                    mb.showerror("error", "Flight fully booked")
                            else:
                                mb.showerror("error", "You have already booked a flight")
                
                        elif c1.get() == 3:
                            if user_seat[3] == "None":
                                if seconds > 0:
                                    if '151' <= seat <= '300':
                                        mb.showinfo("Flight booked", flight_DB.book_second(flight_serial, seconds))
                                        mb.showinfo("Seat number", flight_DB.update_user_seat(3, seat, name, destination))
                                        # flight_DB.update_user_plane_name(1, name)
                                        # flight_DB.update_user_destination(1, destination)

                                    elif seat == '0':
                                        mb.showerror("Error", "No such seat available!")
                                    elif seat < '0':
                                        mb.showerror("Error", "Seat Not Available!")
                                    elif seat <= '151':
                                        mb.showerror("Error", "seat not available for this class")
                                    elif seat > '300':
                                        mb.showerror("Error", "This Plane has only 300 seats")
                                    else:
                                        mb.showerror("Error", 'input not understood')
                                else:
                                    mb.showerror("error", "flight fully booked")
                            else:
                                mb.showerror("error", "You have already booked a flight")
                        else:
                            mb.showinfo("Info", "Please choose your desired class ")
                        window_6.destroy()

                    r1 = flight_DB.view_plane(5)
                    window_6 = Toplevel()
                    window_6.title("flight details")
                    window_6.config(bg="white")
                    window_6.geometry("1000x600")
                    seat_number = Label(window_6, text="Enter your serial number", fg="black", bg="white",
                                          font=("segoe ui semibold", 12))
                    label_1 = Label(window_6, text=f"Name: {r1[1]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_2 = Label(window_6, text=f"Destination: {r1[2]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_3 = Label(window_6, text=f"Business Seats: {r1[3]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_4 = Label(window_6, text=f"First class Seats: {r1[4]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_5 = Label(window_6, text=f"Second class seats: {r1[5]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_6 = Label(window_6, text=f"Business class price ($): {r1[6]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_7 = Label(window_6, text=f"First class price($): {r1[7]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_8 = Label(window_6, text=f"Second class price($): {r1[8]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_9 = Label(window_6, text=f"Flight type:{r1[9]}", fg="black", bg="white",
                                    font=("segoe ui semibold", 12))
                    label_10 = Label(window_6, text=f"Departure time: {r1[10]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    label_11 = Label(window_6, text=f"Departure time: {r1[11]}", fg="black", bg="white",
                                     font=("segoe ui semibold", 12))
                    preferred_seat_entry = Entry(window_6, width=3, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=1)

                    book_1_button = Button(window_6, bg=front, fg=back, text="book", font=("segoe ui semibold", 12),
                                           activebackground=front, activeforeground=back, command=book_flight)
                    c1 = IntVar()
                    # x = c1.get()

                    business_class_radio = Radiobutton(window_6, variable=c1, value=1)
                    First_class_radio = Radiobutton(window_6, variable=c1, value=2)
                    Second_class_radio = Radiobutton(window_6, variable=c1, value=3)

                    seat_number.pack(pady=5, expand=True)
                    preferred_seat_entry.pack(expand=True)
                    label_1.pack(pady=5, expand=True)
                    label_2.pack(pady=5, expand=True)
                    label_3.pack(pady=5, expand=True)
                    label_4.pack(pady=5, expand=True)
                    label_5.pack(pady=5, expand=True)
                    label_6.pack(pady=5, expand=True)
                    business_class_radio.pack(expand=True)
                    label_7.pack(pady=5, expand=True)
                    First_class_radio.pack(expand=True)
                    label_8.pack(pady=5, expand=True)
                    Second_class_radio.pack(expand=True)
                    label_9.pack(pady=5, expand=True)
                    label_10.pack(pady=5, expand=True)
                    label_11.pack(pady=5, expand=True)
                    book_1_button.pack(pady=5, expand=True)
                    window_5.destroy()
                d5 = flight_DB.view_plane(5)
                plane_5 = Image.open("Icelandair_Boeing_757-200_Wedelstaedt.jpg", mode="r")
                resize_plane_5 = plane_5.resize((160, 160))
                final_plane_5 = ImageTk.PhotoImage(resize_plane_5)
                flight_5 = Button(window_5, image=final_plane_5, command=plane5)
                d_5label = Label(window_5, text=f"{d5[2]}", bg="white", fg="black", font=("segoe ui semibold", 12))
                flight_5.image = final_plane_5
                flight_5.place(x=760, y=20)
                d_5label.place(x=785, y=200)

            def bookedflight():
                def cancel_flight():
                    seat = "None"
                    plane = "None"
                    destination = "None"
                    Name_1 = flight_DB.view_plane(1) 
                    Name_2 = flight_DB.view_plane(2) 
                    Name_3 = flight_DB.view_plane(3) 
                    Name_4 = flight_DB.view_plane(4) 
                    Name_5 = flight_DB.view_plane(5) 
                    user_seat = flight_DB.view_user(1)
                    if user_seat[3] != "None":          
                        if user_seat[4] == Name_1[1]:
                            flight_serial = Name_1[0]
                            business_1 = Name_1[3]
                            first_1 = Name_1[4]
                            second_1 = Name_1[5]  
                            if '50'>= user_seat[3] >='1':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(3, seat, plane, destination))
                                flight_DB.cancel_business(flight_serial, business_1)
                            elif  '150' >= user_seat[3] >'51':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(3, seat, plane, destination))
                                flight_DB.cancel_first(flight_serial, first_1)
                            else:
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(3, seat, plane, destination))
                                flight_DB.cancel_second(flight_serial, second_1)    
                        elif user_seat[4] == Name_2[1]:
                            flight_serial = Name_2[0]
                            business_1 = Name_2[3]
                            first_1 = Name_2[4]
                            second_1 = Name_2[5]  
                            if  '70' >= user_seat[3] > '0':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(3, seat, plane, destination))
                                flight_DB.cancel_business(flight_serial, business_1)
                            elif '190' >= user_seat[3] >= '71':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(3, seat, plane, destination))
                                flight_DB.cancel_first(flight_serial, first_1)
                            else :
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(3, seat, plane, destination))
                                flight_DB.cancel_second(flight_serial, second_1)    
                        elif user_seat[4]== Name_3[2]:
                            flight_serial = Name_3[0]
                            business_1 = Name_3[3]
                            first_1 = Name_3[4]
                            second_1 = Name_3[5]  
                            if '50' >= user_seat[3] >= '1':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_business(flight_serial, business_1)
                            elif '150' >= user_seat[3] >= '51':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_first(flight_serial, first_1)
                            else :
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_second(flight_serial, second_1)    
                        elif user_seat[4]== Name_4[1]:
                            flight_serial = Name_4[0]
                            business_1 = Name_4[3]
                            first_1 = Name_4[4]
                            second_1 = Name_4[5]  
                            if '70' >= user_seat[3] >= '1':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_business(flight_serial, business_1)
                            elif '190' >= user_seat[3] >= '71':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_first(flight_serial, first_1)
                            else :
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_second(flight_serial, second_1)    
                        elif user_seat[4]== Name_5[1]:
                            flight_serial = Name_5[0]
                            business_1 = Name_5[3]
                            first_1 = Name_5[4]
                            second_1 = Name_5[5]  
                            if '50' >= user_seat[3] >= '1':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_business(flight_serial, business_1)
                            elif '150' >= user_seat[3] >= '51':
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_first(flight_serial, first_1)
                            else :
                                mb.showinfo("Flight cancelled", flight_DB.cancel_booking(2, seat, plane, destination))
                                flight_DB.cancel_second(flight_serial, second_1)    
                        else:
                            mb.showerror("Error", "Visit book flight page")
                    else:
                        mb.showerror("Error", "You dont have any flight booked")
                
                    window_7.destroy()

                user_seat = flight_DB.view_user(2)
                window_7 = Tk()
                window_7.config(bg="White")
                window_7.title(f"{name}'s bookings")
                window_7.geometry("1000x600")
                wel_label = Label(window_7, text=f"Welcome {name}, your bookings are:", bg="white", fg="black",
                                  font=('segoe ui semibold', 20))
                seat_label = Label(window_7, text=f"seat number: {user_seat[3]}", bg="white", fg="black",
                                   font=('segoe ui semibold', 17))
                name_label = Label(window_7, text=f"Plane name: {user_seat[4]}", bg="white", fg="black",
                                   font=('segoe ui semibold', 17))
                destination_label = Label(window_7, text=f"Destination: {user_seat[5]}", bg="white", fg="black",
                                   font=('segoe ui semibold', 17))
                # date_label = Label(window_7, text=f"Departure date: {user_seat[3]}", bg="white", fg="black",
                #                    font=('segoe ui semibold', 17))
                # time_label = Label(window_7, text=f"Departure time: {user_seat[3]}", bg="white", fg="black",
                #                    font=('segoe ui semibold', 17))
                
                cancel_label = Label(window_7, text=f"Cancel booking:", bg="white", fg="black",
                                     font=('segoe ui semibold', 17))
                cancel_button = Button(window_7, text="cancel", bg=front, fg=back, font=("segoe ui semibold", 17), command=cancel_flight)
                #ser_label = Label(window_7, text=f"serial number", bg="white", fg="black",
                                  # font=('segoe ui semibold', 17))
                # serial_number_entry_2 = Entry(window_7, width=3, font=('segoe ui semibold', 13), highlightbackground="black", highlightthickness=2)
                wel_label.pack(expand=TRUE)
                seat_label.pack(expand=TRUE)
                name_label.pack(pady=10, expand=True)
                destination_label.pack(pady=10, expand=True)
                # ser_label.pack(expand=TRUE)
                # serial_number_entry_2.pack(expand=TRUE)
                cancel_label.pack(pady=10, expand=TRUE)

                cancel_button.pack(pady=20, expand=TRUE)
            window.destroy()

            window_3 = Tk()
            window_3.config(bg="white")
            window_3.title(f"{name}'s Login")
            window_3.geometry("1000x600")
            global new_pic
            pic = Image.open("1.png", mode="r")
            resize_pic = pic.resize((160, 160))
            new_pic = ImageTk.PhotoImage(resize_pic)
            welcome_label = Label(window_3, text=f"Welcome {name}", bg="white", fg="black",
                                  font=("segoe ui semibold", 14))
            image_label = Label(window_3, image=new_pic)
            image_label.image = pic
            # serial_number_label = Label(window_3, text="Serial", fg="black", bg="white", font=("segoe ui semibold", 17))
            #   serial_number_entry_3 = Entry(window_3, width=3, font=('segoe ui semibold', 13),
                # highlightbackground="black", highlightthickness=2)

            view_flight_label = Label(window_3, text="view upcoming flights", bg="white", fg="black",
                                      font=("segoe ui semibold", 14))
            view_flights_button = Button(window_3, text="view", bg=front, fg=back, activeforeground=back,
                                         font=("segoe ui semibold", 14), activebackground=front, command=view_upcoming)
            view_booked_label = Label(window_3, text="Your bookings", bg="white", fg="black",
                                      font=("segoe ui semibold", 14))

            view_booked_button = Button(window_3, text="view", bg=front, fg=back, activeforeground=back,
                                        font=("segoe ui semibold", 14), activebackground=front, command=bookedflight)
            v = tkinter.StringVar()
            combobox = ttk.Combobox(window_3, textvariable=v)
            combobox["values"] = ["New York", "London", "Manchester", "Las vegas", "Toronto"]
            combobox.current(0)
            welcome_label.pack(pady=10)
            # serial_number_label.place(y=350, x=80)
            # serial_number_entry_3.place(y=350, x=180)
            image_label.place(x=460, y=50)
            view_flight_label.place(x=80, y=180)
            view_flights_button.place(x=300, y=180)
            view_booked_label.place(x=80, y=280)
            view_booked_button.place(x=300, y=280)

            # combobox.place(x=700, y=180)





window = Tk()
# Image storage
icon = PhotoImage(file="1.png")


def show():
    hide_but = Button(window, image=hide_image, command=hide, relief=FLAT, activebackground="white",
                      bd=0, bg="white")
    hide_but.place(x=630, y=357)
    Password_entry.config(show="")


def hide():
    show_but = Button(window, image=show_image, command=show, relief=FLAT, activebackground="white",
                      bd=0, bg="white")
    show_but.place(x=630, y=357)
    Password_entry.config(show="*")


window.title("Shamzi Airways")
window.geometry('1000x600')
window.iconphoto(True, icon)
window.config(bg=back)
hidei = Image.open("download (3).png", mode="r")
resize_hidei = hidei.resize((24, 24))
showei = Image.open("download.png", mode="r")
resize_showei = showei.resize((24, 24))
hide_image = ImageTk.PhotoImage(resize_hidei)
show_image = ImageTk.PhotoImage(resize_showei)

# Labels
title_label = Label(window, text="Enter name and password", bg=back, fg=front, font=('Lucida calligraphy', 16))
name_label = Label(window, text="Name", bg=back, fg=front, font=("segoe ui semibold", 14))
Password_label = Label(window, text="Password", bg=back, fg=front, font=("segoe ui semibold", 14))

# Entries
name_entry = Entry(window, borderwidth=2, highlightcolor=front, highlightthickness=2, font=("segoe ui semibold", 14), relief=RIDGE)
Password_entry = Entry(window, borderwidth=2, highlightcolor=front, highlightthickness=2, font=("segoe ui semibold", 14), show="*", relief=GROOVE)

# Buttons
login_button = Button(window, fg=back, bg=front, text="login", highlightcolor=front, activebackground=front,
                      activeforeground=back, font=("segoe ui semibold", 14), command=login)
create_button = Button(window, fg=back, bg=front, text="create account", highlightcolor=front, activebackground=front,
                       activeforeground=back, font=("segoe ui semibold", 14), command=createacct)
hide_b = Button(window, image=hide_image, command=show, relief=FLAT, activebackground="white",
                bd=0, bg="white")
show_b = Button(window, image=show_image, command=show, relief=FLAT, activebackground="white",
                bd=0, bg="white")
show_b.place(x=630, y=357)

# Packing
title_label.pack(expand=True)
name_label.pack(expand=True)
name_entry.pack(expand=True)
Password_label.pack(expand=True)
Password_entry.pack(expand=True)
login_button.pack(expand=True)
create_button.pack(expand=True)


window.mainloop()
