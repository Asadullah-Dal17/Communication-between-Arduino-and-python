import serial

Arduino = serial.Serial(port="COM3", baudrate=9600)

while True:
    read_data= int(Arduino.readline())
    print(read_data)
