from paho.mqtt.client import Client
import traceback
import sys
import time 
import random
import numpy as np

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    
    def actualizar_datos(t, n):
     
        # comprobar si el nuevo nº es máx / mín
        if userdata[f'maximo_{t}'] < n:
            userdata[f'maximo_{t}'] = n
        if userdata[f'minimo_{t}'] > n:
            userdata[f'minimo_{t}'] = n
                
        # actualizar datos
        userdata[f'total_{t}'] += n
        userdata[f'numero_datos_{t}'] += 1
    
    try:
        n =  float(msg.payload)
        
        # actualizar valores generales
        if userdata['maximo'] < n:
            userdata['maximo'] = n
        if userdata['minimo'] > n:
            userdata['minimo'] = n
        userdata['total'] += n
        userdata['numero_datos'] += 1
        
        # actualizar datos parciales
        if msg.topic == 'temperature/t1':
            actualizar_datos("t1", n)
        if msg.topic == 'temperature/t2':
            actualizar_datos("t2", n)
            
    except ValueError:
        pass
      
    except Exception as e:
        raise e

def main(broker):
    userdata = {
        'maximo_t1': 0,
        'minimo_t1': 10000000,
        'total_t1': 0,
        'numero_datos_t1':0,
        'maximo_t2': 0,
        'minimo_t2': 10000000,
        'total_t2': 0,
        'numero_datos_t2':0,
        'maximo': 0,
        'minimo': 10000000,
        'total': 0,
        'numero_datos':0,
    }
    client = Client(userdata=userdata)
    client.on_message = on_message

    print(f'Connecting on channels numbers on {broker}')
    client.connect(broker)
    
    client.subscribe('temperature/#')

    client.loop_start()
    t0 = time.time()

    while True:
        # Cada 4 seg (aprox) recogemos los datos
        if (time.time()-t0) > 4: 
          
            # calcular medias
            media_t1 = userdata['total_t1'] / userdata['numero_datos_t1'] 
            media_t2 = userdata['total_t2'] / userdata['numero_datos_t2']
            media_t  = userdata['total']    / userdata['numero_datos']
            
            # publicar
            client.publish('/clients/maximo_t1', str(userdata["maximo_t1"]))
            client.publish('/clients/minimo_t1', str(userdata["minimo_t1"]))
            client.publish('/clients/media_t1',  str(media_t1))
            client.publish('/clients/maximo_t2', str(userdata["maximo_t2"]))
            client.publish('/clients/minimo_t2', str(userdata["minimo_t2"]))
            client.publish('/clients/media_t2',  str(media_t2))
            client.publish('/clients/maximo',    str(userdata["maximo"]))
            client.publish('/clients/minimo',    str(userdata["minimo"]))
            client.publish('/clients/media',     str(media_t))
            
            # reiniciar tiempos
            time.sleep(random.random())
            t0 = time.time()
            


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
