
int k =0;

const int AIN1 = 13;           //control pin 1 on the motor driver for the front  right motor
const int AIN2 = 12;           //control pin 2 on the motor driver for the right motor
const int PWMA = 11;           //speed control pin on the motor driver for the right motor


const int AIN3 = 8;           //control pin 1 on the motor driver for the front left motor
const int AIN4 = 7;           //control pin 2 on the motor driver for the right motor
const int PWMB = 6;           //speed control pin on the motor driver for the right motor

const int AIN5 = 9;           //control pin 1 on the motor driver for the right motor
const int AIN6 = 10;           //control pin 2 on the motor driver for the right motor
const int PWMC = 5;           //speed control pin on the motor driver for the right motor

const int AIN7 = 4;           //control pin 1 on the motor driver for the right motor
const int AIN8 = 2;           //control pin 2 on the motor driver for the right motor
const int PWMD = 3;           //speed control pin on the motor driver for the right motor

const int motorSpeed1 = 125-50;
const int motorSpeed2 = 100-50;
const int motorSpeed3 = 100-50;
const int motorSpeed4 = 100;

int sv1 = 0;
int sv2 = 0;

int s1 = A5;
int s2 = A4;

void setup() 
{
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
    
  pinMode(AIN3, OUTPUT);
  pinMode(AIN4, OUTPUT);
  pinMode(PWMB, OUTPUT);
  
  pinMode(AIN5, OUTPUT);
  pinMode(AIN6, OUTPUT);
  pinMode(PWMC, OUTPUT);
  
  pinMode(AIN7, OUTPUT);
  pinMode(AIN8, OUTPUT);
  pinMode(PWMD, OUTPUT);
  
  Serial.begin(9600);
}


void loop() 
{
  
    k=1;
    sv1 = analogRead(s1);
    sv2 = analogRead(s2);
    
    digitalWrite(13, LOW);           //clockwise Front Right              
    digitalWrite(12, HIGH);
    analogWrite(PWMA, abs(motorSpeed1));       

    digitalWrite(8, HIGH);           //clockwise Front Left              
    digitalWrite(7, LOW);
    analogWrite(PWMB, abs(motorSpeed2));

    digitalWrite(9, HIGH);           //clockwise Rear Right              
    digitalWrite(10, LOW);
    analogWrite(PWMC, abs(motorSpeed3));   

    digitalWrite(2, LOW);           //clockwise Rear Left              
    digitalWrite(4, HIGH);
    analogWrite(PWMD, abs(motorSpeed4)); 
    
    Serial.print("\n");
    Serial.print(k);
  

    delay(1000);
}
