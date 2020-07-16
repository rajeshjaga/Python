import os
import asyncio as asyn

filName="tutorial.mp4"
f=open(filName,"w+")
f.write("hello your hacked")


async def deleteThis():
    await asyn.sleep(2)
    os.system('del terminate.py -y')

asyn.run( deleteThis())
