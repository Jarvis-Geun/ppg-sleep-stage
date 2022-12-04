#define PIN 13   
#define NUMPIXELS 5             
#define BRIGHTNESS 180
#include <Adafruit_NeoPixel.h> 
#include <avr/power.h>
#include <TimerOne.h>   // PPG

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

// PPG
int analogPin0=0;
int analogPin1=1;
int analogPin2=2;
int analogPin3=3;

// LED
int PulseSensorPurplePin = 0;  
int LED13 = 13; 
int delayval = 0; 
 
int Signal;         
int Threshold = 400;      // 초기설정 임계값이 "500" (임계값은 조절하면 됨)
 
 
// The SetUp Function:
void setup() {
  pinMode(LED13, OUTPUT);      
  Serial.begin(9600);       
  
  Timer1.initialize(2000); //us단위로 설정
  Timer1.attachInterrupt(AnalogAD);
  Timer1.start();
}


void AnalogAD()
{  
  int reading0=analogRead(analogPin0);  
  int reading1=analogRead(analogPin1);  
  int reading2=analogRead(analogPin2);
  int reading3=analogRead(analogPin3);

  float Voltage0=(float)reading0/1023*5;
  float Voltage1=(float)reading1/1023*5;
  float Voltage2=(float)reading2/1023*5;
  float Voltage3=(float)reading3/1023*5;

  if (Voltage1>1.65) digitalWrite(13,HIGH);
  else digitalWrite(13,LOW);

  // String str=String(Voltage0,3) +","+ String(Voltage1,3)+","+ String(Voltage2,3)+","+ String(Voltage3,3);
  String str=String(Voltage0,5);

  Serial.println(str);
}


// The Main Loop Function
void loop() {
 
  Signal = analogRead(PulseSensorPurplePin);
                                             
 
  //  Serial.println(Signal);                    
 if(Serial.available()>0){
    char serialRead = Serial.read();

    if(serialRead == '0'){
      strip.clear();
      strip.show();
    }
    else if(serialRead == '1'){
       for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
         strip.setPixelColor(i, strip.Color(56, 34, 11)); // Moderately bright green color.

         strip.show(); // This sends the updated pixel color to the hardware.

         delay(delayval); // Delay for a period of time (in milliseconds).
      }
    }
    else if(serialRead == '2'){
       for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
         strip.setPixelColor(i, strip.Color(113,68,22)); // Moderately bright green color.

         strip.show(); // This sends the updated pixel color to the hardware.

         delay(delayval); // Delay for a period of time (in milliseconds).
      }
    }
    else if(serialRead == '3'){
       for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
         strip.setPixelColor(i, strip.Color(170,102,34)); // Moderately bright green color.

         strip.show(); // This sends the updated pixel color to the hardware.

         delay(delayval); // Delay for a period of time (in milliseconds).
      }
    }
  }
// 
//   if(Signal > 600){                          // "Signal"에서 보내주는 임계값이 "600"이 넘으면 LED가 켜짐.(임계값은 조절하면 됨)
//     digitalWrite(LED13,HIGH);
//     colorWipe(strip.Color(100,100,100));  
// delay(0.01);  // 0.2초씩 센서가 확인 (센서값은 조절하면 됨)
//   } 
//   if(Signal< 520){
//     digitalWrite(LED13,LOW);                // "Signal"에서 보내주는 임계값이 "520"보다 낮으면 LED가 꺼짐.(임계값은 조절하면 됨)
//     colorWipe(strip.Color(0,0,0)); 
// delay(0.02);   // 0.02초씩 센서가 확(센서값은 조절하면 됨)
//   }
 


 
 
}

//void colorWipe(uint32_t c){    
//
//for(uint16_t i=0; i<strip.numPixels(); i++){
//
//strip.setPixelColor(i,c);
//strip.show();
//delay(wait);

//   }

//}
