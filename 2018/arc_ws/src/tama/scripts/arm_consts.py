"""
arm.py用定数ファイル
"""
# defined const

DEBUG = 0

UNKNOWN = 0

# pin number
PIN_SARVO1 = 4
PIN_SARVO2 = 14
PIN_INCW = 15
PIN_INCCW = 18

#Sarvo PWM
CW_SARVO1 = 2400
CW_SARVO2 = 2400
CCW_SARVO1 = 550
CCW_SARVO2 = 550

PLUS_SERVO2 = 50

SOFTPWM_W_MAX = 255
SOFTPWM_W_2_5 = (2/5.0) * SOFTPWM_W_MAX
SOFTPWM_W_1_3 = (1/3.0) * SOFTPWM_W_MAX
SOFTPWM_W_OFF = 0

BASE_UP_FIGURE = 1.0
BASE_DN_FIGURE = 1.0

SOFTPWM_F_20K = (20 * 1000)

HIGH = 1
LOW = 0
