import tkinter as tk
from PIL import ImageTk, Image
root=tk.Tk()
root.title("To-Do-List")
root.geometry("400x600+400+100")
root.resizable(width=False, height=False)
task_list=[]


def deletetask():
    task=str(listbox.get(tk.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("text.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
        listbox.delete(tk.ANCHOR)

def addtask():
    task=task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open("text.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
            listbox.insert(tk.END, task)
def opentaskfile():
    try:
        global task_list
        with open("text.txt", "r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(tk.END, task)
    except:
        file=open("text.txt", "w")
        pass

image1=ImageTk.PhotoImage(Image.open("image/top.png").resize((400,600)))
image2=ImageTk.PhotoImage(Image.open("image/tick.png").resize((40,40)))
image4=ImageTk.PhotoImage(Image.open("image/mainpart.png").resize((400,400)))
trash=ImageTk.PhotoImage(Image.open("image/trash.png").resize((50, 50)))

root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="image/tick.png"))
imagelabel=tk.Label(root,image=image1, bg='white')
imagelabel2=tk.Label(root, image=image2, bg="#f691cf")
imagelabel4=tk.Label(root, image=image4, bg='white')
infolabel=tk.Label(root, text="All tasks",font="cardo 30", fg="white", bg="#f691cf")

imagelabel.place(x=0, y=0)
imagelabel2.place(x=340, y=11)
imagelabel4.place(x=0, y=180)
infolabel.place(x=140, y=15)

#main
frame=tk.Frame(root, width=400, height=40, bg="#d89de8")
frame.place(x=0, y=170)
task=tk.StringVar()
task_entry=tk.Entry(frame, width=18, font="cardo 30",bg="#d89de8", bd=0)
task_entry.place(x=10,y=5)


button = tk.Button(frame, text="Add", font="arial 20", width=7, height=2, bg="#d89de8", fg="black", bd=0, activebackground="#d89de8", highlightbackground="white", command=addtask)
button.place(x=300, y=0)

frame1=tk.Frame(root, bd=3, width=700, height=300,  bg="white")
frame1.pack(pady=(280,0))

listbox= tk.Listbox(frame1,font=('arial',12),width=47,height=14,bg="white",fg="black",cursor="hand2",selectbackground="lightblue")
listbox.pack(side=tk.LEFT , fill=tk.BOTH, padx=2)
scrollbar= tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT , fill= tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
opentaskfile()
#delete
tk.Button(root, image=trash,bd=0, command=deletetask).pack(side=tk.BOTTOM, pady=13)

root.mainloop()
