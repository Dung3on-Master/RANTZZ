import os, click, wget
import PySimpleGUI as sg

Prog_name = 'RANTZZ'
user = os.getenv('username')

Full_Scan_Path = 'C:\\'
Quick_Scan_Paths = os.listdir(f"C:\\Users\\{user}")
progs = []
progs_names = []
Infected_Files = []
main_file = f'C:\\Users\\{user}\\AppData\\Local\\RANTZZ'

watchlist_file = 'Watchlist'

threats_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threats.list'
threat_extentions_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threatextentions.list'
threat_txt_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threatstxt.list'


with open("threats.list") as inputfile:
    threats = ", ".join([line.rstrip("\n") for line in inputfile])
    all_threats = threats.split(', ')

with open("threatextentions.list") as inputfile:
    all_threats_exten = inputfile.read().split(', ')

with open("threatstxt.list") as inputfile:
    threats_txt = ", ".join([line.rstrip("\n") for line in inputfile])
    all_threats_txt = threats_txt.split(', ')


def write(txt, file):
    txt = str(txt)
    intodoc = open(file, 'w+')
    intodoc.write(txt)
    intodoc.close()



def scan(progs, threats, threat_extentions, Threat_txt):
    Infected_Files = []
    final_list = []

    print("scanning")

    with click.progressbar(progs) as bar:
        for prog in bar:

            if os.path.basename(prog) in all_threats:
                Infected_Files.append(prog)

        for virus in Infected_Files:
            extreme_check = open(virus, 'r')
            extreme_check_txt = extreme_check.read()
            extreme_check.close()
            for threats_t in Threat_txt:
                if threats_t in extreme_check_txt:
                    file_with_virus = virus.replace("\\", "\\\\")
                    final_list.append(os.path.basename(file_with_virus))

    os.chdir(main_file)

    if not final_list:
        final_list = 'nothing'
    if not Infected_Files:
        Infected_Files = 'nothing'

    final_list = str(final_list)
    Infected_Files = str(Infected_Files)

    sg.popup(f"suspected: \n {Infected_Files}\n \ninfected: \n {final_list}", title="infected files", location=(10, 10))
    if final_list == 'nothing' or Infected_Files == 'nothing':
        sg.popup("Done", title="Done", location=(10, 10))
    else:
        Delete = sg.popup_yes_no("Do you wish to delete them? we can only do an basic delete", location=(10, 10))
        if Delete == "Yes":
            sg.popup("Deleting", title="Deleting", location=(10, 10))
            try:
                for the_file in file_with_virus:
                    os.remove(the_file)
                sg.popup("Deleted Successfully", title="Deleted", location=(10, 10))
            except:
                sg.popup("Error While Deleting", title="Error", location=(10, 10))
        else:
            sg.Popup(f"ok, we won't delete {final_list}", title="Not Deleting", location=(10, 10))
        
            write(final_list, watchlist_file)
            sg.Popup(f"Added: \n{final_list}, to watchlist", title="Application Added To Watchlist", location=(10, 10))





def Full_Scan(threats, threat_extentions, Threat_txt):
    progs = []
    progs_names = []

    for root, directories, files in os.walk(Full_Scan_Path, topdown=True):
        for name in files:
            Full_Name = os.path.join(root, name)
            File_Name = os.path.basename(Full_Name)
            progs.append(Full_Name)
            progs_names.append(File_Name)
    
    scan(progs, threats, threat_extentions, Threat_txt)
    

def Quick_Scan(threats, threat_extentions, Threat_txt):
    progs = []
    progs_names = []

    for Quick_Scan_Path in Quick_Scan_Paths:
        for root, directories, files in os.walk(f"C:\\Users\\{user}\\{Quick_Scan_Path}", topdown=False):
            for name in files:
                Full_Name = os.path.join(root, name)
                File_Name = os.path.basename(Full_Name)
                progs.append(Full_Name)
                progs_names.append(File_Name)
    
    scan(progs, threats, threat_extentions, Threat_txt)


def Spesific_File_Scan(threats, threat_extentions, Threat_txt):
    progs = []
    progs_names = []

    text = sg.popup_get_file('Enter the file you wish to scan')
    progs.append(text)
    
    scan(progs, threats, threat_extentions, Threat_txt)


def Update():
    Update = sg.popup_yes_no("Do you wish to update your scanners")
    if Update == 'Yes':
        
        try:
            os.remove(f'{main_file}\\threats.list')
            os.remove(f'{main_file}\\threatextentions.list')
            os.remove(f'{main_file}\\threatstxt.list')

            wget.download(threats_url, f'{main_file}\\threats.list')        
            wget.download(threat_extentions_url, f'{main_file}\\threatextentions.list')
            wget.download(threat_txt_url, f'{main_file}\\threatstxt.list')

            print("Complete")
            sg.Popup('Updated Successfully', title='Updated')
        except FileNotFoundError:
            wget.download(threats_url, f'{main_file}\\threats.list')        
            wget.download(threat_extentions_url, f'{main_file}\\threatextentions.list')
            wget.download(threat_txt_url, f'{main_file}\\threatstxt.list')

            print("Complete")
            sg.Popup('Updated Successfully', title='Updated')
        except:
            sg.Popup("An error occured while downloading update, \nThis could be from your internet or your storage \nIf you don't retry, your scanners may stop working")



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(Prog_name)],
            [sg.Button('Full Scan')],
            [sg.Button('Quick Scan')],
            [sg.Button('Spesific File Scan')],
            [sg.Text(' ')],
            [sg.Button('Update Database')],
            [sg.Button('Cancel')] ]

# Create the Window
window = sg.Window(Prog_name, layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Full Scan':
        Full_Scan(all_threats, all_threats_exten, all_threats_txt)
    if event == 'Quick Scan':
        Quick_Scan(all_threats, all_threats_exten, all_threats_txt)
    if event == 'Spesific File Scan':
        Spesific_File_Scan(all_threats, all_threats_exten, all_threats_txt)
    if event == 'Update Database':
        Update()

window.close()