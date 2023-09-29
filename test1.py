
import asyncio
import wizwalker
from wizwalker import Client, MemoryReadError, XYZ
from wizwalker.memory import DynamicClientObject
from typing import *
from wizwalker import ClientHandler


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
    



async def check(client: Client, self, name: str):
    while await get_base_entities_with_vague_name(self, parasaur) == False:
        asyncio.sleep(0.1)
    if  await get_base_entities_with_vague_name(self, parasaur) == True:
        print("Found!")
        

async def setup():
    handler = ClientHandler()
    print(f"Activating Special Lxghtend Hooks :O")
    async with ClientHandler() as handler:
        client = handler.get_new_clients()[0]
        await client.activate_hooks()
        await client.mouse_handler.activate_mouseless()
    await check()


async def main():
    print('Entity Checker by Lxghtend')
    print('Press Enter to start.')
    input()
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