import random
moods = [
    "😡 Aaj mood khrab hai !",
    "😴 Sone do yaar !",
    "🤣 Tum funny ho !",
    "🤔 Tum kuch zyada hi sochte ho !",
    "😎 tum smart lagte ho !"
]
name = input("write your name !")
print("\nHello ", name)
print(random.choice(moods))
