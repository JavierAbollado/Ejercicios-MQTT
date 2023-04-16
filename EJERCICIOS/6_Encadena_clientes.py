from paho.mqtt.client import Client
import sys
import sympy # to check prime numbers

def on_message_main(client, userdata, msg):

    print(msg.topic, msg.payload)
    n =  float(msg.payload)

    # si el nº es entero 
    if n % 1 == 0: 
        n = int(n)
        # si el nº es primo
        if sympy.isprime(n):
                
            if not userdata['numbers']._userdata['find_first_prime']:

                userdata['numbers']._userdata['find_first_prime'] = True
                
                # activamos humidity (nos suscribimos y con ello empezaremos a checkear los datos)
                userdata['humidity'].subscribe('humidity') 

                # activamos "topic" para poder ver el mensaje de aviso (cuando se encuentre el segundo primo)
                userdata['humidity'].subscribe(userdata['info']._userdata["topic"]) 

                # start
                userdata['numbers'].loop_start()
                userdata['humidity'].loop_start()

                # publicamos mensaje de aviso
                client.publish(userdata['info']._userdata['topic'], userdata['info']._userdata['mensaje_prime1'])

            else:

                userdata['numbers']._userdata['find_first_prime'] = False

                # publicamos mensaje de aviso
                client.publish(userdata['info']._userdata['topic'], userdata['info']._userdata['mensaje_prime2'])

                # publicamos mensaje de ¡tiempo terminado! -> así "humidity" parará
                client.publish(userdata['info']._userdata['topic'], userdata['info']._userdata['exit'])


def on_message_humidity(client, userdata, msg):

    if msg.payload == 'time out!':
        client.unsubscribe('humidity')
        media = userdata['suma_total'] / userdata['num_datos']
        client.publish('/clients/PrimeNumbersAndHumidity', media)

    if msg.topic == 'humidity':
        n =  float(msg.payload)
        userdata['suma_total'] += n
        userdata['num_datos'] += 1
        
            
            

"""
     - Tenemos 3 clients y uno que tiene a todos. 
     - El cliente "numbers" irá viendo si sale algún nº primo en caso positivo entonces activa el estado dos 
    (find_first_prime = True), y además suscribimos el "humidity" a los canales f"{topic}" y "humidity" para que a partir 
    de ese momento comienza a cojer datos. 
     - Cuando "numbers" encuentre el 2º primo, entonces mandará el mensaje de aviso por el canal f"{topic}" y este será recibido
    por "humidity" el cual parará de tomar datos, se desuscribirá y publicará la media obtenida entre el tiempo del 1º y 2º primo encontrado.
     - Vuelta a comenzar los pasos anteriores.  
"""
def main(broker):

    data_numbers = {
        'find_first_prime':False
    }
    
    data_humidity = {
        'suma_total':0,
        'num_datos':0
    }

    data_info = {
        'topic'         : '/clients/PrimeNumbersAndHumidity',
        'message_prime1': 'First prime founded! Time starts now!',
        'message_prime2': 'Second prime founded!',
        'exit'          : 'Time out!'
    }

    client_numbers = Client(userdata=data_numbers)
    client_humidity = Client(userdata=data_humidity)
    client_info = Client(userdata=data_info)
    
    clients = Client(userdata={"numbers":client_numbers, "humidity":client_humidity, "info":client_info})
    
    clients.on_message = on_message_main
    client_humidity.on_message = on_message_humidity

    print(f'Connecting on channels numbers on {broker}')
    client_numbers.connect(broker)
    client_humidity.connect(broker)
    client_info.connect(broker)
    clients.connect(broker)
    
    client_numbers.subscribe('numbers')
    
    client_numbers.loop_forever()
    client_humidity.loop_forever()
    client_info.loop_forever()
    clients.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
    
