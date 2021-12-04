#include <cvzone.h>

SerialData serialData(2,1);
int valsRec[2];

void setup() {
  // put your setup code here, to run once:
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  serialData.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valsRec);

  digitalWrite(12, valsRec[0]);
  digitalWrite(11, valsRec[1]);
}
