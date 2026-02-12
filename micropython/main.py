###################
# A I - A N N E ###
###################

import time, utime, array, math
from machine import Pin, SPI, PWM
import framebuf
import rp2

####################### Basic Setup #######################

# WS2812 / RGB Matrix Parameter
NUM_LEDS = 160
PIN_NUM = 6
BRIGHTNESS = 0.05

# LCD PINs
BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

# LCD Colours
LCD_BLUE  = 0x1F00
LCD_WHITE = 0xFFFF
LCD_BLACK = 0x0000

####################### Buttons Setup #######################

KEY_CTRL = Pin(3, Pin.IN, Pin.PULL_UP)
KEY_A    = Pin(15, Pin.IN, Pin.PULL_UP)
KEY_B    = Pin(17, Pin.IN, Pin.PULL_UP)

def wait_release(pin, delay_ms=25):
    utime.sleep_ms(delay_ms)
    while pin.value() == 0:
        utime.sleep_ms(10)
    utime.sleep_ms(delay_ms)

def pressed(pin):
    return pin.value() == 0

####################### LCD Setup #######################

class LCD_1inch14(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 240
        self.height = 135

        self.cs = Pin(CS, Pin.OUT)
        self.rst = Pin(RST, Pin.OUT)

        self.cs(1)
        self.spi = SPI(1, 10_000_000, polarity=0, phase=0, sck=Pin(SCK), mosi=Pin(MOSI), miso=None)
        self.dc = Pin(DC, Pin.OUT)
        self.dc(1)

        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()

    def write_cmd(self, cmd):
        self.cs(1); self.dc(0); self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1); self.dc(1); self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        self.rst(1); self.rst(0); self.rst(1)

        self.write_cmd(0x36); self.write_data(0x70)
        self.write_cmd(0x3A); self.write_data(0x05)

        self.write_cmd(0xB2)
        for v in (0x0C,0x0C,0x00,0x33,0x33): self.write_data(v)

        self.write_cmd(0xB7); self.write_data(0x35)
        self.write_cmd(0xBB); self.write_data(0x19)
        self.write_cmd(0xC0); self.write_data(0x2C)
        self.write_cmd(0xC2); self.write_data(0x01)
        self.write_cmd(0xC3); self.write_data(0x12)
        self.write_cmd(0xC4); self.write_data(0x20)
        self.write_cmd(0xC6); self.write_data(0x0F)

        self.write_cmd(0xD0)
        self.write_data(0xA4); self.write_data(0xA1)

        self.write_cmd(0xE0)
        for v in (0xD0,0x04,0x0D,0x11,0x13,0x2B,0x3F,0x54,0x4C,0x18,0x0D,0x0B,0x1F,0x23): self.write_data(v)

        self.write_cmd(0xE1)
        for v in (0xD0,0x04,0x0C,0x11,0x13,0x2C,0x3F,0x44,0x51,0x2F,0x1F,0x1F,0x20,0x23): self.write_data(v)

        self.write_cmd(0x21)
        self.write_cmd(0x11)
        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00); self.write_data(0x28)
        self.write_data(0x01); self.write_data(0x17)

        self.write_cmd(0x2B)
        self.write_data(0x00); self.write_data(0x35)
        self.write_data(0x00); self.write_data(0xBB)

        self.write_cmd(0x2C)

        self.cs(1); self.dc(1); self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)

####################### RGB Matrix Setup #######################

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT,
             autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0) [T3 - 1]
    jmp(not_x, "do_zero")   .side(1) [T1 - 1]
    jmp("bitloop")          .side(1) [T2 - 1]
    label("do_zero")
    nop()                   .side(0) [T2 - 1]
    wrap()

sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
sm.active(1)

pixels = array.array("I", [0] * NUM_LEDS)

def rgb(r, g, b):
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return (g << 16) | (r << 8) | b

def pixels_show():
    sm.put(pixels, 8)
    utime.sleep_us(50)

def pixels_fill(col):
    for i in range(NUM_LEDS):
        pixels[i] = col

def pixels_set(i, col):
    if 0 <= i < NUM_LEDS:
        pixels[i] = col

def xy_set(x, y, col):
    if 0 <= x < 16 and 0 <= y < 10:
        x_rot = 15 - x
        y_rot = 9 - y
        pos = x_rot + y_rot * 16
        pixels_set(pos, col)

####################### 3x5 Font #######################

FONT_3x5 = {
    "0": [0b111, 0b101, 0b101, 0b101, 0b111],
    "1": [0b010, 0b110, 0b010, 0b010, 0b111],
    "2": [0b111, 0b001, 0b111, 0b100, 0b111],
    "3": [0b111, 0b001, 0b111, 0b001, 0b111],
    "4": [0b101, 0b101, 0b111, 0b001, 0b001],
    "5": [0b111, 0b100, 0b111, 0b001, 0b111],
    "6": [0b111, 0b100, 0b111, 0b101, 0b111],
    "7": [0b111, 0b001, 0b001, 0b001, 0b001],
    "8": [0b111, 0b101, 0b111, 0b101, 0b111],
    "9": [0b111, 0b101, 0b111, 0b001, 0b111],
}

CHAR_W = 3
CHAR_H = 5

NUMBER_COLOR  = rgb(0, 0, 255)
CURSOR_COLOR  = rgb(0, 255, 0)
BG_COLOR      = rgb(0, 0, 0)
DECIMAL_COLOR = rgb(255, 255, 255)

def draw_char(x0, y0, ch, col):
    glyph = FONT_3x5.get(ch)
    if glyph is None:
        return
    for y in range(CHAR_H):
        row = glyph[y]
        for x in range(CHAR_W):
            if row & (1 << (CHAR_W - 1 - x)):
                xy_set(x0 + x, y0 + y, col)

def draw_decimal_point(x, y0):
    # 1 Pixel unten als Dezimalpunkt
    xy_set(x, y0 + CHAR_H - 1, DECIMAL_COLOR)

def draw_page_4digits_layout(d4, cursor_index=None, animator=None):
    """
    d4: Liste aus 4 Ziffern [a,b,c,d]
    Layout (16 Spalten):
    a(0-2) .(3) b(4-6) __(7-8) c(9-11) .(12) d(13-15)
    """
    y0 = (10 - CHAR_H) // 2  # vertikal zentriert
    pixels_fill(BG_COLOR)

    # feste X-Positionen
    x_a = 0
    x_dot1 = 3
    x_b = 4
    x_c = 9
    x_dot2 = 12
    x_d = 13

    # a
    col = CURSOR_COLOR if (cursor_index == 0) else NUMBER_COLOR
    draw_char(x_a, y0, str(d4[0]), col)

    # .
    draw_decimal_point(x_dot1, y0)

    # b
    col = CURSOR_COLOR if (cursor_index == 1) else NUMBER_COLOR
    draw_char(x_b, y0, str(d4[1]), col)

    # (Leer Leer) sind automatisch, weil Background schwarz bleibt

    # c
    col = CURSOR_COLOR if (cursor_index == 2) else NUMBER_COLOR
    draw_char(x_c, y0, str(d4[2]), col)

    # .
    draw_decimal_point(x_dot2, y0)

    # d
    col = CURSOR_COLOR if (cursor_index == 3) else NUMBER_COLOR
    draw_char(x_d, y0, str(d4[3]), col)

    if animator is not None:
        animator.tick()

    pixels_show()

####################### Bar Animation #######################

ROW_LENGTH = 16

class RowChaseAnimator:
    def __init__(self, row=1, color=None, delay_ms=150):
        self.row = row
        self.color = color if color is not None else rgb(255, 255, 255)
        self.delay_ms = delay_ms
        self.pos = 0
        self.last_ms = utime.ticks_ms()

    def _row_start(self):
        return self.row * ROW_LENGTH

    def clear_row(self):
        start = self._row_start()
        for i in range(start, start + ROW_LENGTH):
            pixels[i] = BG_COLOR

    def draw(self):
        start = self._row_start()
        pixels[start + self.pos] = self.color

    def tick(self):
        now = utime.ticks_ms()
        if utime.ticks_diff(now, self.last_ms) >= self.delay_ms:
            self.last_ms = now
            self.pos = (self.pos - 1) % ROW_LENGTH

        self.clear_row()
        self.draw()

def input_four_numbers_one_decimal(animator=None):
    digits = [0] * 8

    page = 0
    idx = 0
    
    def redraw():
        start = page * 4
        d4 = digits[start:start+4]
        draw_page_4digits_layout(d4, cursor_index=idx, animator=animator)

    redraw()

    while True:
        if pressed(KEY_A):
            g = page * 4 + idx
            digits[g] = (digits[g] + 1) % 10
            redraw()
            wait_release(KEY_A)

        elif pressed(KEY_B):
            g = page * 4 + idx
            digits[g] = (digits[g] - 1) % 10
            redraw()
            wait_release(KEY_B)

        elif pressed(KEY_CTRL):
            wait_release(KEY_CTRL)
            idx += 1
            if idx >= 4:
                # Seite abgeschlossen -> nächste Seite oder fertig
                idx = 0
                page += 1
                if page >= 2:
                    return digits
            redraw()

        if animator is not None:
            animator.tick()
            pixels_show()

        utime.sleep_ms(10)

####################### Neural Network #######################

# Activation Functions
def sigmoid(z):
    if z >= 0:
        ez = math.exp(-z)
        return 1 / (1 + ez)
    else:
        ez = math.exp(z)
        return ez / (1 + ez)

def relu(z):
    return max(0, z)

def leaky_relu(z):
    return z if z > 0 else 0.01 * z

def tanh(z):
    return math.tanh(z)

def activate(z, func):
    if func == 'sigmoid':
        return sigmoid(z)
    elif func == 'relu':
        return relu(z)
    elif func == 'leaky_relu':
        return leaky_relu(z)
    elif func == 'tanh':
        return tanh(z)
    else:
        return z

# Neural Network Basics
def dense(n_neurons, input_vector, weights, biases, activation):
    output = []
    for j in range(n_neurons):
        z = 0
        for i in range(len(input_vector)):
            z += weights[j][i] * input_vector[i]
        z += biases[j]
        a = activate(z, activation)
        output.append(a)
    return output

####################### Start #######################

if __name__ == '__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)

    LCD = LCD_1inch14()
    LCD.rect(0, 0, 240, 135, LCD_BLUE)
    LCD.text("----- A I - A N N E -----", 21, 20, LCD_WHITE)
    LCD.text("Button A:", 20, 45, LCD_BLUE)
    LCD.text("DATA (+)", 100, 45, LCD_WHITE)
    LCD.text("Button B:", 20, 65, LCD_BLUE)
    LCD.text("DATA (-)", 100, 65, LCD_WHITE)
    LCD.text("Black Button:", 20, 85, LCD_BLUE)
    LCD.text("SET", 131, 85, LCD_WHITE)
    LCD.text("-------------------------", 20, 110, LCD_WHITE)
    LCD.show()

    led = Pin(25, Pin.OUT)
    led.value(0)

    chase = RowChaseAnimator(row=1, color=rgb(255, 255, 255), delay_ms=150)

    while True:
        digits = input_four_numbers_one_decimal(animator=chase)

        x = []
        for i in range(0, 8, 2):
            x.append(digits[i] + digits[i+1] / 10.0)
            
        x_original = x[:]
        print(x_original)

        ##################################################
        ### START: COPY & PASTE OF EXPORTED PARAMETERS ###
        ##################################################

        # Normalization Parameters
        X_MINS = [4.9, 2.0, 3.0, 1.0]
        X_MAXS = [7.9, 3.8, 6.9, 2.5]
        
        ################################################
        ### END: COPY & PASTE OF EXPORTED PARAMETERS ###
        ################################################
        
        EPS = 1e-9
        
        x = [(x[i] - X_MINS[i]) / (X_MAXS[i] - X_MINS[i] + EPS) for i in range(4)]

        ##################################################
        ### START: COPY & PASTE OF EXPORTED PARAMETERS ###
        ##################################################

        # Weights and Biases
        w1 = [[2.0318275159327572,2.1949451951583794,-4.302246268496513,-2.598382621956279],
              [-0.5559216400008825,0.2666561996915462,1.082518497691295,1.0136473449244923],
              [-0.6175798949412958,-0.10454799530402879,-0.054962799172132495,0.1987922857641155],
              [-1.007375608620601,-0.4231575581157903,6.464799480004846,4.215511964957278]]
        b1 = [4.036820213151002,-0.23209355962716968,0.18527410662307447,-1.100843389757179]
        w2 = [[-3.201738501457912,0.7683954027706076,0.44142317549186416,4.328985233516645],
              [2.769779929038592,-0.5009713800557559,-0.3435411703767652,-2.151276169076909]]
        b2 = [-0.8985959523593179,0.7390613653344147]
        w3 = [[7.212246846148128,-4.609981923525531]]
        b3 = [-1.4399910457235603]

        # Neural Network Architecture
        l_out = dense(4, x, w1, b1, 'leaky_relu')
        l_out = dense(2, l_out, w2, b2, 'sigmoid')
        l_out = dense(1, l_out, w3, b3, 'sigmoid')
        print(l_out)

        ################################################
        ### END: COPY & PASTE OF EXPORTED PARAMETERS ###
        ################################################

        pred_prob = l_out[0]
        pred_class = 1 if pred_prob >= 0.5 else 0

        led.value(pred_class)

        # LCD Classification Report
        LCD.fill(LCD_BLACK)
        LCD.rect(0, 0, 240, 135, LCD_BLUE)
        LCD.text("-- P R E D I C T I O N --", 21, 20, LCD_WHITE)

        LCD.text("Input:", 20, 45, LCD_BLUE)
        LCD.text("%.1f %.1f %.1f %.1f" % (x_original[0], x_original[1], x_original[2], x_original[3]), 75, 45, LCD_WHITE)

        LCD.text("Value:", 20, 65, LCD_BLUE)
        LCD.text("%0.2f" % pred_prob, 75, 65, LCD_WHITE)

        LCD.text("Class:", 20, 85, LCD_BLUE)
        LCD.text("%d" % pred_class, 75, 85, LCD_WHITE)
        
        LCD.text("-------------------------", 20, 110, LCD_WHITE)

        LCD.show()

        chase.tick()
        pixels_show()
        utime.sleep_ms(10)
