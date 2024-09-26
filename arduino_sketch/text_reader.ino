#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); 

void setup() {
    lcd.begin(16, 2); 
    lcd.backlight();  
    Serial.begin(9600); 
}

void loop() {
    if (Serial.available()) {
        String text = Serial.readStringUntil('\n'); 
        lcd.clear();    
        lcd.setCursor(0, 0); 
        lcd.print(text); 
    }
}

