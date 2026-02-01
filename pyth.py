import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Generate x values
x = np.linspace(0, 2*np.pi, 200)
line, = ax.plot(x, np.sin(x))

# Update function for animation
def update(frame):
    y = np.sin(x + 0.1 * frame)   # wave shifting with time
    line.set_ydata(y)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()