int chan = 1;
int val_2 = 0;
int val_3 = 0;
int val_4 = 0;
int old_val_2 = 0;
int old_val_3 = 0;
int old_val_4 = 0;

void setup(){
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
}
void loop(){
   val_2 = digitalRead(2); // 入力を読み取りvalに格納
   val_3 = digitalRead(3); // 入力を読み取りvalに格納
   val_4 = digitalRead(4); // 入力を読み取りvalに格納
  //変化があるかどうかチェック
  if((val_2 == HIGH) && (old_val_2 == LOW)) {
    Serial.println(1,DEC);
    delay(100);
  }
  if((val_3 == HIGH) && (old_val_3 == LOW)) {
    Serial.println(2,DEC);
    delay(100);
  }
  if((val_4 == HIGH) && (old_val_4 == LOW)) {
    Serial.println(3,DEC);
    delay(100);
  }
  old_val_2 = val_2;  // valはもう古くなったので保管しておく
  old_val_3 = val_3;  // valはもう古くなったので保管しておく
  old_val_4 = val_4;  // valはもう古くなったので保管しておく
}