"""
 le pc (server) envoie les données (la valeur des touches de la mannette )   par wifi à la raspberrypi (client)

"""

import json
import socket
from threading import Timer

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5000))
server.listen(5)
print("Server is now running...")

def background_controller():
    message = {
            "CH1" : 10,
            "CH2" : 20,
            "CH3" : 30,
            "CH4" : 40,
        }
    json_message = json.dumps(message)
    print(f"envoie des données : {json_message}")
    clientsocket.send(bytes(json_message, "utf-8"))
    Timer(5, background_controller).start()

while True: 
    try:
        clientsocket, addresse = server.accept()
        print(f"connection from addresse {addresse} has been established")
        background_controller()

    except KeyboardInterrupt:
        print("Server arrêté manuellement")
        
        
    except Exception as e:
        print("Une erreur c'est produite coté server : ", e)
        


#print("Server disconnected")