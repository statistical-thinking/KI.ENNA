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
    def zero_dim(x):
        z = [0 for i in range(len(x))]
        return z

    def add_dim(x, y):
            z = [x[i] + y[i] for i in range(len(x))]
            return z

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
            if x[i] >= 0:
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

    # Basics for matrices
    def zeros(rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)
        return M

    # Transpose metrices
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

    # Single neuron
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
            yp = tanh([tmp[i] + b for i in range(len(tmp))])
        elif activation == "softmax":
            yp = tanh([tmp[i] + b for i in range(len(tmp))])
        else:
            print("Invalid activation function--->")

        return yp

    # Network density
    def dense(nunit, x, w, b, activation):
        res = []
        for i in range(nunit):
            z = neuron(x, w[i], b[i], activation)
            res.append(z)
        return res

    def print_matrix(M, decimals=3):
        for row in M:
            print([round(x, decimals) + 0 for x in row])

    # Test data
    Xtest = [[ 0.81575475, -0.21746808, -0.12904165, -0.65303909],
       [ 0.05761837,  1.59476592,  0.84485761,  1.71304456],
       [ 0.96738203,  0.68864892, -0.00730424, -0.41643072],
       [ 2.02877297,  0.38660992,  2.06223168,  1.00321947],
       [ 1.42226386,  0.99068792,  1.33180724,  0.29339437],
       [ 0.81575475,  0.99068792,  1.21006983,  1.4764362 ],
       [-1.00377258,  0.38660992, -0.49425387, -0.41643072],
       [ 0.05761837, -0.51950708, -0.00730424,  0.29339437],
       [ 0.36087292,  0.38660992,  1.08833242,  1.23982783],
       [ 0.66412748,  0.38660992,  0.35790798,  1.4764362 ],
       [ 0.05761837,  0.08457092,  0.84485761,  0.29339437],
       [-0.70051802, -0.51950708,  0.23617057,  0.53000274],
       [ 0.20924564, -0.21746808,  0.84485761,  1.00321947],
       [-0.24563619,  0.08457092, -0.25077906, -0.65303909],
       [-2.06516352, -1.42562408, -1.95510276, -1.59947255],
       [-1.15539985, -1.42562408, -1.34641572, -1.36286418],
       [ 0.05761837, -1.12358508, -0.00730424, -0.41643072],
       [ 0.20924564,  0.08457092, -0.73772869, -0.88964745],
       [-0.39726347, -0.51950708,  0.23617057, -0.17982236],
       [ 0.5125002 ,  0.08457092, -0.37251647, -0.88964745]]
    
    ytrue = [0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0]

    # Include parameters
    w1 = [[-0.75323504, -0.25906014],
          [-0.46379513, -0.5019245 ],
          [ 2.1273055 ,  1.7724446 ],
          [ 1.1853403 ,  0.88468695]]
    b1 = [0.53405946, 0.32578036]
    w2 = [[-1.6785783,  2.0158117,  1.2769054],
          [-1.4055765,  0.6828738,  1.5902631]]
    b2 = [ 1.18362  , -1.1555661, -1.0966455]
    w3 = [[ 0.729278  , -1.0240695 ],
          [-0.80972326,  1.4383037 ],
          [-0.90892404,  1.6760625 ]]
    b3 = [0.10695826, 0.01635581]
    w4 = [[-0.2019448],
          [ 1.5772797]]
    b4 = [-1.2177287]

    # Transpose
    w1 = transpose(w1)
    w2 = transpose(w2)
    w3 = transpose(w3)
    w4 = transpose(w4)

    # Confusion matrix
    def classification_report(ytrue, ypred):
        tmp = 0
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for i in range(len(ytrue)):
            if ytrue[i] == ypred[i]:
                tmp += 1
            if ytrue[i] == 1 and ypred[i] == 1:  # true positive
                TP += 1
            if ytrue[i] == 0 and ypred[i] == 0:  # true negative
                TN += 1
            if ytrue[i] == 0 and ypred[i] == 1:  # false positive
                FP += 1
            if ytrue[i] == 1 and ypred[i] == 0:  # false negative
                FN += 1
        accuracy = tmp / len(ytrue)
        conf_matrix = [[TN, FP], [FN, TP]]

        print("Accuracy: " + str(accuracy))
        print("Confusion Matrix:")
        print(print_matrix(conf_matrix))

    # Run neural network
    yout1 = dense(2, transpose(Xtest), w1, b1, 'tanh') # input layer: 2 neurons
    yout2 = dense(3, yout1, w2, b2, 'sigmoid') # hidden layer: 3 neurons
    yout3 = dense(2, yout2, w3, b3, 'relu') # hidden layer: 2 neurons
    ypred = dense(1, yout3, w4, b4,'sigmoid') # output layer: 1 neuron
    print("Predictions with 8 neurons:")
    print(ypred)

    # Confusion matrix
    ypred_class = [1 if i > 0.5 else 0 for i in ypred[0]]
    print(ypred_class)
    print(classification_report(ytrue,ypred_class))

    # Include parameters (small)
    w5 = [[ 0.50914556, -0.18116623, -0.04498423],
          [ 0.33949652, -0.42303845, -0.37400272],
          [-1.4968083 ,  1.2034143 ,  0.95544535],
          [-1.344156  ,  0.39220142,  1.2244085 ]]
    b5 = [0.83684736, 0.5311056 , 0.7652087 ]
    w6 = [[-2.1645586 ,  1.3892978 ],
          [ 0.43439832, -1.8758974 ],
          [ 0.92036045, -1.5745732 ]]
    b6 = [0.9615521, 0.4445824]
    w7 = [[ 1.6905344],
          [-2.6346245]]
    b7 = [0.4316521]

    # Transpose (small)
    w5 = transpose(w5)
    w6 = transpose(w6)
    w7 = transpose(w7)

    # Run neural network (small)
    yout4 = dense(3, transpose(Xtest), w5, b5, 'relu') # input layer: 3 neurons
    yout5 = dense(2, yout4, w6, b6, 'relu') # hidden layer: 2 neurons
    ypred = dense(1, yout5, w7, b7,'relu') # output layer: 1 neuron
    print("Predictions with 6 neurons:")
    print(ypred)

    # Confusion matrix (small)
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
            LCD.text("Accuracy: 0.9500",25,45,WHITE)
            LCD.text("LOSS: 0.1408",25,55,WHITE)
            LCD.text("- - - - - - - - - - - -",25,65,BLUE)
            LCD.text("Confusion",25,95,WHITE)
            LCD.text("Matrix:",25,105,WHITE)
            LCD.text("[A]",150,85,BLUE)
            LCD.text("[B]",180,85,BLUE)
            LCD.text("[A]",120,95,BLUE)
            LCD.text("[B]",120,105,BLUE)
            LCD.text("09",154,95,WHITE)
            LCD.text("00",154,105,WHITE)
            LCD.text("01",184,95,WHITE)
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
            LCD.text("Accuracy: 0.9000",25,45,WHITE)
            LCD.text("LOSS: 0.1577",25,55,WHITE)
            LCD.text("- - - - - - - - - - - -",25,65,BLUE)
            LCD.text("Confusion",25,95,WHITE)
            LCD.text("Matrix:",25,105,WHITE)
            LCD.text("[A]",150,85,BLUE)
            LCD.text("[B]",180,85,BLUE)
            LCD.text("[A]",120,95,BLUE)
            LCD.text("[B]",120,105,BLUE)
            LCD.text("08",154,95,WHITE)
            LCD.text("00",154,105,WHITE)
            LCD.text("02",184,95,WHITE)
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
    LCD.text("Loading Features:",25,35,WHITE)
    LCD.text("- - - - - - - - - - - -",25,45,BLUE)
    LCD.text("[X1] ~ Sepal Length",25,55,WHITE)
    LCD.text("[X2] ~ Sepal Width",25,65,WHITE)
    LCD.text("[X3] ~ Petal Length",25,75,WHITE)
    LCD.text("[X4] ~ Petal Width",25,85,WHITE)
    LCD.text("- - - - - - - - - - - -",25,95,BLUE)
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