import time, os, wget

user = os.getenv('username')

yesorno = input("Are you Sure? (y or n): ")

if yesorno == "y" or yesorno == "Y":
    print("ok.  starting")
    time.sleep(1)

    os.remove(f'C:/Users/{user}/Desktop/antiVIRUS/threats.txt')

    time.sleep(4)

    url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threats.txt'
    wget.download(url, f'C:/Users/{user}/Desktop/antiVIRUS/threats.txt')

else:
    print("ok.  stopping")
    time.sleep(1)
    
