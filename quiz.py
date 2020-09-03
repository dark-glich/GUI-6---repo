from tkinter import *
import sqlite3
import tkinter.font

score = 0
grade = "POOR"
color = "brown"
root = Tk()
root.title("LOGIN WINDOW")
root.iconbitmap("Graphicloads-100-Flat-Home.ico")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
connection = sqlite3.connect("accounts registered")
cursor = connection.cursor()


def result(s, a, b, c):
    s.destroy()
    global score, grade, color
    result_window = Tk()
    result_window.title("RESULT")
    result_window.iconbitmap("Custom-Icon-Design-Pretty-Office-7-Trophy-gold.ico")
    if a.get() == 1:
        score += 1
    if b.get() == 1:
        score += 1
    if c.get() == 1:
        score += 1
    if score == 1:
        grade = "AVERAGE"
        color = "dark green"
    if score == 2:
        grade = "QUITE WELL"
        color = "green"
    if score == 3:
        grade = "PERFECT"
        color = "light green"
    result_frame = LabelFrame(result_window, text="RESULT :", font=("arial", 50, "bold"), fg="grey")
    result_frame.grid(row=0, column=0)
    results = Label(result_frame, text=grade + " = YOU GOT " + str(score) + " OUT OF 3 ! ", font=("arial", 40, "bold"), fg=color)
    results.grid(row=0, column=0)
    answer_frame = LabelFrame(result_window, text="ANSWERS :", pady=50, font=("arial", 50, "bold"), fg="grey")
    answer_frame.grid(row=1, column=0)
    answers = [
        (" ANSWER :: 1 = (b) 6 ,", 0, "light blue"),
        (" ANSWER :: 2 = (c) D ,", 1, "blue"),
        (" ANSWER :: 3 = (a) 21 June", 2, "dark blue")
    ]
    for answer, rows, c in answers:
        f = Label(answer_frame, text=answer, font=("arial", 20, "bold"), fg=c)
        f.grid(row=rows, column=0)
    print("SCORE : " + str(score) + "\n#THANKS FOR PLAYING")


def op_c(a, b, c):
    if a.get() == 1:
        b.set(0)
        c.set(0)


def quiz(a):
    a.destroy()
    game = Tk()
    game.title("B's QUIZ")
    c, v = game.winfo_screenwidth(), game.winfo_screenheight()
    game.geometry("%dx%d+0+0" % (c, v))
    game.iconbitmap("Seanau-Flat-App-Questionmark.ico")
    font2 = ("arial", 20)
    font = ("arial", 50, "bold")
    ea = LabelFrame(game, pady=60, text="NOOB", font=font, fg="light blue")
    ea.grid(row=0, column=0)
    am = LabelFrame(game, padx=20, pady=76, text="AMATEUR", font=font, fg="blue")
    am.grid(row=0, column=1)
    ma = LabelFrame(game, padx=6, pady=76, text="MASTER", font=font, fg="dark blue")
    ma.grid(row=0, column=2)

    ea2 = LabelFrame(game, pady=50, padx=192)
    am2 = LabelFrame(game, padx=219, pady=50)
    ma2 = LabelFrame(game, padx=143, pady=50)
    ea2.grid(row=1, column=0)
    am2.grid(row=1, column=1)
    ma2.grid(row=1, column=2)

    op, cp, dp = IntVar(), IntVar(), IntVar()
    my_font = tkinter.font.Font(size=20)
    op_1 = Checkbutton(ea2, text="4", variable=op, command=lambda: op_c(op, cp, dp))
    op_2 = Checkbutton(ea2, text="6", variable=cp, command=lambda: op_c(cp, op, dp))
    op_3 = Checkbutton(ea2, text="8", variable=dp, command=lambda: op_c(dp, cp, op))
    op_1.grid(row=0, column=0)
    op_2.grid(row=1, column=0)
    op_3.grid(row=2, column=0)
    op_3['font'], op_2['font'],  op_1['font'] = my_font, my_font, my_font

    od, bd, pd = IntVar(), IntVar(), IntVar()
    od_1 = Checkbutton(am2, text="J", variable=od, command=lambda: op_c(od, bd, pd))
    od_2 = Checkbutton(am2, text="M", variable=bd, command=lambda: op_c(bd, od, pd))
    od_3 = Checkbutton(am2, text="D", variable=pd, command=lambda: op_c(pd, bd, od))
    od_1.grid(row=0, column=0)
    od_2.grid(row=1, column=0)
    od_3.grid(row=2, column=0)
    od_1['font'], od_2['font'], od_3['font'] = my_font, my_font, my_font

    pa, la, sa = IntVar(), IntVar(), IntVar()
    pa_1 = Checkbutton(ma2, text="21 June", variable=pa, command=lambda: op_c(pa, la, sa))
    pa_2 = Checkbutton(ma2, text="3 May", variable=la, command=lambda: op_c(la, pa, sa))
    pa_3 = Checkbutton(ma2, text="18 July", variable=sa, command=lambda: op_c(sa, la, pa))
    pa_1.grid(row=0, column=0)
    pa_2.grid(row=1, column=0)
    pa_3.grid(row=2, column=0)
    pa_1['font'], pa_2['font'], pa_3['font'] = my_font, my_font, my_font

    questions = [
        (ea, ":: Q-1 :: \n if there are 4 people and all\n hugged each other then how many\n hugs were made ? ", 0),
        (am, ":: Q-2 :: \n continue the order : \n \'J, F, M, A, M, J, J, A, S, O, N, ____\'", 0),
        (ma, ":: Q-3 :: \n  When is the International Yoga \n Day is celebrated?", 0)
    ]
    for r, q, col in questions:
        lam = Label(r, text=q, font=font2)
        lam.grid(row=1, column=col)

    result_button = Button(game, text="SHOW RESULT", font=("arial", 20, "bold"), command=lambda: result(game, cp, pd, pa),
                           fg="orange", relief="ridge")
    result_button.grid(row=3, column=1, ipadx=135, ipady=30)


def sub(a, b, c, d, e, f, g):
    global connection, cursor
    f_name, s_name, email, age, country, user = a.get(), b.get(), c.get(), d.get(), e.get(), f.get()
    connection = sqlite3.connect("accounts registered")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts VALUES (:f_name, :s_name, :email, :age, :country, :user)",
                   {
                       "f_name": "first name : " + f_name,
                       "s_name": "second name : " + s_name,
                       "email": "email id : " + email,
                       "age": "age : " + age,
                       "country": "country : " + country,
                       "user": "user : " + user
                   })

    cursor.execute("SELECT *, oid FROM accounts")
    k = cursor.fetchall()
    ide = str(k[-1])
    print("ACCOUNT REGISTERD : \n" + ide)
    connection.commit()
    connection.close()
    a.delete(0, END), b.delete(0, END), c.delete(0, END), d.delete(0, END), e.delete(0, END), f.delete(0, END)
    quiz(g)


def acount():
    root.destroy()
    window = Tk()
    window.title("CREATE ACCOUNT")
    window.iconbitmap("Icons8-Windows-8-User-Interface-Login.ico")
    create_frame = LabelFrame(window, text="CREATE A ACCOUNT", font=("arial", 20, "bold"), padx=40, pady=40, fg="light blue")
    create_frame.grid(row=0, column=0, pady=30)

    first_name = Label(create_frame, text="first name       : ", font=("arial", 15, "bold"))
    second_name = Label(create_frame, text="second name  : ", font=("arial", 15, "bold"))
    email = Label(create_frame, text="email address : ", font=("arial", 15, "bold"))
    age = Label(create_frame, text="your age         : ", font=("arial", 15, "bold"))
    country = Label(create_frame, text="your country  : ", font=("arial", 15, "bold"))
    user = Label(create_frame, text="user name      : ", font=("arial", 15, "bold"))

    first_name.grid(row=0, column=0)
    second_name.grid(row=1, column=0)
    email.grid(row=2, column=0)
    age.grid(row=3, column=0)
    country.grid(row=4, column=0)
    user.grid(row=5, column=0)

    first_name_entry = Entry(create_frame)
    second_name_entry = Entry(create_frame)
    email_entry = Entry(create_frame)
    age_entry = Entry(create_frame)
    country_entry = Entry(create_frame)
    user_entry = Entry(create_frame)

    first_name_entry.grid(row=0, column=1, ipadx=80)
    second_name_entry.grid(row=1, column=1, ipadx=80)
    email_entry.grid(row=2, column=1, ipadx=80)
    age_entry.grid(row=3, column=1, ipadx=80)
    country_entry.grid(row=4, column=1, ipadx=80)
    user_entry.grid(row=5, column=1, ipadx=80)
    g = StringVar(create_frame)
    g.set("None")
    gen = Label(create_frame, text="gender            : ", font=("arial", 15, "bold"))
    gen.grid(row=6, column=0)
    gender = OptionMenu(create_frame, g, "male", "female")
    gender.grid(row=6, column=1, ipadx=110, columnspan=30)
    submit = Button(window, text="create account", relief="ridge"
                    , command=lambda: sub(first_name_entry, second_name_entry, email_entry, age_entry, country_entry, user_entry, window), fg="orange", font=("arial ", 20, "bold"))
    submit.grid(row=1, column=0, ipadx=180, ipady=10)


login_frame = LabelFrame(root, text=" PLEASE LOGIN ", font=("arial", 50, "bold"), relief="ridge", padx=50, pady=50, fg="light "
                                                                                                                       "blue")
login_frame.grid(row=1, column=0, ipadx=250, ipady=100)
create_button = Button(login_frame, text="CREATE ACCOUNT", font=("arial", 20, "bold"), command=acount, fg="orange", relief="ridge")
create_button.grid(row=0, column=0, padx=100, pady=200, ipadx=100, ipady=50)
guest_button = Button(login_frame, text="LOGIN AS GUEST", font=("arial", 20, "bold"), command=lambda: quiz(root), fg="orange", relief="ridge")
guest_button.grid(row=0, column=1, padx=100, pady=200, ipadx=100, ipady=50)
connection.commit()
connection.close()

root.mainloop()
