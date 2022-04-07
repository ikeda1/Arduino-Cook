#define botao1 6
#define botao2 7
#define botao3 8
#define botao4 9

int K_d;
int K_a;
int K_w;
int K_s;

unsigned long previousMillis_idle = 0;
unsigned long previousMillis_botao1 = 0;
unsigned long previousMillis_botao2 = 0;
unsigned long previousMillis_botao3 = 0;
unsigned long previousMillis_botao4 = 0;
unsigned long previousMillis_nw = 0;
unsigned long previousMillis_ne = 0;
unsigned long previousMillis_sw = 0;
unsigned long previousMillis_se = 0;


int intervalo = 70;
int tempo = 0;

void setup() 
{
  Serial.begin(115200);
  pinMode(botao1, INPUT);
  pinMode(botao2, INPUT);
  pinMode(botao3, INPUT);
  pinMode(botao4, INPUT);
}

void loop() 
{
  K_d = digitalRead(botao1);
  K_a = digitalRead(botao2);
  K_w = digitalRead(botao3);
  K_s = digitalRead(botao4);
  
  if (K_d == HIGH)
  {
    delay(tempo);
    unsigned long currentMillis_botao1 = millis();
    if ((unsigned long)(currentMillis_botao1 - previousMillis_botao1) >= intervalo)
    {
      previousMillis_botao1 = millis();
      Serial.println("DIR");
    }
  }

  else if (K_a == HIGH)
  {
    delay(tempo);
    unsigned long currentMillis_botao2 = millis();
    if ((unsigned long)(currentMillis_botao2 - previousMillis_botao2) >= intervalo)
    {
      previousMillis_botao2 = millis();
      Serial.println("ESQ");
    }
  }

  else if (K_w == HIGH)
  {
    delay(tempo);
    unsigned long currentMillis_botao3 = millis();
    if ((unsigned long)(currentMillis_botao3 - previousMillis_botao3) >= intervalo)
    {
      previousMillis_botao3 = millis();
      Serial.println("CIM");
    }
  }

  else if (K_s == HIGH)
  {
    delay(tempo);
    unsigned long currentMillis_botao4 = millis();
    if ((unsigned long)(currentMillis_botao4 - previousMillis_botao4) >= intervalo)
    {
      previousMillis_botao4 = millis();
      Serial.println("BAI");
    }
  }
  else
  {
    unsigned long currentMillis_idle = millis();
    if ((unsigned long)(currentMillis_idle - previousMillis_idle) >= intervalo)
    {
      previousMillis_idle = millis();
      Serial.println("lll");
    }  
  }

}
