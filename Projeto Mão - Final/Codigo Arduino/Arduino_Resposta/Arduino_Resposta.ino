const int Motor_1_ida = 2;    //Indicador
const int Motor_1_volta = 3;  //Indicador
const int Motor_2_ida = 4;    //Medio
const int Motor_2_volta = 5;  //Medio
const int Motor_3_ida = 6;    //Anelar
const int Motor_3_volta = 8;  //Anelar
const int Motor_4_ida = 9;    //Minimo
const int Motor_4_volta = 10; //Minimo
const int Motor_5_ida = 11;   //Dedao
const int Motor_5_volta = 12; //Dedao

void setup() 
{
  Serial.begin(9600);
  pinMode(Motor_1_ida, OUTPUT);
  pinMode(Motor_1_volta, OUTPUT);
  pinMode(Motor_2_ida, OUTPUT);
  pinMode(Motor_2_volta, OUTPUT);
  pinMode(Motor_3_ida, OUTPUT);
  pinMode(Motor_3_volta, OUTPUT);
  pinMode(Motor_4_ida, OUTPUT);
  pinMode(Motor_4_volta, OUTPUT);
  pinMode(Motor_5_ida, OUTPUT);
  pinMode(Motor_5_volta, OUTPUT);
}

// Ajustar o tempo conforme necessário

void dedao_ida()
{
  digitalWrite(Motor_5_ida, HIGH);
  delay(1600);
  digitalWrite(Motor_5_ida, LOW);
}
void dedao_volta()
{
  digitalWrite(Motor_5_volta, HIGH);
  delay(1300);
  digitalWrite(Motor_5_volta, LOW); 
}
void indicador_ida()
{
  digitalWrite(Motor_1_ida, HIGH);
  delay(3200);
  digitalWrite(Motor_1_ida, LOW);
}
void indicador_volta()
{
  digitalWrite(Motor_1_volta, HIGH);
  delay(2150);
  digitalWrite(Motor_1_volta, LOW);
}
void medio_ida()
{
  digitalWrite(Motor_2_ida, HIGH);
  delay(2200);
  digitalWrite(Motor_2_ida, LOW);
}
void medio_volta()
{
  digitalWrite(Motor_2_volta, HIGH);
  delay(1700);
  digitalWrite(Motor_2_volta, LOW); 
}
void anelar_ida()
{
  digitalWrite(Motor_3_ida, HIGH);
  delay(2000);
  digitalWrite(Motor_3_ida, LOW);
}
void anelar_volta()
{
  digitalWrite(Motor_3_volta, HIGH);
  delay(1600);
  digitalWrite(Motor_3_volta, LOW); 
}
void minimo_ida()
{
  digitalWrite(Motor_4_ida, HIGH);
  delay(1800);
  digitalWrite(Motor_4_ida, LOW);
}
void minimo_volta()
{
  digitalWrite(Motor_4_volta, HIGH);
  delay(1500);
  digitalWrite(Motor_4_volta, LOW); 
}

///////////////////////////////////////////////////////////////////////////////

void dedao_abaixado()//2
{
  dedao_ida();
  delay (5000);
  dedao_volta();
}
void indicador_abaixado()//3
{
  indicador_ida();
  delay (5000);
  indicador_volta();
}
void medio_abaixado()//4
{
  medio_ida();
  delay (5000);
  medio_volta();
}
void anelar_abaixado()//5
{
  anelar_ida();
  delay (5000);
  anelar_volta();
}
void minimo_abaixado()//6
{
  minimo_ida();
  delay (5000);
  minimo_volta();
}
void tres_medio_anelar_minimo() //7
{
  dedao_ida();
  indicador_ida();
  delay (5000);
  indicador_volta();
  dedao_volta();
}
void tres_indicador_medio_anelar() //8
{
  dedao_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  dedao_volta();
}
void tres_indicador_medio_minimo() //9
{
  dedao_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  dedao_volta();
}
void tres_indicador_anelar_minimo() //10
{
  dedao_ida();
  medio_ida();
  delay (5000);
  medio_volta();
  dedao_volta();
}
void tres_dedao_anelar_minimo() //11
{
  indicador_ida();
  medio_ida();
  delay (5000);
  medio_volta();
  indicador_volta();
}
void tres_dedao_medio_minimo() //12
{
  indicador_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  indicador_volta();
}
void tres_dedao_medio_anelar() //13
{
  indicador_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  indicador_volta();
}
void tres_dedao_indicador_minimo() //14
{
  medio_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  medio_volta();
}
void tres_dedao_indicador_anelar() //15
{
  medio_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  medio_volta();
}
void tres_dedao_indicador_medio() //16
{
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
}
void dois_anelar_minimo() //17
{
  dedao_ida();
  indicador_ida();
  medio_ida();
  delay (5000);
  medio_volta();
  indicador_volta();
  dedao_volta();
}
void dois_indicador_medio() //18
{
  dedao_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  dedao_volta();
}
void dois_medio_minimo() //19
{
  dedao_ida();
  indicador_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  indicador_volta();
  dedao_volta();
}
void dois_medio_anelar() //20
{
  dedao_ida();
  indicador_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  indicador_volta();
  dedao_volta();
}
void dois_indicador_minimo() //21
{
  dedao_ida();
  medio_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  medio_volta();
  dedao_volta();
}
void dois_dedao_minimo() //22
{
  indicador_ida();
  medio_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  medio_volta();
  indicador_volta();
}
void dois_dedao_medio() //23
{
  indicador_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  indicador_volta();
}
void dois_dedao_anelar() //24
{
  indicador_ida();
  medio_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  medio_volta();
  indicador_volta();
}
void dois_dedao_indicador() //25
{
  medio_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  medio_volta();
}
void dedao_levantado() //26
{
  indicador_ida();
  medio_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  medio_volta();
  indicador_volta();
}
void indicador_levantado() //27
{
  dedao_ida();
  medio_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  medio_volta();
  dedao_volta();
}
void medio_levantado() //28
{
  dedao_ida();
  indicador_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  indicador_volta();
  dedao_volta();
}
void anelar_levantado() //29
{
  dedao_ida();
  indicador_ida();
  medio_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  medio_volta();
  indicador_volta();
  dedao_volta();
}
void minimo_levantado() //30
{
  dedao_ida();
  indicador_ida();
  medio_ida();
  anelar_ida();
  delay (5000);
  anelar_volta();
  medio_volta();
  indicador_volta();
  dedao_volta();
}
void mao_fechada()//31
{
  dedao_ida();
  indicador_ida();
  medio_ida();
  anelar_ida();
  minimo_ida();
  delay (5000);
  minimo_volta();
  anelar_volta();
  medio_volta();
  indicador_volta();
  dedao_volta();
}
void loop() 
{
  if (Serial.available() > 0) 
  {
    int numero_recebido = Serial.parseInt();

    switch(numero_recebido)
    {
      case 2:

        dedao_abaixado();
        break;

      case 3:

        indicador_abaixado();
        break;

      case 4:

        medio_abaixado();
        break;

      case 5:

        anelar_abaixado();
        break;

      case 6:

        minimo_abaixado();
        break;

      case 7:

        tres_medio_anelar_minimo();
        break;

      case 8:

        tres_indicador_medio_anelar();
        break;

      case 9:

        tres_indicador_medio_minimo();
        break;

      case 10:

        tres_indicador_anelar_minimo();
        break;

      case 11:

        tres_dedao_anelar_minimo();
        break;

      case 12:

        tres_dedao_medio_minimo();
        break;

      case 13:

        tres_dedao_medio_anelar();
        break;

      case 14:

        tres_dedao_indicador_minimo();
        break;

      case 15:

        tres_dedao_indicador_anelar();
        break;

      case 16:

        tres_dedao_indicador_medio();
        break;

      case 17:

        dois_anelar_minimo();
        break;

      case 18:

        dois_indicador_medio();
        break;

      case 19:

        dois_medio_minimo();
        break;

      case 20:

        dois_medio_anelar();
        break;

      case 21:

        dois_indicador_minimo();
        break;

      case 22:

        dois_dedao_minimo();
        break;

      case 23:

        dois_dedao_medio();
        break;

      case 24:

        dois_dedao_anelar();
        break;

      case 25:

        dois_dedao_indicador();
        break;

      case 26:

        dedao_levantado();
        break;

      case 27:

        indicador_levantado();
        break;

      case 28:

        medio_levantado();
        break;

      case 29:

        anelar_levantado();
        break;

      case 30:

        minimo_levantado();
        break;

      case 31:

        mao_fechada();
        break;

      default:

        break;
    }

    Serial.println(numero_recebido);

  }
}