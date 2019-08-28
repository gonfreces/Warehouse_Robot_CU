/*
  Logic:
- The slave RPi is connected to the main RPi via I2C and connected to Arduino via serial communication
- Main RPi detects the correct pickup pallet by identifying the QR code using OpenCV and camera 
- The slave RPi then commands the arduino to execute this code 
  
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

//Defining the motors

const int AIN1 = 4;           //control pin 1 on the motor driver for the front  right motor
const int AIN2 = 2;           //control pin 2 on the motor driver for the right motor
const int PWMA = 3;           //speed control pin on the motor driver for the right motor


const int AIN3 = 5;           //control pin 1 on the motor driver for the front left motor
const int AIN4 = 7;           //control pin 2 on the motor driver for the right motor
const int PWMB = 6;           //speed control pin on the motor driver for the right motor

const int motorSpeed1 = 255;//125-50;
const int motorSpeed2 = 255;//100-50;

int sv1 = 0;
int sv2 = 0;

int s1 = A5;
int s2 = A4;

int ti =0;

//Code Initialization
void setup() 
{
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
    
  pinMode(AIN3, OUTPUT);
  pinMode(AIN4, OUTPUT);
  pinMode(PWMB, OUTPUT);
  
  // initialize i2c as slave
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  //  Wire.onRequest(sendData);
}

void loop() 
{
  
  Serial.print ("\r\n Entire time: ");
  if (Serial.available() > 0) { ti = Serial.read(); }
  Serial.print("Moving forward for ");
  Serial.println(ti);   
  delay(100);
} // end loop

// callback for received data
void receiveData(int byteCount) 
{
  int i = 0;
  while (Wire.available()) 
  {
    number[i] = Wire.read();
    i++;
   }
  number[i] = '\0';

  //inpu+t code for now
  
  if(number[0] == '1') { callFwd(); }
  if(number[0] == '0') { callStop();}
  
}  // end while

void callFwd()
{
  Serial.println("\nGoing forward");
  Serial.println("\nStarting motors");
     
  sv1 = analogRead(s1);
  sv2 = analogRead(s2);
  
  digitalWrite(AIN1, LOW);           //clockwise Front Right              
  digitalWrite(AIN2, HIGH);
  analogWrite(PWMA, abs(motorSpeed1));       

  digitalWrite(AIN3, HIGH);           //clockwise Front Left              
  digitalWrite(AIN4, LOW);
  analogWrite(PWMB, abs(motorSpeed2));
}

void callStop()
{
  Serial.println("\nStopping");
       
  sv1 = analogRead(s1);
  sv2 = analogRead(s2);
  
  digitalWrite(AIN1, LOW);           //clockwise Front Right              
  digitalWrite(AIN2, LOW);
  analogWrite(PWMA, 0);       

  digitalWrite(AIN3, LOW);           //clockwise Front Left              
  digitalWrite(AIN4, LOW);
  analogWrite(PWMB, 0);
}

// callback for sending data
void sendData() 
{
  Wire.write(number);
}


//End of the program
