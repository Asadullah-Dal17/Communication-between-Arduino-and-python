import cv2
import serial
import numpy as np
import time

# Variable
# posting of Rectangle
x, y =10, 10
fonts = cv2.FONT_HERSHEY_COMPLEX
rectWidth, rectHeight= 100, 120
def ControlFunc(val):
    pass
# Createing window
cv2.namedWindow("Frame")
# trackbars
cv2.createTrackbar("RED", "Frame", 0,255, ControlFunc)
cv2.createTrackbar("GREEN", "Frame", 0, 255, ControlFunc)
cv2.createTrackbar("BLUE", "Frame",0,255, ControlFunc)

# setting up Ardunio
Arduino = serial.Serial(port='COM3', baudrate=9600)
time.sleep(1)
# cap = cv2.VideoCapture(1)
# create empty image

while True:
    # ret, frame =cap.read()

    # creating the empty image using Numpy
    frame = np.zeros([200,480,3], dtype=np.uint8)
    if (Arduino.readline()) != None:
        LDR_Data= int(Arduino.readline())
        time.sleep(0.02)
        # print(LDR_Data)
        Arduino.flush()
        # drwa text on the screen/ LDR Value
        cv2.putText(frame,f"LDR_value = {LDR_Data}",(130,50),fonts, 1,(0,255,0), 2)
    Red_Value = cv2.getTrackbarPos("RED", "Frame")
    Green_Value= cv2.getTrackbarPos("GREEN", "Frame")
    Blue_Value = cv2.getTrackbarPos("BLUE", "Frame")
    Color_to_Ard =f"R{Red_Value}G{Green_Value}B{Blue_Value}"
    Arduino.write(Color_to_Ard.encode())
    time.sleep(0.002)
    Arduino.flush()
    # print(Color_to_Ard)
    # print(Color_to_Ard)
    # print(Red_Value)
    cv2.rectangle(frame,(x,y), (x+rectWidth, y+rectHeight), (Blue_Value,Green_Value,Red_Value),-1 )
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1)==ord('q'):
        data ="R0G0B0"
        print(data)
        Arduino.write(data.encode())
        time.sleep(0.002)
        Arduino.flush()
        break
cv2.destroyAllWindows()
# cap.release()
