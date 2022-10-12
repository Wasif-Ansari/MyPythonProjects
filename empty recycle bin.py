import winshell

try:
    winshell.recycle_bin().empty(confirm=False,show_progress=True,sound=True)
    print("Recycle bin emptied")
except:
    print("already empty")