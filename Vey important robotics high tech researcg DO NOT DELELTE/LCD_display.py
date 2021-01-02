import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import time

lcd_columns = 16

lcd_rows = 2

i2c = busio.I2C(board.SCL, board.SDA)

lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = [50, 50, 50]

def Ijustmetyou():
    lcd.clear()
    lcd.message = 'Hey, I just met\nyou'
    time.sleep(1.78)
    lcd.clear()
    lcd.message = 'and this is\ncrazy'
    time.sleep(1.93)
    lcd.clear()
    lcd.message = "But here's my\nnumber"
    time.sleep(1.67)
    lcd.clear()
    lcd.message = 'so call me maybe'
    time.sleep(1.59)
    lcd.clear()
    lcd.message = "It's hard to\nlook right"
    time.sleep(1.36)
    lcd.clear()
    lcd.message = 'at you, baby'
    time.sleep(1.35)
    lcd.clear()
    lcd.message = "But here's my\nnumber"
    time.sleep(1.25)
    lcd.clear()
    lcd.message = 'so call me maybe'
    time.sleep(1.23)
    lcd.clear()
    lcd.message = 'Hey, I just met\nyou'
    time.sleep(1.45)
    lcd.clear()
    lcd.message = 'and this is\ncrazy'
    time.sleep(1.12)
    lcd.clear()
    lcd.message = "But here's my\nnumber"
    time.sleep(1.16)
    lcd.clear()
    lcd.message = 'so call me maybe'
    time.sleep(1.67)
    lcd.clear()
    lcd.message = 'And all the\nother boys'
    time.sleep(1.76)
    lcd.clear()
    lcd.message = 'Try to chase me'
    time.sleep(1.40)
    lcd.clear()
    lcd.message = "But here's my\nnumber"
    time.sleep(1.51)
    lcd.clear()
    lcd.message = 'so call me maybe'
    time.sleep(5)
    lcd.clear()

