#include <LiquidCrystal.h>

int x = 0;
int currx = 1023;
String btnStr = "None";
 
LiquidCrystal lcd( 8 , 9 , 4 , 5 , 6 , 7 );

void setup() {
  
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);

  lcd.clear();
  
  lcd.setCursor(0,0);
  lcd.print("Analog 0: ");
  lcd.print(currx);
  lcd.setCursor(0,1);
  lcd.print(btnStr);

  
  // Print a message to the LCD.
  //lcd.print("Sarah Loves");
  //lcd.setCursor(0,1); // move to the begining of the second line
  //lcd.print("Big Black Cock");
}
 
void loop() {
  
  
  x = analogRead(A0);
  
  // check if x has changed
  if ( ( x != 1023 ) && ( x != currx ) ) {

    // Update Screen And Change Currx
    lcd.setCursor( 10 , 0 );
    lcd.print("     ");
    lcd.setCursor( 10 , 0 );
    lcd.print(x);
    currx = x;

    if ( currx > 740 && currx < 745 ) {
      btnStr = "Select"; 
    }
    else if ( currx > 500 && currx < 510 ) {
      btnStr = "Left";
    }
    else if ( currx < 10 ) {
      btnStr = "Right";
    }
    else if ( currx > 140 && currx < 150 ) {
      btnStr = "Up";
    }
    else if ( currx > 320 && currx < 365 ) {
      btnStr = "Down";
    }

    // update button pressed
    lcd.setCursor( 0 , 1 );
    lcd.print("     ");
    lcd.setCursor( 0 , 1 );
    lcd.print( btnStr );  
      
  }
  
  
  // Turn off the display:
  //lcd.noDisplay();
  //delay(500);
  //Turn on the display:
  //lcd.display();
  //delay(1500);
}
