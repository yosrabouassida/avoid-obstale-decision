import RPi.GPIO as GPIO 
import time 
import numpy as np
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)

class MotorControler(object):

    def __init__(self, parent=None):

        self._data = {'name': 'MOTOR', 'delay': 0.01, 'LD': 14 'LU': 15, 'RD': 18, 'RU': 23}
        self.init_pin()
    def init_pin(self):
        self.GPIO_LD_PIN = self._data.get('LD', -1) 
        self.GPIO_LU_PIN = self._data.get('LU', -1)
        self.GPIO_RD_PIN = self._data.get('RD', -1) 
        self.GPIO_RU_PIN = self._data.get('RU', -1)
    
        if self.GPIO_LD_PIN == -1 or self.GPIO_LU_PIN == -1 or self.GPIO_RD_PIN == -1 or self.GPIO_RU_PIN == -1:

            print('message', 'FATAL ERROR : INVALID PIN ENCOUNTER # ' + str(self.GPIO_LD_PIN) + ', ' + + str(self.GPIO_LU_PIN) + ', ' + + str(self.GPIO_RD_PIN) + ', ' + + str(self.GPIO_RU_PIN))
    # pin setup    class MotorControler(object):
    def __init__(self, parent=None):
        self._data = {'name': 'MOTOR', 'delay': 0.01, 'LD': 14 'LU': 15, 'RD': 18, 'RU': 23}
        self.init_pin()
    def init_pin(self):
        self.GPIO_LD_PIN = self._data.get('LD', -1) 
        self.GPIO_LU_PIN = self._data.get('LU', -1)
        self.GPIO_RD_PIN = self._data.get('RD', -1) 
        self.GPIO_RU_PIN = self._data.get('RU', -1)
        if self.GPIO_LD_PIN == -1 or self.GPIO_LU_PIN == -1 or self.GPIO_RD_PIN == -1 or self.GPIO_RU_PIN == -1:
            print('message', 'FATAL ERROR : INVALID PIN ENCOUNTER # ' + str(self.GPIO_LD_PIN) + ', ' + + str(self.GPIO_LU_PIN) + ', ' + + str(self.GPIO_RD_PIN) + ', ' + + str(self.GPIO_RU_PIN))
    # pin setup
    # set GPIO numbering mode and define output pins
        GPIO.setup(self.GPIO_LD_PIN, GPIO.OUT) 
        GPIO.setup(self.GPIO_LU_PIN, GPIO.OUT) 
        GPIO.setup(self.GPIO_RD_PIN, GPIO.OUT) 
        GPIO.setup(self.GPIO_RU_PIN, GPIO.OUT) 
        time.sleep(0.5) # warmup time self.stop()
    def stop(self):
        GPIO.output(self.GPIO_LD_PIN, False) 
        GPIO.output(self.GPIO_LU_PIN, False)
        GPIO.output(self.GPIO_RD_PIN, False) 
        GPIO.output(self.GPIO_RU_PIN, False)
    def step_forward(self):
        GPIO.output(self.GPIO_LD_PIN, False) 
        GPIO.output(self.GPIO_LU_PIN, True)
        GPIO.output(self.GPIO_RD_PIN, False) 
        GPIO.output(self.GPIO_RU_PIN, True) 
        print('Move Forward')
    def step_backward(self):
        GPIO.output(self.GPIO_LD_PIN, True) 
        GPIO.output(self.GPIO_LU_PIN, False)
        GPIO.output(self.GPIO_RD_PIN, True) 
        GPIO.output(self.GPIO_RU_PIN, False) 
        print('Move Backward')
    def step_right(self):


        GPIO.output(self.GPIO_LD_PIN, True)
        GPIO.output(self.GPIO_LU_PIN, False)
        GPIO.output(self.GPIO_RD_PIN, False) 
        GPIO.output(self.GPIO_RU_PIN, True) 
       print('Move Right')
    def step_left(self):

        GPIO.output(self.GPIO_LD_PIN, False) 
        GPIO.output(self.GPIO_LU_PIN, True)
        GPIO.output(self.GPIO_RD_PIN, True)
        GPIO.output(self.GPIO_RU_PIN, False)
        print('Move Left')
    def move_forward(self, count=15):
        for i in range(count):
            self.step_forward() self.stop()
    def move_backward(self, count=15):
        for i in range(count):
            self.step_backward() self.stop()
    def move_right(self, count=15):
        for i in range(count):
            self.step_right() self.stop()
    def move_left(self, count=15): 
        for i in range(count):
            self.step_left() self.stop()
    def readings():

        IR_SENSOR_A = 2 
        IR_SENSOR_B = 3 
        IR_SENSOR_C = 6 
        IR_SENSOR_D = 4
        GPIO.setup(IR_SENSOR_A, GPIO.IN) 
        GPIO.setup(IR_SENSOR_B, GPIO.IN) 
        GPIO.setup(IR_SENSOR_C, GPIO.IN) 
        GPIO.setup(IR_SENSOR_D, GPIO.IN)
        time.sleep(0.5) # warmup time
        ir_measure_a = GPIO.input(IR_SENSOR_A)
        ir_measure_b = GPIO.input(IR_SENSOR_B)
        ir_measure_c = GPIO.input(IR_SENSOR_C) 
        ir_measure_d = GPIO.input(IR_SENSOR_D)
        print(ir_measure_a, ir_measure_b, ir_measure_c, ir_measure_d)
    return [ir_measure_a, ir_measure_b, ir_measure_c, ir_measure_d]
    # FOR DEMO 
    def run():
        motor = MotorControler()          
        while True:
            sensor = readings()
            if sensor[1] == 0 and sensor[2] == 0:
                motor.move_forward(count=15) 
            elif sensor[1] == 1 and sensor[2] == 1:
                if np.random.ranf() > 0.5 :
                    motor.move_left(count=15) 
                else:
                    motor.move_left(count=15) # provide more condotion for better maneuvering
    run()