int sensorPin = A5;    // select the input pin for the potentiometer

int k =0;


const int AIN1 = 13;           //control pin 1 on the motor driver for the right motor
const int AIN2 = 12;            //control pin 2 on the motor driver for the right motor
const int PWMA = 11;            //speed control pin on the motor driver for the right motor

const int BIN1 = 9;           //control pin 1 on the motor driver for the right motor
const int BIN2 = 8;            //control pin 2 on the motor driver for the right motor
const int PWMB = 10;            //speed control pin on the motor driver for the right motor

const int BIN1_2 = 7;           //control pin 1 on the motor driver for the right motor
const int BIN2_2 = 6;            //control pin 2 on the motor driver for the right motor
const int PWMC = 5;            //speed control pin on the motor driver for the right motor

const int AIN1_2 = 4;           //control pin 1 on the motor driver for the right motor
const int AIN2_2 = 2;            //control pin 2 on the motor driver for the right motor
const int PWMD = 3 ;    
int sensorValue = 0;  
int motorSpeed1 = 155;
int motorSpeed2 = 80;

void setup() 
{
    pinMode(AIN1, OUTPUT);
    pinMode(AIN2, OUTPUT);
    pinMode(PWMA, OUTPUT);
    pinMode(BIN1, OUTPUT);
    pinMode(BIN2, OUTPUT);
    pinMode(PWMB, OUTPUT);

    pinMode(AIN1_2, OUTPUT);
    pinMode(AIN2_2, OUTPUT);
    pinMode(PWMD, OUTPUT);

    pinMode(BIN1_2, OUTPUT);
    pinMode(BIN2_2, OUTPUT);
    pinMode(PWMC, OUTPUT);


   Serial.begin(9600);
  //pinMode(ledPin, OUTPUT);
}

void loop() 
{
  
  sensorValue = analogRead(sensorPin);
  
  Serial.print("\n");
  Serial.print(k);
  
  Serial.print("\n");
  Serial.print(sensorValue);
  
  if (sensorValue<600)
  {
    sensorValue = analogRead(sensorPin);
    k=1;                                    //if yellow line detected 
    
    digitalWrite(13, HIGH);                 //clockwise Front left              
    digitalWrite(12, LOW);
    analogWrite(PWMA, abs(motorSpeed1));
    
    digitalWrite(9, LOW);                         
    digitalWrite(8, HIGH);                  //clockwise rear left
    analogWrite(PWMB, abs(motorSpeed1));
    
    digitalWrite(7, HIGH);                  //clockwise rear right 
    digitalWrite(6, LOW);
    analogWrite(PWMC, abs(motorSpeed2));  
    
    digitalWrite(4, HIGH);                  //clockwise front right 
    digitalWrite(2, LOW);
    analogWrite(PWMD, abs(motorSpeed2)); 
    
    //Serial.print("\n");
    //Serial.print(sensorValue);
    
  }
  else
  {
    
    sensorValue = analogRead(sensorPin);
    k=0;
    digitalWrite(13, HIGH);             //clockwise Front left              
    digitalWrite(12, LOW);
    analogWrite(PWMA, abs(motorSpeed2));    
    digitalWrite(9, LOW);                         
    digitalWrite(8, HIGH);              //clockwise rear left
    analogWrite(PWMB, abs(motorSpeed2));
    digitalWrite(7, HIGH);              //clockwise rear right 
    digitalWrite(6, LOW);
    analogWrite(PWMC, abs(motorSpeed1));  
    digitalWrite(4, HIGH);              //clockwise front right 
    digitalWrite(2, LOW);
    analogWrite(PWMD, abs(motorSpeed1)); 
  }
  
  Serial.print("\n");
  Serial.print(k);
  
  
  //Serial.print("sensor = \n");
  //Serial.print(sensorValue);
  delay(100);

}


