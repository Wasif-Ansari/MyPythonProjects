import getpass

database = {"wasif":"123", "ansari":"456"}

username = input("Enter your username: ")
password = input("Enter your password: ")

for i in database.keys():
    if username==i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break
print("Verified")