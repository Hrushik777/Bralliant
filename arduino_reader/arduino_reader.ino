#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); 

const int ledPins[] = {2, 3, 4, 5, 6, 7};

void setup() {
    for (int i = 0; i < 6; i++) {
        pinMode(ledPins[i], OUTPUT);
    }
    lcd.begin(16, 2); 
    lcd.backlight();  
    Serial.begin(9600); 
}

void loop() {
    if (Serial.available()) {
        String text = Serial.readStringUntil('|'); 
        String braille = Serial.readStringUntil('\n');

        lcd.clear();    
        lcd.setCursor(0, 0); 
        lcd.print(text);

        for (int i = 0; i < braille.length(); i += 6) {

                lcd.setCursor(0,1);
                lcd.print("Current: ");
                lcd.print(text[i/6]);

                for (int j = 0; j < 6; j++) {
                    if (braille[i + j] == '1') digitalWrite(ledPins[j], HIGH);   
                    else digitalWrite(ledPins[j], LOW); 
                }

                delay(3000); 
        }

      lcd.clear();

    }
}

