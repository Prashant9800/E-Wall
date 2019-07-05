#include <CapacitiveSensor.h>

/*
 * CapitiveSense Library Demo Sketch
 * Paul Badger 2008
 * Uses a high value resistor e.g. 10M between send pin and receive pin
 * Resistor effects sensitivity, experiment with values, 50K - 50M. Larger resistor values yield larger sensor values.
 * Receive pin is the sensor pin - try different amounts of foil/metal on this pin
 */
int arr[16][4] = {
  {0,0,0,0},
  {1,0,0,0},
  {0,1,0,0},
  {1,1,0,0},
  {0,0,1,0},
  {1,0,1,0},
  {0,1,1,0},
  {1,1,1,0},
  {0,0,0,1},
  {1,0,0,1},
  {0,1,0,1},
  {1,1,0,1},
  {0,0,1,1},
  {1,0,1,1},
  {0,1,1,1},
  {1,1,1,1}
  };


long cap[20];int total[20];int loops = 7;
int Average[20]={0};
int flag=0;
int current;
int start = millis();
CapacitiveSensor   cs_12_13 = CapacitiveSensor(13,12);        // 10M resistor between pins 4 & 2, pin 2 is sensor pin, add a wire and or foil if desired
CapacitiveSensor   cs_11_14 = CapacitiveSensor(11,14);        // 10M resistor between pins 4 & 6, pin 6 is sensor pin, add a wire and or foil
//CapacitiveSensor   cs_2_7 = CapacitiveSensor(2,7);        // 10M resistor between pins 4 & 8, pin 8 is sensor pin, add a wire and or foil
//CapacitiveSensor   cs_2_9 = CapacitiveSensor(2,9);
//CapacitiveSensor   cs_2_10 = CapacitiveSensor(2,10);
//CapacitiveSensor   cs_2_12 = CapacitiveSensor(2,12);
void setup()                    
{
   //cs_2_4.reset_CS_AutoCal(); // turn off autocalibrate on channel 1 - just as an example
   pinMode(2,OUTPUT);         // A
   pinMode(3,OUTPUT);  //B
   pinMode(4,OUTPUT); //C
   pinMode(5,OUTPUT);//D

   pinMode(6,OUTPUT);//A
   pinMode(7,OUTPUT);//B
   pinMode(8,OUTPUT);//C
   pinMode(9,OUTPUT);//D
    cs_12_13.set_CS_AutocaL_Millis(10000);
   Serial.begin(9600);
}

void loop()                    
{

   /* 
    for(int i = 0;i < 5 ;i++){
      digitalWrite(2,arr[i][0]);
      digitalWrite(3,arr[i][1]);
      digitalWrite(4,arr[i][2]);
      digitalWrite(5,arr[i][2]);

      digitalWrite(6,arr[i + 1][0]);
      digitalWrite(7,arr[i + 1][1]);
      digitalWrite(8,arr[i + 1][2]);
      digitalWrite(9,arr[i + 1][3]);      
      delay(5);
      cap[i] = cs_12_13.capacitiveSensor(5);
     
    }*/
    //Serial.print(millis() - start);        // check on performance in milliseconds
    //Serial.print("\t");                    // tab character for debug windown spacing
if(Serial.available()){
      char a=Serial.read();
      if(a=='a')
      flag=1;
     }
     if(flag==0){
      start=millis();
     //current =millis();
     while(current-start<600){
      current=millis();
     for(int i = 0;i < loops ;i++){
      digitalWrite(2,arr[i][0]);
      digitalWrite(3,arr[i][1]);
      digitalWrite(4,arr[i][2]);
      digitalWrite(5,arr[i][3]);

      digitalWrite(6,arr[i + 1][0]);
      digitalWrite(7,arr[i + 1][1]);
      digitalWrite(8,arr[i +1][2]);
      digitalWrite(9,arr[i + 1][3]);      
      delay(5);
      cap[i] = cs_12_13.capacitiveSensor(5);
     // Serial.print(cap[i]);
      //Serial.print("\t");
      //cs_12_13.set_CS_AutocaL_Millis(10000);     
    }
     Serial.println();
     }
     flag=1;
     }
     if(flag==1){
        
     for(int i = 0;i < loops ;i++){
      digitalWrite(2,arr[i][0]);
      digitalWrite(3,arr[i][1]);
      digitalWrite(4,arr[i][2]);
      digitalWrite(5,arr[i][3]);

      digitalWrite(6,arr[i + 1][0]);
      digitalWrite(7,arr[i + 1 ][1]);
      digitalWrite(8,arr[i + 1][2]);
      digitalWrite(9,arr[i + 1][3]);      
      delay(5);
      Average[i] = cs_12_13.capacitiveSensor(5);
      //cs_12_13.set_CS_AutocaL_Millis(10000);
     
    }//     for(int i=0;i<5;i++){
//      Average[i]/=10;
//      //Average[i]=0;
//     }
//     for(int i = 0;i < 5;i++){
//     Serial.print(Average[i]);
//     Serial.print("\t");
//     Serial.println();
//     }
     flag=2;
     }
     else{
     for(int i = 0;i < loops ;i++){
      digitalWrite(2,arr[i][0]);
      digitalWrite(3,arr[i][1]);
      digitalWrite(4,arr[i][2]);
      digitalWrite(5,arr[i][3]);

      digitalWrite(6,arr[i + 1][0]);
      digitalWrite(7,arr[i + 1][1]);
      digitalWrite(8,arr[i + 1][2]);
      digitalWrite(9,arr[i + 1][3]);      
      delay(5);
      cap[i] = cs_12_13.capacitiveSensor(5);
      
    }
     //Serial.println(start);
     //Serial.print("\t");// check on performance in milliseconds
                         // tab character for debug window spacing
for(int i = 0;i < loops;i++){
  Serial.print(cap[i]);
  Serial.print("\t");
  //Serial.print(Average[i]);
  //Serial.print("\t");
  //Serial.print(cap[i]- Average[i]);
  //Serial.print("\t");

}
    Serial.println();
                              // arbitrary delay to limit data to serial port 
}
}
