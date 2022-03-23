import tkinter
from tkinter import ttk
import json
from numpy import who
import subprocess
root = tkinter.Tk()

root.title("OneUI Debloater")
root.iconbitmap('icon.ico')
img = tkinter.PhotoImage(file='bannerpng.png')
tkinter.Label(
    root,
    image=img
).pack() #grid(column=0,row=0)
def real_uninstaller():
    root.destroy()
    confirm.destroy()
    un_win = tkinter.Tk()
    un_win.title("Uninstalling...")
    un_win.iconbitmap('icon.ico')
    text=ttk.Label(un_win,text="Preparing...")
    bar = ttk.Progressbar(un_win, orient='horizontal', length=400, mode='indeterminate')
    bar.pack()
    text.pack()
    un_win.update()
    actualUn = []
    for i in importer:
        if i.get() =="":
            pass
        else:
           actualUn.append(i.get()) 
        un_win.update()
    bar["mode"]='determinate'
    bar["maximum"]=len(actualUn)
    un_win.update()
    c=0
    for i in actualUn:
        c=c+1
        text["text"]=f"Uninstalling {c} of {len(actualUn)} ({i})"
        bar["value"]=c
        un_win.update()
        subprocess.call(f"adb shell pm uninstall -k --user 0 {i}")
    text["text"]=f"Done!"
def start_uninstall(evvent=None):
    global confirm
    confirm = tkinter.Tk()
<<<<<<< Updated upstream
=======
    confirm.title("U sure?")
    confirm.iconbitmap('icon.ico')
>>>>>>> Stashed changes
    confirm.geometry("400x200")
    ttk.Label(confirm,text="Are you sure about what you're going to do? Please make sure you\nhave alternative apps for uninstalled.").pack() #grid(column=0,row=0)
    confirm.update()
<<<<<<< Updated upstream
    uninstall=[arzone.get(),ardrawing.get()]
##Uninstallers
#Definiting what should be uninsstalled
arzone = tkinter.StringVar()
ardrawing = tkinter.StringVar()
visionarapps = tkinter.StringVar()
#bixpypack = Bixby,Bixby Vision,Bixby Voice,Bixby Vision Framework,Bixby Service
bixbypack = tkinter.StringVar()
bookmarkprovider = tkinter.StringVar()
briefing = tkinter.StringVar()
chrome = tkinter.StringVar()
deco_pic=tkinter.StringVar()
dexonpc = tkinter.StringVar()
devicehealthservices = tkinter.StringVar()
duo = tkinter.StringVar()
facebook = tkinter.StringVar()
#Galaxy Pack = Galaxy Themes, Wearable
galaxypack = tkinter.StringVar()
gameboster = tkinter.StringVar()
gamelauncher=tkinter.StringVar()
gameoptimizingservice=tkinter.StringVar()
gmail = tkinter.StringVar()
google = tkinter.StringVar()
playservicesar = tkinter.StringVar()
googleplayvideos = tkinter.StringVar()
googleassistant = tkinter.StringVar()
googlephotos = tkinter.StringVar()
healthservice = tkinter.StringVar()
linksharing = tkinter.StringVar()
office = tkinter.StringVar()
onedrive = tkinter.StringVar()
outlook = tkinter.StringVar()
privateshare = tkinter.StringVar()
daily = tkinter.StringVar()
dex = tkinter.StringVar()
galaxynofreinds = tkinter.StringVar() # ;)
globalgoals = tkinter.StringVar()
health = tkinter.StringVar()
internet = tkinter.StringVar()
kids = tkinter.StringVar()
spass = tkinter.StringVar()
passprovider = tkinter.StringVar()
pay = tkinter.StringVar()
suckingfolder = tkinter.StringVar() # :)
dumbthings = tkinter.StringVar()
smarttutor = tkinter.StringVar()
frickkey = tkinter.StringVar()
wearablemanager = tkinter.StringVar()
youtube = tkinter.StringVar()
passautofill = tkinter.StringVar()
bixbywakeup = tkinter.StringVar()
dexlauncher=tkinter.StringVar()
googledocs=tkinter.StringVar()
microsoftappmanager = tkinter.StringVar()
voicenote = tkinter.StringVar()
maps = tkinter.StringVar()
livewalpaperpicker=tkinter.StringVar()
swiftkey= tkinter.StringVar()
samsungkeyboard = tkinter.StringVar()
peoplestripe=tkinter.StringVar()
myfiles=tkinter.StringVar()
reminder=tkinter.StringVar()
daemonapp=tkinter.StringVar()
audiohearing=tkinter.StringVar()
aremojieditor=tkinter.StringVar()
webmanual=tkinter.StringVar()
simcard=tkinter.StringVar()
samsungtips=tkinter.StringVar()
avatarstickers=tkinter.StringVar()
routines=tkinter.StringVar()
kidsinstaller=tkinter.StringVar()
yandexsearch=tkinter.StringVar()
#Checkboxes
ttk.Label(root,text="Select the apps you would like to uninstall",font=("Calibri", 17)).grid(column=0,row=1)
ttk.Checkbutton(root,text="Ar Zone",variable=arzone,onvalue='1',offvalue='0').grid(column=0,row=2)
ttk.Checkbutton(root,text="Ar Drawing",variable=ardrawing,onvalue='1',offvalue='0').grid(column=0,row=3)
ttk.Checkbutton(root,text="Vision Ar Apps",variable=visionarapps,onvalue='1',offvalue='0').grid(column=0,row=4)
ttk.Checkbutton(root,text="Bixby Pack",variable=bixbypack,onvalue='1',offvalue='0').grid(column=0,row=5)
ttk.Label(root,text="Bixby,Bixby Vision,Bixby Voice,Bixby Vision Framework,Bixby Service").grid(column=0,row=6)
ttk.Checkbutton(root,text="Bookmark Provider",variable=bookmarkprovider,onvalue='1',offvalue='0').grid(column=0,row=7)
ttk.Checkbutton(root,text="Briefing",variable=briefing,onvalue='1',offvalue='0').grid(column=0,row=8)
ttk.Checkbutton(root,text="Chrome",variable=chrome,onvalue='1',offvalue='0').grid(column=0,row=9)
ttk.Checkbutton(root,text="DECO PIC",variable=deco_pic,onvalue='1',offvalue='0').grid(column=0,row=10)
ttk.Checkbutton(root,text="Dex On PC",variable=dexonpc,onvalue='1',offvalue='0').grid(column=0,row=11)
ttk.Checkbutton(root,text="Device Health Services",variable=devicehealthservices,onvalue='1',offvalue='0').grid(column=0,row=12)
ttk.Checkbutton(root,text="Briefing",variable=briefing,onvalue='1',offvalue='0').grid(column=0,row=13)
ttk.Button(root,text="Get rid of selected bloatware!",command=start_uninstall).grid(column=0,row=14)
=======
    ttk.Button(confirm, text="Yes",command=real_uninstaller).pack() #grid(row=1,column=0)
    ttk.Button(confirm, text="No",command=confirm.destroy).pack() #grid(row=1,column=1)
#load json and make some checkboxes with it
import json
applist = open("applist.json")
whole_json=""
for i in applist.readlines():
    whole_json = whole_json+ i.replace("\n","")
def parse(event=None):
    uninstall=[]
    for a in importer:
        uninstall.append(a.get())
    print(uninstall)
"""
ttk.Checkbutton(root,text="Bixby Pack",variable=bixbypack,onvalue='1',offvalue='0').grid(column=0,row=5)
ttk.Label(root,text="Bixby,Bixby Vision,Bixby Voice,Bixby Vision Framework,Bixby Service").grid(column=0,row=6)
"""
ttk.Label(root,text="tesxt").pack() #.grid(column=0,row=16)
importer=[]
counter=0
j=json.loads(whole_json)
print()
for i in list(j["packages"].items()):
    importer.append(tkinter.StringVar())
    ttk.Checkbutton(root,text=i[0],variable=importer[counter],onvalue=i[1],offvalue="",command=parse).pack()
    counter=counter+1
ttk.Button(root,text="Delete this bloat!",command=start_uninstall).pack()
>>>>>>> Stashed changes
root.mainloop()