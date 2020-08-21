import string, random, time, os, ctypes, click, sys, shutil, tkinter, wget

from tkinter import *
from tkinter import messagebox
from pathlib import Path

user = os.getenv('username')

def rantsstart():

   master = Tk()
   
   Label(master, text="Rantzz Security").grid(row=0, sticky=W)

   Button(master, text='Full Scan', command=fullscanstart).grid(row=1, sticky=W, pady=4)

   Button(master, text='Selective Scan', command=scanstart).grid(row=2, sticky=W, pady=4)

   Button(master, text='File Scan', command=spesificscanstart).grid(row=3, sticky=W, pady=4)

   Button(master, text='Move To Secure Folder', command=movetosurcurefolder).grid(row=4, sticky=W, pady=4)

   Label(master, text=" ").grid(row=5, sticky=W)

   Button(master, text='Update Database', command=update).grid(row=6, sticky=W, pady=4)

   Button(master, text='Quit', command=master.quit).grid(row=7, sticky=W, pady=4)
   
   time.sleep(1)
   print("log waiting for input")

   mainloop()



def scanstart():


    whatfile = input("what folder should we scan? (desktop, downloads, documents, etc), (please start with a capital): ")

    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
    with open("threats.txt") as inputfile:
        threats = ", ".join([line.rstrip("\n") for line in inputfile])
        allthreats = threats.split(', ')

    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
    with open("threatextentions.txt") as inputfile:
        allthreatsexten = inputfile.read().split(', ')

    #start scan

    

    messagebox.askokcancel("Starting Scan", "We Will Start Scanning your files")

    root = tkinter.Tk()
    root.withdraw()

    print('starting scan')            

    time.sleep(1)

    with click.progressbar(range(1000000)) as bar:
        for i in bar:
            pass

    #show the files

    os.chdir(f'C:/Users/{user}')

    path = f'C:/Users/{user}/{whatfile}'

    progs = [ ]

    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)



    #check program

    infectfiles = []
    with click.progressbar(progs) as bar:
        for prog in bar:

            if os.path.basename(prog) in allthreats:
                infectfiles.append(prog)

            elif os.path.basename(prog) in ["deadcomputer.jpg"]:
                infectfiles.append(prog)

            for ext in allthreatsexten:
                if os.path.basename(prog).endswith(ext):
                    infectfiles.append(prog)


    #end

    time.sleep(2)

    root = tkinter.Tk()
    root.withdraw()

    if len(infectfiles) >0:
        messagebox.showerror("Warning", f"{ ', '.join([os.path.basename(f) for f in infectfiles])} files may include malicious code")

        root = tkinter.Tk()
        root.withdraw()

        time.sleep(0.5)
        delete = messagebox.askyesno(title="Delete files?", message="Do you wish to delete them?")
        if delete:
            messagebox.showinfo("Deleting", "Okay we will begin deleting them")
            time.sleep(1)
            messagebox.showinfo("Sucsessfully Deleted", "The file/s were successfully removed")

            for x in infectfiles:
                os.remove(x)
            time.sleep(1)
        else:
            messagebox.showinfo("Not Deleting", "Okay")

    else:
        messagebox.showinfo("Scan Complete", "you currently have no malicious files present in that file")

        root = tkinter.Tk()
        root.withdraw()

    time.sleep(4)
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")


def movetosurcurefolder():

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


def fullscanstart():


    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
    with open('threats.txt') as inputfile:
        threats = ", ".join([line.rstrip("\n") for line in inputfile])
        allthreats = threats.split(', ')

    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
    with open("threatextentions.txt") as inputfile:
        allthreatsexten = inputfile.read().split(', ')


    #start scan

    

    messagebox.askokcancel("Starting Scan", "We Will Start Scanning your files")

    root = tkinter.Tk()
    root.withdraw()

    print('preparing')            

    #collect all files


    os.chdir('C:/')

    path1 = 'C:/'



    progs = [ ]

    for root, directories, files in os.walk(path1, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)


    #check if they are a virus program

    print("starting scan")
    time.sleep(1)

    infectfiles = []
    with click.progressbar(progs) as bar:
        for prog in bar:

            if os.path.basename(prog) in allthreats:
                infectfiles.append(prog)

            elif os.path.basename(prog) in ["deadcomputer.jpg"]:
                infectfiles.append(prog)

            for ext in allthreatsexten:
                if os.path.basename(prog).endswith(ext):
                    infectfiles.append(prog)
    

    #warnings and telling you to delete the files

    time.sleep(2)

    root = tkinter.Tk()
    root.withdraw()

    if len(infectfiles) >0:
        messagebox.showerror("Warning", f"{ ', '.join([os.path.basename(f) for f in infectfiles])} files may include malicious code")

        root = tkinter.Tk()
        root.withdraw()

        
        time.sleep(0.5)
        delete = messagebox.askyesno(title="Delete files?", message="Do you wish to delete them? are system can only do a basic delete.")
        if delete:
            messagebox.showinfo("Deleting", "Okay we will begin deleting them")
            time.sleep(1)

            for x in infectfiles:
                os.remove(x)
            time.sleep(1)
            messagebox.showinfo("Sucsessfully Deleted", "The file/s were successfully removed")

        else:
            messagebox.showinfo("Not Deleting", "Okay")

    else:
        messagebox.showinfo("Scan Complete", "you currently have no malicious files that we can see on your computer")

        root = tkinter.Tk()
        root.withdraw()


    time.sleep(4)
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")


def spesificscanstart():


    Whatfile = input("What File Should We Scan? ")

    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
    with open('threats.txt') as inputfile:
        threats = ", ".join([line.rstrip("\n") for line in inputfile])
        allthreats = threats.split(', ')

    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")

    with open("threatextentions.txt") as inputfile:
        allthreatsexten = inputfile.read().split(', ')


    #start scan

    

    messagebox.askokcancel("Starting Scan", f"We Will Start Searching for {Whatfile}")

    root = tkinter.Tk()
    root.withdraw()

    print('starting scan')            

    time.sleep(1)

    with click.progressbar(range(1000000)) as bar:
        for i in bar:
            pass


    #collect and show all files

    time.sleep(0.4)


    os.chdir(f'C:/Users/{user}')

    path1 = f'C:/Users/{user}/Downloads'
    path2 = f'C:/Users/{user}/Desktop'
    path3 = f'C:/Users/{user}/Documents'
    path4 = f'C:/Users/{user}/Music'
    path5 = f'C:/Users/{user}/Pictures'
    path6 = f'C:/Users/{user}/Videos'
    path7 = f'C;/Users/{user}/3D Objects'
    path8 = f'C:/Users/{user}/AppData'


    progs = [ ]

    for root, directories, files in os.walk(path1, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path2, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path3, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path4, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path5, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path6, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path7, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)

    for root, directories, files in os.walk(path8, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)



    #check if they are a virus program

    infectfiles = []
    for prog in progs:
        
        if os.path.basename(prog) == f"{Whatfile}":
            print("Found!")

            infectfiles = []
            with click.progressbar(progs) as bar:
                for prog in bar:

                    if os.path.basename(prog) in allthreats:
                        infectfiles.append(prog)

                    elif os.path.basename(prog) in ["deadcomputer.jpg"]:
                        infectfiles.append(prog)

                    for ext in allthreatsexten:
                        if os.path.basename(prog).endswith(ext):
                            infectfiles.append(prog)

        

    #warnings and telling you to delete the files

    time.sleep(2)

    root = tkinter.Tk()
    root.withdraw()

    if len(infectfiles) >0:
        messagebox.showerror("Warning", f"{ ', '.join([os.path.basename(f) for f in infectfiles])} may include malicious code")

        root = tkinter.Tk()
        root.withdraw()

        
        time.sleep(0.5)
        delete = messagebox.askyesno(title="Delete files?", message="Do you wish to delete it?")
        if delete:
            messagebox.showinfo("Deleting", "Okay we will delete it")
            time.sleep(1)
            messagebox.showinfo("Sucsessfully Deleted", "The file/s were successfully removed")

            for x in infectfiles:
                os.remove(x)
            time.sleep(1)
        else:
            messagebox.showinfo("Not Deleting", "Okay")

    else:
        messagebox.showinfo("Scan Complete", "the file you selected is free of viruses")

        root = tkinter.Tk()
        root.withdraw()

    time.sleep(4)
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")


def update():


    yesorno = input("Are you Sure? (y or n): ")

    if yesorno == "y" or yesorno == "Y":
        print("ok.  starting")
        time.sleep(1)

        os.remove(f'C:/Users/{user}/Desktop/antiVIRUS/threats.txt')
        os.remove(f'C:/Users/{user}/Desktop/antiVIRUS/threatextentions.txt')

        time.sleep(4)

        url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threats.txt'
        wget.download(url, f'C:/Users/{user}/Desktop/antiVIRUS/threats.txt')

        url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threatextentions.txt'
        wget.download(url, f'C:/Users/{user}/Desktop/antiVIRUS/threatextentions.txt')
        


    else:
        print("ok.  stopping")
        time.sleep(1)

    print("\n \n \n \n \n")


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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
        print("================\nlogin sucsessful\n================")
        time.sleep(1)
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
        time.sleep(0.1)
        rantsstart()

    elif passkeyenter == "DeV":
        print("\n \n \n \n")
        print("=====================================\n logged in sucsessfully as DEVELOPER\n=====================================")
        time.sleep(2)
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
        time.sleep(0.1)
        rantsstart()

    else:
        print("\n \n \n \n")
        print("error logging in, please try copieing the passkey from the document.")
        passtry = True

