#include <CapacitiveSensor.h>
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
 
long capX[7],capY[7];

CapacitiveSensor   cs_12_13 = CapacitiveSensor(13,12);        
CapacitiveSensor   cs_11_10 = CapacitiveSensor(14,11);
void setup() {
   pinMode(2,OUTPUT);         // A
   pinMode(3,OUTPUT);  //B
   pinMode(4,OUTPUT); //C
   pinMode(5,OUTPUT);//D

//   pinMode(6,OUTPUT);//A
//   pinMode(7,OUTPUT);//B
//   pinMode(8,OUTPUT);//C
//   pinMode(9,OUTPUT);//D
//
   pinMode(22,OUTPUT);// A
   pinMode(23,OUTPUT);//B
   pinMode(24,OUTPUT);//C
   pinMode(25,OUTPUT);//D

//   pinMode(30,OUTPUT);//A
//   pinMode(31,OUTPUT);//B
//   pinMode(32,OUTPUT);//C
//   pinMode(33,OUTPUT);//D
   // cs_12_13.set_CS_AutocaL_Millis(1000);
   // cs_11_10.set_CS_AutocaL_Millis(1000);
   Serial.begin(9600);  

}

void loop() {
  for(int i = 1;i < 7 ;i++){   
      digitalWrite(5,arr[i][0]);
      digitalWrite(4,arr[i][1]);
      digitalWrite(3,arr[i][2]);
      digitalWrite(2,arr[i][3]);
      
      digitalWrite(22,arr[i + 1][0]);
      digitalWrite(23,arr[i + 1][1]);
      digitalWrite(24,arr[i + 1][2]);
      digitalWrite(25,arr[i + 1][3]);

      capX[i] = cs_12_13.capacitiveSensor(2);
//      digitalWrite(30,arr[i + 1 ][0]);
//      digitalWrite(31,arr[i + 1][1]);
//      digitalWrite(32,arr[i + 1][2]);
//      digitalWrite(33,arr[i + 1][3]);
    
  }
  for(int i = 1;i < 8 ;i++){   
      digitalWrite(5,arr[i][0]);
      digitalWrite(4,arr[i][1]);
      digitalWrite(3,arr[i][2]);
      digitalWrite(2,arr[i][3]);
      
      capY[i] = cs_11_10.capacitiveSensor(2);
     }

  for(int i = 1;i < 7;i++){
  Serial.print(capX[i]);
  Serial.print("\t");

  }
  for(int i = 1;i < 8;i++){
  Serial.print(capY[i]);
  Serial.print("\t");


}
    Serial.println();
delay(50);
}
