import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcd_columns = 16

lcd_rows = 2

i2c = busio.I2C(board.SCL, board.SDA)

lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = [50, 50, 50]



lcd.clear()

lcd.message = 'asdasdaidhsiuhqufqiufgfuyqgfqouydgqodygqduyqgduyqgduyqgdqouygdyqsgdougogqudyw'

while True:

        