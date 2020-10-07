import os, wget
import win32com.client
import pythoncom
import PySimpleGUI as sg

threats_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threats.list'
threat_extentions_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threatextentions.list'
threat_txt_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/threatstxt.list'
RANTZZ_main_url = 'https://rantzzsecurity.weebly.com/uploads/1/3/0/9/130919827/rantzz.txt'

user = os.getenv('username')

main_file = f'C:\\Users\\{user}\\AppData\\Local\\RANTZZ'


try:
    os.chdir(main_file)
    
    try:
        check = open(f'{main_file}\\threats.list', 'r')
        check.close()
        
    except FileNotFoundError:
        wget.download(threats_url, f'{main_file}\\threats.list')        
        wget.download(threat_extentions_url, f'{main_file}\\threatextentions.list')
        wget.download(threat_txt_url, f'{main_file}\\threatstxt.list')
        wget.download(RANTZZ_main_url, f'{main_file}\\RANTZZ.py')

        # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
        desktop = f'C:/Users/{user}/Desktop' # path to where you want to put the .lnk
        path = os.path.join(desktop, 'HI.lnk')
        target = f'C:/Users/{user}/Desktop/ANTIvirus2/menu1.py'

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
        shortcut.save()

    except ConnectionError:
        sg.popup("An error occurred, please check your internet connection")
        exit()

    sg.popup("RANTZZ was successfully installed")

except:
    os.mkdir(main_file)
    os.chdir(main_file)
    wget.download(threats_url, f'{main_file}\\threats.list')        
    wget.download(threat_extentions_url, f'{main_file}\\threatextentions.list')
    wget.download(threat_txt_url, f'{main_file}\\threatstxt.list')
    wget.download(RANTZZ_main_url, f'{main_file}\\RANTZZ.py')

    # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
    desktop = f'C:/Users/{user}/Desktop' # path to where you want to put the .lnk
    path = os.path.join(desktop, 'RANTZZ.lnk')
    target = f'C:/Users/{user}/Desktop/ANTIvirus2/menu1.py'

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()
    sg.popup("RANTZZ was successfully installed \na shortcut was created on your Desktop")