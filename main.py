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
    screen.title("Simulation")
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
            if (BOARD_W/2 < molecule.xcor() < BOARD_W/2+50) or molecule.xcor() < -BOARD_W/2 or (BOARD_H/2 < molecule.ycor() < BOARD_H/2+50) or molecule.ycor() < -BOARD_H/2:
                molecule.bounce(borders, move_type)

        for molecule in molecules:
            if (BOARD_W/2+50 > molecule.xcor()) > -BOARD_W/2-50 and (BOARD_H/2+50 > molecule.ycor() > -BOARD_H/2-50):
                molecule.move(move_type)

        for i in range(0, len(molecules)):
            for j in range(i+1, len(molecules)):
                if molecules[i].xcor() < BOARD_W/2+50 and molecules[i].ycor() < BOARD_H/2+50:
                    if molecules[i].distance(molecules[j]) < precision:
                        n += 1
                        molecules[i].size_increase(molecules[i].size_a, molecules[j].size_a)
                        molecules[j].goto(BOARD_H, BOARD_W)

        cond_score = n/number*100
        formatted_cond = "{:.2f}".format(cond_score)
        time.sleep(TIME_DELAY)

        if not simulation:
            molecules.clear()
            screen.clear()
            screen.bgcolor("black")
            running = False

        now = time.time() - start
        formatted_time = "{:.2f}".format(now)
        time_label.config(text=f"Time of simulation: {formatted_time}")
        cond_label.config(text=f"Condesation score: {formatted_cond}%")
        rep.add_result(formatted_time, formatted_cond)
    screen.exitonclick()


window = Tk()
window.title("Condenser")
window.config(padx=50, pady=25, bg='#84DFFF')

#Scales
number_scale = Scale(from_=0, to=200, orient=HORIZONTAL, bg='#84DFFF')
number_scale.set(100)
number_scale.grid(row=1, column=1)
precision_scale = Scale(from_=0, to=40, orient=HORIZONTAL, bg='#84DFFF')
precision_scale.set(10)
precision_scale.grid(row=2, column=1)
speed_scale = Scale(from_=0, to=20, orient=HORIZONTAL, bg='#84DFFF')
speed_scale.set(5)
speed_scale.grid(row=3, column=1)

#Buttons
start_button = Button(height=1, width=9, text="START", font=('Arial', 12, "bold"), bg='#9AE66E', command=start)
start_button.grid(row=0, column=0)
end_button = Button(height=1, width=9, text="RESET", font=('Arial', 12, "bold"), bg='#FF6D6D', command=end)
end_button.grid(row=0, column=1)

move_var = IntVar()
chaotic_radiobutton = Radiobutton(text="Chaotic", variable=move_var, value=0, bg='#84DFFF')
chaotic_radiobutton.grid(row=4, column=0)
steady_radiobutton = Radiobutton(text="Steady", variable=move_var, value=1, bg='#84DFFF')
steady_radiobutton.grid(row=5, column=0)

border_var = IntVar()
noborder_radiobutton = Radiobutton(text="No borders", variable=border_var, value=0, bg='#84DFFF')
noborder_radiobutton.grid(row=4, column=1)
border_radiobutton = Radiobutton(text="Borders", variable=border_var, value=1, bg='#84DFFF')
border_radiobutton.grid(row=5, column=1)
vborder_radiobutton = Radiobutton(text="Virtual borders", variable=border_var, value=2, bg='#84DFFF')
vborder_radiobutton.grid(row=6, column=1)

#Labels
number_label = Label(height=2, text="Number: ", font=('Arial', 12, "bold"), bg='#84DFFF')
number_label.grid(row=1, column=0)
precision_label = Label(height=2, text="Precision: ", font=('Arial', 12, "bold"), bg='#84DFFF')
precision_label.grid(row=2, column=0)
speed_label = Label(height=2, text="Speed: ", font=('Arial', 12, "bold"), bg='#84DFFF')
speed_label.grid(row=3, column=0)

time_label = Label(height=2, text="Time of simulation: ", font=('Arial', 12, "bold"), bg='#84DFFF')
time_label.grid(row=9, column=0, columnspan=2)
cond_label = Label(height=2, text="Condesation score: ", font=('Arial', 12, "bold"), bg='#84DFFF')
cond_label.grid(row=10, column=0, columnspan=2)

window.mainloop()