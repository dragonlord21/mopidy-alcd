import logging
import Adafruit_CharLCD_Mod as LCD
from Adafruit_LCD_plate import LCDplate


plate = LCDplate()
plate.start("Starting".center(16),"Mopidy LCD".center(16))
