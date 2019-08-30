#include <Wire.h>
#define SLAVE_ADDRESS 0x04

int dt = 1000; //delay variable 

char number[50];
int state = 0;
char in[2] ="10";
int k =0;

const int AIN1 = 4;           //control pin 1 on the motor driver for the front  right motor
const int AIN2 = 2;           //control pin 2 on the motor driver for the right motor
const int PWMA = 3;           //speed control pin on the motor driver for the right motor


const int AIN3 = 5;           //control pin 1 on the motor driver for the front left motor
const int AIN4 = 7;           //control pin 2 on the motor driver for the right motor
const int PWMB = 6;           //speed control pin on the motor driver for the right motor


const int motorspeed1 = 100;//125-50;
const int motorspeed2 = 140;//100-50;

//int sv1 = 0;
//int sv2 = 0;

//int s1 = A5;
//int s2 = A4;

void setup() 
{
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
    
  pinMode(AIN3, OUTPUT);
  pinMode(AIN4, OUTPUT);
  pinMode(PWMB, OUTPUT);
  
  Serial.begin(9600);

  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  //while(Wire.available()){
  Wire.onReceive(receiveData);//}
  //  Wire.onRequest(sendData);
  
}


void loop() 
{
   
    delay(100);
}

void receiveData(int byteCount) 
{
  int i = 0;
  while (Wire.available()) 
  {
    number[i] = Wire.read();
    i++;delay(100);
    //Serial.print("hi");
  }
  //number[i] = '\0';
  Serial.println(number);
  if(number == '6') 
   { rightturn();}

  if (number =='/')
  { leftturn();}
}    

 void rightturn()
 {
   digitalWrite(4,LOW);
   digitalWrite(2,HIGH);
   analogWrite(PWMA, abs(motorspeed1));   //right motor turn ?

   digitalWrite(5,HIGH);
   digitalWrite(7,LOW);
   analogWrite(PWMB, abs(motorspeed2));   //left motor left ?

   delay(2*dt);

   digitalWrite(4,LOW);
   digitalWrite(2,HIGH);
   analogWrite(PWMA, abs(motorspeed1));   //right motor turn ?

   digitalWrite(5,HIGH);
   digitalWrite(7,LOW);
   analogWrite(PWMB, abs(motorspeed2-motorspeed2));   //left motor left ?
   
   
   delay(5*dt);

   digitalWrite(4,LOW);
   digitalWrite(2,HIGH);
   analogWrite(PWMA, abs(motorspeed1));   //right motor turn ?

   digitalWrite(5,HIGH);
   digitalWrite(7,LOW);
   analogWrite(PWMB, abs(motorspeed2));   //left motor left ?
   
 } 

void leftturn()
 {
   digitalWrite(4,LOW);
   digitalWrite(2,HIGH);
   analogWrite(PWMA, abs(motorspeed1));   //right motor turn ?

   digitalWrite(5,HIGH);
   digitalWrite(7,LOW);
   analogWrite(PWMB, abs(motorspeed2));   //left motor left ?

   delay(2*dt);

   digitalWrite(4,LOW);
   digitalWrite(2,HIGH);
   analogWrite(PWMA, abs(motorspeed1-motorspeed1));   //right motor turn ?

   digitalWrite(5,HIGH);
   digitalWrite(7,LOW);
   analogWrite(PWMB, abs(motorspeed2));   //left motor left ?
   
   
   delay(5*dt);

   digitalWrite(4,LOW);
   digitalWrite(2,HIGH);
   analogWrite(PWMA, abs(motorspeed1));   //right motor turn ?

   digitalWrite(5,HIGH);
   digitalWrite(7,LOW);
   analogWrite(PWMB, abs(motorspeed2));   //left motor left ?
   
 }

