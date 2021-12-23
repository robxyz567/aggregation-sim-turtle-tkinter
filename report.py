from datetime import datetime


class Report:
    def __init__(self, number, speed, precision, m_type, b_type):
        now = datetime.now()
        now = now.strftime("%d/%m/%Y, %H:%M:%S")
        with open('report.txt', 'a') as file:
            file.write(f"\n\nTime: {now} \nMolecules number: {number} \nMolecules speed: {speed} \nPrecision: {precision} \nMoving type: {m_type} \nBorder type: {b_type}")

    def add_result(self, time, score):
        with open('report.txt', 'a') as file:
            file.write(f"\n{time},{score}")




