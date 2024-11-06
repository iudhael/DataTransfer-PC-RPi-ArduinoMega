/*
Reception de données provenant d'une raspberry pi par i2c
*/

#include<Wire.h>

int data[4]; //tableau pour contenir les valeurs recu CH1 CH2 CH3 CH4
int index = 0;
int i =0;
#define ARDUINO_MEGA_ADDR 8

void setup() {
  Wire.begin(ARDUINO_MEGA_ADDR);
  Serial.begin(9600);
  Wire.onReceive(receiveEvent);

}

void loop() {

  //receiveEvent(int bytes)

  // Affiche les valeurs reçues toutes les secondes
  Serial.print("CH1: "); Serial.println(data[0]);
  Serial.print("CH2: "); Serial.println(data[1]);
  Serial.print("CH3: "); Serial.println(data[2]);
  Serial.print("CH4: "); Serial.println(data[3]);
  delay(1000);

}

// Fonction appelée lors de la réception de données
void receiveEvent(int bytes) {
  while (Wire.available()) {
    int value = Wire.read();  // Lit la valeur
    if (index < 4) {  // Vérifie que l'index est dans les limites du tableau
      data[index] = value;
      index++;
    }
    if (index >= 4) {
      index = 0;  // Réinitialise l'index pour la prochaine série de valeurs
    }
  }
}


// Fonction appelée lors de la réception de données
/*void receiveEvent(int bytes) {
  if(Wire.available()) {
    int value = Wire.read();  // Lit la valeur
    if (index < 4) {  // Vérifie que l'index est dans les limites du tableau
      data[index] = value;
      index++;
    }
    if (index >= 4) {
      index = 0;  // Réinitialise l'index pour la prochaine série de valeurs
    }
  }
}*/


