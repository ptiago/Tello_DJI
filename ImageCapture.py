from djitellopy import tello
import cv2

drone_1 = tello.Tello()
drone_1.connect()
print(drone_1.get_battery())

drone_1.streamon()

while True:
    img = drone_1.get_frame_read().frame
    cv2.imshow("Imagem", img)
    cv2.waitKey(1)