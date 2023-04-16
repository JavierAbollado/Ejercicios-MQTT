from paho.mqtt.client import Client
from tkinter import Tk, Label, Button, Entry, StringVar, font
from time import time

#  Interfaz gráfica con tkinter
window = Tk()
window.title("Una ventana de prueba")

l = Label(window, text="Una ventana con texto... \n incluso en varias líneas", height=20, width=60, font=font.Font(family="Helvetica", size=14))
l.pack()

msg_l = Label(window,text="Message?")
msg_l.pack()
msg_t = StringVar()
msg = Entry(window, width=20, textvariable=msg_t)
msg.pack()

def ejec_button():
    client.publish('clients/tkinter', msg.get())

send = Button(window, text="Send", command=ejec_button)
send.pack()

# Cliente con callback
def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

    client.window.winfo_children()[0].config(text=msg.payload)
    client.window.winfo_children()[0].pack()

client = Client()
client.on_message = on_message
client.window = window

# Prueba que consiste en mostrar en el interfaz gráfico lo que publica el botón del interfaz

client.connect("picluster02.mat.ucm.es")
client.subscribe('clients/tkinter')

# Esencial entender el papel de estas dos últimas líneas, donde se lanzan 'implicitamente' los procesos que se encargan de gestionar los eventos del cliente mqtt y de la ventana del interfaz.

client.loop_start()
client.window.mainloop()
