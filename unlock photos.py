from cryptography.fernet import Fernet
key = Fernet.generate_key()


with open("key.key","rb") as f:
    key = f.read()

fernet = Fernet(key)

with open("IMG20220205115922.jpg","rb") as f:
    Photo = f.read()

lock = fernet.decrypt(Photo)

with open("IMG20220205115922.jpg", "wb") as Unlock_photo:
    Unlock_photo.write(lock)

print("Your Photo is Unlocked ")