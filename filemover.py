import time, os, click, shutil, tkinter
from pathlib import Path
from tkinter import messagebox
from tkinter import *

def movetosurcurefolder():

    user = os.getenv('username')
    filesercure = input("what file do you want to Sercure? (please add the ending e.g paskey.txt): ")
    fileplace = input("What file is it in? (Downloads, Documents, etc): ")

    filemoving = f"C:\\Users\\{user}\\{fileplace}"

    print(f"finding file: {filesercure}")

    with click.progressbar(range(1000000)) as bar:
        for i in bar:
            pass


    os.chdir(filemoving)

    filefound = ''

    for root, dirs, files in os.walk(".", topdown = True):
        for name in files:
            if name == filesercure:
                    print("found")
                    filefound = os.path.abspath(os.path.join(root, name))
                    time.sleep(1)
                    print(filefound)
            else:
                    with click.progressbar(range(10000)) as bar:
                        for i in bar:
                            pass   

    print(filefound)

    time.sleep(1)
    print(f"moving file: {filesercure}")

    with click.progressbar(range(1000000)) as bar:
        for i in bar:
            pass  

    time.sleep(1)

    # Move a file from the directory
    os.rename(f'{filefound}', f'C:\\Users\\{user}\\Desktop\\antiVIRUS\\SecureFolder\\{os.path.basename(filefound)}')

    messagebox.showinfo("Finished moving", "All Done!")

    root = tkinter.Tk()
    root.withdraw()

    time.sleep(3)

    
if __name__ == "__main__":
    movetosurcurefolder()