import asyncio
import wizwalker
from wizwalker import Client, MemoryReadError, XYZ
from wizwalker.memory import DynamicClientObject
from typing import *

class SprintyClient():
	# FULL CREDIT TO SIROLAF FOR THIS CLASS
	def __init__(self, client: Client):
		self.client = client


    async def find_closest_by_name(self, name: str, only_safe: bool = False, excluded_ids: Set[int] = None) -> Optional[DynamicClientObject]:
            return await self.find_closest_of_entities(await self.get_base_entities_with_name(name, excluded_ids), only_safe)


    async def tp_to_closest_by_vague_name(self, name: str, only_safe: bool = False, excluded_ids: Set[int] = None) -> bool:
            if e := await self.find_closest_by_vague_name(name, only_safe, excluded_ids):
                await self.client.teleport(await e.location())
                return True
            return False
            
    async def find_closest_by_vague_name(self, name: str, only_safe: bool = False, excluded_ids: Set[int] = None) -> Optional[DynamicClientObject]:
            return await self.find_closest_of_entities(await self.get_base_entities_with_vague_name(name, excluded_ids), only_safe)


    async def find_closest_of_entities(self, entities: List[DynamicClientObject], only_safe: bool = False) \
                -> Optional[DynamicClientObject]:
            closest = None
            smallest_dist = 0
            self_pos = await self.client.body.position()
            for w in entities:
                dist = self_pos.distance(await w.location())
                if closest is None or dist < smallest_dist:
                    smallest_dist = dist
                    closest = w
            return closest


    async def get_base_entity_list(self, excluded_ids: Set[int] = None) -> List[DynamicClientObject]:
            return await self.remove_excluded_entities_from(await self.client.get_base_entity_list(), excluded_ids)


    async def get_base_entities_with_predicate(self, predicate: Callable, excluded_ids: Set[int] = None):
        entities = []

        for entity in await self.get_base_entity_list(excluded_ids):
            if await predicate(entity):
                entities.append(entity)

        return entities
            
    async def get_base_entities_with_vague_name(self, name: str, excluded_ids: Set[int] = None) -> List[DynamicClientObject]:
            async def _pred(e):
                if temp := await e.object_template():
                    return name.lower() in (await temp.object_name()).lower()
                return False

            return await self.get_base_entities_with_predicate(_pred, excluded_ids)
            
            
    async def remove_excluded_entities_from(self, entities: List[DynamicClientObject], excluded_ids: Set[int] = None) \
                -> List[DynamicClientObject]:
            if excluded_ids is not None and len(excluded_ids) > 0:
                res = []
                for e in entities:
                    if excluded_ids is None or await e.global_id_full() not in excluded_ids:
                        res.append(e)
                return res
            return entities 
    
    
async def enter_pet_mode():
    #click window pet system
    #click play as pet until its gone
    #add some way to check if pet mode worked? possibly check for self as an entity in pet mode?
    
#add failsafe where if combat is not entered in 1 minute, shut the bot down, possibly switch realms instead
    




async def locate_and_teleport_to_parasaur(client: Client, self, name: str):
    while await get_base_entities_with_vague_name(self, parasaur) == False #will this break automatically?
        await client.teleport(-4529.26513671875, 8810.4248046875, 2.954559326171875)
        await asyncio.sleep(2)
        if await get_base_entities_with_vague_name(self, parasaur) == True:
            break   
        await client.teleport(-812.3797607421875, 3391.8662109375, 3.31903076171875)
        await asyncio.sleep(2)
        if await get_base_entities_with_vague_name(self, parasaur) == True:
            break   
        await client.teleport(4538.18017578125, 8573.890625, 25.11590576171875)
        await asyncio.sleep(2)
        if await get_base_entities_with_vague_name(self, parasaur) == True:
            break   
        await client.teleport(1168.223388671875, 2431.079345703125, 3.714691162109375)
        await asyncio.sleep(2)
        if await get_base_entities_with_vague_name(self, parasaur) == True:
            break   
    if await get_base_entities_with_vague_name(self, parasaur) != False #might have to rework this but idk how
        await tp_to_closest_by_vague_name(self, parasaur)
    else:
        pass #idk      