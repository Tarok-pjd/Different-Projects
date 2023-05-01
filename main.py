import network, socket
import time, sys
from machine import Pin, PWM
import os

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        name = input("Please insert WLAN-Name: ")
        pwd = input("Please insert WLAN-Pasword: ")
        wlan.connect(name, pwd)
        while not wlan.isconnected():
            pass

#define PIN
A1 = Pin(4, Pin.OUT, value=0)
B1 = Pin(15, Pin.OUT, value=0)
A2 = Pin(17, Pin.OUT, value=0)
B2 = Pin(16, Pin.OUT, value=0)
pwmB1 = PWM(B1, 1000)
pwmB2 = PWM(B2, 1000)
pwmB1.duty_u16(0)
pwmB2.duty_u16(0)


if __name__ == '__main__':
    do_connect()
    server = socket.socket()
    server.bind(("", 1234))
    server.listen(3)
    blink = Pin(2, Pin.OUT, value=0)
    first = True
    while True:
        if first:
            blink.on()
            first = False
        conn, addr = server.accept()
        try:
            while True:
                blink.off()
                first = True
                order = conn.recv(512)
                if order == b"e":
                    conn.close()
                    break
                elif order == b"o":
                    pwmB1.duty_u16(0)
                    pwmB2.duty_u16(0)
                    A1.off()
                    A2.off()
                    continue
                elif order == b"forward":
                    pwmB1.duty_u16(int(65535*1))
                    pwmB2.duty_u16(int(65535*1))
                    continue
                elif order == b"s":
                    A1.on()
                    A2.on()
                    continue
                elif order == b"a":
                    pwmB1.duty_u16(int(65535*1))
                    pwmB2.duty_u16(int(65535*0.5))
                    continue
                elif order == b"d":
                    pwmB1.duty_u16(int(65535*0.5))
                    pwmB2.duty_u16(int(65535*1))
                    continue

        except Exception as ex:
            conn.close()
        finally:
            pwmB1.duty_u16(0)
            pwmB2.duty_u16(0)
            A1.off()
            A2.off()
