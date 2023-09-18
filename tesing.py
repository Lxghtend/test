import subprocess
import asyncio
import wizwalker
import copy
import re
from time import time
from wizwalker.constants import Keycode
from wizwalker.memory import Window
from wizwalker import Client, client
from wizwalker.memory.memory_objects.window import Window
from wizwalker import ClientHandler


# Team Up Paths
team_up_button_path = ['WorldView', 'NPCRangeWin', 'imgBackground', 'TeamUpButton']
team_up_confirm_path = ['WorldView', 'TeamUpConfirmationWindow', 'TeamUpConfirmationBackground', 'TeamUpButton']



async def get_window_from_path(root_window, name_path):
    async def _recurse_follow_path(window, path):
        if len(path) == 0:
            return window

        for child in await window.children():
            if await child.name() == path[0]:
                found_window = await _recurse_follow_path(child, path[1:])
                if not found_window is False:
                    return found_window

        return False

    return await _recurse_follow_path(root_window, name_path)


async def click_window_from_path(mouse_handler, base_window, path): #credit ultimate314
    try:
        await mouse_handler.click_window(await window_from_path(base_window, path))
    except:
        pass


# Returns a window, given a path 
async def window_from_path(base_window:Window, path:list[str]) -> Window:
    # Credit to SirOlaf for the original function; I'm modifying it - credit ultimate314;  and now me i have stolen this mwah haha - milwr i think?
    if not path:
        return base_window
    for child in await base_window.children():
        if await child.name() == path[0]:
            if found_window := await window_from_path(child, path[1:]):
                return found_window
    return False


async def is_visible_by_path(client: Client, path: list[str]):
    # FULL CREDIT TO SIROLAF FOR THIS FUNCTION
    # checks visibility of a window from the path
    root = client.root_window
    windows = await get_window_from_path(root, path)
    if windows == False:
        return False
    elif await windows.is_visible():
        return True
    else:
        return False

refresh_button = ["Worldview", "TeamHelpWindow", "TeamHelpRefreshButton"]

async def join_team_up(client: Client):
    npc_range = ["WorldView", "NPCRangeWin"]
    team_up_kiosk = ["WorldView", "TeamHelpWindow"]
    wizard_city = ["WorldView", "TeamHelpWindow", "TabBackground1"]
    team_up_arrow = ["Worldview", "TeamHelpWindow", "NextWorldPageButton"]
    if  await is_visible_by_path(client.root_window, npc_range) :
         await client.send_key(Keycode.X) 
    while not await is_visible_by_path(client.root_window, team_up_kiosk):
        await asyncio.sleep(0.1)
    while not  await is_visible_by_path(client.root_window, wizard_city) :
        await click_window_from_path(client.mouse_handler, client.root_window, team_up_arrow) 
        asyncio.sleep(0.2)
    if await is_visible_by_path(client.root_window, wizard_city):
          await click_window_from_path(client.mouse_handler, client.root_window, wizard_city) 
    await asyncio.sleep(1)
    await read_first_dungeon(client)
    

first_dungeon_button = ["WorldView", "TeamHelpWindow", "Line1", "InstanceSprite"]
second_dungeon_button = ["WorldView", "TeamHelpWindow", "Line2", "InstanceSprite"]
third_dungeon_button = ["WorldView", "TeamHelpWindow", "Line3", "InstanceSprite"]
fourth_dungeon_button = ["WorldView", "TeamHelpWindow", "Line4", "InstanceSprite"]
fifth_dungeon_button =  ["WorldView", "TeamHelpWindow", "Line5", "InstanceSprite"]

async def read_first_dungeon(client: Client) -> str:
    first_dungeon_text = ["WorldView", "TeamHelpWindow", "Line1", "InstanceSprite"]
    try:
            # FIRST DUNGEON
            first_dungeon_name = await get_window_from_path(client.root_window, first_dungeon_text)
            first_dungeon = await first_dungeon_name.maybe_text()
            first_dungeon = first_dungeon.replace("<center>", '')
            first_dungeon = first_dungeon.replace("</center>", '')
    except:
        first_dungeon = ""
    print(first_dungeon)
    return first_dungeon

async def read_second_dungeon(client: Client) -> str:
    second_dungeon_text = ["WorldView", "TeamHelpWindow", "Line2", "InstanceSprite"]
    try:
            second_dungeon_name = await get_window_from_path(client.root_window, second_dungeon_text)
            second_dungeon = await second_dungeon_name.maybe_text()
            second_dungeon = second_dungeon.replace("<center>", '')
            second_dungeon = second_dungeon.replace("</center>", '')
    except:
        second_dungeon = ""
    print(second_dungeon)
    return second_dungeon

async def read_third_dungeon(client: Client) -> str:
        third_dungeon_text = ["WorldView", "TeamHelpWindow", "Line3", "InstanceSprite"]
        try:
            third_dungeon_name = await get_window_from_path(client.root_window, third_dungeon_text)
            third_dungeon = await third_dungeon_name.maybe_text()
            third_dungeon = third_dungeon.replace("<center>", '')
            third_dungeon = third_dungeon.replace("</center>", '')
        except: 
            third_dungeon = ""
        print(third_dungeon)
        return third_dungeon

async def read_fourth_dungeon(client: Client) -> str:
    fourth_dungeon_text = ["WorldView", "TeamHelpWindow", "Line4", "InstanceSprite"]
    try:
            fourth_dungeon_name = await get_window_from_path(client.root_window, fourth_dungeon_text)
            fourth_dungeon = await fourth_dungeon_name.maybe_text()
            fourth_dungeon = fourth_dungeon.replace("<center>", '')
            fourth_dungeon = fourth_dungeon.replace("</center>", '')
    except:
        fourth_dungeon = ""
    print(fourth_dungeon)
    return fourth_dungeon
    
async def read_fifth_dungeon(client: Client) -> str:
    fifth_dungeon_text = ["WorldView", "TeamHelpWindow", "Line5", "InstanceSprite"]
    try:
            fifth_dungeon_name = await get_window_from_path(client.root_window, fifth_dungeon_text)
            fifth_dungeon = await fifth_dungeon_name.maybe_text()
            fifth_dungeon = fifth_dungeon.replace("<center>", '')
            fifth_dungeon = fifth_dungeon.replace("</center>", '')
    except:
        fifth_dungeon = ""
    print(fifth_dungeon)
    return fifth_dungeon

async def read_dungeons(client):
    first_dungeon = await read_first_dungeon
    if first_dungeon == "Skull Fort":
         await click_window_from_path(client.mouse_handler, client.root_window, first_dungeon_button) 
    else:
        second_dungeon = await read_second_dungeon(client)
        if second_dungeon == "Skull Fort":
             await click_window_from_path(client.mouse_handler, client.root_window, second_dungeon_button) 
        else:
            third_dungeon = await read_third_dungeon(client)
            if third_dungeon == "Skull Fort":
                 await click_window_from_path(client.mouse_handler, client.root_window, third_dungeon_button) 
            else:
                fourth_dungeon = await read_fourth_dungeon(client)
                if fourth_dungeon == "Skull Fort":
                     await click_window_from_path(client.mouse_handler, client.root_window, fourth_dungeon_button) 
                else:
                    fifth_dungeon = await read_fifth_dungeon(client)
                    if fifth_dungeon == "Skull Fort":
                         await click_window_from_path(client.mouse_handler, client.root_window, fifth_dungeon_button) 
                    else:
                        await click_window_from_path(client.mouse_handler, client.root_window, refresh_button) 
                        await read_dungeons(client)






async def setup(): #activates all hooks that it can for a client, to be replaced
    handler = ClientHandler()
    print(f"Activating Special Lxghtend Hooks :O")
    async with ClientHandler() as handler:
        client = handler.get_new_clients()[0]
        await client.activate_hooks()
        await client.mouse_handler.activate_mouseless()
    await join_team_up(client)


async def main():
    print('Auto Team Up Bot by Lxghtend')
    input('Press Enter to start.')
    await setup()

    # Error Handling
async def run():
        try:
            await main()
        except:
         import traceback
         traceback.print_exc()
         print('Send this error to Lxghtend')

if __name__ == "__main__":
        asyncio.run(run())



'''
C:\Users\ \Downloads>py -m tesing
Auto Team Up Bot by Lxghtend
Press Enter to start.
Activating Special Lxghtend Hooks :O
Traceback (most recent call last):
  File "C:\Users\ \Downloads\tesing.py", line 201, in run
    await main()
  File "C:\Users\ \Downloads\tesing.py", line 196, in main
    await setup()
  File "C:\Users\ \Downloads\tesing.py", line 190, in setup
    await join_team_up(client)
  File "C:\Users\ \Downloads\tesing.py", line 74, in join_team_up
    if  await is_visible_by_path(client.root_window, npc_range) :
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ \Downloads\tesing.py", line 58, in is_visible_by_path
    root = client.root_window
           ^^^^^^^^^^^^^^^^^^
AttributeError: 'CurrentRootWindow' object has no attribute 'root_window'
'''