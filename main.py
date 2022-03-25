import tkinter
from tkinter import ttk
import json
import subprocess
import json
import os

# #Functions for pages
def next_page(event=None):
    global j
    global page_numba
    if not page_numba == int(j["total_pages"]):
        page_numba= page_numba+1
    element_loader()

def previous_page(event=None):
    global j
    global page_numba
    if not page_numba == 1:
        page_numba= page_numba-1
    element_loader()



#This is the place where the real fun begins. 
def real_uninstaller():
    #Since we started the deletin procedure, we must delete old windows.
    root.destroy()
    confirm.destroy()
    #Creating progress window...
    un_win = tkinter.Tk()
    #Title and icon stuff
    un_win.title("Uninstalling...")
    un_win.iconbitmap('img/icon.ico')
    #Setting a text and progress bar
    text=ttk.Label(un_win,text="Preparing...")
    bar = ttk.Progressbar(un_win, orient='horizontal', length=400, mode='indeterminate')
    bar.pack()
    text.pack()
    #No mainloop, cause our program might freeze.
    un_win.update()
    actualUn = []
    for i in importer:
            #As you see in aplist.json, some apps have multiple packages. Because of tkinter limitaions,
            #they are going from list to string, with spaces. we first split this
            #and then add to what's actually being uninstalled avoiding '' (empty bracket from apps that user didn't select)
            i = i.get().split(" ")
            for o in i:
                if i ==[""]:
                    pass
                else:
                  actualUn.append(i) 
            un_win.update() # debugging
    #calculation is done, let's change the origress bar
    bar["mode"]='determinate'
    bar["maximum"]=len(actualUn)
    #and update the window
    un_win.update()
    #counter
    c=0
    #for a reason, the packages are stored as lists, so without this block of code we would 
    # try to pass ['com.facebook.katana'] instead of com.facebook.katana
    a = []
    for i in actualUn:
        for o in i:
            a.append(o)
    for i in a:
            c=c+1
            #changing text to what's uninstalled.
            text["text"]=f"Uninstalling {c} of {len(actualUn)} ({i})"
            bar["value"]=c-1
            un_win.update()
            subprocess.call(f"adb shell pm uninstall -k --user 0 {i}")
    #if done, lets notify the user and enter mainloop so window will stay open.
    bar["value"] = len(actualUn)
    text["text"]=f"Done!"
    ttk.Button(un_win,text="Exit",command=un_win.destroy).pack()
    un_win.mainloop()
    
def confirm_uninstall(evvent=None):
    #This is only a confirmation windows, for an actual uninstaller see line 34.
    global confirm
    confirm = tkinter.Tk()

    confirm.title("U sure?")
    confirm.iconbitmap('img/icon.ico')
    confirm.geometry("400x200")
    ttk.Label(confirm,text="Are you sure about what you're going to do? Please make sure you\nhave alternative apps for uninstalled.").pack() #grid(column=0,row=0)
    confirm.update()
    ttk.Button(confirm, text="Yes",command=real_uninstaller).pack() #grid(row=1,column=0)
    ttk.Button(confirm, text="No",command=confirm.destroy).pack() #grid(row=1,column=1
def chosen():
    global selector
    global dire
    global opt
    global applist
    global chooser
    global PATH
    ch=selector.get()
    appfilemoment=list(opt).index(ch)
    applist = open(dire[appfilemoment])
    chooser.destroy()
    PATH = dire[appfilemoment].replace("\\applist.json","").replace("/applist.json","")
    return
def choose_appfile():
    global selector
    global dire
    global chooser
    global opt
    chooser=tkinter.Tk()
    chooser.title("Choose appfile")
    chooser.iconbitmap("img/icon.ico")
    ttk.Label(chooser,text="Please choose which appfile you want to use:").pack()
    opt = []
    dire=[]
    for i in os.listdir("app-lists"):
        f = open(f"app-lists/{i}/applist.json")
        pa=""
        for c in f.readlines():
            pa = pa+c.replace("\n","")
        opt.append(json.loads(pa)["title"])
        dire.append(f"app-lists/{i}/applist.json")
        f.close()
    opt = tuple(opt)
    selector = ttk.Combobox(chooser,values=opt,state="readonly")
    selector.current(0)
    selector.pack()
    apply = ttk.Button(chooser,text="Apply",command=chosen)
    apply.pack()

    chooser.mainloop()
choose_appfile()

#load json and make some checkboxes with it


#JSON Stuff
whole_json=""
for i in applist.readlines():
    whole_json = whole_json+ i.replace("\n","")
def parse(event=None):
    uninstall=[]
    for a in importer:
        uninstall.append(a.get())
j=json.loads(whole_json)


#Window
root = tkinter.Tk()
#Icon and title
root.title(f"{j['title']} Debloater")
if os.path.exists(f"{PATH}/icon.ico"):
    root.iconbitmap(f'{PATH}/icon.ico')
else:
    root.iconbitmap("img/icon.ico")
if os.path.exists(f"{PATH}/banner.png"):
    #App banner
    img = tkinter.PhotoImage(file=f'{PATH}/banner.png')
    banner = tkinter.Label(
        root,
        image=img
    )
    banner.pack() #grid(column=0,row=0)
else:
    img = tkinter.PhotoImage(file=f'img/banner.png')
    banner = tkinter.Label(
        root,
        image=img
    )
    banner.pack() #grid(column=0,row=0)









importer=[]
counter=0
page_numba=1
checkboxes=[]

#json loaded,  make window with it.
def element_loader():
    global counter
    global img
    # Since this function is called several time, 
    # we might need to destroy everything whats is in windows.
    # This is beacuse we don't want to 
    # have duplicated objects.
    if not checkboxes==[]:
        for i in root.pack_slaves():
            i.pack_forget()
            banner.pack()
    #Since i'm planning for this to be an "engine" for debloating, here 
    #it check's if applist.json is seperated.
    if not j["needs_pages"]:
        #and if no, it will place checkboxes in one window.
        try:
            j["packages"]["1"]
            ttk.Label(root,text=f"Invalid applist.json! (File defines it doesn't need pages, meanwhile it's in pages format.)").pack()
            return
        except:
            pass
        for i in list(j["packages"].items()):
                importer.append(tkinter.StringVar())
                ttk.Checkbutton(root,text=i[0],variable=importer[counter],onvalue=i[1],offvalue="",command=parse).pack()
                counter=counter+1
    #but if yes, it will...
    else:
        try:
            #check total pages...
            j["packages"][str(j["total_pages"])]
        except Exception as e:
            #..and if missing, show this to a user.
            ttk.Label(root,text=f"Invalid applist.json! (Total pages not defined or defined not propetly. )").pack()
            return
        page = ttk.Label(root,text=f"Displaying page {page_numba} of {j['total_pages']}")
        page.pack()
        #Define buttons for going back and forth, see line 20.
        next_button = ttk.Button(root,text="Next page",command=next_page)
        prevoius_button = ttk.Button(root,text="Previous page",command=previous_page)
        next_button.pack()
        prevoius_button.pack()
        #Show checkboxes
        for i in list(j["packages"][str(page_numba)].items()):
            importer.append(tkinter.StringVar())
            checkboxes.append(ttk.Checkbutton(root,text=i[0],variable=importer[counter],onvalue=i[1],offvalue="",command=parse))
            checkboxes[len(checkboxes)-1].pack()
            counter=counter+1
    #Bloat delete, see line 70
    ttk.Button(root,text="Delete this bloat!",command=confirm_uninstall).pack()

element_loader()
root.mainloop()