from zipfile import ZipFile

with ZipFile("new.zip","r") as zip_object:
    zip_object.extractall()

print(zip_object.namelist())