import pyfiglet

font = pyfiglet.figlet_format('Wasif Ansari')
print(font)

with open("design","w") as f:
    f.write(font)

