import numpy as np
import matplotlib.pyplot as plt


one_line_max_length = 70


def add_enters_to_title(title):
    if len(title) <= one_line_max_length:
        return title
    else:
        space_cnt = title.count(' ')
        enter_pos = space_cnt // 2

        i = 0
        while enter_pos > 0:
            if (title[i] == ' '):
                enter_pos -= 1
            i += 1

        return add_enters_to_title(title[:i]) + "\n" + add_enters_to_title(title[i:])



data = np.loadtxt("data.txt", dtype=int)
settings = np.loadtxt("settings.txt")

dt = settings[0]
dv = settings[1]

fig, ax = plt.subplots(figsize=(10, 8))

time = np.linspace(0, (len(data) - 1) * dt, len(data))
volt = data * dv

ax.plot(time, volt,)
ax.plot(time, volt, 'D', markevery=0.04, label='V(t)', markersize=4, color='r', marker='o')

title = "Зарядка и разрядка конденсатора от времени в RC цепи"

ax.set_title(add_enters_to_title(title), fontsize=14)
ax.set(xlabel='Время t, с', ylabel='Напряжение V, В')

time_of_expr = len(data) * dt
time_charge = np.argmax(data) * dt
time_discharge = time_of_expr - time_charge

ax.text(8, 1.5, f"Время зарядки  = {round(time_charge, 2)} c")
ax.text(8, 1.4, f"Время разрядки = {round(time_discharge, 2)} c")

ax.grid(which='major')
ax.minorticks_on()
ax.grid(which='minor', linestyle=':')

ax.legend()

plt.savefig("graph.png")
plt.savefig("graph.svg")

plt.show()
