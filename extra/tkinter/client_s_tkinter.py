from paho.mqtt.client import Client
from tkinter import Tk, Label, font

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

    window.winfo_children()[0].config(text=msg.payload)
    window.winfo_children()[0].pack()

window = Tk()
window.title("Una ventana de prueba")

l = Label(window, text="Una ventana con texto... \n incluso en varias líneas", height=20, width=60, font=font.Font(family="Helvetica", size=14))
l.pack()


client = Client()
client.on_message = on_message
client.window = window

client.connect("picluster02.mat.ucm.es")
topic = "clients/tkinter"
client.subscribe(topic)

client.loop_start()
client.window.mainloop()
