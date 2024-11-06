"""
la raspberrypi (client) recoie les valeurs des touches de la mannette par wifi du pc (server) et les envoies 
 par i2c à l'arduino MEGA
"""
import socket
import json
import smbus
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addresse_server = "192.168.77.55"
client.connect((addresse_server, 5000))

ARDUINO_ADDRESS = 8

# Fonction pour envoyer les valeurs dans l'ordre CH1, CH2, CH3, CH4
def send_data(data):
    bus = smbus.SMBus(1)  
    values = [ data["CH1"], data["CH2"], data["CH3"], data["CH4"] ]
    
    for value in values:
        try:
            bus.write_byte(ARDUINO_ADDRESS, value)  # Envoi de chaque valeur
            time.sleep(0.1)  # Pause entre les envois pour éviter la surcharge
        except Exception as e:
            print(f"Erreur d'envoi de la valeur {value}: {e}")



while True:
    try:
        data = json.loads(client.recv(1024).decode("utf-8"))
        print(data)
        send_data(data)
    
    except KeyboardInterrupt:
        print("Client arrêté manuellement")
        
        
    except Exception as e:
        print("Une erreur c'est produite coté client ", e)
        data = {
            "CH1" : 0,
            "CH2" : 0,
            "CH3" : 0,
            "CH4" : 0,
        }
            #send_data(data)
