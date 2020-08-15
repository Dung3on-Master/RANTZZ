import string, random, time, os
import rantssecuritymenu

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

user = os.getenv('username')

file = open(f"C:/Users/{user}/Desktop/passkey.txt","w") 

idfornow = f'{id_generator()}'
file.write(f"your passkey is: {idfornow}") 

file.close()

print("copy your passkey into the passkey  \n \n \n \n")

passtry = True
if passtry == True:

    passkeyenter = input("passkey: ")
    if passkeyenter == f"{idfornow}":
        print("\n \n \n \n")
        print("login sucsessful")
        time.sleep(1)
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
        time.sleep(1)
        rantssecuritymenu.rantsstart()        
    else:
        print("\n \n \n \n")
        print("error logging in, please try copieing the passkey from the document.")
        passtry = True
