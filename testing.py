import asyncio
import keyboard
import re
import math

codes = ["2002", "3005", "2884", "2994", "1002", "1992", "3482", "7267", "3018", "6565", "7659", "2913", "2034", "4494", "6168", "3872", "0029", "6324", "9649", "1958", "8825", "7378", "6257", "8501", "6334", "7697", "2095", "7302"]

async def send_code():
        print("Press P on the Keyboard for the next code!")
        while True:
            if keyboard.record(until="p"):
                code = codes[+1]
                print(code)
                #keyboard.send("2")
    
async def first_n_digits(code, n):
    return code // 10 ** (int(math.log(code, 10)) - n + 1)


async def main():
    await send_code()

asyncio.run(main())


