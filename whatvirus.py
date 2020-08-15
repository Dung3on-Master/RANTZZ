import os

myfile = ''
user = os.getenv('username')
os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
myfile = open("threats.txt", "r")
content = myfile.read()

allthreats = [content]
print(allthreats)
