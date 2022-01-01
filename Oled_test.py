import board
import busio
import adafruit_ssd1306
# Oled參數
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for I2C.
''' 
輸入指令：i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --          '''
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# 清空螢幕
oled.fill(0)
oled.show()

# Hello world
# (text,x,y,color)
oled.text('Hello', 0, 5, 1)
oled.text('World', 0, 15, 1)
oled.show()
print(board.board_id)