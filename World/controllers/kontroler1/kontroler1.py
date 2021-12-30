from controller import Robot
import time
import random

if __name__ == "__main__":
    robot = Robot()

    timestep = 64
    max_speed = 10

    left_motor = robot.getDevice('motor_l')
    right_motor = robot.getDevice('motor_p')
    pleft_motor = robot.getDevice('motor_pl')
    pright_motor = robot.getDevice('motor_pp')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    pleft_motor.setPosition(float('inf'))
    pleft_motor.setVelocity(0.0)
    
    pright_motor.setPosition(float('inf'))
    pright_motor.setVelocity(0.0)
    
    ir = robot.getDevice('ir1')
    ir.enable(timestep)
    
    irs = robot.getDevice('ir2')
    irs.enable(timestep)
    
    irt = robot.getDevice('ir3')
    irt.enable(timestep)
    
    irw = robot.getDevice('ir4')
    irw.enable(timestep)
    
    zawroc = 0
    tyl = 0
    x = 3
    y = 66
    i= 10
    start = time.time()
    
    left_speed = 0 * max_speed
    right_speed = 0 * max_speed
    pleft_speed = 0 * max_speed
    pright_speed = 0 * max_speed
    
    while robot.step(timestep) != -1:

        ir_value=ir.getValue()
        irs_value=irs.getValue()
        irt_value=irt.getValue()
        irw_value=irw.getValue()

        now = time.time()
        if irs_value < 1000 or irw_value < 1000:
            if irs_value < 1000 and irw_value < 1000:
                left_speed = 0.85 * max_speed
                right_speed = 0.85 * max_speed
                pleft_speed = 0.85 * max_speed
                pright_speed = 0.85 * max_speed
                left_motor.setVelocity(left_speed)
                right_motor.setVelocity(right_speed)
                pleft_motor.setVelocity(pleft_speed)
                pright_motor.setVelocity(pright_speed)
            elif irs_value < 1000:
                left_speed = 0.5 * max_speed
                right_speed = 0.75 * max_speed
                pleft_speed = 0.5 * max_speed
                pright_speed = 0.75 * max_speed
                left_motor.setVelocity(left_speed)
                right_motor.setVelocity(right_speed)
                pleft_motor.setVelocity(pleft_speed)
                pright_motor.setVelocity(pright_speed)
            elif irw_value < 1000:
                left_speed = 0.75 * max_speed
                right_speed = 0.5 * max_speed
                pleft_speed = 0.75 * max_speed
                pright_speed = 0.5 * max_speed
                left_motor.setVelocity(left_speed)
                right_motor.setVelocity(right_speed)
                pleft_motor.setVelocity(pleft_speed)
                pright_motor.setVelocity(pright_speed) 
        elif zawroc > 0:
            zawroc = zawroc -1
            if tyl > 0:
                tyl = tyl -1
                left_speed = -max_speed
                right_speed = -max_speed
                pleft_speed = -max_speed
                pright_speed = -max_speed
            else:
                left_speed = -max_speed * 0
                right_speed = -max_speed * 0.9
                pleft_speed = -max_speed * 0
                pright_speed = -max_speed * 0.9
        elif 700 < ir_value or 700 < irt_value:
            if 700 < ir_value and 700 < irt_value:
                zawroc = 30
                tyl = 10
            elif 700 < ir_value:
                left_speed = 0 * max_speed
                pleft_speed = 0 * max_speed
            elif 700 < irt_value:
                right_speed = 0 * max_speed
                pright_speed = 0 * max_speed
        elif now-start > 2:
            random.seed(y)
            x = random.randint(1,5)
            y = random.randint(1,30)
            if x == 1:
                left_speed = 0.1 * max_speed
                right_speed = 0.75 * max_speed
                pleft_speed = 0.1 * max_speed
                pright_speed = 0.75 * max_speed
            elif x == 2:
                left_speed = 0.3 * max_speed
                right_speed = 0.75 * max_speed
                pleft_speed = 0.3 * max_speed
                pright_speed = 0.75 * max_speed
            elif x == 3:
                left_speed = 0.75 * max_speed
                right_speed = 0.75 * max_speed
                pleft_speed = 0.75 * max_speed
                pright_speed = 0.75 * max_speed
            elif x == 4:
                left_speed = 0.75 * max_speed
                right_speed = 0.3 * max_speed
                pleft_speed = 0.75 * max_speed
                pright_speed = 0.3 * max_speed
            elif x == 5:
                left_speed = 0.75 * max_speed
                right_speed = 0.1 * max_speed
                pleft_speed = 0.75 * max_speed
                pright_speed = 0.1 * max_speed
                    
            start=time.time()       
            
#        print (ir_value)
#        print (irt_value)
#        print (irs_value)
#        print (irw_value)

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        pleft_motor.setVelocity(pleft_speed)
        pright_motor.setVelocity(pright_speed)