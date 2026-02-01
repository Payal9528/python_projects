from colorama import Fore, Style, init
import time

init(autoreset=True)

def type_write(text, color=Fore.WHITE, speed=0.05):
    for char in text:
        print(color + char + Style.RESET_ALL, end="", flush=True)
        time.sleep(speed)
    print()

def main():
    type_write("✨ What is Python? ✨", Fore.CYAN, 0.07)
    type_write("Python is powerful and easy to learn.", Fore.GREEN, 0.05)
    type_write("It is used in AI, Data Science, Web Development.", Fore.MAGENTA, 0.05)
    type_write("🚀 Learn Python, shape the future!", Fore.BLUE, 0.07)

# ✅ Make sure to call main()
if __name__ == "__main__":
    main()
