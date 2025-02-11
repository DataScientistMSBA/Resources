'''
Source: https://youtu.be/t5Bo1Je9EmE?si=YL4VpJXFtoJIGEW4
'''

import asyncio

'''
Coroutines: Are computer program components that generalize subroutines for non-preeptive multitasking, by allowing multiple execution to be suspended and resumed. (Wikipedia)
'''

'''Error: RuntimeWaring: coroutine 'main' was never awaited'''
# async def main():
#     print('Hello')
# main()

'''Error: 'await' outside function'''
# async def main():
#     print('Hello')
# await main()

'''
Async Event-Loop: In computer science, the event loop is a programming construct or design that waits for and dispatches events or messages in a program. It works by making a request to some internal or external "event provider" (that generally blocks the request until an event has arrived), and then calls the relevant event handler ("dispatches the event"). (Wikipedia)
'''
# async def main(): 
#     print('Hello')
# asyncio.run(main())

'''
Async/Await Keywords
'''
# async def main():
#     print('Hello')
# async def foo(txt):
    # print(txt)
    # await asyncio.sleep(1)
    # print(txt)
# asyncio.run(main())