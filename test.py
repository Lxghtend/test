import subprocess
import asyncio
import wizwalker
import copy
from time import time
from wizwalker.constants import Keycode
from wizwalker.memory import Window
from wizwalker import Client, client
from wizwalker.memory.memory_objects.window import Window
from wizwalker import ClientHandler







async def checkBackPackSpace(client: Client):
    backPackSpace = str('100/150')
    backPackSpace =  backPackSpace.split("/")
    backPackSpace = backPackSpace[0]
    backPackSpace = int(backPackSpace)
    backPackSpace = ((backPackSpace - 150)*-1)
    x = "Clear your bag! You need 49 space available. You have"
    y = backPackSpace
    z = '.'
    if backPackSpace > 49:
        print(x,y,z)
        input('Press Enter after you have cleared up space in your bag.')
        '''
        more unused code due to the fact the user might not be looking at the screen
        print("Closing in 3.")
        await asyncio.sleep(1)
        print("Closing in 2.")
        await asyncio.sleep(1)
        print("Closing in 1.")
        await client.close()
        '''
    if backPackSpace <= 49:
        print(backPackSpace)


asyncio.run(checkBackPackSpace(client))

