import time
import sys

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
     # line break at the end
# Example usage
animate_text("Hello Payal! Ye ek simple text animation hai 😊", delay=0.30)