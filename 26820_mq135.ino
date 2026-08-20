int sensorValue; // Variable para leer la salida analógica
int digitalValue; // Variable para leer la salida digital

void setup()
{
  Serial.begin(9600);    // Configura la comunicación serie a 9600 baudios
  pinMode(13, OUTPUT);   // Pin 13 como salida para el LED
  pinMode(2, INPUT);     // Pin 2 como entrada para el pin DO del MQ135
}

void loop()
{
  sensorValue = analogRead(A0); // Lee la entrada analógica A0
  digitalValue = digitalRead(2); // Lee la entrada digital del pin 2

  if (sensorValue > 400)
  {
    digitalWrite(13, HIGH); // Enciende el LED si supera 400
  }
  else
  {
    digitalWrite(13, LOW);  // Apaga el LED si es menor o igual a 400
  }

  Serial.print("Analógico: ");
  Serial.println(sensorValue, DEC);
  
  Serial.print("Digital: ");
  Serial.println(digitalValue, DEC);

  delay(1000); // Espera 1 segundo para la siguiente lectura
}
