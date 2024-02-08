from djitellopy import tello
from time import sleep

drone_1 = tello.Tello()
drone_1.connect()
print(drone_1.get_battery())

drone_1.takeoff()
sleep(2)
drone_1.send_rc_control(0,0,0,100)
sleep(5)
drone_1.send_rc_control(0,0,0,0)
drone_1.land()