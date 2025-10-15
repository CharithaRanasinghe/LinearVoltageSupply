import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

V_ref = 1.25
R1 = 240
R2_min = 0
R2_max = 5000

R2_init = 2500

V_in = 12
V_drop = 3

def V_out(R2): #is a function of R2 (adj res)
    V_calc =  V_ref * (1 + R2/R1) #lm317 equation
    return np.minimum(V_calc, V_in - V_drop) # saturate


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
R2_vals = np.linspace(R2_min, R2_max, 1000)
Vout_vals = V_out(R2_vals)
line, = plt.plot(R2_vals, Vout_vals, lw=2)
plt.xlabel("Potentiometer Resistance (Ω)")
plt.ylabel("Output Voltage (V)")
plt.title("LM317 Output Voltage vs Potentiometer")
plt.grid(True)

ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Pot (Ω)', R2_min, R2_max, valinit=R2_init)

def update(val):
    R2_current = slider.val
    Vout_current = V_out(R2_current)
    line.set_ydata(V_out(R2_vals))
    ax.set_title(f"LM317 Output Voltage: {Vout_current:.2f} V")
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
