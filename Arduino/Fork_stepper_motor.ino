const int stepPin = 5; 
const int dirPin = 4; 
const int limit = 1000;
const int d = 1500;
const int pd = 500;


void setup() 
{
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
}


void loop() 
{
  
  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
                             // Makes 200 pulses for making one full cycle rotation
  callstepper(limit,stepPin,d);
    
  delay(pd); // One second delay
  
  digitalWrite(dirPin,LOW); //Changes the rotations direction
                            // Makes 400 pulses for making two full cycle rotation
  
  callstepper(limit,stepPin,d);
  
  delay(pd);
}

void callstepper(int l, int p, int d)
{
   for(int x = 0; x < l; x++) 
  {
    digitalWrite(p,HIGH);
    delayMicroseconds(d);
    digitalWrite(p,LOW);
    delayMicroseconds(d);
  }
}

