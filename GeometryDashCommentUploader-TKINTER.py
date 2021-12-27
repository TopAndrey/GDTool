import gd
import asyncio
import time
from tkinter import *
upd = 1
c = str()
d = int()

def tkinter():
    global upd
    global c
    global a
    global b
    global d
    global tms
    async def onClick():
        async def onClick2():
            while upd == 1: 
                client = gd.Client()
                level = await client.get_level(int(d.get()))
                for i in range(int(tms.get())):
                    await client.login(a.get(), b.get())
                    await level.comment(c.get()+str(' '*i))
                    lbl2['text'] = 'Comment Uploaded!','('+str(i+1)+')'
                    if i < int(tms.get())-1:
                        lbl2['text'] = ('Waiting...')   # This comment was uploaded with "GD.py"
                        for j in range(16):
                            time.sleep(1)
                            lbl2['text'] = str(round((100/16)*(j+1), 0))+'%','waited...'
                        await level.comment(str(c.get())+str('  '))
                        lbl2['text'] = 'Comment Uploaded!','('+(str(i+1))+')'
        btn = Button(root, text='UPLOAD!', font = 50, command = lambda: asyncio.run(onClick2()))
        btn.pack(side=TOP)
        
    root = Tk()
    root.geometry('300x300')
    lb1 = Label(root, text='GD CommentBot', font=('Fixedsys', 25))     #d43c31 , #5eff00 , #00ddff
    lb1.pack(side = TOP, pady = 8)
    a = Entry(root, font = ('Arial Bold',15))
    b = Entry(root, font = ('Arial Bold',15))
    a.insert(0, 'Username')
    b.insert(0, 'Password')
    a.pack()
    b.pack()
    c = Entry(root, font = ('Arial', 14))
    c.insert(0, 'Comment')
    c.pack(pady=4)
    d = Entry(root, font = ('Arial', 14))
    d.insert(0, 'ID of level')
    d.pack()
    tms = Entry(root, font = ('Arial', 14))                 
    tms.insert(0, 'How many comments?')
    tms.pack(pady=4)
    lbl2 = Label(root)
    asyncio.run(onClick())
    
    root.mainloop()
print('IDs Example: 13519 = The Nightmare, 6508283 = ReTraY')
tkinter()
        
# ----------------------------------------------- #
async def repeat():
    global upd
    upd = 1
    global c
    while upd == 1:
        c = str(input('Comment: '))
        print('Example: 13519 = The Nightmare, 6508283 = ReTraY')
        d = int(input('ID of level, that you wanna comment: '))
        tms = int(input('How many comments do you want? (1-4): '))
        client = gd.Client()
        level = await client.get_level(d)
        for i in range(tms):
            await level.comment(c+str(' '*i),100)
            print('Comment Uploaded!','('+str(i+1)+')')
            if i < tms-1:
                print('Waiting...')
                for j in range(16):
                    time.sleep(1)
                    print(str(round((100/16)*(j+1), 0))+'%','waited...')
                await level.comment(c+str('  '),100)
                print('Comment Uploaded!','('+(str(i+2))+')')

# =============================================== #
        print('All Comments Uploaded! Do you want to upload it another time? [1] / [0]')
        upd = int(input('>>> '))
        if upd == 1:
            break
            asyncio.run(repeat())
        else:
            print('YOU EXITED THE PROGRAM')
            break
            input()

print('WELCOME')
print('THIS IS GD COMMENT BOT. IT IS NOW IN BETA.')
print('WARNING! You need to have installed GD API! You can get it at:   https://github.com/nekitdev/gd.py   ')
print('==============================================')

