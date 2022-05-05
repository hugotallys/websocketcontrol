
import matplotlib.pyplot as plt
import asyncio
import threading
import websockets
import time
import threading
from queue import Queue
queue_out = Queue(maxsize=100)
queue_out.put([0.0, 0.0, 0.0])
queue_in = Queue(maxsize=100)
queue_in.put(0)
queue_ref = Queue(maxsize=100)
queue_ref.put([0.0, 10, 0.0])
queue_ref_in = Queue(maxsize=100)
queue_ref_in.put(10)

last_out = [0.0, 0.0, 0.0]


def view():
    x = [0.0]*100
    y = [1.0]*100
    plt.plot(x, y)
    plt.show()
    while True:
        try:
            if not queue_out.empty():
                last_out = queue_out.get()
            print(last_out)
        except Exception as e:
            print(e)
            return


async def echo(websocket):
    #x = threading.Thread(target=view)
    # x.start()
    while True:
        try:
            startTime = time.time()
            await websocket.send("get references")
            received = (await websocket.recv()).split(",")
            # queue_ref.put(received)
            # print(received)
            await websocket.send("get outputs")
            received = (await websocket.recv()).split(",")
            # print("Outputs: " + received[1])
            """plt.scatter(time.time(), float(received[1]))
            plt.show()"""
            queue_out.put(received)
            """while queue_in.empty():
                time.sleep(0.0001)

            await websocket.send("set input|"+str(queue_in.get()))"""
            # Aqui mestre hugo
            '''if loop:
                while queue_ref_in.empty():
                    time.sleep(0.0001)
                await websocket.send("set references|"+str(queue_ref_in.get()))'''
            ellapsedTime = 0.0
            while ellapsedTime < 0.01:
                time.sleep(0.0001)
                endTime = time.time()
                ellapsedTime = endTime - startTime
        except Exception as e:
            print(e)
            return
    # x.join()


def server(loop):
    asyncio.set_event_loop(loop)
    server = websockets.serve(echo, "localhost", 6660)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()


loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
x = threading.Thread(target=server, args=(loop,))
x.start()
x.join()
