int chan = 1;
void setup(){
  Serial.begin(9600);
}
void loop(){
  Serial.println(chan,DEC);
  delay(5000);
  if(chan==12){
    chan=1;
  }else{
    chan++;
  }
  }
