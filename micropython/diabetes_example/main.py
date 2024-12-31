###################
# K I - E N N A ###
###################

from machine import Pin,SPI,PWM
import array, utime
import framebuf
import math
import rp2

####################### Basic Setup ##############################

# RGB Matrix Parameter
NUM_LEDS = 160
PIN_NUM = 6
brightness = 0.015

# LCD PINs
BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

# Colours
BLUE = 0x1F00
WHITE = 0xFFFF
BLACK = 0x0000

# RGB Matrix Basics
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
sm.active(1)

# Display a pattern on the LEDs
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

####################### Functions ##############################

def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    utime.sleep_ms(10)

def pixels_set(i, colour):
    ar[i] = (colour[1]<<16) + (colour[0]<<8) + colour[2]

def clear():
    colour = (0,0,0)
    pixels_fill(colour)

def rgb_neural_net():
    # Input Layer
    for i in range(126,125,-1):
        pixels_set(i,(0,0,255))
    for i in range(125,124,-1):
        pixels_set(i,(0,0,255))
    for i in range(110,109,-1):
        pixels_set(i,(0,0,255))
    for i in range(109,108,-1):
        pixels_set(i,(0,0,255))

    for i in range(62,61,-1):
        pixels_set(i,(0,0,255))
    for i in range(61,60,-1):
        pixels_set(i,(0,0,255))
    for i in range(46,45,-1):
        pixels_set(i,(0,0,255))
    for i in range(45,44,-1):
        pixels_set(i,(0,0,255))
        
        utime.sleep(1)
        pixels_show()
        
    # Input Layer Network
    for i in range(108,107,-1):
        pixels_set(i,(255,255,255))
    for i in range(123,122,-1):
        pixels_set(i,(255,255,255))
    for i in range(91,90,-1):
        pixels_set(i,(255,255,255))

    for i in range(60,59,-1):
        pixels_set(i,(255,255,255))
    for i in range(75,74,-1):
        pixels_set(i,(255,255,255))
    for i in range(43,42,-1):
        pixels_set(i,(255,255,255))

    # Hidden Layer 1
    for i in range(138,137,-1):
        pixels_set(i,(0,0,255))
    for i in range(137,136,-1):
        pixels_set(i,(0,0,255))
    for i in range(122,121,-1):
        pixels_set(i,(0,0,255))
    for i in range(121,120,-1):
        pixels_set(i,(0,0,255))

    for i in range(90,89,-1):
        pixels_set(i,(0,0,255))
    for i in range(89,88,-1):
        pixels_set(i,(0,0,255))
    for i in range(74,73,-1):
        pixels_set(i,(0,0,255))
    for i in range(73,72,-1):
        pixels_set(i,(0,0,255))

    for i in range(42,41,-1):
        pixels_set(i,(0,0,255))
    for i in range(41,40,-1):
        pixels_set(i,(0,0,255))
    for i in range(26,25,-1):
        pixels_set(i,(0,0,255))
    for i in range(25,24,-1):
        pixels_set(i,(0,0,255))

        utime.sleep(1)
        pixels_show()
        
    # Hidden Layer 1 Network
    for i in range(120,119,-1):
        pixels_set(i,(255,255,255))
    for i in range(88,87,-1):
        pixels_set(i,(255,255,255))
    for i in range(103,102,-1):
        pixels_set(i,(255,255,255))
        
    for i in range(72,71,-1):
        pixels_set(i,(255,255,255))
    for i in range(40,39,-1):
        pixels_set(i,(255,255,255))
    for i in range(55,54,-1):
        pixels_set(i,(255,255,255))

    # Hidden Layer 2
    for i in range(118,117,-1):
        pixels_set(i,(0,0,255))
    for i in range(117,116,-1):
        pixels_set(i,(0,0,255))
    for i in range(102,101,-1):
        pixels_set(i,(0,0,255))
    for i in range(101,100,-1):
        pixels_set(i,(0,0,255))

    for i in range(54,53,-1):
        pixels_set(i,(0,0,255))
    for i in range(53,52,-1):
        pixels_set(i,(0,0,255))
    for i in range(38,37,-1):
        pixels_set(i,(0,0,255))
    for i in range(37,36,-1):
        pixels_set(i,(0,0,255))

        utime.sleep(1)
        pixels_show()

    # Hidden Layer 2 Network
    for i in range(100,99,-1):
        pixels_set(i,(255,255,255))
    for i in range(83,82,-1):
        pixels_set(i,(255,255,255))

    for i in range(52,51,-1):
        pixels_set(i,(255,255,255))
    for i in range(67,66,-1):
        pixels_set(i,(255,255,255))

    # Output Layer
    for i in range(82,81,-1):
        pixels_set(i,(0,0,255))
    for i in range(81,80,-1):
        pixels_set(i,(0,0,255))
    for i in range(66,65,-1):
        pixels_set(i,(0,0,255))
    for i in range(65,64,-1):
        pixels_set(i,(0,0,255))

        utime.sleep(1)
        pixels_show()

def rgb_neural_net_small():
    # Input Layer
    for i in range(140,139,-1):
        pixels_set(i,(0,0,255))
    for i in range(139,138,-1):
        pixels_set(i,(0,0,255))
    for i in range(124,123,-1):
        pixels_set(i,(0,0,255))
    for i in range(123,122,-1):
        pixels_set(i,(0,0,255))

    for i in range(92,91,-1):
        pixels_set(i,(0,0,255))
    for i in range(91,90,-1):
        pixels_set(i,(0,0,255))
    for i in range(76,75,-1):
        pixels_set(i,(0,0,255))
    for i in range(75,74,-1):
        pixels_set(i,(0,0,255))

    for i in range(44,43,-1):
        pixels_set(i,(0,0,255))
    for i in range(43,42,-1):
        pixels_set(i,(0,0,255))
    for i in range(28,27,-1):
        pixels_set(i,(0,0,255))
    for i in range(27,26,-1):
        pixels_set(i,(0,0,255))

        utime.sleep(1)
        pixels_show()
        
    # Input Layer Network
    for i in range(122,121,-1):
        pixels_set(i,(255,255,255))
    for i in range(90,89,-1):
        pixels_set(i,(255,255,255))
    for i in range(105,104,-1):
        pixels_set(i,(255,255,255))
        
    for i in range(74,73,-1):
        pixels_set(i,(255,255,255))
    for i in range(42,41,-1):
        pixels_set(i,(255,255,255))
    for i in range(57,56,-1):
        pixels_set(i,(255,255,255))

    # Hidden Layer
    for i in range(120,119,-1):
        pixels_set(i,(0,0,255))
    for i in range(119,118,-1):
        pixels_set(i,(0,0,255))
    for i in range(104,103,-1):
        pixels_set(i,(0,0,255))
    for i in range(103,102,-1):
        pixels_set(i,(0,0,255))

    for i in range(56,55,-1):
        pixels_set(i,(0,0,255))
    for i in range(55,54,-1):
        pixels_set(i,(0,0,255))
    for i in range(40,39,-1):
        pixels_set(i,(0,0,255))
    for i in range(39,38,-1):
        pixels_set(i,(0,0,255))

        utime.sleep(1)
        pixels_show()

    # Hidden Layer Network
    for i in range(102,101,-1):
        pixels_set(i,(255,255,255))
    for i in range(85,84,-1):
        pixels_set(i,(255,255,255))

    for i in range(54,53,-1):
        pixels_set(i,(255,255,255))
    for i in range(69,68,-1):
        pixels_set(i,(255,255,255))

    # Output Layer
    for i in range(84,83,-1):
        pixels_set(i,(0,0,255))
    for i in range(83,82,-1):
        pixels_set(i,(0,0,255))
    for i in range(68,67,-1):
        pixels_set(i,(0,0,255))
    for i in range(67,66,-1):
        pixels_set(i,(0,0,255))

        utime.sleep(1)
        pixels_show()

def rgb_feed_forward():
    for i in range(3):
        # Feed Forward Input Layer
        for i in range(126,125,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(125,124,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(110,109,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(109,108,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(62,61,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(61,60,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(46,45,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(45,44,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(126,125,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(125,124,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(110,109,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(109,108,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(62,61,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(61,60,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(46,45,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(45,44,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        # Feed Forward Hidden Layer 1
        for i in range(138,137,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(137,136,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(122,121,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(121,120,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(90,89,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(89,88,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(74,73,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(73,72,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(42,41,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(41,40,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(26,25,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(25,24,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(138,137,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(137,136,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(122,121,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(121,120,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(90,89,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(89,88,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(74,73,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(73,72,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(42,41,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(41,40,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(26,25,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(25,24,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        # Feed Forward Hidden Layer 2
        for i in range(118,117,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(117,116,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(102,101,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(101,100,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(54,53,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(53,52,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(38,37,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(37,36,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(118,117,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(117,116,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(102,101,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(101,100,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(54,53,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(53,52,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(38,37,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(37,36,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        # Feed Forward Output Layer
        for i in range(82,81,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(81,80,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(66,65,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(65,64,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
            
        for i in range(82,81,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(81,80,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(66,65,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(65,64,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)

def rgb_feed_forward_small():
    for i in range(3):
        # Feed Forward Input Layer
        for i in range(140,139,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(139,138,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(124,123,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(123,122,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(92,91,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(91,90,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(76,75,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(75,74,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(44,43,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(43,42,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(28,27,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(27,26,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(140,139,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(139,138,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(124,123,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(123,122,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(92,91,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(91,90,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(76,75,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(75,74,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(44,43,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(43,42,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(28,27,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(27,26,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        # Feed Forward Hidden Layer
        for i in range(120,119,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(119,118,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(104,103,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(103,102,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(56,55,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(55,54,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(40,39,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(39,38,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(120,119,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(119,118,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(104,103,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(103,102,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        for i in range(56,55,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(55,54,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(40,39,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)
        for i in range(39,38,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.01)

        # Feed Forward Output Layer
        for i in range(84,83,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(83,82,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(68,67,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(67,66,-1):
            pixels_set(i,(0,255,255))
            pixels_show()
            utime.sleep(0.03)
            
        for i in range(84,83,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(83,82,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(68,67,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)
        for i in range(67,66,-1):
            pixels_set(i,(0,0,255))
            pixels_show()
            utime.sleep(0.03)

# Buttons Setup
KEY_CTRL=Pin(3,Pin.IN,Pin.PULL_UP)
KEY_A=Pin(15,Pin.IN,Pin.PULL_UP)
KEY_B=Pin(17,Pin.IN,Pin.PULL_UP)

# Display Setup
class LCD_1inch14(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 240
        self.height = 135
        
        self.cs = Pin(CS,Pin.OUT)
        self.rst = Pin(RST,Pin.OUT)
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,10000_000,polarity=0, phase=0,sck=Pin(SCK),mosi=Pin(MOSI),miso=None)
        self.dc = Pin(DC,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
        
        self.white =   0xffff
        
    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize dispaly"""  
        self.rst(1)
        self.rst(0)
        self.rst(1)
        
        self.write_cmd(0x36)
        self.write_data(0x70)

        self.write_cmd(0x3A) 
        self.write_data(0x05)

        self.write_cmd(0xB2)
        self.write_data(0x0C)
        self.write_data(0x0C)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x33)

        self.write_cmd(0xB7)
        self.write_data(0x35) 

        self.write_cmd(0xBB)
        self.write_data(0x19)

        self.write_cmd(0xC0)
        self.write_data(0x2C)

        self.write_cmd(0xC2)
        self.write_data(0x01)

        self.write_cmd(0xC3)
        self.write_data(0x12)   

        self.write_cmd(0xC4)
        self.write_data(0x20)

        self.write_cmd(0xC6)
        self.write_data(0x0F) 

        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)

        self.write_cmd(0xE0)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2B)
        self.write_data(0x3F)
        self.write_data(0x54)
        self.write_data(0x4C)
        self.write_data(0x18)
        self.write_data(0x0D)
        self.write_data(0x0B)
        self.write_data(0x1F)
        self.write_data(0x23)

        self.write_cmd(0xE1)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0C)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2C)
        self.write_data(0x3F)
        self.write_data(0x44)
        self.write_data(0x51)
        self.write_data(0x2F)
        self.write_data(0x1F)
        self.write_data(0x1F)
        self.write_data(0x20)
        self.write_data(0x23)
        
        self.write_cmd(0x21)

        self.write_cmd(0x11)

        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x28)
        self.write_data(0x01)
        self.write_data(0x17)
        
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x35)
        self.write_data(0x00)
        self.write_data(0xBB)
        
        self.write_cmd(0x2C)
        
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)

# Setup neural net
def neural_network():
    
    # Mathematical Basics - I
    def zero_dim(x):
        z = [0 for i in range(len(x))]
        return z

    # Mathematical Basics - II
    def add_dim(x, y):
            z = [x[i] + y[i] for i in range(len(x))]
            return z

    # Mathematical Basics - III
    def zeros(rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)
        return M

    # Mathematical Basics - IV
    def transpose(M):
        if not isinstance(M[0], list):
            M = [M]
        rows = len(M)
        cols = len(M[0])
        MT = zeros(cols, rows)
        for i in range(rows):
            for j in range(cols):
                MT[j][i] = M[i][j]
        return MT

    # Mathematical Basics - V
    def dense(nunit, x, w, b, activation):
        res = []
        for i in range(nunit):
            z = neuron(x, w[i], b[i], activation)
            res.append(z)
        return res

    # Mathematical Basics - VI
    def print_matrix(M, decimals=3):
        for row in M:
            print([round(x, decimals) + 0 for x in row])

    # ReLU
    def relu(x):
        y = []
        for i in range(len(x)):
            if x[i] >= 0:
                y.append(x[i])
            else:
                y.append(0)    
        return y

    # Leaky ReLU
    def leaky_relu(x, alpha=0.01):
        p = []
        for i in range(len(x)):
            if x[i] > 0:
                p.append(x[i])
            else:
                p.append(alpha * x[i])
        return p

    # Tanh
    def tanh(x):
        t = [(math.exp(x[val]) - math.exp(-x[val])) / (math.exp(x[val]) + math.exp(-x[val])) for val in range(len(x))]
        return t

    # Sigmoid
    def sigmoid(x):
        z = [1 / (1 + math.exp(-x[val])) for val in range(len(x))]
        return z

    # Softmax
    def softmax(x):
        max_x = max(x[val])
        exp_x = [math.exp(val - max_x) for val in range(len(x))]
        sum_exp_x = sum(exp_x)
        s = [j / sum_exp_x for j in exp_x]
        return s

    # Single Neuron
    def neuron(x, w, b, activation):

        tmp = zero_dim(x[0])

        for i in range(len(x)):
            tmp = add_dim(tmp, [(float(w[i]) * float(x[i][j])) for j in range(len(x[0]))])

        if activation == "sigmoid":
            yp = sigmoid([tmp[i] + b for i in range(len(tmp))])
        elif activation == "relu":
            yp = relu([tmp[i] + b for i in range(len(tmp))])
        elif activation == "leaky_relu":
            yp = relu([tmp[i] + b for i in range(len(tmp))])
        elif activation == "tanh":
            yp = relu([tmp[i] + b for i in range(len(tmp))])
        elif activation == "softmax":
            yp = relu([tmp[i] + b for i in range(len(tmp))])
        else:
            print("Function unknown!")

        return yp

    # Standardized Data
    Xtest = [[-8.44885053e-01, 2.44447821e+00, 3.56431752e-01,
              1.40909441e+00, -6.92890572e-01, 1.38436175e+00,
              2.78492300e+00, -9.56461683e-01],
             [-5.47918591e-01, -4.34859164e-01, 2.53036252e-01,
              5.93629620e-01, 1.75399020e-01, 2.04012771e-01,
              -2.04994488e-01, -8.71373930e-01],
             [4.60143347e-02, -1.40507067e+00, -3.67336746e-01,
              -1.28821221e+00, -6.92890572e-01, 2.54780469e-01,
              -2.44256030e-01, -7.01198424e-01],
             [3.42980797e-01, 1.41167241e+00, 1.49640753e-01,
              -9.63790522e-02, 8.26616214e-01, -7.85957342e-01,
              3.47687230e-01, 1.51108316e+00],
             [-1.14185152e+00, -3.09670582e-01, -2.12243497e-01,
              -1.28821221e+00, -6.92890572e-01, -9.38260437e-01,
              5.68155894e-01, -1.90671905e-01],
             [-8.44885053e-01, -1.24858494e+00, 1.49640753e-01,
              -1.59107113e-01, -3.45574735e-01, -6.84421946e-01,
              -5.70428848e-01, -7.86286177e-01],
             [1.53084665e+00, 9.73512376e-01, 4.59827252e-01,
              8.44541864e-01, 7.91884630e-01, 2.80164319e-01,
              1.27184355e+00, -2.04963989e-02],
             [-2.50952128e-01, 1.72464386e+00, 8.73409251e-01,
              4.05445437e-01, 6.61641192e-01, 1.65936998e-01,
              2.06009452e+00, 1.59617091e+00],
             [-5.47918591e-01, 1.91083743e-01, -5.74127746e-01,
              2.17261253e-01, 1.69490581e+00, -5.44810776e-01,
              3.40706745e+00, -7.01198424e-01],
             [6.39947260e-01, -5.60047745e-01, 1.49640753e-01,
              7.19085742e-01, 9.56859653e-01, 7.24381677e-01,
              -4.46603982e-01, 1.85143417e+00],
             [-2.50952128e-01, 1.16129525e+00, 3.56431752e-01,
              9.69997986e-01, 1.43441893e+00, -4.98257194e-02,
              1.14499856e+00, -4.45935165e-01],
             [3.42980797e-01, 2.06891246e+00, 3.56431752e-01,
              4.05445437e-01, 1.10446888e+00, 1.47320522e+00,
              1.69768028e+00, 1.68125866e+00],
             [3.42980797e-01, -2.15779146e-01, 2.53036252e-01,
              -1.28821221e+00, -6.92890572e-01, -9.00184663e-01,
              8.21845863e-01, 2.02160968e+00],
             [-5.47918591e-01, -1.21728780e+00, -8.84314245e-01,
              9.18051311e-02, 3.05642459e-01, -4.43275380e-01,
              3.70605920e+00, -7.01198424e-01],
             [1.23388019e+00, -1.74933927e+00, 1.49640753e-01,
              1.54533192e-01, -6.92890572e-01, 9.41978774e-04,
              3.86948773e-01, 7.45293379e-01],
             [-1.14185152e+00, -4.03562018e-01, -5.71502470e-02,
              -3.36509911e-02, -6.92890572e-01, -5.95578474e-01,
              9.51710966e-01, -1.05584152e-01],
             [1.23388019e+00, 1.81853530e+00, 1.49640753e-01,
              1.34636635e+00, 4.35885898e-01, 8.97854505e-02,
              7.46342896e-01, 2.34766861e-01],
             [-8.44885053e-01, -1.49896210e+00, -9.87709745e-01,
              -6.60931602e-01, -6.92890572e-01, -1.14133123e+00,
              -6.76133001e-01, -1.04154944e+00],
             [4.60143347e-02, 3.47569469e-01, 8.73409251e-01,
              6.56357681e-01, -6.92890572e-01, -5.06735003e-01,
              -1.59692708e-01, 2.53213620e+00],
             [3.42980797e-01, -6.85236326e-01, -7.80918745e-01,
              4.68173498e-01, 2.77897893e-02, 2.54780469e-01,
              8.19167867e-02, -2.75759658e-01],
             [4.60143347e-02, 7.23135213e-01, 6.66618252e-01,
              7.19085742e-01, -6.92890572e-01, 8.25917074e-01,
              2.48023314e-01, 3.19854614e-01],
             [-5.47918591e-01, -9.05905652e-02, 5.63222752e-01,
              -1.28821221e+00, -6.92890572e-01, 1.38436175e+00,
              6.67819810e-01, -1.04154944e+00],
             [-5.47918591e-01, -1.06080207e+00, -3.57259724e+00,
              1.54533192e-01, -6.92890572e-01, -3.92507682e-01,
              9.09429304e-01, -7.01198424e-01],
             [-2.50952128e-01, -1.87452785e+00, 6.66618252e-01,
              4.68173498e-01, -6.92890572e-01, 3.05548168e-01,
              -6.91233595e-01, 1.08564439e+00],
             [-8.44885053e-01, -7.47830617e-01, -1.60545747e-01,
              -3.47291297e-01, 5.22714857e-01, -1.11594738e+00,
              4.56753625e-02, -9.56461683e-01],
             [-8.44885053e-01, 9.71923068e-02, -4.70732246e-01,
              7.19085742e-01, -6.92890572e-01, 4.83235111e-01,
              1.27218567e-01, -1.04154944e+00],
             [-1.14185152e+00, -5.28750600e-01, 3.56431752e-01,
              -1.28821221e+00, -6.92890572e-01, -1.72515976e+00,
              3.32586637e-01, -5.31022918e-01],
             [2.71871250e+00, 1.00480952e+00, 9.76804751e-01,
              1.03272605e+00, 5.22714857e-01, 1.09244749e+00,
              2.12049689e+00, 4.90030120e-01],
             [-5.47918591e-01, -2.78373437e-01, -1.60545747e-01,
              9.18051311e-02, -6.92890572e-01, -8.87492739e-01,
              -4.97945999e-01, -7.86286177e-01],
             [3.42980797e-01, -3.40967728e-01, -5.71502470e-02,
              -1.28821221e+00, -6.92890572e-01, -7.60573493e-01,
              -5.43247780e-01, -2.75759658e-01],
             [9.36913723e-01, 4.72758051e-01, 2.53036252e-01,
              3.42717375e-01, 4.79300377e-01, -7.60573493e-01,
              5.28894351e-01, 1.51108316e+00],
             [-1.14185152e+00, -5.91344890e-01, -2.63941247e-01,
              1.59727860e+00, -1.56246903e-02, 1.09244749e+00,
              7.28564306e-02, -1.04154944e+00],
             [-1.14185152e+00, -5.91344890e-01, 8.73409251e-01,
              -2.21835174e-01, 2.18813500e-01, -3.41739984e-01,
              6.73860047e-01, -5.31022918e-01],
             [-5.47918591e-01, 3.45980161e-02, -8.84314245e-01,
              1.40909441e+00, 6.79006984e-01, 5.34002809e-01,
              1.03929441e+00, -4.45935165e-01],
             [-8.44885053e-01, -5.92934199e-02, -7.80918745e-01,
              -4.72747419e-01, -2.58745776e-01, -1.23017470e+00,
              -8.05998104e-01, -7.86286177e-01],
             [3.42980797e-01, 1.47426670e+00, -2.63941247e-01,
              -1.28821221e+00, -6.92890572e-01, 1.15169300e-01,
              -1.01740641e+00, 6.60205626e-01],
             [2.12477957e+00, 4.72758051e-01, 7.70013751e-01,
              9.07269925e-01, 4.35885898e-01, -4.68659229e-01,
              -6.39891577e-01, 7.45293379e-01],
             [-5.47918591e-01, -1.21887711e-01, 1.08020025e+00,
              -9.63790522e-02, -7.64049618e-02, -8.62108890e-01,
              -4.79825287e-01, -1.04154944e+00],
             [-8.44885053e-01, -5.92934199e-02, -1.29789624e+00,
              1.66000666e+00, -1.45868129e-01, 4.45159338e-01,
              -5.79489204e-01, -7.01198424e-01]]
    
    ytrue = [1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]

    # Include Parameters
    w1 = [[-0.34662053,  0.65511954],
           [ 0.5935057 ,  0.6294829 ],
           [-0.12298097, -0.16659012],
           [-0.18622346,  0.24092631],
           [ 0.45131862, -0.65687644],
           [ 0.5652807 ,  0.22770791],
           [-0.00432371,  0.29822987],
           [ 0.6685666 , -0.50518966]]
    b1 = [1.2871962 , 0.17089938]
    w2 = [[-0.6698178 ,  0.38651687,  1.1558827 ],
           [ 0.8407776 , -1.3820485 , -0.05414521]]
    b2 = [-0.07933541,  0.5355358 ,  0.3076397 ]
    w3 = [[ 0.47389838, -0.48936632],
           [-0.5548221 ,  0.536068  ],
           [ 1.0642822 ,  0.0441233 ]]
    b3 = [-0.02199756,  0.8423532 ]
    w4 = [[ 1.3345304],
           [-1.80047  ]]
    b4 = [-0.7458876]

    # Transpose
    w1 = transpose(w1)
    w2 = transpose(w2)
    w3 = transpose(w3)
    w4 = transpose(w4)

    # Neural Network
    yout1 = dense(2, transpose(Xtest), w1, b1, 'relu') # input layer (2 neurons)
    yout2 = dense(3, yout1, w2, b2, 'relu') # hidden layer (3 neurons)
    yout3 = dense(2, yout2, w3, b3, 'relu') # hidden layer (2 neurons)
    ypred = dense(1, yout3, w4, b4,'sigmoid') # output layer (1 neuron)
    print("Predictions with 8 neurons:")
    print(ypred)

    # Confusion Matrix Basics
    def classification_report(ytrue, ypred):
        TP = TN = FP = FN = 0
    
        for true, pred in zip(ytrue, ypred):
            if true == pred:
                if true == 1:
                    TP += 1
                else:
                    TN += 1
            else:
                if true == 1:
                    FN += 1
                else:
                    FP += 1

        accuracy = (TP + TN) / len(ytrue)
        conf_matrix = [[TN, FP], [FN, TP]]

        print("Accuracy: " + str(accuracy))
        print("Confusion Matrix:")
        print(print_matrix(conf_matrix))

    # Confusion Matrix
    ypred_class = [1 if i > 0.5 else 0 for i in ypred[0]]
    print(ypred_class)
    print(classification_report(ytrue,ypred_class))

    # Include Parameters (S)
    w5 = [[ 0.38001454, -0.12518068, -0.60575366],
          [ 1.1286397 ,  0.77441347, -0.24946934],
          [-0.3657592 , -0.43073633,  0.12212432],
          [ 0.10864732,  0.4490554 , -0.24930577],
          [-0.27232662,  0.20741941,  0.7047888 ],
          [ 0.36831862, -0.25138912, -0.89533746],
          [ 0.27688333,  0.12808096, -0.3986453 ],
          [ 0.0657485 ,  1.172397  , -0.49063933]]
    b5 = [ 0.38096386,  0.32786837, -0.33324558]
    w6 = [[-0.85773826,  1.1585809 ],
          [-1.7594414 , -0.27292567],
          [ 1.2282224 ,  0.7099379 ]]
    b6 = [ 0.42388713, -0.11927897]
    w7 = [[-2.4726155 ],
          [ 0.81422347]]
    b7 = [-0.48662367]

    # Transpose (S)
    w5 = transpose(w5)
    w6 = transpose(w6)
    w7 = transpose(w7)

    # Neural Network (S)
    yout4 = dense(3, transpose(Xtest), w5, b5, 'relu') # input layer (3 neurons)
    yout5 = dense(2, yout4, w6, b6, 'relu') # hidden layer (2 neurons)
    ypred = dense(1, yout5, w7, b7,'sigmoid') # output layer (1 neuron)
    print("Predictions with 6 neurons:")
    print(ypred)

    # Confusion Matrix (S)
    ypred_class = [1 if i > 0.5 else 0 for i in ypred[0]]
    print(ypred_class)
    print(classification_report(ytrue,ypred_class))

####################### Interface Setup ##############################

def first_choice():
     while True:
        if (KEY_A.value() == 0):

            # Initializing
            LCD.fill(BLACK)
            LCD.text("I N I T I A L I Z E",45,60,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()
            utime.sleep(0.1)

            rgb_neural_net_small()
                        
            LCD.fill(BLACK)
            LCD.text("This neural network consists",8,32,WHITE)
            LCD.text("of 3 layers and 6 neurons.",17,52,WHITE)
            LCD.text("[A]:",40,92,BLUE)
            LCD.text("Train",75,92,WHITE)
            LCD.text("[B]:",125,92,BLUE)
            LCD.text("About",160,92,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

            utime.sleep(0.1)
            
            second_choice()
        
        elif (KEY_B.value() == 0):

            # Initializing
            LCD.fill(BLACK)
            LCD.text("I N I T I A L I Z E",45,60,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()
            utime.sleep(0.1)

            rgb_neural_net()
                        
            LCD.fill(BLACK)
            LCD.text("This neural network consists",8,32,WHITE)
            LCD.text("of 4 layers and 8 neurons.",17,52,WHITE)
            LCD.text("[A]:",40,92,BLUE)
            LCD.text("Train",75,92,WHITE)
            LCD.text("[B]:",125,92,BLUE)
            LCD.text("About",160,92,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

            utime.sleep(0.1)
            
            third_choice()

        elif (KEY_CTRL.value() == 0):
             
            machine.reset()

def second_choice():
     while True:
        if (KEY_A.value() == 0):

            # Model Summary
            LCD.fill(BLACK)
            LCD.text("L E A R N I N G",60,60,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()
            utime.sleep(0.1)
            
            rgb_feed_forward_small()
            neural_network()
            
            LCD.fill(BLACK)
            LCD.text("Neural Network Summary:",25,15,WHITE)
            LCD.text("- - - - - - - - - - - -",25,25,BLUE)
            LCD.text("500 EPOs @ 0.035 LR",25,35,WHITE)
            LCD.text("Accuracy: 0.8718",25,45,WHITE)
            LCD.text("LOSS: 0.3462",25,55,WHITE)
            LCD.text("- - - - - - - - - - - -",25,65,BLUE)
            LCD.text("Confusion",25,95,WHITE)
            LCD.text("Matrix:",25,105,WHITE)
            LCD.text("[N]",150,85,BLUE)
            LCD.text("[P]",180,85,BLUE)
            LCD.text("[N]",120,95,BLUE)
            LCD.text("[P]",120,105,BLUE)
            LCD.text("24",154,95,WHITE)
            LCD.text("01",154,105,WHITE)
            LCD.text("04",184,95,WHITE)
            LCD.text("10",184,105,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

            utime.sleep(0.1)

        elif (KEY_B.value() == 0):

            # Features
            LCD.fill(BLACK)
            LCD.text("Training Process:",25,15,WHITE)
            LCD.text("- - - - - - - - - - - -",25,25,BLUE)
            LCD.text("The flow of information",25,35,WHITE)
            LCD.text("is uni-directional from",25,45,WHITE)
            LCD.text("the input layer through",25,55,WHITE)
            LCD.text("the hidden layers on to",25,65,WHITE)
            LCD.text("the output layer, each",25,75,WHITE)
            LCD.text("of them based upon",25,85,WHITE)
            LCD.text("neurons that process",25,95,WHITE)
            LCD.text("the information.",25,105,WHITE)
            LCD.text("- - - - - - - - - - - -",25,115,BLUE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()
            
            utime.sleep(5)
            
            LCD.fill(BLACK)
            LCD.text("This neural network consists",8,32,WHITE)
            LCD.text("of 3 layers and 6 neurons.",17,52,WHITE)
            LCD.text("[A]:",40,92,BLUE)
            LCD.text("Train",75,92,WHITE)
            LCD.text("[B]:",125,92,BLUE)
            LCD.text("About",160,92,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

            utime.sleep(0.1)

        elif (KEY_CTRL.value() == 0):
             
            machine.reset()

def third_choice():
     while True:
        if (KEY_A.value() == 0):

            # Model Summary
            LCD.fill(BLACK)
            LCD.text("L E A R N I N G",60,60,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()
            utime.sleep(0.1)
            
            rgb_feed_forward()
            neural_network()
            
            LCD.fill(BLACK)
            LCD.text("Neural Network Summary:",25,15,WHITE)
            LCD.text("- - - - - - - - - - - -",25,25,BLUE)
            LCD.text("500 EPOs @ 0.035 LR",25,35,WHITE)
            LCD.text("Accuracy: 0.9230",25,45,WHITE)
            LCD.text("LOSS: 0.3121",25,55,WHITE)
            LCD.text("- - - - - - - - - - - -",25,65,BLUE)
            LCD.text("Confusion",25,95,WHITE)
            LCD.text("Matrix:",25,105,WHITE)
            LCD.text("[N]",150,85,BLUE)
            LCD.text("[P]",180,85,BLUE)
            LCD.text("[N]",120,95,BLUE)
            LCD.text("[P]",120,105,BLUE)
            LCD.text("27",154,95,WHITE)
            LCD.text("02",154,105,WHITE)
            LCD.text("01",184,95,WHITE)
            LCD.text("09",184,105,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

            utime.sleep(0.1)

        elif (KEY_B.value() == 0):

            # Features
            LCD.fill(BLACK)
            LCD.text("Training Process:",25,15,WHITE)
            LCD.text("- - - - - - - - - - - -",25,25,BLUE)
            LCD.text("The flow of information",25,35,WHITE)
            LCD.text("is uni-directional from",25,45,WHITE)
            LCD.text("the input layer through",25,55,WHITE)
            LCD.text("the hidden layers on to",25,65,WHITE)
            LCD.text("the output layer, each",25,75,WHITE)
            LCD.text("of them based upon",25,85,WHITE)
            LCD.text("neurons that process",25,95,WHITE)
            LCD.text("the information.",25,105,WHITE)
            LCD.text("- - - - - - - - - - - -",25,115,BLUE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()
            
            utime.sleep(5)
            
            LCD.fill(BLACK)
            LCD.text("This neural network consists",8,32,WHITE)
            LCD.text("of 4 layers and 8 neurons.",17,52,WHITE)
            LCD.text("[A]:",40,92,BLUE)
            LCD.text("Train",75,92,WHITE)
            LCD.text("[B]:",125,92,BLUE)
            LCD.text("About",160,92,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

            utime.sleep(0.1)

        elif (KEY_CTRL.value() == 0):
             
            # Initializing
            LCD.fill(BLACK)
            LCD.text("C A M E R A M O D E",45,60,WHITE)
            LCD.rect(0,0,240,135,BLUE)
            LCD.show()

# Startbildschirm
if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)

    LCD = LCD_1inch14()
    LCD.fill(BLACK)
    LCD.text("K  I  -  E  N  N  A",45,60,WHITE)
    LCD.rect(0,0,240,135,BLUE)
    LCD.show()

    utime.sleep(3)

    # Features
    LCD.fill(BLACK)
    LCD.text("Loading Features:",25,15,WHITE)
    LCD.text("- - - - - - - - - - - -",25,25,BLUE)
    LCD.text("[X1] ~ Pregnancies",25,35,WHITE)
    LCD.text("[X2] ~ Glucose",25,45,WHITE)
    LCD.text("[X3] ~ Blood Pressure",25,55,WHITE)
    LCD.text("[X4] ~ Skin Thickness",25,65,WHITE)
    LCD.text("[X5] ~ Insulin",25,75,WHITE)
    LCD.text("[X6] ~ Body Mass Index",25,85,WHITE)
    LCD.text("[X7] ~ Diabetes History",25,95,WHITE)
    LCD.text("[X8] ~ Years of Age",25,105,WHITE)
    LCD.text("- - - - - - - - - - - -",25,115,BLUE)
    LCD.rect(0,0,240,135,BLUE)
    LCD.show()
            
    utime.sleep(5)
    
    # Initilisierung
    LCD.fill(BLACK)
    LCD.text("Select a number of neurons",15,32,WHITE)
    LCD.text("for the neural network:",30,52,WHITE)
    LCD.text("[A]:",45,92,BLUE)
    LCD.text("Six",80,92,WHITE)
    LCD.text("[B]:",115,92,BLUE)
    LCD.text("Eight",150,92,WHITE)
    LCD.rect(0,0,240,135,BLUE)
    LCD.show()
    
    first_choice()
