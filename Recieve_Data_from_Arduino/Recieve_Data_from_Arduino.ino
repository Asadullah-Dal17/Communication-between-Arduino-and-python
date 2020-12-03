// defining the pin of Light dependent Resistor
int LDR_PIN= A0;

// variable
int LDR_Value ;
void setup(){

  Serial.begin(9600);

}
void loop(){
LDR_Value=analogRead(LDR_PIN);
Serial.println(LDR_Value);
}
