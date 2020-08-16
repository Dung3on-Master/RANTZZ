import sys, os, time, tkinter, ctypes, click
from tkinter import messagebox

def scanstart():


    user = os.getenv('username')
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

if __name__ == "__main__":
    scanstart()
