from turtle import Screen
from tkinter import *
from molecule import Molecule
from frame import Frame
from report import Report
import time

TIME_DELAY = 0.1
BOARD_W = 800
BOARD_H = 800


def end():
    global simulation
    simulation = False


def start():
    global simulation
    simulation = True

    move_type = int(move_var.get())
    borders = int(border_var.get())

    screen = Screen()
    screen.setup(width=BOARD_W + 50, height=BOARD_H + 50)
    screen.bgcolor("black")
    screen.title("Aggregation Simulator")
    screen.tracer(0)

    number = int(number_scale.get())
    speed = int(speed_scale.get())
    precision = int(precision_scale.get())

    rep = Report(number, speed, precision, move_type, borders)

    if borders == 1 or borders == 2:
        frame = Frame(BOARD_W, BOARD_H, borders)

    molecules = []
    for i in range(0, number):
        molecules.append(Molecule(BOARD_W, BOARD_H, speed))

    n = 0
    running = True
    start = time.time()
    while running:

        screen.update()

        for molecule in molecules:
            if (400 < molecule.xcor() < 450) or molecule.xcor() < -400 or (400 < molecule.ycor() < 450) or molecule.ycor() < -400:
                molecule.bounce(borders, move_type)

        for molecule in molecules:
            if 500 > molecule.xcor() > -500:
                molecule.move(move_type)

        z = 0
        for molecule in molecules:
            if -450 < molecule.xcor() < 450 and -450 < molecule.ycor() < 450:
                z += 1

        for i in range(0, len(molecules)):
            for j in range(i+1, len(molecules)):
                if molecules[i].xcor() < 450:
                    if molecules[i].distance(molecules[j]) < precision:
                        n += 1
                        molecules[i].size_increase(molecules[i].size_a, molecules[j].size_a)
                        molecules[j].goto(1000, 1000)

        cond_score = n/number*100
        formatted_cond = "{:.2f}".format(cond_score)
        time.sleep(TIME_DELAY)

        if not simulation:
            molecules.clear()
            screen.clear()
            screen.bgcolor("black")
            running = False

        now = time.time() - start
        formatted_string = "{:.2f}".format(now)
        time_label.config(text=f"Time of simulation: {formatted_string}")
        cond_label.config(text=f"Condesation score: {formatted_cond}%")
        rep.add_result(formatted_string, formatted_cond)
    screen.exitonclick()


window = Tk()
window.title("Kondensator")
window.config(padx=50, pady=25, bg='#F2EDD7')

#Scales
number_scale = Scale(from_=0, to=200, orient=HORIZONTAL)
number_scale.set(100)
number_scale.grid(row=2, column=0, columnspan=4)
speed_scale = Scale(from_=0, to=25, orient=HORIZONTAL)
speed_scale.set(5)
speed_scale.grid(row=3, column=0, columnspan=4)
precision_scale = Scale(from_=0, to=50, orient=HORIZONTAL)
precision_scale.set(10)
precision_scale.grid(row=4, column=0, columnspan=4)

#Buttons
on = IntVar()

start_button = Button(height=1, width=9, text="START", font=('Arial', 12, "bold"), bg='#9AE66E', command=start)
start_button.grid(row=0, column=0)
end_button = Button(height=1, width=9, text="RESET", font=('Arial', 12, "bold"), bg='#FF6D6D', command=end)
end_button.grid(row=0, column=1)

move_var = IntVar()
chaotic_radiobutton = Radiobutton(text="Chaotic", variable=move_var, value=0)
chaotic_radiobutton.grid(row=5, column=0)
steady_radiobutton = Radiobutton(text="Steady", variable=move_var, value=1)
steady_radiobutton.grid(row=6, column=0)

border_var = IntVar()
noborder_radiobutton = Radiobutton(text="No borders", variable=border_var, value=0)
noborder_radiobutton.grid(row=7, column=0)
border_radiobutton = Radiobutton(text="Borders", variable=border_var, value=1)
border_radiobutton.grid(row=8, column=0)
vborder_radiobutton = Radiobutton(text="Virtual borders", variable=border_var, value=2)
vborder_radiobutton.grid(row=9, column=0)

#Labels
time_label = Label(height=2, text="Waiting ...", font=('Arial', 14, "bold"), bg='#F2EDD7')
time_label.grid(row=10, column=0, columnspan=3)

cond_label = Label(height=2, text="Condesation score ...", font=('Arial', 14, "bold"), bg='#F2EDD7')
cond_label.grid(row=11, column=0, columnspan=3)

window.mainloop()