from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open("key.key","wb") as f:
    f.write(key)

fernet = Fernet(key)

with open("IMG20220205115922.jpg","rb") as f:
    Photo = f.read()

lock = fernet.encrypt(Photo)

with open("IMG20220205115922.jpg", "wb") as lock_photo:
    lock_photo.write(lock)

print("Your Photo is locked ")

