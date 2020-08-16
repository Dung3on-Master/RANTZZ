import sys, os, time, tkinter, ctypes, click
from tkinter import messagebox

def fullscanstart():


    user = os.getenv('username')

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

    print('starting scan')            

    time.sleep(1)

    #collect and show all files


    os.chdir('C:/')

    path1 = 'C:/'



    progs = [ ]

    for root, directories, files in os.walk(path1, topdown=True):
        for name in files:
            fullName = os.path.join(root, name)
            progs.append(fullName)


    #check if they are a virus program

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

    print(progs)

    time.sleep(4)
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")


if __name__ == "__main__":
    fullscanstart()