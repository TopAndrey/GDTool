import gd
import asyncio
import time

async def main():
    a = input('Your GD Username: ')
    b = input('Your GD Password: ')
    upd = 1
    while upd == 1:
        c = str(input('Comment: '))
        print('Example: 13519 = The Nightmare, 6508283 = ReTraY')
        d = int(input('ID of level, that you wanna comment: '))
        tms = int(input('How many comments do you want? (1-4): '))
        client = gd.Client()
        level = await client.get_level(d)
        for i in range(tms):
            await client.login(a, b)
            await level.comment(c)
            print('Comment Uploaded!','('+str(i+1)+')')
            if i < tms-1:
                print('Waiting...')
                for j in range(16):
                    time.sleep(1)
                    print(str(round((100/16)*(j+1), 0))+'%','waited...')
        print('Comment Uploaded!','('+(i+1)+')')
        time.sleep(9999)
# ----------------------------------------------- #
        print('All Comments Uploaded! Do you want to upload another comment? [1] / [0]')
        upd = int(input('>>> '))

    print('YOU EXITED THE PROGRAM')
    input()

print('WELCOME')
print('THIS IS GD COMMENT BOT. IT IS NOW IN BETA.')
print('WARNING! You need to have installed GD API! You can get it at:   https://github.com/nekitdev/gd.py   ')
print('==============================================')
asyncio.run(main()) 
