import time
lines = ["ESKA BE CHHAYA.......",
        "TU TAKDA NAI SANU.....",
        "TAK DE NI JEENU ....",
        "OH TAKTDA NE SANU. ...",
        "TAKDE NE JEENU ....",
        "HO TAKDE NE SANU....",
        "FIRDE VE JEENU.....",
        "YA LAZ SAMI ....",
        "FIRDE VE SANU....",
        "YA LAZ SAMI ....",
        "NAZERA DE BICHBI YA LAZ SAMI....",
        ]
for line in lines:
    for ch in line:
      print(ch ,end="",flush=True)
    time.sleep(1.5)
    print()
    time.sleep(0.7)