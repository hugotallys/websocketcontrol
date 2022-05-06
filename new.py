
import matplotlib.pyplot as plt
import asyncio
import threading
import websockets
import time
import threading
from queue import Queue
import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

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
    # x = threading.Thread(target=view)
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
            print("Outputs: " + received[1])
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


X = deque(maxlen=20)
X.append(1)

Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=100,
            n_intervals=10000

        ),
    ]
)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    X.append(X[-1]+1)
    value = queue_out.get()
    print(value)
    Y.append(float(value[1]))  # random.uniform(-0.1, 0.1))
    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )
    time.sleep(0.002)
    return {'data': [data],
            'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]), yaxis=dict(range=[min(Y), max(Y)]),)}


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop = asyncio.new_event_loop()
    x = threading.Thread(target=server, args=(loop,))
    x.start()
    app.run_server()
    x.join()
