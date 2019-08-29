/*
  I2C Pinouts
  SDA -> A4
  SCL -> A5
*/

//Import the library required
#include <Wire.h>

//Slave Address for the Communication
#define SLAVE_ADDRESS 0x04

char number[50];
int state = 0;
char in[2] ="10";

//Code Initialization
void setup() {
  // initialize i2c as slave
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  //  Wire.onRequest(sendData);
  Serial.println(number[0]);
  
}

void loop() {
  delay(100);
  if(strcmp(number,in)== 0){Serial.println("yes");}
  Wire.onReceive(receiveData);
  int i = 0;
  while (Wire.available()) {
    number[i] = Wire.read();
    i++;
    Serial.print("hi");
  }
  number[i] = '\0';

  if(number[0] == in[0]) 
   {
     Serial.println("\nstarting motors");
   }
  //if(Serial.available()>0)
  //{
  // in = Serial.readString();
  // if(in=="start motors")
  // {Serial.println(in);}
//   Serial.println(in);
   //else {Serial.println("mate");}
  //}
} // end loop

// callback for received data
void receiveData(int byteCount) 
{
  int i = 0;
  while (Wire.available()) {
    number[i] = Wire.read();
    i++;
    //Serial.print("hi");
  }
  number[i] = '\0';
 // Serial.println(number);
  //Serial.print('5');
 //for (i=0;i<sizeof(number)-1;i++)
 // {
   if(number[0] == '1') 
   {
     Serial.println("\nstarting motors");
   }
 // }  
}  // end while

// callback for sending data
void sendData() 
{
  Wire.write(number);
}

//End of the program
