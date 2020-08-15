import sys, os, time, tkinter, ctypes, click
from tkinter import messagebox

def spesificscanstart():


    user = os.getenv('username')
    Whatfile = input("What File Should We Scan? ")

    myfile = ''
    os.chdir(f"C:/Users/{user}/Desktop/antiVIRUS")
    myfile = open("threats.txt", "r")
    content = myfile.read()

    allthreats = content.split(', ')
    print(allthreats)


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

    print("Files Scanned:  \n")
    time.sleep(0.4)


    os.chdir(f'C:/Users/{user}')

    path1 = f'C:/Users/{user}/Downloads'
    path2 = f'C:/Users/{user}/Desktop'
    path3 = f'C:/Users/{user}/Documents'
    path4 = f'C:/Users/{user}/Music'
    path5 = f'C:/Users/{user}/Pictures'
    path6 = f'C:/Users/{user}/Videos'
    path7 = f'C;/Users/{user}/3D Objects'


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



    #check if they are a virus program

    infectfiles = []
    for prog in progs:
        
        if os.path.basename(prog) == f"{Whatfile}":
            print("Found!")

            if os.path.basename(prog) in allthreats:
                print(f"{prog} is infected")
                infectfiles.append(prog)

            elif os.path.basename(prog) in ["deadcomputer.jpg"]:
                print(f"{prog} was made by a malicious file")
                infectfiles.append(prog)

            elif os.path.basename(prog).startswith("kbdhid") and os.path.basename(prog).endswith(".sys"):
                print(f"{prog} was made by a malicious file")
                infectfiles.append(prog)

        else:
            print("searching")
        

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

if __name__ == "__main__":
    spesificscanstart()