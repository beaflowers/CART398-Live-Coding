import board
import busio
import analogio
import time
import wifi
import socketpool 
import adafruit_mpu6050

#mpu6050 bus
i2c = busio.I2C(board.GP15, board.GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)

#wifi connectivity
# SSID = "!!Kelly's_Day_In_The_Park!!"
# PASSWORD = "guestGuest"
# 
# wifi.radio.connect(SSID, PASSWORD)
# pool = socketpool.SocketPool(wifi.radio)
# UDP_IP = "192.168.4.2"   # your computer IP
# UDP_PORT = 8000                                                                                                                                                    vcvvcccvccvcvcvvcffgfgggggggggggggggggggggggggggggggggggggggggooxoxoxooxgggfgoxfggoggggggggxoxogoxgxoxoxoxox5555555555555555555555555555555555555555555555555555555555556
# 
# sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
                     
#photoresistor


start = time.monotonic()

def td():
    #send to UDP in TD 
    msg = f"/light1 {light1}"
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    
    msg = f"/light2 {light2}"
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    
    msg = f"/accel {accel_y}"
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    
    
    
while True:
    # print("My IP:", wifi.radio.ipv4_address)
    current_time = time.monotonic() - start
        
    accel_x, accel_y, accel_z = mpu.acceleration
    gyro_x, gyro_y, gyro_z = mpu.gyro
    
    #save to file
    line = "{:.2f},{},{}\n".format(
        accel_x,
        accel_y,
        accel_z
        )
    print(line)
    
#     td()
    print("send")
        
    
    
    time.sleep(1)

