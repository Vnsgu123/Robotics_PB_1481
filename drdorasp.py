
'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 3D of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			socket_client_rgb.py
# Functions:
# 					[ Comma separated list of functions in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import socket
import time
import os
import sys
import cv2
import numpy as np
import RPi.GPIO as GPIO
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera

# GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

##############################################################

################# ADD UTILITY FUNCTIONS HERE #################


##############################################################
# initializing the pin numbers where motors are connected
L_PWM_PIN1 = 38
L_PWM_PIN2 = 40
R_PWM_PIN2 = 32
R_PWM_PIN1 = 33
ENA = 31
ENA1 = 37
e1 = 24
e2 = 26
count = 0
ter = 0
fagg = 0

# declare motor pins as output pins
# motors get input from the PWM pins


def rgb_led_setup():
    """
    Purpose:
    ---
    This function configures pins connected to rgb led as output and
    enables PWM on the pins

    Input Arguments:
    ---
    You are free to define input arguments for this function.

    Returns:
    ---
    You are free to define output parameters for this function.

    Example call:
    ---
    rgb_led_setup()
    """

    ################## ADD YOUR CODE HERE	##################
    redPin = 29
    greenPin = 16
    bluePin = 22

    # ENA =31
    # ENA =37
    global r, g, b
# GPIO.setmode(GPIO.BOARD)
    GPIO.setup(redPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(greenPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(bluePin, GPIO.OUT, initial=GPIO.LOW)

    # GPIO.setup(R_PWM_PIN, GPIO.OUT, initial=GPIO.HIGH)
    r = GPIO.PWM(redPin, 100)
    g = GPIO.PWM(greenPin, 100)
    b = GPIO.PWM(bluePin, 100)

# # e=GPIO.PWM(R_PWM_PIN, 100)			words = i.split('_')

    r.start(0)
    b.start(0)
    g.start(0)
# return r,g,b
#    print("hello")

    ##########################################################


def rgb_led_set_color(color):
    """

    ---
    This function takes the color as input and changes the color of rgb led
    connected to Raspberry Pi

    Input Arguments:
    ---

    `color` : [ string ]
                    color detected in QR code communicated by server

    You are free to define any additional input arguments for this function.

    Returns:
    ---
    You are free to define output parameters for this function.

    Example call:
    ---
    rgb_led_set_color(color)
    """

    ################## ADD YOUR CODE HERE	##################
    time.sleep(1)
# 	print("------------------------------------------------")
    if color == 'Red':
        r.ChangeDutyCycle(100)
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)
#
# 		GPIO.output(redPin,GPIO.LOW)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.HIGH)
    if color == 'Green':

        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(100)
        b.ChangeDutyCycle(0)

#
# 		GPIO.output(redPin,GPIO.LOW)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.LOW)

    if color == 'Blue':
        # 		print("blue")
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(100)
#
# 		GPIO.output(redPin,GPIO.LOW)
# 		GPIO.output(greenPin,GPIO.LOW)
# 		GPIO.output(bluePin,GPIO.HIGH)

    if color == 'Orange':
        # 		print("orange")
        r.ChangeDutyCycle(90)
        g.ChangeDutyCycle(25.7)
        b.ChangeDutyCycle(0)

# 		GPIO.output(redPin,GPIO.HIGH)
# 		GPIO.output(greenPin,GPIO.LOW)
# 		GPIO.output(bluePin,GPIO.HIGH)

    if color == 'Sky Blue':
        # 		print("skyblue")
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(100)
        b.ChangeDutyCycle(100)
#
# 		GPIO.output(redPin,GPIO.HIGH)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.HIGH)

    if color == 'Pink':
        # 		print("pink")
        r.ChangeDutyCycle(100)
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(47.84)

# 		GPIO.output(redPin,GPIO.HIGH)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.LOW)


def motor_pin_setup():
    global L_MOTOR1, L_MOTOR2, R_MOTOR1, R_MOTOR2, E1, E2

    GPIO.setup(R_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(R_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ENA1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(e1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(e2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # setting initial PWM frequency for all 4 pins
    L_MOTOR1 = GPIO.PWM(L_PWM_PIN1, 27)
    R_MOTOR1 = GPIO.PWM(R_PWM_PIN1, 30)
    L_MOTOR2 = GPIO.PWM(L_PWM_PIN2, 27)
    R_MOTOR2 = GPIO.PWM(R_PWM_PIN2, 30)
    E1 = GPIO.PWM(ENA, 100)
    E2 = GPIO.PWM(ENA1, 100)

    # setting initial speed (duty cycle) for each pin as 0
    L_MOTOR1.start(0)
    R_MOTOR1.start(0)
    L_MOTOR2.start(0)
    R_MOTOR2.start(0)


def left(stream):
    # k=True
    count1 = ter
    count2 = count
    # while k:
    # L_MOTOR1.ChangeDutyCycle(0)
    # R_MOTOR1.ChangeDutyCycle(50)
    # L_MOTOR2.ChangeDutyCycle(50)

    # if ter > count1 + 21:
    # print("cbuycUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
    # k=False
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)

    R_MOTOR1.ChangeDutyCycle(32)
    L_MOTOR2.ChangeDutyCycle(36)
    stream1 = camera.capture_continuous(
        rawCapture, format="bgr", use_video_port=True)

    # R_MOTOR1.ChangeDutyCycle(0)
    # L_MOTOR2.ChangeDutyCycle(0)
    # cv2.waitKey(2000)
    for frame in stream:
        image1 = frame.array
        key = cv2.waitKey(1) & 0xFF
        # R_MOTOR1.ChangeDutyCycle(43)
        # L_MOTOR2.ChangeDutyCycle(43)
        gausss1 = cv2.GaussianBlur(image1, (5, 5), 0)

        gray1 = cv2.cvtColor(gausss1, cv2.COLOR_BGR2GRAY)
        ret, thresh11 = cv2.threshold(
            gray1, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # th31 = cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

        # hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # gauss = cv2.GaussianBlur(hsv,(5,5),0)

        # low_b = np.array([0,0,168])
        # high_b = np.array([172,111,255])

        # mask = cv2.inRange(gauss, low_b, high_b)

        # out1 = cv2.bitwise_and(image,image, mask= mask)

        # out3 = cv2.bitwise_not(mask)

        contours, hierarchy = cv2.findContours(
            thresh11, 1, cv2.CHAIN_APPROX_NONE)

        c = max(contours, key=cv2.contourArea)
        approx1 = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)

        x1, y1, w1, h1 = cv2.boundingRect(c)
        print("area == ======================================================================================================================================================================== ", w1, h1, len(c))

        if w1 > 10 and w1 < 290 and h1 > 40 and h1 < 520 and ter > count1 + 4 and count > count2 + 4:
            cv2.waitKey(1000)
            print("fnrefuyrgfygfyruyerfyurevyfuehiujoifjwu9hfywiyfhu34ty4ikr3h   ", w1)
            R_MOTOR1.ChangeDutyCycle(0)
            L_MOTOR2.ChangeDutyCycle(0)
            cv2.destroyAllWindows()
            rawCapture.truncate(0)
            traversel(stream)
            # cv2.waitKey(1000)
            print("-delay for sprint  ------------------ 0dbufbhrh")
            break

        # print("area == ======================================================================================================================================================================== ",w1,h1,len(c) )

        cv2.drawContours(image1, [approx1], 0, (0, 255, 255), 5)
        cv2.imshow("new turn image", image1)
        cv2.imshow("kem cho ", thresh11)
        cv2.waitKey(3)
        rawCapture.truncate(0)
        if key == ord("q"):
            cv2.destroyAllWindows()
            GPIO.cleanup()
            break


def right(stream):
    # k=True
    count1 = ter
    count2 = count
    # while k:
    # L_MOTOR1.ChangeDutyCycle(0)
    # R_MOTOR1.ChangeDutyCycle(50)
    # L_MOTOR2.ChangeDutyCycle(50)

    # if ter > count1 + 21:
    # print("cbuycUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
    # k=False
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)

    L_MOTOR1.ChangeDutyCycle(32)
    R_MOTOR2.ChangeDutyCycle(33)
    stream1 = camera.capture_continuous(
        rawCapture, format="bgr", use_video_port=True)

    # R_MOTOR1.ChangeDutyCycle(0)
    # L_MOTOR2.ChangeDutyCycle(0)
    # cv2.waitKey(2000)
    for frame in stream:
        image1 = frame.array
        key = cv2.waitKey(1) & 0xFF
        # R_MOTOR1.ChangeDutyCycle(43)
        # L_MOTOR2.ChangeDutyCycle(43)
        gausss1 = cv2.GaussianBlur(image1, (5, 5), 0)

        gray1 = cv2.cvtColor(gausss1, cv2.COLOR_BGR2GRAY)
        ret, thresh11 = cv2.threshold(
            gray1, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # th31 = cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

        # hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # gauss = cv2.GaussianBlur(hsv,(5,5),0)

        # low_b = np.array([0,0,168])
        # high_b = np.array([172,111,255])

        # mask = cv2.inRange(gauss, low_b, high_b)

        # out1 = cv2.bitwise_and(image,image, mask= mask)

        # out3 = cv2.bitwise_not(mask)

        contours, hierarchy = cv2.findContours(
            thresh11, 1, cv2.CHAIN_APPROX_NONE)

        c = max(contours, key=cv2.contourArea)
        approx1 = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)

        x1, y1, w1, h1 = cv2.boundingRect(c)
        print("area == ======================================================================================================================================================================== ", w1, h1, len(c))

        if w1 > 10 and w1 < 290 and h1 > 40 and h1 < 520 and ter > count1 + 4 and count > count2 + 4:
            cv2.waitKey(100)
            print("fnrefuyrgfygfyruyerfyurevyfuehiujoifjwu9hfywiyfhu34ty4ikr3h   ", w1)
            R_MOTOR2.ChangeDutyCycle(0)
            L_MOTOR1.ChangeDutyCycle(0)

            cv2.destroyAllWindows()
            rawCapture.truncate(0)
            # cv2.waitKey(500)
            traversel(stream)
            print("going in traversel ")
            # cv2.waitKey(1000)
            print("-delay for sprint  ------------------ 0dbufbhrh")
            break

        # print("area == ======================================================================================================================================================================== ",w1,h1,len(c) )

        cv2.drawContours(image1, [approx1], 0, (0, 255, 255), 5)
        cv2.imshow("new turn image", image1)
        cv2.imshow("kem cho ", thresh11)
        cv2.waitKey(3)
        rawCapture.truncate(0)
        if key == ord("q"):
            cv2.destroyAllWindows()
            GPIO.cleanup()
            break


def straight(stream):
    traversel(stream)


def wait(stream):
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    print("wait")
    motor_pause(5)


def motor_pause(secs):
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    L_MOTOR2.ChangeDutyCycle(0)
    R_MOTOR2.ChangeDutyCycle(0)
    time.sleep(secs)
    print(motor_pause)


def traversel(stream):
    # initialize the camera and grab a reference to the raw camera capture
    # camera = PiCamera()
    # camera.resolution = (640, 480)
    # camera.framerate = 64
    # rawCapture = PiRGBArray(camera, size=(640, 480))
    # stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)
    # motor_pin_setup()
    # L_MOTOR1.ChangeDutyCycle(39.6)
    # R_MOTOR1.ChangeDutyCycle(42.8)
    # p=40.225
    # pp=41.8
    # ter=0
    fagg = 0
    p = 37
    pp = 39
    r = p
    global ter
    ter = 0
    l = pp
    prevtime = 0
    preverror = 0
    # GPIO.add_event_detect(e1, GPIO.FALLING,callback=button_pressed_callback)
    # GPIO.add_event_detect(e2, GPIO.FALLING,callback=callw)
    flag2 = 0
    flag1 = 0
    fag1 = 0
    fag2 = 0
    fag3 = 0
    fag4 = 0
    check = 0
    fag5 = 0
    fag6 = 0
    cap = 0
    # capture frames from the camera
    for frame in stream:
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        fag6 = 0
        image = frame.array
        key = cv2.waitKey(1) & 0xFF
        kk = image.shape
        # print("uevghdcegvfgyurgvuhefgyvierru8yfg7845gfuefcvergdiufg76refhgrugyrgwuyfewgf34fgur3fg6fg5h5fbuyeryfhejhfygrghejhgeggiu4h",kk)
        frame = image[:, :]
        # clear the stream in preparation for the next frame
        gausss = cv2.GaussianBlur(frame, (5, 5), 0)

        gray = cv2.cvtColor(gausss, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(
            gray, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        th3 = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gauss = cv2.GaussianBlur(hsv, (5, 5), 0)
        # ret,thresh1 = cv2.threshold(gauss,100,255,cv2.THRESH_BINARY_INV)

        low_b = np.array([0, 0, 168])
        high_b = np.array([172, 111, 255])
        yellow_lower = np.array([20, 100, 100])
        yellow_upper = np.array([30, 255, 255])
        mask = cv2.inRange(gauss, low_b, high_b)
        mask1 = cv2.inRange(gauss, yellow_lower, yellow_upper)
        # mask3 = cv2.inRange(thresh1, low_b, high_b)
        # out5 = cv2.bitwise_and(image,image, mask3= mask3)
        # out4 = cv2.bitwise_not(out5)
        out1 = cv2.bitwise_and(image, image, mask=mask)
        # contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE

        out2 = cv2.bitwise_and(image, image, mask=mask1)
        # contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE
        out3 = cv2.bitwise_not(mask)

        # out3 = cv2.GaussianBlur(out2,(5,5),0)

        contours, hierarchy = cv2.findContours(
            thresh1, 1, cv2.CHAIN_APPROX_NONE)
        # rawCapture.truncate(0)

        # left(stream,rawCapture)
        U = 0
        contours1, hierarchy1 = cv2.findContours(
            mask1, 1, cv2.CHAIN_APPROX_NONE)
        # approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)

        c = max(contours, key=cv2.contourArea)
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)

        x, y, w, h = cv2.boundingRect(c)

        # print("area ==  ",w,h,len(c) )
        print("area == ======================================================================================================================================================================== ", w, h, len(c))

        # approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)
        # x,y,w,h=cv2.boundingRect(c)
        cv2.drawContours(image, [approx], 0, (0, 255, 255), 5)
        # contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)

        M = cv2.moments(c)
        flag3 = 0
        qq = 0
        cv2.imshow('thresh1', thresh1)
        cv2.imshow('3', th3)

        # cv2.imshow('hsv',hsv)
        # cv2.imshow('mask',mask)
        # cv2.imshow('and',out)
        cv2.imshow('not', out2)
        # cv2.imshow('thresh',thresh1)
        # cv2.imshow('thresh mask',mask3)
        # cv2.imshow('thresh',)
        # cv2.imshow('thresh not',out4)
        # cv2.imshow('thresh and',out5)

        cv2.imshow('maitrey', image)
        cv2.waitKey(3)

        if cap == 0:
            cv2.waitKey(3000)
            cap = 1
        # cv2.waitKey(3)

        if fag4 == 1:
            cv2.waitKey(6000)
            fag1 = 0
            fag2 = 0
            fag3 = 0
            fagg = 0
            fag5 = 0
            fag4 = 0
        if fag5 == 0:
            for contour in contours1:
                print("__________________------------------------------------------------------------2345-------------------------------------------------------------------------------------------------")
                # flag3=1
                # flag4=1
                R_MOTOR1.ChangeDutyCycle(0)
                L_MOTOR1.ChangeDutyCycle(0)
                cv2.waitKey(3000)
                print(
                    "egfygewfggffeywfiuehfjhroir8u893263trkhou099ruouhkegtugtiueyithto23how3wht3oith32oi ", count, ter)
                # wer = 35 - count
                # print(len(contour))
                qq = qq+1
                approx = cv2.approxPolyDP(
                    contour, 0.01 * cv2.arcLength(contour, True), True)
                # if len(contour) >2000:
                # 	flag=1
                cv2.drawContours(image, [approx], 0, (0, 0, 255), 5)
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                if fag1 == 0:
                    fag2 = 1
                    fag1 = 1
                fag5 = 1
                break
                # cc=count
                # while count < cc +23:
                # print("ready to turn ")
                # left()

        if fag2 == 1:
            fag3 = 1
            # print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # check = count + wer
            # print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",check,count)
            fag2 = 0

        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX : "+str(cx)+"  CY : "+str(cy))
            time.sleep(0.4)
        er = image.shape
        er = er[1]/2
        error = cx-er
        currtime = time.time()
        dt = currtime-prevtime
        dt = currtime-prevtime
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  ter ===   ", ter)
        if ter > 33:
            # cv2.waitKey(9000)
            print("##################################################################################################################################")
            R_MOTOR1.ChangeDutyCycle(0)
            L_MOTOR1.ChangeDutyCycle(0)
            cv2.waitKey(1000)
            print("##################################################################################################################################")
            ter = 0
            # cv2.waitKey(1000)

            rawCapture.truncate(0)
            cv2.destroyAllWindows()
            # cv2.waitKey(4000)
            print("all windows break traversel")
            break
            return
            # left(stream)
            # GPIO.cleanup()
            print("##################################################################################################################################")
            R_MOTOR1.ChangeDutyCycle(0)
            L_MOTOR1.ChangeDutyCycle(0)
            # cv2.waitKey(1000)
            ter = 0
            check = 0
            fag3 = 0
            fag4 = 1
            fag6 = 1
        # cv2.waitKey(9000)

        if error > 20 and fag6 == 0:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  pass 1 ===   ", ter)

            print("move left ", error)

            pout = 0.02*error
            de = error-preverror
            dout = 0.0001*de/dt
            l = pp+pout+dout
            r = p-pout+dout
            if r > 48:
                r = 48
            if l < 32:
                l = 32
            if r < 32:
                r = 32
            if l > 48:
                l = 48
            # print("r l ========================================================================================================================================== ",r,l)

            R_MOTOR1.ChangeDutyCycle(r)
            L_MOTOR1.ChangeDutyCycle(l)
            time.sleep(0.0)
            # if count > check and fag3 == 1:
            # left()
            # fag3==0
        elif error < -20 and fag6 == 0:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  pass 2 ===   ", ter)

            print("move right ", error)
            error = -error
            pout = 0.002*error
            de = error-preverror
            dout = 0.0001*de/dt
            ll = pp-pout+dout
            rr = p+pout+dout
            if rr > 48:
                rr = 48
            if ll < 32:
                ll = 32

            if rr < 32:
                rr = 32
            if ll > 48:
                ll = 48
            # print("rr lll ====            ================================================================================================================== ",rr,ll)
            R_MOTOR1.ChangeDutyCycle(rr)
            L_MOTOR1.ChangeDutyCycle(ll)
            time.sleep(0.4)
            # if count > check and fag3 == 1:
            # left()
            # fag3==0
        else:
            if fag6 == 0:
                R_MOTOR1.ChangeDutyCycle(p)
                L_MOTOR1.ChangeDutyCycle(pp)
                time.sleep(0.4)
            else:
                print("indian space rearch center")
            # if count > check and fag3 == 1:
                # left()
                # fag3==0

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  pass 3 ===   ", ter)

        print("error 000000000000000000=-99t8y45g", error)
        # for contour in contours:
        # x,y,w,h=cv2.boundingRect(contour)
        # M = cv2.moments(contour)
        # if M["m00"] !=0 :
        # cx = int(M['m10']/M['m00'])
        # cy = int(M['m01']/M['m00'])
        # #print("CX : "+str(cx)+"  CY : "+str(cy))
        # time.sleep(0.4)

        # if  w > 25 and w < 45 and h > 55 and h < 220 and len(contour) <500 and  len(contour) > 130 and cx > 15 and cx < 340:

        # x,y,w,h=cv2.boundingRect(contour)
        # print("hyyyyyyyyyyyyyyyyyyyyyyyyyy",x,y,w,h,len(contour))
        # approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(contour, True), True)
        # x,y,w,h=cv2.boundingRect(contour)
        # cv2.drawContours(image, [approx], 0, (0, 255, 255), 5)
        # M = cv2.moments(contour)

        # # if M["m00"] !=0 :
        # # cx = int(M['m10']/M['m00'])
        # # cy = int(M['m01']/M['m00'])
        # print("CX : "+str(cx)+"  CY : "+str(cy))
        # # time.sleep(0.4)

        # h=image.shape
        # print(h)
        # if cx < 290 :
        # print("right")
        # r=r-2
        # l=l+2
        # #R_MOTOR1.ChangeDutyCycle(r)
        # #L_MOTOR1.ChangeDutyCycle(l)
        # time.sleep(0.4)
        # #GPIO.output(L_PWM_PIN1,GPIO.HIGH)
        # #E1.ChangeDutyCycle(100)
        # r=p
        # l=pp
        # #GPIO.output(R_PWM_PIN1,GPIO.LOW)
        # #E2.ChangeDutyCycle(100)
        # elif cx > 330 :
        # print("left")
        # r=r+2
        # l=l-2
        # #R_MOTOR1.ChangeDutyCycle(r)
        # #L_MOTOR1.ChangeDutyCycle(l)
        # #GPIO.output(L_PWM_PIN1,GPIO.LOW)
        # #E1.ChangeDutyCycle(100)
        # r=p
        # l=pp

        # #GPIO.output(R_PWM_PIN1,GPIO.HIGH)
        # #E2.ChangeDutyCycle(100)
        # else :
        # print("qwduyqfd")
        # #R_MOTOR1.ChangeDutyCycle(r)
        # #L_MOTOR1.ChangeDutyCycle(l)
        # time.sleep(0.4)

        # #GPIO.output(L_PWM_PIN1,GPIO.HIGH)

        # GPIO.output(R_PWM_PIN1,GPIO.HIGH)

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  pass 3 ===   ", ter)
        # cv2.waitKey(9000)

        preverror = error
        prevtime = currtime
        rawCapture.truncate(0)
        # cv2.imshow('maitrey',image)
        # cv2.imshow('mask',mask)
        # cv2.imshow('mask1',mask1)
        # cv2.imshow('out',out)
        cv2.waitKey(1)
        # rawCapture.truncate(0)

        # show the frame
        # cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  pass 4 ===   ", ter)
        # cv2.waitKey(9000)

        # if the `q` key was pressed, break from the loop and close display window
        if key == ord("q"):
            cv2.destroyAllWindows()
            GPIO.cleanup()
            break


def setup_client(host, port):
    """
    Purpose:
    ---
    This function creates a new socket client and then tries
    to connect to a socket server.

    Input Arguments:
    ---
    `host` :	[ string ]
            host name or ip address for the server

    `port` : [ string ]
            integer value specifying port name
    Returns:

    `client` : [ socket object ]
                a new client socket object
    ---


    Example call:
    ---
    client = setup_client(host, port)
    """

    client = None

    ################## ADD YOUR CODE HERE	##################
    # client=socket.socket(socket.AF_INET, sock			words = i.split('_')et.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(client)
    print(host, port)
    client.connect((host, port))

    ##########################################################

    return client


def receive_message_via_socket(client):
    """
    Purpose:
    ---
    This function listens for a message from the specified
    socket connection and returns the message when received.

    Input Arguments:
    ---
    `client` :	[ socket object ]
            client socket object created by setup_client() function
    Returns:
    ---
    `message` : [ string ]
            message received through socket communication

    Example call:
    ---
    message = receive_message_via_socket(connection)
    """

    message = None

    ################## ADD YOUR CODE HERE	##################
    message = client.recv(256).decode('utf-8')

    ##########################################################

    return message


def send_message_via_socket(client, message):
    """
    Purpose:
    ---
    This function sends a message over the specified socket connection

    Input Arguments:
    ---
    `client` :	[ socket object ]
            client socket object created by setup_client() function

    `message` : [ string ]
            message sent through socket communication

    Returns:
    ---
    None

    Example call:
    ---
    send_message_via_socket(connection, message)
    """

    ################## ADD YOUR CODE HERE	##################
    msg = message.encode('utf-8')
    client.send(msg)

    ##########################################################

    ##########################################################


def button_pressed_callback(channel):
    global count
    count = count+1
    # print("count! of encoder 1",count)
    # return count


def callw(channel):
    global fagg
    global ter
    ter = ter+1
    if ter > 35:
        # ter=0
        R_MOTOR1.ChangeDutyCycle(0)
        L_MOTOR1.ChangeDutyCycle(0)
        print("yeh mene stop kiy ahai function")
        cv2.waitKey(3000)
        fagg = 1
    print("count! of envcoder 2", ter)
    # return ter


def wait():
    time.sleep(5)


if __name__ == "__main__":

    host = "10.25.2.249"
    port = 5050
    #
    # 		##
    # 		redPin = 24
    # 		gndPin = 23
    # 		greenPin = 5
    # 		bluePin = 18
    #
    # 		## PWM values to be set for rgb led to display different colors
    # 		pwm_values = {"Red": (255, 0, 0), "Blue": (0, 0, 255), "Green": (0, 255, 0), "Orange": (255, 35, 0), "Pink": (255, 0, 122), "Sky Blue": (0, 100, 100)}
    #
    #
    # 		## Configure rgb led pins
    # 		rgb_led_setup()
    #
    #
    # Set up new socket client and connect to a socket server
    try:
        client = setup_client(host, port)

    except socket.error as error:
        print("Error in setting up server")
        print(error)
        sys.exit()

    # Wait for START command from socket_server_rgb.pys
    message = receive_message_via_socket(client)
    if message == "START":
        print("\nTask 3D Part 3 execution started !!")
    motor_pin_setup()
    rgb_led_setup()
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    stream = camera.capture_continuous(
        rawCapture, format="bgr", use_video_port=True)
    GPIO.add_event_detect(e1, GPIO.FALLING, callback=button_pressed_callback)
    GPIO.add_event_detect(e2, GPIO.FALLING, callback=callw)

    while True:
        # Receive message from socket_server_rgb.py
        # camera = PiCamera()
        # camera.resolution = (640, 480)

        # camera.framerate = 32
        # rawCapture = PiRGBArray(camera, size=(640, 480))
        # stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)

        message = receive_message_via_socket(client)

        # If received message is STOP, break out of loop
        if message == "STOP":
            print("\nTask 3D Part 3 execution stopped !!")
            break
        # else:
            # print("Color received: " + message)
        if message == "Sky Blue":
            rgb_led_set_color(message)
        if message == "Red":
            rgb_led_set_color(message)
        if message == "Green":
            rgb_led_set_color(message)
        if message == "Pink":
            print("pink")
            rgb_led_set_color(message)
            time.sleep(5)

        if message == "Orange":
            print("orange ")
            rgb_led_set_color(message)
            time.sleep(5)
        if message == "Blue":
            rgb_led_set_color(message)

        if message == "LEFT":
            left(stream)
            # time.sleep(2)
            motor_pause(0.5)

        if message == "RIGHT":
            right(stream)
            # time.sleep(2)
            motor_pause(0.5)

        if message == "STRAIGHT":
            straight(stream)
            time.sleep(2)
            motor_pause(0.5)

        if message == "WAIT_5":
            wait()
            time.sleep(0.5)
        kkkk = "NEXT"
        send_message_via_socket(client, kkkk)

    print("maitrey")
