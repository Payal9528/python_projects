import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis("off")  # Hide axes

# Text object in the middle
text = ax.text(0.5, 0.5, "", ha="center", va="center", fontsize=20, color="blue")

# Message to animate
message = "What is Python?\n\nPython is a powerful, easy-to-learn programming language.\nIt is used in web development, data science, AI, and more!"

# Update function for animation
def update(i):
    text.set_text(message[:i])  # Show text gradually
    return text,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(message)+1, interval=100, blit=True)

# Save as video (requires ffmpeg installed)
ani.save("what_is_python.mp4", writer="ffmpeg", fps=30)

print("✅ Video saved as what_is_python.mp4")
