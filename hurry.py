'''
*****************************************************************************************
*
*        		     ===============================================
*           		       Pharma Bot (PB) Theme (eYRC 2022-23)
*        		     ===============================================
*
*  This script contains all the past implemented functions of Pharma Bot (PB) Theme 
*  (eYRC 2022-23).
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			PB_theme_functions.py
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
from zmqRemoteApi import RemoteAPIClient
import traceback
import zmq
import numpy as np
import cv2
from pyzbar.pyzbar import decode
import json
from cv2 import aruco
import math
#from pyzbar import pyzbar

##############################################################

################# ADD UTILITY FUNCTIONS HERE #################


##############################################################


################## ADD SOCKET COMMUNICATION ##################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 3D for setting up a Socket
Communication Server in this section
"""


def setup_server(host, port):
    """
    Purpose:
    ---
    This function creates a new socket server and then binds it 
    to a host and port specified by user.

    Input Arguments:
    ---
    `host` :	[ string ]
                    host name or ip address for the server

    `port` : [ string ]
                    integer value specifying port name
    Returns:

    `server` : [ socket object ]
    ---


    Example call:
    ---
    server = setupServer(host, port)
    """

    server = None

    ################## ADD YOUR CODE HERE	##################
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    ##########################################################

    return server


def setup_connection(server):
    """
    Purpose:
    ---
    This function listens for an incoming socket client and
    accepts the connection request

    Input Arguments:
    ---
    `server` :	[ socket object ]
                    socket object created by setupServer() function
    Returns:
    ---
    `server` : [ socket object ]

    Example call:
    ---
    connection = setupConnection(server)
    """
    connection = None
    address = None

    ################## ADD YOUR CODE HERE	##################
    server.listen()
    # while True:
    connection, address = server.accept()

    ##########################################################

    return connection, address


def receive_message_via_socket(connection):
    """
    Purpose:
    ---
    This function listens for a message from the specified
    socket connection and returns the message when received.

    Input Arguments:
    ---
    `connection` :	[ connection object ]
                    connection object created by setupConnection() function
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
    message = connection.recv(64).decode('utf-8')

    ##########################################################

    return message


def send_message_via_socket(connection, message):
    """
    Purpose:
    ---
    This function sends a message over the specified socket connection

    Input Arguments:
    ---
    `connection` :	[ connection object ]
                    connection object created by setupConnection() function

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
    connection.send(msg)

    ##########################################################

##############################################################
##############################################################


######################### ADD TASK 2B ########################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 2B for reading QR code from
CoppeliaSim arena in this section
"""


def read_qr_code(sim):
    """
    Purpose:
    ---
    This function detects the QR code present in the CoppeliaSim vision sensor's 
    field of view and returns the message encoded into it.

    Input Arguments:
    ---
    `sim`    :   [ object ]
            ZeroMQ RemoteAPI object

    Returns:
    ---
    `qr_message`   :    [ string ]
            QR message retrieved from reading QR code

    Example call:
    ---
    control_logic(sim)
    """
    qr_message = None

    ##############  ADD YOUR CODE HERE  ##############
    m = sim.getObject("/vision_sensor")
    qr_message = None
    ##############  ADD YOUR CODE HERE  ##############
    # Retrieve the handle of the Arena_dummy scene object.
    # e=sim.getObject("/left_joint")
    # r=sim.getObject("/right_joint")
    # sim.setJointTargetVelocity(e,0)
    # sim.setJointTargetVelocity(r,0)
    # arena_dummy_handle = sim.getObject("/Arena_dummy")

    # Retrieve the handle of the child script attached to the Arena_dummy scene object.
    # childscript_handle = sim.getScript(sim.scripttype_childscript, arena_dummy_handle, "")

    # Call the activate_qr_code() function defined in the child script to make the QR code visible at checkpoint E
    # sim.callScriptFunction("activate_qr_code", childscript_handle, "checkpoint E")

    img1, resX, resY = sim.getVisionSensorCharImage(m)
    # print(type(resX))
    # resX=resX-20
    # print(resX)
    img1 = np.frombuffer(img1, dtype=np.uint8).reshape(resY, resX, 3)
    img1 = cv2.flip(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), 0)
    # print(img.shape)
    img1 = img1[0:512, 70:442]
    # cv2.imshow('maitrey',img1)
    # print("{{{{{{{{{{{{{{{{{{{{{br")
    qr_message = decode(img1)
    # qr_message=d.data.decode('utf-8')
    # print("***************************************************",qr_message)

    ##################################################

    ##################################################

    return qr_message

##############################################################
##############################################################


############### ADD ARENA PARAMETER DETECTION ################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 1A and 3A for detecting arena parameters
from configuration image in this section
"""


def detect_all_nodes(image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a list of
    nodes in which traffic signals, start_node and end_node are present in the image

    Input Arguments:
    ---
    `maze_image` :	[ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `traffic_signals, start_node, end_node` : [ list ], str, str
                    list containing nodes in which traffic signals are present, start and end node too

    Example call:
    ---
    traffic_signals, start_node, end_node = detect_all_nodes(maze_image)
    """
    traffic_signals = []
    start_node = ""
    end_node = ""

############## ADD YOUR CODE HERE	##############
    traffic_signals = []
    start_node = ""
    end_node = ""

    ############## ADD YOUR CODE HERE	##############
    frame = image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    li = []
    for i in range(0, 3):
        if i == 0:
            # print("maitrey")
            mask = cv2.inRange(hsv, (0, 100, 20), (10, 255, 255))
        if i == 1:
            # print("patel")
            mask = cv2.inRange(hsv, (36, 50, 70), (89, 255, 255))
        if i == 2:
            # print("impossible")
            mask = cv2.inRange(hsv, (129, 50, 70), (158, 255, 255))

        # mask=cv2.inRange(hsv,l_b,u_b)
        # mask=cv2.inRange(hsv,(0,100,20),(10,255,255))
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("frames", frame)
        # cv2.imshow("hsv", hsv)
        # cv2.imshow("musk", mask)
        # cv2.imshow("res", res)
        imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
        # cv2.imshow('thresh image ',thrash)

        contours, _ = cv2.findContours(
            thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.waitKey(1)
        # cv2.imshow(" new", frame)
        for contour in contours:
            approx = cv2.approxPolyDP(
                contour, 0.01 * cv2.arcLength(contour, True), True)
            # cv2.drawContours(frame, [approx], 0, (0, 255, 155), 2)
            # cv2.imshow('contour',frame)
            M = cv2.moments(contour)
            if len(approx) == 4 and len(contour) < 50:
                # print(len(contour))
                if M['m00'] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                # print(cx,cy)
                cy = cy/100
                cy = int(cy)
                if cx == 100:
                    w = 'A'
                elif cx == 200:
                    w = 'B'
                elif cx == 300:
                    w = 'C'
                elif cx == 400:
                    w = 'D'
                elif cx == 500:
                    w = 'E'
                elif cx == 600:
                    w = 'F'
                elif cx == 700:
                    w = 'G'

                q = w+str(cy)
                li.append(q)
        if i == 0:
            traffic_signals = li
            # print("'traffic signals':",end ='')
            # print(traffic_signals)

        if i == 1:
            start_node = li[0]
            # print("'start node':",end ='')
            # print(start_node)

        if i == 2:
            end_node = li[0]
            # print("'End node':",end ='')
            # print(end_node)

        # print("'traffic signals':",end ='')
        # print(li)
        li = []

    ##################################################


##################################################

    return traffic_signals, start_node, end_node


def detect_horizontal_roads_under_construction(image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a list
    containing the missing horizontal links

    Input Arguments:
    ---
    `maze_image` :	[ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `horizontal_roads_under_construction` : [ list ]
                    list containing missing horizontal links

    Example call:
    ---
    horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
    """
    horizontal_roads_under_construction = []

    ############## ADD YOUR CODE HERE	##############
    q = 100
    w = 200
    for j in range(1, 6):
        qq = 96
        ww = 105

        for i in range(1, 7):

            crop_img = image[qq:ww, q:w]
            # cv2.imshow('cropimge',crop_img)
            cv2.waitKey(2)
            gray = cv2.cvtColor(crop_img, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(gray, (0, 0, 231), (180, 18, 255))
            res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
            # cv2.imshow('res image ',res)
            imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
            # cv2.imshow('thresh image ',thrash)
            contours, _ = cv2.findContours(
                thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            cv2.waitKey(1)
            # print(len(contours))
            # cv2.imshow(" new", img)
            for contour in contours:
                approx = cv2.approxPolyDP(
                    contour, 0.01 * cv2.arcLength(contour, True), True)
                # cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
                # cv2.imshow('contour',crop_img)

                if j == 1:
                    u = 'A'+str(i)
                    z = 'B'+str(i)
                    v = u+'-'+z
                elif j == 2:
                    u = 'B'+str(i)
                    z = 'C'+str(i)
                    v = u+'-'+z
                elif j == 3:
                    u = 'C'+str(i)
                    z = 'D'+str(i)
                    v = u+'-'+z
                elif j == 4:
                    u = 'D'+str(i)
                    z = 'E'+str(i)
                    v = u+'-'+z
                elif j == 5:
                    u = 'E'+str(i)
                    z = 'F'+str(i)
                    v = u+'-'+z
                elif j == 6:
                    u = 'F'+str(i)
                    z = 'G'+str(i)
                    v = u+'-'+z

                # print(v)
                horizontal_roads_under_construction.append(v)
                # print(list)

            qq = qq+100
            ww = ww+100
        q = q+100
        w = w+100

    ##################################################
    cv2.waitKey(0)

    ##################################################

    return horizontal_roads_under_construction


def detect_vertical_roads_under_construction(image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a list
    containing the missing vertical links

    Input Arguments:
    ---
    `maze_image` :	[ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `vertical_roads_under_construction` : [ list ]
                    list containing missing vertical links

    Example call:
    ---
    vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
    """
    vertical_roads_under_construction = []

    ############## ADD YOUR CODE HERE	##############
    qq = 95
    ww = 107
    for j in range(1, 7):
        q = 100
        w = 200

        for i in range(1, 6):

            crop_img = image[q:w, qq:ww]
            # cv2.imshow('cropimge',crop_img)
            cv2.waitKey(2)
            gray = cv2.cvtColor(crop_img, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(gray, (0, 0, 231), (180, 18, 255))
            res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
            # cv2.imshow('res image ',res)
            imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
            # cv2.imshow('thresh image ',thrash)
            contours, _ = cv2.findContours(
                thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            cv2.waitKey(1)
            # print(len(contours))
            # cv2.imshow(" new", img)
            for contour in contours:
                approx = cv2.approxPolyDP(
                    contour, 0.01 * cv2.arcLength(contour, True), True)
                # cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
                # cv2.imshow('contour',crop_img)
                k = i
                l = i+1

                if j == 1:
                    u = 'A'+str(k)
                    z = 'A'+str(l)
                    v = u+'-'+z
                elif j == 2:
                    u = 'B'+str(k)
                    z = 'B'+str(l)
                    v = u+'-'+z
                elif j == 3:
                    u = 'C'+str(k)
                    z = 'C'+str(l)
                    v = u+'-'+z
                elif j == 4:
                    u = 'D'+str(k)
                    z = 'D'+str(l)
                    v = u+'-'+z
                elif j == 5:
                    u = 'E'+str(k)
                    z = 'E'+str(l)
                    v = u+'-'+z
                elif j == 6:
                    u = 'F'+str(k)
                    z = 'F'+str(l)
                    v = u+'-'+z
                elif j == 7:
                    u = 'G'+str(k)
                    z = 'G'+str(l)
                    v = u+'-'+z

                # print(v)
                vertical_roads_under_construction.append(v)
                # print(list)

            q = q+100
            w = w+100
        qq = qq+100
        ww = ww+100
    # print("'vertical_road_under_construction':",end ='')
    # print(vertical_roads_under_construction)

    cv2.waitKey(0)
    ##################################################

    ##################################################

    return vertical_roads_under_construction


def detect_medicine_packages(image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a nested list of
    details of the medicine packages placed in different shops

    ** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers 
       as well as in the alphabetical order of colors.
       For example, the list should first have the packages of shop_1 listed. 
       For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.

    Input Arguments:
    ---
    `maze_image` :	[ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `medicine_packages` : [ list ]
                    nested list containing details of the medicine packages present.
                    Each element of this list will contain 
                    - Shop number as Shop_n
                    - Color of the package as a string
                    - Shape of the package as a string
                    - Centroid co-ordinates of the package
    Example call:
    ---
    medicine_packages = detect_medicine_packages(maze_image)
    """
    medicine_packages = []

    ############## ADD YOUR CODE HERE	##############
    z = 100
    q = 200
    for i in range(0, 6):
        # print(z,q)
        cropped_image = image[100:200, z:q]
        # cv2.waitKey(0)
        # print(z,q)
        # cv2.imshow('corp 1',cropped_image)
        gray = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2HSV)
        # cv2.imshow('gray image ',gray)
        for p in range(0, 4):
            # print(p)
            if p == 3:
                l_b = (25, 50, 70)
                h_b = (52, 255, 255)
            elif p == 2:
                l_b = (128, 50, 70)
                h_b = (160, 255, 255)
            elif p == 1:
                l_b = (90, 50, 70)
                h_b = (128, 255, 255)

            elif p == 0:
                # print("ooooo")
                l_b = (52, 50, 70)
                h_b = (89, 255, 255)

            mask = cv2.inRange(gray, l_b, h_b)
            res = cv2.bitwise_and(cropped_image, cropped_image, mask=mask)
            # cv2.imshow('res image ',res)
            imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
            # cv2.imshow('thresh image ',thrash)
            contours, _ = cv2.findContours(
                thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            cv2.waitKey(1)
            # cv2.imshow(" new", img)
            for contour in contours:
                approx = cv2.approxPolyDP(
                    contour, 0.01 * cv2.arcLength(contour, True), True)
                # cv2.drawContours(cropped_image, [approx], 0, (0, 0, 255), 2)
                # cv2.imshow('contour',cropped_image)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                if len(approx) == 3:
                    # print('triangle',p)
                    li = []
                    www = str(i+1)
                    vv = 'Shop_'+www
                    li.append(vv)
                    if p == 0:
                        li.append('Green')
                    elif p == 1:
                        li.append('Orange')
                    elif p == 2:
                        li.append('Pink')
                    else:
                        li.append('Skyblue')
                    li.append('Triangle')
                    M = cv2.moments(contour)
                    if M['m00'] != 0:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                    # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
                    l = []
                    e = i+1
                    cx = e*100+cx
                    cy = 100+cy
                    l.append(cx)
                    l.append(cy)
                    li.append(l)
                    # print(cx,cy)
                    # print(li)
                    medicine_packages.append(li)
                    # cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                elif len(approx) == 4:

                    li = []
                    ww = str(i+1)
                    v = 'Shop_'+ww
                    li.append(v)
                    if p == 0:
                        li.append('Green')
                    elif p == 1:
                        li.append('Orange')
                    elif p == 2:
                        li.append('Pink')
                    else:
                        li.append('Skyblue')
                    li.append('Square')
                    M = cv2.moments(contour)
                    if M['m00'] != 0:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                    # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
                    l = []
                    t = i+1
                    cx = t*100+cx
                    cy = 100+cy
                    l.append(cx)
                    l.append(cy)
                    li.append(l)
                    # print(cx,cy)
                    # print(li)
                    medicine_packages.append(li)
                else:
                    li = []
                    w = str(i+1)
                    f = 'Shop_'+w
                    li.append(f)
                    if p == 0:
                        li.append('Green')
                    elif p == 1:
                        li.append('Orange')
                    elif p == 2:
                        li.append('Pink')
                    else:
                        li.append('Skyblue')
                    li.append('Circle')
                    M = cv2.moments(contour)
                    if M['m00'] != 0:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                    # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
                    l = []
                    g = i+1
                    cx = g*100+cx
                    cy = 100+cy
                    l.append(cx)
                    l.append(cy)
                    li.append(l)
                    # print(cx,cy)
                    # print(li)
                    medicine_packages.append(li)
                    # cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        # cv2.waitKey()
        z = z+100
        q = q+100
    # print(medicine_packages_present)
    cv2.waitKey(0)
    ##################################################

    ##################################################

    return medicine_packages


def detect_paths_to_graph(image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a dictionary of the
    connect path from a node to other nodes and will be used for path planning

    HINT: Check for the road besides the nodes for connectivity 

    Input Arguments:
    ---
    `maze_image` :	[ numpy array ]
                    numpy array of image returned by cv2 library
    Returns: U7YHGN8765
    ---
    `paths` : { dictionary }
                    Every node's connection to other node and set it's value as edge value 
                    Eg. : { "D3":{"C3":1, "E3":1, "D2":1, "D4":1}, 
                                    "D5":{"C5":1, "D2":1, "D6":1 }  }

                    Why edge value 1? -->> since every road is equal

    Example call:
    ---
    paths = detect_paths_to_graph(maze_image)
    """

    paths = {}

    ############## ADD YOUR CODE HERE	##############
    horizontal_roads_under_construction = []
    A1, A2, A3, A4, A5, A6 = {}, {}, {}, {}, {}, {}
    B1, B2, B3, B4, B5, B6 = {}, {}, {}, {}, {}, {}
    C1, C2, C3, C4, C5, C6 = {}, {}, {}, {}, {}, {}
    D1, D2, D3, D4, D5, D6 = {}, {}, {}, {}, {}, {}
    E1, E2, E3, E4, E5, E6 = {}, {}, {}, {}, {}, {}
    F1, F2, F3, F4, F5, F6 = {}, {}, {}, {}, {}, {}
    G1, G2, G3, G4, G5, G6 = {}, {}, {}, {}, {}, {}
    print("itna jaldi kyu ")
    q = 100
    w = 200
    flag = 0
    for j in range(1, 6):
        qq = 96
        ww = 105

        for i in range(1, 7):
            print("abhi toh chalu kiya hai ")
            flag = 0
            crop_img = image[qq:ww, q:w]
            # cv2.imshow('cropimge',crop_img)
            #cv2.waitKey(2)
            gray = cv2.cvtColor(crop_img, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(gray, (0, 0, 231), (180, 18, 255))
            res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
            # cv2.imshow('res image ',res)
            imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
            # cv2.imshow('thresh image ',thrash)
            contours, _ = cv2.findContours(
                thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            #cv2.waitKey(1)
            # print(len(contours))
            # cv2.imshow(" new", img)
            for contour in contours:
                print("vo hum nava ")
                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                # cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
                # cv2.imshow('contour',crop_img)
                flag = 1

                if j == 1:
                    u = 'A'+str(i)
                    z = 'B'+str(i)
                    v = u+'-'+z
                elif j == 2:
                    u = 'B'+str(i)
                    z = 'C'+str(i)
                    v = u+'-'+z
                elif j == 3:
                    u = 'C'+str(i)
                    z = 'D'+str(i)
                    v = u+'-'+z
                elif j == 4:
                    u = 'D'+str(i)
                    z = 'E'+str(i)
                    v = u+'-'+z
                elif j == 5:
                    u = 'E'+str(i)
                    z = 'F'+str(i)
                    v = u+'-'+z
                elif j == 6:
                    u = 'F'+str(i)
                    z = 'G'+str(i)
                    v = u+'-'+z

                # print(v)
                horizontal_roads_under_construction.append(v)
                print("undhyv innhhh unhhun")
                # print(list)

            if flag == 0:
                if j == 1:
                    if i == 1:
                        u = 'A'+str(i)
                        z = 'B'+str(i)
                        # q='A'+i
                        # o='B'+i
                        A1[z] = 1
                        B1[u] = 1
                        # print(A1,B1)
                    if i == 2:
                        u = 'A'+str(i)
                        z = 'B'+str(i)
                        # q='A'+i
                        # o='B'+i
                        A2[z] = 1
                        B2[u] = 1
                        # print(A2,B2)
                    if i == 3:
                        u = 'A'+str(i)
                        z = 'B'+str(i)
                        # q='A'+i
                        # o='B'+i
                        A3[z] = 1
                        B3[u] = 1
                        # print(A3,B3)
                    if i == 4:
                        u = 'A'+str(i)
                        z = 'B'+str(i)
                        # q='A'+i
                        # o='B'+i
                        A4[z] = 1
                        B4[u] = 1
                        # print(A4,B4)
                    if i == 5:
                        u = 'A'+str(i)
                        z = 'B'+str(i)
                        # q='A'+i
                        # o='B'+i
                        A5[z] = 1
                        B5[u] = 1
                        # print(A5,B5)
                    if i == 6:
                        u = 'A'+str(i)
                        z = 'B'+str(i)
                        # q='A'+i
                        # o='B'+i
                        A6[z] = 1
                        B6[u] = 1
                        # print(A6,B6)

                elif j == 2:
                    if i == 1:
                        u = 'B'+str(i)
                        z = 'C'+str(i)
                        # q='A'+i
                        # o='B'+i
                        B1[z] = 1
                        C1[u] = 1
                        # print(B1,C1)
                    if i == 2:
                        u = 'B'+str(i)
                        z = 'C'+str(i)
                        B2[z] = 1
                        C2[u] = 1
                        # q='A'+i
                        # o='B'+i
                        # print(B2,C2)
                    if i == 3:
                        u = 'B'+str(i)
                        z = 'C'+str(i)
                        B3[z] = 1
                        C3[u] = 1
                        # q='A'+i
                        # o='B'+i
                        # print(B3,C3)
                    if i == 4:
                        u = 'B'+str(i)
                        z = 'C'+str(i)
                        B4[z] = 1
                        C4[u] = 1
                        # q='A'+i
                        # o='B'+i
                        # print(B4,C4)
                    if i == 5:
                        u = 'B'+str(i)
                        z = 'C'+str(i)
                        B5[z] = 1
                        C5[u] = 1
                        # q='A'+i
                        # o='B'+i
                        # print(B5,C5)
                    if i == 6:
                        u = 'B'+str(i)
                        z = 'C'+str(i)
                        B6[z] = 1
                        C6[u] = 1
                        # q='A'+i
                        # o='B'+i
                        # print(B6,C6)

                elif j == 3:
                    if i == 1:
                        u = 'C'+str(i)
                        z = 'D'+str(i)
                        # q='A'+i
                        # o='C'+i
                        C1[z] = 1
                        D1[u] = 1
                        # print(C1,D1)
                    if i == 2:
                        u = 'C'+str(i)
                        z = 'D'+str(i)
                        # q='A'+i
                        C2[z] = 1
                        D2[u] = 1
                        # o='C'+i
                        # print(C2,D2)
                    if i == 3:
                        u = 'C'+str(i)
                        z = 'D'+str(i)
                        # q='A'+i
                        C3[z] = 1
                        D3[u] = 1
                        # o='C'+i
                        # print(C3,D3)
                    if i == 4:
                        u = 'C'+str(i)
                        z = 'D'+str(i)
                        # q='A'+i
                        # o='C'+i
                        C4[z] = 1
                        D4[u] = 1
                        # print(C4,D4)
                    if i == 5:
                        u = 'C'+str(i)
                        z = 'D'+str(i)
                        # q='A'+i
                        C5[z] = 1
                        D5[u] = 1
                        # o='C'+i
                        # print(C5,D5)
                    if i == 6:
                        u = 'C'+str(i)
                        z = 'D'+str(i)
                        # q='A'+i
                        C6[z] = 1
                        D6[u] = 1
                        # o='C'+i
                        # print(C6,D6)

                elif j == 4:
                    if i == 1:
                        u = 'D'+str(i)
                        z = 'E'+str(i)
                        # q='A'+i
                        # o='D'+i
                        D1[z] = 1
                        E1[u] = 1
                        # print(D1,E1)
                    if i == 2:
                        u = 'D'+str(i)
                        z = 'E'+str(i)
                        # q='A'+i
                        D2[z] = 1
                        E2[u] = 1
                        # o='D'+i
                        # print(D2,E2)
                    if i == 3:
                        u = 'D'+str(i)
                        z = 'E'+str(i)
                        # q='A'+i
                        D3[z] = 1
                        E3[u] = 1
                        # o='D'+i
                        # print(D3,E3)
                    if i == 4:
                        u = 'D'+str(i)
                        z = 'E'+str(i)
                        D4[z] = 1
                        E4[u] = 1
                        # q='A'+i
                        # o='D'+i
                        # print(D4,E4)
                    if i == 5:
                        u = 'D'+str(i)
                        z = 'E'+str(i)
                        # q='A'+i
                        D5[z] = 1
                        E5[u] = 1
                        # o='D'+i
                        # print(D5,E5)
                    if i == 6:
                        u = 'D'+str(i)
                        z = 'E'+str(i)
                        D6[z] = 1
                        E6[u] = 1
                        # q='A'+i
                        # o='D'+i
                        # print(D6,E6)

                elif j == 5:
                    if i == 1:
                        u = 'E'+str(i)
                        z = 'F'+str(i)
                        # q='A'+i
                        # o='E'+i
                        E1[z] = 1
                        F1[u] = 1
                        # print(E1,F1)
                    if i == 2:
                        u = 'E'+str(i)
                        z = 'F'+str(i)
                        # q='A'+i
                        E2[z] = 1
                        F2[u] = 1
                        # o='E'+i
                        # print(E2,F2)
                    if i == 3:
                        u = 'E'+str(i)
                        z = 'F'+str(i)
                        # q='A'+i
                        E3[z] = 1
                        F3[u] = 1
                        # o='E'+i
                        # print(E3,F3)
                    if i == 4:
                        u = 'E'+str(i)
                        z = 'F'+str(i)
                        # q='A'+i
                        E4[z] = 1
                        F4[u] = 1
                        # o='E'+i
                        # print(E4,F4)
                    if i == 5:
                        u = 'E'+str(i)
                        z = 'F'+str(i)
                        # q='A'+i
                        E5[z] = 1
                        F5[u] = 1
                        # o='E'+i
                        # print(E5,F5)
                    if i == 6:
                        u = 'E'+str(i)
                        z = 'F'+str(i)
                        # q='A'+i
                        E6[z] = 1
                        F6[u] = 1
                        # o='E'+i
                        # print(E6,F6)

                elif j == 6:
                    if i == 1:
                        u = 'F'+str(i)
                        z = 'G'+str(i)
                        # q='A'+i
                        # o='F'+i
                        F1[z] = 1
                        G1[u] = 1
                        # print(F1,G1)
                    if i == 2:
                        u = 'F'+str(i)
                        z = 'G'+str(i)
                        # q='A'+i
                        F2[z] = 1
                        G2[u] = 1
                        # o='F'+i
                        # print(F2,G2)
                    if i == 3:
                        u = 'F'+str(i)
                        z = 'G'+str(i)
                        # q='A'+i
                        F3[z] = 1
                        G3[u] = 1
                        # o='F'+i
                        # print(F3,G3)
                    if i == 4:
                        u = 'F'+str(i)
                        z = 'G'+str(i)
                        # q='A'+i
                        F4[z] = 1
                        G4[u] = 1
                        # o='F'+i
                        # print(F4,G4)
                    if i == 5:
                        u = 'F'+str(i)
                        z = 'G'+str(i)
                        # q='A'+i
                        F5[z] = 1
                        G5[u] = 1
                        # o='F'+i
                        # print(F5,G5)
                    if i == 6:
                        u = 'F'+str(i)
                        z = 'G'+str(i)
                        # q='A'+i
                        F6[z] = 1
                        G6[u] = 1
                        # o='F'+i
                        # print(F6,G6)

            qq = qq+100
            ww = ww+100
        q = q+100
        w = w+100

    ##################################################
    # cv2.imshow('contour',image)
    #cv2.waitKey(0)
    # print(horizontal_roads_under_construction)
    print("abhi toh baki hai ")
    vertical_roads_under_construction = []
    qq = 95
    ww = 107
    flag1=0
    for j in range(1, 7):
        print("j====",j)
        q = 100
        w = 200

        for i in range(1, 6):
            print("i=====",i)
            flag1 = 0
            crop_img = image[q:w, qq:ww]
            # cv2.imshow('cropimge',crop_img)
            #cv2.waitKey(2)
            gray = cv2.cvtColor(crop_img, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(gray, (0, 0, 231), (180, 18, 255))
            res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
            # cv2.imshow('res image ',res)
            imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
            # cv2.imshow('thresh image ',thrash)
            contours1, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            #cv2.waitKey(1)
            # print(len(contours))
            # cv2.imshow(" new", img)
            for contour in contours1:
                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                # cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
                # cv2.imshow('contour',crop_img)
                k = i
                l = i+1
                flag1 = 1
                if j == 1:
                    u = 'A'+str(k)
                    z = 'A'+str(l)
                    v = u+'-'+z
                elif j == 2:
                    u = 'B'+str(k)
                    z = 'B'+str(l)
                    v = u+'-'+z
                elif j == 3:
                    u = 'C'+str(k)
                    z = 'C'+str(l)
                    v = u+'-'+z
                elif j == 4:
                    u = 'D'+str(k)
                    z = 'D'+str(l)
                    v = u+'-'+z
                elif j == 5:
                    u = 'E'+str(k)
                    z = 'E'+str(l)
                    v = u+'-'+z
                elif j == 6:
                    u = 'F'+str(k)
                    z = 'F'+str(l)
                    v = u+'-'+z
                elif j == 7:
                    u = 'G'+str(k)
                    z = 'G'+str(l)
                    v = u+'-'+z

                # print(v)
                vertical_roads_under_construction.append(v)
                print("likdi de meri ham dum   ")

                print(list)
            if flag1 == 0:
                print('ha bhai andar = ',i,j)
                
                if j == 1:
                    if i == 1:
                        u = 'A'+str(i)
                        z = 'A'+str(i+1)
                        # q='A'+i
                        # o='B'+i
                        A1[z] = 1
                        A2[u] = 1
                        # print(A1,A2)
                    if i == 2:
                        u = 'A'+str(i)
                        z = 'A'+str(i+1)
                        # q='A'+i
                        # o='B'+i
                        A2[z] = 1
                        A3[u] = 1
                        # print(A2,A3)
                    if i == 3:
                        u = 'A'+str(i)
                        z = 'A'+str(i+1)
                        # q='A'+i
                        # o='B'+i
                        A3[z] = 1
                        A4[u] = 1
                        # print(A3,A4)
                    if i == 4:
                        u = 'A'+str(i)
                        z = 'A'+str(i+1)
                        # q='A'+i
                        # o='B'+i
                        A4[z] = 1
                        A5[u] = 1
                        # print(A4,A5)
                    if i == 5:
                        u = 'A'+str(i)
                        z = 'A'+str(i+1)
                        # q='A'+i
                        # o='B'+i
                        A5[z] = 1
                        A6[u] = 1
                        # print(A5,A6)

                elif j == 2:
                    if i == 1:
                        u = 'B'+str(i)
                        z = 'B'+str(i+1)
                        # q='A'+i
                        # o='B'+i
                        B1[z] = 1
                        B2[u] = 1
                        # print(B1,B2)
                    if i == 2:
                        u = 'B'+str(i)
                        z = 'B'+str(i+1)
                        # q='A'+i
                        B2[z] = 1
                        B3[u] = 1
                        # o='B'+i
                        # print(B2,B3)
                    if i == 3:
                        u = 'B'+str(i)
                        z = 'B'+str(i+1)
                        # q='A'+i
                        B3[z] = 1
                        B4[u] = 1
                        # o='B'+i
                        # print(B3,B4)
                    if i == 4:
                        u = 'B'+str(i)
                        z = 'B'+str(i+1)
                        # q='A'+i
                        B4[z] = 1
                        B5[u] = 1
                        # o='B'+i
                        # print(B4,B5)
                    if i == 5:
                        u = 'B'+str(i)
                        z = 'B'+str(i+1)
                        # q='A'+i
                        B5[z] = 1
                        B6[u] = 1
                        # o='B'+i
                        # print("-----------",B6)
                        # print(B5,B6)
                elif j == 3:
                    if i == 1:
                        u = 'C'+str(i)
                        z = 'C'+str(i+1)
                        # q='A'+i
                        # o='C'+i
                        C1[z] = 1
                        C2[u] = 1
                        # print(C1,C2)
                    if i == 2:
                        u = 'C'+str(i)
                        z = 'C'+str(i+1)
                        # q='A'+i
                        C2[z] = 1
                        C3[u] = 1
                        # o='C'+i
                        # print(C2,C3)
                    if i == 3:
                        u = 'C'+str(i)
                        z = 'C'+str(i+1)
                        # q='A'+i
                        C3[z] = 1
                        C4[u] = 1
                        # o='C'+i
                        # print(C3,C4)
                    if i == 4:
                        u = 'C'+str(i)
                        z = 'C'+str(i+1)
                        # q='A'+i
                        C4[z] = 1
                        C5[u] = 1
                        # o='C'+i
                        # print(C4,C5)
                    if i == 5:
                        u = 'C'+str(i)
                        z = 'C'+str(i+1)
                        # q='A'+i
                        C5[z] = 1
                        C6[u] = 1
                        # o='C'+i
                        # print(C5,C6)

                elif j == 4:
                    if i == 1:
                        u = 'D'+str(i)
                        z = 'D'+str(i+1)
                        # q='A'+i
                        # o='D'+i
                        D1[z] = 1
                        D2[u] = 1
                        # print(D1,D2)
                    if i == 2:
                        u = 'D'+str(i)
                        z = 'D'+str(i+1)
                        # q='A'+i
                        # o='D'+i
                        D2[z] = 1
                        D3[u] = 1
                        # print(D2,D3)
                    if i == 3:
                        u = 'D'+str(i)
                        z = 'D'+str(i+1)
                        # q='A'+i
                        # o='D'+i
                        D3[z] = 1
                        D4[u] = 1
                        # print(D3,D4)
                    if i == 4:
                        u = 'D'+str(i)
                        z = 'D'+str(i+1)
                        # q='A'+i
                        # o='D'+i
                        D4[z] = 1
                        D5[u] = 1
                        # print(D4,D5)
                    if i == 5:
                        u = 'D'+str(i)
                        z = 'D'+str(i+1)
                        # q='A'+i
                        # o='D'+i
                        D5[z] = 1
                        D6[u] = 1
                        # print(D5,D6)

                elif j == 5:
                    if i == 1:
                        u = 'E'+str(i)
                        z = 'E'+str(i+1)
                        # q='A'+i
                        # o='E'+i
                        E1[z] = 1
                        E2[u] = 1
                        # print(E1,E2)
                    if i == 2:
                        u = 'E'+str(i)
                        z = 'E'+str(i+1)
                        # q='A'+i
                        E2[z] = 1
                        E3[u] = 1
                        # o='E'+i
                        # print(E2,E3)
                    if i == 3:
                        u = 'E'+str(i)
                        z = 'E'+str(i+1)
                        # q='A'+i
                        E3[z] = 1
                        E4[u] = 1
                        # o='E'+i
                        # print(E3,E4)
                    if i == 4:
                        u = 'E'+str(i)
                        z = 'E'+str(i+1)
                        # q='A'+i
                        E4[z] = 1
                        E5[u] = 1
                        # o='E'+i
                        # print(E4,E5)
                    if i == 5:
                        u = 'E'+str(i)
                        z = 'E'+str(i+1)
                        # q='A'+i
                        E5[z] = 1
                        E6[u] = 1
                        # o='E'+i
                        # print(E5,E6)

                elif j == 6:
                    if i == 1:
                        u = 'F'+str(i)
                        z = 'F'+str(i+1)
                        # q='A'+i
                        # o='F'+i
                        F1[z] = 1
                        F2[u] = 1
                        # print(F1,F2)
                    if i == 2:
                        u = 'F'+str(i)
                        z = 'F'+str(i+1)
                        # q='A'+i
                        # o='F'+i
                        F2[z] = 1
                        F3[u] = 1
                        # print(F2,F3)
                    if i == 3:
                        u = 'F'+str(i)
                        z = 'F'+str(i+1)
                        # q='A'+i
                        F3[z] = 1
                        F4[u] = 1
                        # o='F'+i
                        # print(F3,F4)
                    if i == 4:
                        u = 'F'+str(i)
                        z = 'F'+str(i+1)
                        # q='A'+i
                        F4[z] = 1
                        F5[u] = 1
                        # o='F'+i
                        # print(F4,F5)
                    if i == 5:
                        u = 'F'+str(i)
                        z = 'F'+str(i+1)
                        # q='A'+i
                        F5[z] = 1
                        F6[u] = 1
                        # o='F'+i
                        # print(F5,F6)
                print('khatam',q,w,qq,ww)

            q = q+100
            w = w+100
        qq = qq+100
        ww = ww+100
    print("'vertical_road_under_construction':",end ='')
    print(vertical_roads_under_construction)
    # cv2.imshow('contour',crop_img)
    #cv2.waitKey(0)
    print("tu meri heer mai tera rannja  ")

    # print(A1)
    sorted(A1.items())
    # dict(sorted(A1.items()))
    # print("---------",A1)
    A11 = {}
    for key in sorted(A1):
        # print(key)
        A11[key] = 1
    A12 = {}
    for key in sorted(A2):
        # print(key)
        A12[key] = 1
    A13 = {}
    for key in sorted(A3):
        # print(key)
        A13[key] = 1
    A14 = {}
    for key in sorted(A4):
        # print(key)
        A14[key] = 1
    A15 = {}
    for key in sorted(A5):
        # print(key)
        A15[key] = 1
    A16 = {}
    for key in sorted(A6):
        # print(key)
        A16[key] = 1
    B11 = {}
    for key in sorted(B1):
        # print(key)
        B11[key] = 1
    B12 = {}
    for key in sorted(B2):
        # print(key)
        B12[key] = 1
    B13 = {}
    for key in sorted(B3):
        # print(key)
        B13[key] = 1
    B14 = {}
    for key in sorted(B4):
        # print(key)
        B14[key] = 1
    B15 = {}
    for key in sorted(B5):
        # print(key)
        B15[key] = 1
    B16 = {}
    for key in sorted(B6):
        # print(key)
        B16[key] = 1
    C11 = {}
    for key in sorted(C1):
        # print(key)
        C11[key] = 1
    C12 = {}
    for key in sorted(C2):
        # print(key)
        C12[key] = 1
    C13 = {}
    for key in sorted(C3):
        # print(key)
        C13[key] = 1
    C14 = {}
    for key in sorted(C4):
        # print(key)
        C14[key] = 1
    C15 = {}
    for key in sorted(C5):
        # print(key)
        C15[key] = 1
    C16 = {}
    for key in sorted(C6):
        # print(key)
        C16[key] = 1
    D11 = {}
    for key in sorted(D1):
        # print(key)
        D11[key] = 1
    D12 = {}
    for key in sorted(D2):
        # print(key)
        D12[key] = 1
    D13 = {}
    for key in sorted(D3):
        # print(key)
        D13[key] = 1
    D14 = {}
    for key in sorted(D4):
        # print(key)
        D14[key] = 1
    D15 = {}
    for key in sorted(D5):
        # print(key)
        D15[key] = 1
    D16 = {}
    for key in sorted(D6):
        # print(key)
        D16[key] = 1
    E11 = {}
    for key in sorted(E1):
        # print(key)
        E11[key] = 1
    E12 = {}
    for key in sorted(E2):
        # print(key)
        E12[key] = 1
    E13 = {}
    for key in sorted(E3):
        # print(key)
        E13[key] = 1
    E14 = {}
    for key in sorted(E4):
        # print(key)
        E14[key] = 1
    E15 = {}
    for key in sorted(E5):
        # print(key)
        E15[key] = 1
    E16 = {}
    for key in sorted(E6):
        # print(key)
        E16[key] = 1
    F11 = {}
    for key in sorted(F1):
        # print(key)
        F11[key] = 1
    F12 = {}
    for key in sorted(F2):
        # print(key)
        F12[key] = 1
    F13 = {}
    for key in sorted(F3):
        # print(key)
        F13[key] = 1
    F14 = {}
    for key in sorted(F4):
        # print(key)
        F14[key] = 1
    F15 = {}
    for key in sorted(F5):
        # print(key)
        F15[key] = 1
    F16 = {}
    for key in sorted(F6):
        # print(key)
        F16[key] = 1

    # print(A11,A12,A13,A14,A15,A16)
    # A1=sorted(A1)
    # A2=sorted(A2)
    # A3=sorted(A3)
    # A4=sorted(A4)
    # A5=sorted(A5)
    # A6=sorted(A6)
    # B1=sorted(B1)
    # B2=sorted(B2)
    # B3=sorted(B3)
    # B4=sorted(B4)
    # B5=sorted(B5)
    # B6=sorted(B6)
    # C1=sorted(C1)
    # C2=sorted(C2)
    # C3=sorted(C3)
    # C4=sorted(C4)
    # C5=sorted(C5)
    # C6=sorted(C6)
    # D1=sorted(D1)
    # D2=sorted(D2)
    # D3=sorted(D3)
    # D4=sorted(D4)
    # D5=sorted(D5)
    # D6=sorted(D6)
    # E1=sorted(E1)
    # E2=sorted(E2)
    # E3=sorted(E3)
    # E4=sorted(E4)
    # E5=sorted(E5)
    # E6=sorted(E6)
    # F1=sorted(F1)
    # F2=sorted(F2)
    # F3=sorted(F3)
    # F4=sorted(F4)
    # F5=sorted(F5)
    # F6=sorted(F6)
    print("i am very angry  ")

    # print(A1)
    paths = {}
    paths["A1"] = A11
    paths["A2"] = A12
    paths["A3"] = A13
    paths["A4"] = A14
    paths["A5"] = A15
    paths["A6"] = A16
    paths["B1"] = B11
    paths["B2"] = B12
    paths["B3"] = B13
    paths["B4"] = B14
    paths["B5"] = B15
    paths["B6"] = B16
    paths["C1"] = C11
    paths["C2"] = C12
    paths["C3"] = C13
    paths["C4"] = C14
    paths["C5"] = C15
    paths["C6"] = C16
    paths["D1"] = D11
    paths["D2"] = D12
    paths["D3"] = D13
    paths["D4"] = D14
    paths["D5"] = D15
    paths["D6"] = D16
    paths["E1"] = E11
    paths["E2"] = E12
    paths["E3"] = E13
    paths["E4"] = E14
    paths["E5"] = E15
    paths["E6"] = E16
    paths["F1"] = F11
    paths["F2"] = F12
    paths["F3"] = F13
    paths["F4"] = F14
    paths["F5"] = F15
    paths["F6"] = F16

    # paths=dict({"A1":A1})
    # paths=dict({"A2":A2})
    # paths=dict({"A3":A3})
    # paths=dict({"A4":A4})

    # print(paths)

    # return horizontal_roads_under_construction

    ##################################################
    print("insideeeeeeeeeee")
    return paths

    ##################################################


def path_planning(graph, start, end):
    """
    Purpose:
    ---
    This function takes the graph(dict), start and end node for planning the shortest path

    ** Note: You can use any path planning algorithm for this but need to produce the path in the form of 
    list given below **

    Input Arguments:
    ---
    `graph` :	{ dictionary }
                    dict of all connecting path
    `start` :	str
                    name of start node
    `end` :		str
                    name of end node


    Returns:
    ---
    `backtrace_path` : [ list of nodes ]
                    list of nodes, produced using path planning algorithm

            eg.: ['C6', 'C5', 'B5', 'B4', 'B3']

    Example call:
    ---
    arena_parameters = detect_arena_parameters(maze_image)
    """

    # backtrace_path = []
    # print('path start end ',graph,start,end)
    # ############## ADD YOUR CODE HERE	##############
    # k = start
    # min = 100
    # min3 = 100
    # jj=0
    # rrr=[]
    # backtrace_path.append(start)
    # for i in graph[k]:
    #     d = distance(i, end)
    #     # print(i,k,min,d)
    #     backtrace_path = []
    #     backtrace_path.append(start)
    #     print('back path == ',backtrace_path)
    #     if d <= min:
    #         min = d
    #         backtrace_path.append(i)
    #         # print(backtrace_path)
    #         backtrace_path = path_planning_new(graph, i, end, min, backtrace_path)
    #         # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&",backtrace_path)
    #         if backtrace_path[-1] == end:
    #             flag = 1
    #             if jj == 0:
    #                 a1 = backtrace_path
    #                 lll = len(a1)
    #                 if lll < min3:
    #                     min3 = lll
    #                     rrr = a1
    #             if jj == 1:
    #                 a2 = backtrace_path
    #                 lll = len(a2)
    #                 if lll < min3:
    #                     min3 = lll
    #                     rrr = a2

    #             if jj == 2:
    #                 a3 = backtrace_path
    #                 lll = len(a3)
    #                 if lll < min3:
    #                     min3 = lll
    #                     rrr = a3

    #             if jj == 3:
    #                 a4 = backtrace_path
    #                 lll = len(a4)
    #                 if lll < min3:
    #                     min3 = lll
    #                     rrr = a4
    #         jj=jj+1
    #         # l = len(backtrace_path)
    #         # l = l-2
    #         # # print(l,d)
    #         # if l == d:
    #         # min3 = l
    # o = len(rrr)
    # if o == 1 or o == 0:
    #     rrr = path_planning_new_2(graph, start, end, backtrace_path)

    backtrace_path = []
    backtrace_path_1 = []
    backtrace_path_2 = []
    backtrace_path_3 = []
    print('path start end ',graph,start,end)
    ############## ADD YOUR CODE HERE	##############
    k = start
    # min = 100
    # min3 = 100
    # jj=0
    # rrr=[]
    u=0
    backtrace_path.append(start)
    print('backtraace == ======================================================================================================================================',backtrace_path)
    len1=100
    len2=100
    len3=100
    for i in graph[k]:
        print('backtraace == ======================================================================================================================================',backtrace_path,i)
        backtrace_path.append(start)

        if u == 0:
            backtrace_path_1 = path_new(graph,i,end,backtrace_path)
            len1=len(backtrace_path_1)
            backtrace_path=[]
            print('back and len1',backtrace_path_1,len1)
        if u == 1:
            backtrace_path_2 = path_new(graph,i,end,backtrace_path)
            len2=len(backtrace_path_2)
            backtrace_path=[]
            print('back and len2',backtrace_path_2,len1)

        if u == 2:
            backtrace_path_3 = path_new(graph,i,end,backtrace_path)
            len3=len(backtrace_path_3)
            backtrace_path=[]
            print('back and len3',backtrace_path_3,len1)
        if u == 3:
            backtrace_path_4 = path_new(graph,i,end,backtrace_path)
            len4=len(backtrace_path_4)
            backtrace_path=[]
            print('back and len4',backtrace_path_4,len1)

        u=u+1
    print(backtrace_path_1)
    print("  ")
    print(backtrace_path_2)
    print("  ")
    print(backtrace_path_3)
    print("  ")
    print(backtrace_path_4)

    list=[len1,len2,len3,len4]
    k=min(list)
    print("k==========",k,len1,len2,len3)
    list.sort()
    kk=list[0]
    if k == len1:
        print('u==',u)
        print('return1-------------------------------------------------------------------------------------------------------------------------------------------------------- ',backtrace_path)
        return backtrace_path_1
    if k == len2:
        print('u==',u)

        print('return2 --------------------------------------------------------------------------------------------------------------------------------------------------',backtrace_path_2)
        return backtrace_path_2
    if k == len3:
        print('u==',u)

        print('return3 -----------------------------------------------------------------------------------------------------------------------------------------------',backtrace_path_3)

        return backtrace_path_3
    if k == len4:
        print('u==',u)

        print('return4 -----------------------------------------------------------------------------------------------------------------------------------------------',backtrace_path_4)

        return backtrace_path_4
        

        # u=u+1   
        # d = distance(i, end)
        # # print(i,k,min,d)
        # backtrace_path = []
        # backtrace_path.append(start)
        # print('back path == ',backtrace_path)
        # if d <= min:
        #     min = d
        #     backtrace_path.append(i)
        #     # print(backtrace_path)
        #     backtrace_path = path_planning_new(graph, i, end, min, backtrace_path)
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&",backtrace_path)
        #     if backtrace_path[-1] == end:
        #         flag = 1
        #         if jj == 0:
        #             a1 = backtrace_path
        #             lll = len(a1)
        #             if lll < min3:
        #                 min3 = lll
        #                 rrr = a1
        #         if jj == 1:
        #             a2 = backtrace_path
        #             lll = len(a2)
        #             if lll < min3:
        #                 min3 = lll
        #                 rrr = a2

        #         if jj == 2:
        #             a3 = backtrace_path
        #             lll = len(a3)
        #             if lll < min3:
        #                 min3 = lll
        #                 rrr = a3

        #         if jj == 3:
        #             a4 = backtrace_path
        #             lll = len(a4)
        #             if lll < min3:
        #                 min3 = lll
        #                 rrr = a4
        #     jj=jj+1
            # l = len(backtrace_path)
            # l = l-2
            # # print(l,d)
            # if l == d:
            # min3 = l
    # o = len(rrr)
    # if o == 1 or o == 0:
    #     rrr = path_planning_new_2(graph, start, end, backtrace_path)

#  ########################################################################
    # print("------------------",start,backtrace_path)
    # backtrace_path.append(start)
    # po='zz'
    # w='ww'
    # min=100
    # k=start
    # flag=1
    # flag1=0
    # flag2=0
    # count=0
    # while flag:
    # 	flag1=0
    # 	fagg=0
    # 	for i in graph[k]:
    # 		if fagg == 0:
    # 			qqq=k
    # 			fagg=1
    # 		# print("-------------------",i,graph[k],k)
    # 		d=distance(i,end)
    # 		if d == 0:
    # 			flag=0
    # 		# print("&&&&&",d,min)
    # 		if d <= min and flag2==0:
    # 			flag1=1
    # 			# print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    # 			min = d
    # 			# q=k
    # 			k=i
    # 		if flag2==1 and d<=min and i!=x:
    # 			flag1=1
    # 			min = d
    # 			q=k
    # 			k=i

    # 	if flag1==1:
    # 		print(min)
    # 		ooo=qqq
    # 		backtrace_path.append(k)
    # 		# print(backtrace_path)
    # 		flag2=0
    # 	if flag1==0:
    # 		count=count+1
    # 		if count == 2:
    # 			l=[]
    # 			o=k
    # 			# print(backtrace_path)
    # 			# l=path(end,graph,backtrace_path)z
    # 			flag=0
    # 			min2=100
    # 			min=20
    # 			kk=k
    # 			# print("@@@@@@@@@@@@@@@@@@@@@@",kk)
    # 			while kk != end:
    # 				flag=0
    # 				fag=1
    # 				flag10=0
    # 				flag101=0
    # 				for i in graph[kk]:
    # 					# print("###################################################################################")
    # 					if fag == 1:
    # 						q=kk
    # 						# print(q)
    # 						fag=0
    # 					# print(i)
    # 					d=distance(i,end)
    # 					if d < min:
    # 						# print("%%%%%%%%",d,min)
    # 						min = d
    # 						# print(kk)
    # 						# q=kk
    # 						kk=i
    # 						flag=1
    # 				if flag == 0:
    # 					for j in graph[kk]:
    # 						flag10=0
    # 						# print("99999999999999999999999999999999999999999",po,w,j,kk)
    # 						if j != w and j != po:
    # 							for y in backtrace_path:
    # 								if j == y:
    # 									flag10=1
    # 									po=kk
    # 							if flag10 == 0:
    # 								dd=distance(j,end)
    # 								if dd <= min2:
    # 									flag101=1
    # 									# print("xsftcdstttttttttttttttttttt",min,kk,j,q,w,flag10)
    # 									min2=dd
    # 									kk=j
    # 					if flag101 == 1:
    # 						flag10=0
    # 						backtrace_path.append(kk)
    # 						w=q
    # 						# print("------------",w)
    # 						min2=100
    # 						# print("yyyyyyyyyyyyyyyyyyyy",backtrace_path)
    # 					if flag10 == 1:
    # 						backtrace_path=backtrace_path[:-1]
    # 						ll=kk
    # 						kk=backtrace_path[-1]
    # 						w=backtrace_path[-2]
    # 						# print("ooooooooooooooooooooooooooooooooooooooooooooooooooo",kk,backtrace_path)
    # 				# if flag == 1:
    # 				# 	backtrace_path.append(kk)
    # 			# print(backtrace_path)
    # 			break

    # 		x=k
    # 		# backtrace_path=backtrace_path[:-1]
    # 		k=ooo
    # 		# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",k)
    # 		flag2=1
    ##################################################

    #return backtrace_path

def path_new(graph,start,end,backtrace_path):
    print("r@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22 start end back_trace ",start,end,backtrace_path)
    k = start
    # min = 100
    # min3 = 100
    # jj=0
    flag1=0
    # rrr=[]
    u=0
    backtrace_path_1 = []
    backtrace_path_2 = []
    backtrace_path_3 = []
    li1=backtrace_path
    li2=backtrace_path
    li3=backtrace_path
    final=[]
    if start != end:
        backtrace_path.append(start)
    print('back 1 andar ',backtrace_path)

    if start == end:
        final.append(start)
        return final
    len1=100
    len2=100
    len3=100
    flag=0
    backtrace_path_c=backtrace_path
    for i in graph[k]:
        flag=0
        print('i======',i)
        #print('back_trace == ',backtrace_path_c)
        for j in backtrace_path_c:
            #print('j=======',j,i)
            if i == j:
                flag=1
            # if i == end:
            #     fag=1
            #     if u==1:
            #         backtrace_path_1=backtrace_path_1.append(i)
            #     if u==2:
            #         backtrace_path_1=backtrace_path_2.append(i)
            #     if u==3:
            #         backtrace_path_1=backtrace_path_3.append(i)
       
        if flag == 0:
            print("i ==== inside",i,u)
            flag1=1
            if u == 0:
                backtrace_path_1 = path_new(graph,i,end,backtrace_path)
                len1=len(backtrace_path_1)
                print('back and len1((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((',backtrace_path_1,len1,' ',i)
                backtrace_path_c=[]
                #backtrace_path=[]
            if u == 1:
                backtrace_path_2 = path_new(graph,i,end,backtrace_path)
                len2=len(backtrace_path_2)
                print('back and len2((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((',backtrace_path_2,len2,' ',i)
                backtrace_path_c=[]
                #backtrace_path=[]


            if u == 2:
                backtrace_path_3 = path_new(graph,i,end,backtrace_path)
                len3=len(backtrace_path_3)
                print('back and len3((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((',backtrace_path_3,len3,' ',i)
                backtrace_path_c=[]
                #backtrace_path=[]

        #backtrace_path=[]

        u=u+1
    print('back_trace == ',backtrace_path_c)

    if flag1==1:
        
        list=[len1,len2,len3]
        k=min(list)
        print('k======',k)
        list.sort()
        kk=list[0]
        if k == len1:
            backtrace_path_1.insert(0, start)
            print('len1 == and k ',backtrace_path_1)
            return backtrace_path_1
        if k == len2:
            backtrace_path_2.insert(0, start)

            print('len2 == and k ',backtrace_path_2)
            return backtrace_path_2
        if k == len3:
            backtrace_path_3.insert(0, start)

            print('len3 == and k ',backtrace_path_3)
            return backtrace_path_3
    else:
        return backtrace_path

def paths_to_moves(paths, traffic_signal):
    """
    Purpose:
    ---
    This function takes the list of all nodes produces from the path planning algorithm
    and connecting both start and end nodes

    Input Arguments:
    ---
    `paths` :	[ list of all nodes ]
                    list of all nodes connecting both start and end nodes (SHORTEST PATH)
    `traffic_signal` : [ list of all traffic signals ]
                    list of all traffic signals
    ---
    `moves` : [ list of moves from start to end nodes ]
                    list containing moves for the bot to move from start to end

                    Eg. : ['UP', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN']

    Example call:
    ---
    moves = paths_to_moves(paths, traffic_signal)
    """

    list_moves = []

    ############## ADD YOUR CODE HERE	##############
    # print(paths,traffic_signal)
    k = len(paths)
    kk = k-1
    flag = 0
    flag1 = 0
    dir = 'l'
    for i in range(0, kk):
        # print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",i)
        o = i+1
        # print(i,o)
        # print(paths[i],paths[o],list_moves)
        q = paths[i]
        w = paths[i+1]
        r = paths[i-1]
        flag = 0
        for j in traffic_signal:
            if q == j:
                flag = 1
            if w == j:
                flag1 = 1
        fag2 = 0
        fak = 0
        if flag == 0 or flag == 1:
            if flag == 1:
                list_moves.append("WAIT_5")
            q1 = q[0]
            # print("((((((((((",q1)
            q11 = ord(q1)
            q2 = q[1]
            # print("(((((((((((",q2)
            q2 = int(q2)
            w1 = w[0]
            w11 = ord(w1)
            w2 = w[1]
            w2 = int(w2)
            z1 = r[0]
            z11 = ord(z1)
            z2 = r[1]
            z2 = int(z2)
            r = q2 - w2
            r1 = q11-w11
            # print("----------",q11,w11,r1,r,dir)
            if i == 0 and dir == 'l':
                # print("jrmrmermjcje")
                fag2 = 1
                if r1 == 0 and r > 0:
                    list_moves.append("STRAIGHT")
                    dir = 'N'

                if r1 == 0 and r < 0:
                    list_moves.append("STRAIGHT")
                    dir = 'S'
                if r == 0 and r1 < 0:
                    list_moves.append("RIGHT")
                    dir = 'W'
                if r == 0 and r1 > 0:
                    list_moves.append("LEFT")
                    dir = 'E'

            # if z11==q11==w11:
            # 	list_moves.append("STRAIGHT")
            # 	fag=1
            if dir == 'N' and fag2 == 0 and fak == 0:
                fak = 1
                if r1 == 0 and r > 0 and fag2 == 0:
                    list_moves.append("STRAIGHT")
                    dir = 'N'
                if r1 == 0 and r < 0 and fag2 == 0:
                    list_moves.append("LEFTTTTT")
                if r == 0 and r1 > 0:
                    list_moves.append("LEFT")
                    dir = 'E'
                if r == 0 and r1 < 0:
                    list_moves.append("RIGHT")
                    dir = 'W'
                # print("north",dir)
            if dir == 'S' and fag2 == 0 and fak == 0:
                fak = 1
                if r1 == 0 and r > 0 and fag2 == 0:
                    list_moves.append("STRAIGHT")
                    dir = 'S'
                if r1 == 0 and r < 0 and fag2 == 0:
                    list_moves.append("STRAIGHT")
                if r == 0 and r1 > 0:
                    list_moves.append("RIGHT")
                    dir = 'E'
                if r == 0 and r1 < 0:
                    list_moves.append("LEFT")
                    dir = 'W'
                # print("south",dir)
            if dir == 'E' and fag2 == 0 and fak == 0:
                fak = 1
                if r1 == 0 and r > 0 and fag2 == 0:
                    list_moves.append("RIGHT")
                    dir = 'N'
                if r1 == 0 and r < 0 and fag2 == 0:
                    list_moves.append("LEFT")
                    dir = 'S'
                if r == 0 and r1 > 0:
                    list_moves.append("STRAIGHT")
                    dir = 'E'
                if r == 0 and r1 < 0:
                    list_moves.append("RIGHT")
                    dir = 'W'
                # print("east",dir)
            if dir == 'W' and fag2 == 0 and fak == 0:
                fak = 1
                if r1 == 0 and r > 0 and fag2 == 0:
                    list_moves.append("LEFT")
                    dir = 'N'
                if r1 == 0 and r < 0 and fag2 == 0:
                    list_moves.append("RIGHT")
                    dir = 'S'
                if r == 0 and r1 > 0:
                    list_moves.append("STRAIGHT")
                    dir = 'E'
                if r == 0 and r1 < 0:
                    list_moves.append("STRAIGHT")
                    dir = 'W'
                # print("west",dir)

        # if flag == 1:
        # 		list_moves.append("WAIT_5")
        # print(list_moves)

    #################################################
    # print(paths,traffic_signal)
    return list_moves


def path_planning_new(graph, start, end, min, backtrace_path):
    k = start
    min2 = min
    flag = 0
    jj = 0
    min3=100
    rrr=[]
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    print('back path == ',backtrace_path)

    # min=distance(start,end)
    for i in graph[k]:
        d = distance(i, end)
        # print(i,d,min,backtrace_path)
        if d < min2:
            min2 = d
            backtrace_path.append(i)
            # print(backtrace_path,min)
            backtrace_path = path_planning_new(graph, i, end, min2, backtrace_path)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",backtrace_path[-1])
            if backtrace_path[-1] == end:
                flag = 1
                if jj == 0:
                    a1 = backtrace_path
                    lll = len(a1)
                    if lll < min3:
                        min3 = lll
                        rrr = a1
                if jj == 1:
                    a2 = backtrace_path
                    lll = len(a2)
                    if lll < min3:
                        min3 = lll
                        rrr = a2

                if jj == 2:
                    a3 = backtrace_path
                    lll = len(a3)
                    if lll < min3:
                        min3 = lll
                        rrr = a3

                if jj == 3:
                    a4 = backtrace_path
                    lll =len(a4)
                    if lll < min3:
                        min3 = lll
                        rrr = a4
            jj=jj+1

                # return backtrace_path
        if min == 0:
            return backtrace_path
        jj = jj+1
    if flag == 1:
        return rrr

    # print("uuuuuuuuuuuuu",backtrace_path)
    backtrace_path = backtrace_path[:-1]
    # print(backtrace_path)
    return backtrace_path


def path_planning_new_2(graph, start, end, backtrace_path):
    print('back path  = ',backtrace_path)
    l = []
    o = start
    po = 'pp'
    # print(backtrace_path)
    # l=path(end,graph,backtrace_path)z
    flag = 0
    min2 = 100
    min = 20
    kk = start
    # print("@@@@@@@@@@@@@@@@@@@@@@",kk)
    while kk != end:
        print('back path 2  = ',backtrace_path)
        flag = 0
        fag = 1
        flag10 = 0
        flag101 = 0
        for i in graph[kk]:
            print('back path 3  = ',backtrace_path)

            # print("###################################################################################")
            if fag == 1:
                q = kk
                # print(q)
                fag = 0
            # print(i)
            d = distance(i, end)
            if d < min:
                # print("%%%%%%%%",d,min)
                min = d
                # print(kk)
                # q=kk
                kk = i
                flag = 1
        if flag == 0:
            for j in graph[kk]:
                print('back path 4  = ',backtrace_path)
                print('"""""====',j,' ',w,' ',po)

                flag10 = 0
                # print("99999999999999999999999999999999999999999",po,w,j,kk)
                if j != w and j != po:
                    print('"""""====',j)
                    for y in backtrace_path:
                        print('y==',y)
                        if j == y:
                            flag10 = 1
                            po = kk
                    if flag10 == 0:
                        print("j =---",j,min2)
                        dd = distance(j, end)
                        print('dd , min ',dd,min2)
                        if dd < min2:
                            flag101 = 1
                            print("xsftcdstttttttttttttttttttt",min,kk,j,q,w,flag10)
                            min2 = dd
                            kk = j
            if flag101 == 1:
                flag10 = 0
                backtrace_path.append(kk)
                print('final -- ',backtrace_path)
                w = q
                # print("------------",w)
                min2 = 100
                # print("yyyyyyyyyyyyyyyyyyyy",backtrace_path)
            if flag10 == 1:
                backtrace_path = backtrace_path[:-1]
                ll = kk
                kk = backtrace_path[-1]
                w = backtrace_path[-2]
                # print("ooooooooooooooooooooooooooooooooooooooooooooooooooo",kk,backtrace_path)
        if flag == 1:
            w = kk
            backtrace_path.append(kk)
    print('nfshfhiuhgjherh == ',backtrace_path)
    return backtrace_path


def distance(i, end):
    c = i[0]
    w = ord(c)
    w1 = i[1]
    w1 = int(w1)
    c1 = end[0]
    q = ord(c1)
    q1 = end[1]
    q1 = int(q1)
    r = w1-q1
    if r < 0:
        r = -r
    r1 = w-q
    if r1 < 0:
        r1 = -r1
    f = r1+r
    return f


def path(end, graph, li):
    k = li[2]
    # print(type(k),end)
    flag = 0
    while k != end:
        for i in graph(k):
            # print(i)
            d = distance(i, end)
            if d <= min:
                min = d
                k = i
                flag = 1
        if flag == 0:
            for j in graph(k):
                if j != q:
                    dd = distance(j, end)
                    if dd < min2:
                        min2 = dd
                        k = j
        li.append(k)
        q = k


def detect_arena_parameters(maze_image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a dictionary
    containing the details of the different arena parameters in that image

    The arena parameters are of four categories:
    i) traffic_signals : list of nodes having a traffic signal
    ii) start_node : Start node which is mark in light green
    iii) end_node : End node which is mark in Purple
    iv) paths : list containing paths

    These four categories constitute the four keys of the dictionary

    Input Arguments:
    ---
    `maze_image` :	[ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `arena_parameters` : { dictionary }
                    dictionary containing details of the arena parameters

    Example call:
    ---
    arena_parameters = detect_arena_parameters(maze_image)

    Eg. arena_parameters={"traffic_signals":[], 
                          "start_node": "E4", 
                          "end_node":"A3", 
                          "paths": {}}
    """
    arena_parameters = {}

    ############## ADD YOUR CODE HERE	##############
    traffic_signals, start_node, end_node = detect_all_nodes(maze_image)
    paths = detect_paths_to_graph(maze_image)
    # b = ''.join(str(traffic_signals).split(","))
    traffic_signals.sort()
    arena_parameters["traffic_signals"] = traffic_signals
    arena_parameters["start_node"] = start_node
    arena_parameters["end_node"] = end_node
    # arena_parameters["paths"]=paths
    horizontal_roads_under_construction = []
    horizontal_roads_under_construction = detect_horizontal_roads_under_construction(
        maze_image)
    arena_parameters['horizontal_roads_under_construction'] = horizontal_roads_under_construction
    vertical_roads_under_construction = []
    vertical_roads_under_construction = detect_vertical_roads_under_construction(
        maze_image)
    arena_parameters['vertical_roads_under_construction'] = vertical_roads_under_construction
    medicine_packages_present = []
    medicine_packages_present = detect_medicine_packages(maze_image)
    arena_parameters['medicine_packages'] = medicine_packages_present
    arena_parameters['paths'] = paths

    # print(arena_parameters)

    ##################################################

    return arena_parameters

##############################################################
##############################################################


####################### ADD ARENA SETUP ######################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 4A for setting up the CoppeliaSim
Arena according to the configuration image in this section
"""


def place_packages(medicine_package_details, sim, all_models):
    """
        Purpose:
        ---
        This function takes details (colour, shape and shop) of the packages present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    them on the virtual arena. The packages should be inserted only into the 
    designated areas in each shop as mentioned in the Task document.

    Functions from Regular API References should be used to set the position of the 
    packages.

        Input Arguments:
        ---
        `medicine_package_details` :	[ list ]
                                nested list containing details of the medicine packages present.
                                Each element of this list will contain 
                                - Shop number as Shop_n
                                - Color of the package as a string
                                - Shape of the package as a string
                                - Centroid co-ordinates of the package			

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene

        Example call:
        ---
        all_models = place_packages(medicine_package_details, sim, all_models)
        """
    models_directory = os.getcwd()
    packages_models_directory = os.path.join(
        models_directory, "package_models")
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    # print(medicine_package_details)
    l = len(medicine_package_details)
    i = 0
    # all_models=[]
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    while l:
        ix = medicine_package_details[i][3][0]
        iy = medicine_package_details[i][3][1]
        k = medicine_package_details[i][0]
        # objectHandle=sim.loadModel()

        # print(k)
        if k == 'Shop_1':
            count = count+1
            cx = -0.8305
            if count == 2:
                cx = cx+2*0.0395
            if count == 3:
                cx = cx+4*0.0395
            if count == 4:
                cx = cx+6*0.0395
        if k == 'Shop_2':
            count1 = count1+1
            cx = -0.4745
            if count1 == 2:
                cx = cx+2*0.0395
            if count1 == 3:
                cx = cx+4*0.0395
            if count1 == 4:
                cx = cx+6*0.0395
        if k == 'Shop_3':
            count2 = count2+1
            cx = -0.1185
            if count2 == 2:
                cx = cx+2*0.0395
            if count2 == 3:
                cx = cx+4*0.0395
            if count2 == 4:
                cx = cx+6*0.0395
        if k == 'Shop_4':
            count3 = count3+1
            cx = 0.2375
            if count3 == 2:
                cx = cx+2*0.0395
            if count3 == 3:
                cx = cx+4*0.0395
            if count3 == 4:
                cx = cx+6*0.0395
        if k == 'Shop_5':
            count4 = count4+1
            cx = 0.5935
            if count4 == 2:
                cx = cx+2*0.0395
            if count4 == 3:
                cx = cx+4*0.0395
            if count4 == 4:
                cx = cx+6*0.0395
        # x=350-ix
        # y=350-iy
        # cx=x/350*0.9550
        # cx=-cx
        # cy=y/350*0.9550SS
        # print(ix,iy,x,y,cx,cy)
        cy = 0.6873125
        ia = medicine_package_details[i][1]
        ib = medicine_package_details[i][2]
        ic = ia + '_' + ib
        # print(ic)
        # # print(simGetStringParameter(sim_stringparam_application_path))
        # path='C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/'  + ic + '.ttm'
        # print(path)
        if ic == 'Green_Triangle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Green_cone.ttm')
        if ic == 'Green_Circle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Green_cylinder.ttm')
        if ic == 'Green_Square':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Green_cube.ttm')
        if ic == 'Pink_Triangle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Pink_cone.ttm')
        if ic == 'Pink_Circle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Pink_cylinder.ttm')
        if ic == 'Pink_Square':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Pink_cube.ttm')
        if ic == 'Orange_Triangle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Orange_cone.ttm')
        if ic == 'Orange_Circle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Orange_cylinder.ttm')
        if ic == 'Orange_Square':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Orange_cube.ttm')
        if ic == 'Skyblue_Triangle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Skyblue_cone.ttm')
        if ic == 'Skyblue_Circle':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Skyblue_cylinder.ttm')
        if ic == 'Skyblue_Square':
            objectHandle = sim.loadModel(
                r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Skyblue_cube.ttm')
        keepInPlace = True
        sim.setObjectParent(objectHandle, arena, keepInPlace)

        # e = sim.getObject(ic)
        e = objectHandle
        all_models.append(e)
        position = []
        position.append(cx)
        position.append(cy)
        position.append(0)

        sim.setObjectPosition(e, arena, position)
        i = i+1
        l = l-1


####################################################################

    return all_models


def place_traffic_signals(traffic_signals, sim, all_models):
    """
        Purpose:
        ---
        This function takes position of the traffic signals present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    them on the virtual arena. The signal should be inserted at a particular node.

    Functions from Regular API References should be used to set the position of the 
    signals.

        Input Arguments:
        ---
        `traffic_signals` : [ list ]
                        list containing nodes in which traffic signals are present

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        None

        Example call:
        ---
        all_models = place_traffic_signals(traffic_signals, sim, all_models)
        """
    models_directory = os.getcwd()
    traffic_sig_model = os.path.join(
        models_directory, "signals", "traffic_signal.ttm")
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    traffic_sig_model = os.path.join(
        models_directory, "signals", "traffic_signal.ttm")
    arena = sim.getObject('/Arena')
####################### ADD YOUR CODE HERE #########################
    # print(traffic_signals)
    l = len(traffic_signals)
    i = 0
    while l:
        k = traffic_signals[i]
        # print(k[0],k[1])
        r = k[0]
        y = k[1]
        # print(type(r),type(y))
        if r == 'A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        objectHandle = sim.loadModel(
            r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\signals\traffic_signal.ttm')
        objectAlias = 'Signal_'+r+y
        # print(objectAlias)
        sim.setObjectAlias(objectHandle, objectAlias)

        keepInPlace = True
        sim.setObjectParent(objectHandle, arena, keepInPlace)

        cy = -cy
        # print(cx,cy)
        e = objectHandle
        all_models.append(e)
        position = []
        position.append(cx)
        position.append(cy)
        position.append(0.1539)

        sim.setObjectPosition(e, arena, position)
        i = i+1
        l = l-1


####################################################################

    return all_models


def place_start_end_nodes(start_node, end_node, sim, all_models):
    """
        Purpose:
        ---
        This function takes position of start and end nodes present in 
    the arena and places them on the virtual arena. 
    The models should be inserted at a particular node.

    Functions from Regular API References should be used to set the position of the 
    start and end nodes.

        Input Arguments:
        ---
        `start_node` : [ string ]
    `end_node` : [ string ]


    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        ---
        None

        Example call:
        ---
        all_models = place_start_end_nodes(start_node, end_node, sim, all_models)
        """
    models_directory = os.getcwd()
    start_node_model = os.path.join(
        models_directory, "signals", "start_node.ttm")
    end_node_model = os.path.join(models_directory, "signals", "end_node.ttm")
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    start_node_model = os.path.join(
        models_directory, "signals", "start_node.ttm")
    end_node_model = os.path.join(models_directory, "signals", "end_node.ttm")
    arena = sim.getObject('/Arena')
####################### ADD YOUR CODE HERE #########################
    l = 2
    while l:
        r = start_node[0]
        y = start_node[1]
        if l == 1:
            r = end_node[0]
            y = end_node[1]
        if r == 'A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        if l == 2:
            objectHandle = sim.loadModel(
                r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\signals\start_node.ttm')
            objectAlias = 'Start_Node'

        if l == 1:
            objectHandle = sim.loadModel(
                r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\signals\end_node.ttm')
            objectAlias = 'End_Node'

        # objectAlias='Vertical_missing_road_'+rr+yy+'_'+rrr+yyy
        # print(objectAlias)
        sim.setObjectAlias(objectHandle, objectAlias)

        keepInPlace = True
        sim.setObjectParent(objectHandle, arena, keepInPlace)

        cy = -cy
        # print(cx,cy)
        e = objectHandle
        all_models.append(e)
        position = []
        position.append(cx)
        position.append(cy)
        position.append(0.1539)

        sim.setObjectPosition(e, arena, position)
        l = l-1


####################################################################

    return all_models


def place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models):
    """
        Purpose:
        ---
        This function takes the list of missing horizontal roads present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    horizontal barricades on virtual arena. The barricade should be inserted 
    between two nodes as shown in Task document.

    Functions from Regular API References should be used to set the position of the 
    horizontal barricades.

        Input Arguments:
        ---
        `horizontal_roads_under_construction` : [ list ]
                        list containing missing horizontal links		

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        ---
        None

        Example call:
        ---
        all_models = place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
        """
    models_directory = os.getcwd()
    horiz_barricade_model = os.path.join(
        models_directory, "barricades", "horizontal_barricade.ttm")
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    horiz_barricade_model = os.path.join(
        models_directory, "barricades", "horizontal_barricade.ttm")
    arena = sim.getObject('/Arena')
####################### ADD YOUR CODE HERE #########################
    # print(horizontal_roads_under_construction)
    l = len(horizontal_roads_under_construction)
    i = 0
    while l:
        # print(horizontal_roads_under_construction[i],horizontal_roads_under_construction[i][0],horizontal_roads_under_construction[i][3])
        r = horizontal_roads_under_construction[i][0]
        y = horizontal_roads_under_construction[i][1]
        # print(r,y,"----------")
        if r == 'A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x1 = cx
        y1 = cy
        rr = r
        yy = y
        rr = str(rr)
        yy = str(yy)
        r = horizontal_roads_under_construction[i][3]
        y = horizontal_roads_under_construction[i][4]
        if r == 'A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x2 = cx
        y2 = cy
        rrr = r
        yyy = y
        rrr = str(rrr)
        yyy = str(yyy)

        x = (x1+x2)/2
        y = (y1+y2)/2
        y = -y
        # print(x,y)
        objectHandle = sim.loadModel(
            r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\barricades\horizontal_barricade.ttm')
        # print(type(rr),type(yy),type(r),type(y))
        objectAlias = 'Horizontal_missing_road_'+rr+yy+'_'+rrr+yyy
        # print(objectAlias)
        sim.setObjectAlias(objectHandle, objectAlias)

        keepInPlace = True
        sim.setObjectParent(objectHandle, arena, keepInPlace)

        e = objectHandle
        all_models.append(e)
        position = []
        position.append(x)
        position.append(y)
        position.append(0)

        sim.setObjectPosition(e, arena, position)

        i = i+1
        l = l-1

####################################################################
    return all_models


####################################################################

    return all_models


def place_vertical_barricade(vertical_roads_under_construction, sim, all_models):
    """
        Purpose:
        ---
        This function takes the list of missing vertical roads present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    vertical barricades on virtual arena. The barricade should be inserted 
    between two nodes as shown in Task document.

    Functions from Regular API References should be used to set the position of the 
    vertical barricades.

        Input Arguments:
        ---
        `vertical_roads_under_construction` : [ list ]
                        list containing missing vertical links		

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
        ---
        None

        Example call:
        ---
        all_models = place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
        """
    models_directory = os.getcwd()
    vert_barricade_model = os.path.join(
        models_directory, "barricades", "vertical_barricade.ttm")
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    vert_barricade_model = os.path.join(
        models_directory, "barricades", "vertical_barricade.ttm")
    arena = sim.getObject('/Arena')
####################### ADD YOUR CODE HERE #########################
    # print(vertical_roads_under_construction)
    l = len(vertical_roads_under_construction)
    i = 0
    while l:
        # print(vertical_roads_under_construction[i],vertical_roads_under_construction[i][0],vertical_roads_under_construction[i][3])
        r = vertical_roads_under_construction[i][0]
        y = vertical_roads_under_construction[i][1]
        # print(r,y,"----------")
        if r == 'A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x1 = cx
        y1 = cy
        rr = r
        yy = y
        rr = str(rr)
        yy = str(yy)

        r = vertical_roads_under_construction[i][3]
        y = vertical_roads_under_construction[i][4]
        if r == 'A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x2 = cx
        y2 = cy
        rrr = r
        yyy = y

        rrr = str(rrr)
        yyy = str(yyy)
        x = (x1+x2)/2
        y = (y1+y2)/2
        y = -y
        # print(x,y)
        objectHandle = sim.loadModel(
            r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\barricades\vertical_barricade.ttm')
        objectAlias = 'Vertical_missing_road_'+rr+yy+'_'+rrr+yyy
        # print(objectAlias)
        sim.setObjectAlias(objectHandle, objectAlias)

        keepInPlace = True
        sim.setObjectParent(objectHandle, arena, keepInPlace)

        e = objectHandle
        all_models.append(e)
        position = []
        position.append(x)
        position.append(y)
        position.append(0)

        sim.setObjectPosition(e, arena, position)

        i = i+1
        l = l-1


####################################################################

    return all_models

##############################################################
##############################################################
def perspective_transform(image):
    
    """
    Purpose:
    ---
    This function takes the image as an argument and returns the image after 
    applying perspective transform on it. Using this function, you should
    crop out the arena from the full frame you are receiving from the 
    overhead camera feed.

    HINT:
    Use the ArUco markers placed on four corner points of the arena in order
    to crop out the required portion of the image.

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by cv2 library 

    Returns:
    ---
    `warped_image` : [ numpy array ]
            return cropped arena image as a numpy array
    
    Example call:
    ---
    warped_image = perspective_transform(image)
    """   
    warped_image = [] 
#################################  ADD YOUR CODE HERE  ###############################

    # cv2.imshow("Frame",image) # displaying the captured frames
    # calib_data_path = "../calib_data/MultiMatrix.npz"
    # calib_data = numpy.load
    # (calib_data_path)
    # print(calib_data.files)
    # cam_mat = calib_data["camMatrix"]
    # dist_coef = calib_data["distCoef"]
    # r_vectors = calib_data["rVector"]
    # t_vectors = calib_data["tVector"]
    # print(cam_mat)
    # print(dist_coef)
    # print(r_vectors)
    # print(t_vectors)
    # h,  w = image.shape[:2]
    # print(h,w)
    # newcameramtx, roi = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coef, (w,h), 1, (w,h))

    # dst = cv2.undistort(image,cam_mat, dist_coef, None, newcameramtx)
    # x, y, w, h = roi
    # print(x,y,w,h)
    # dst = dst[y:y+h, x:x+w]

    # cv2.imshow("Fram---e",dst) # displaying the captured frames
    # cv2.waitKey(5000)
    ArUco_details_dict,ArUco_corners=detect_ArUco_details(image)
    print(ArUco_details_dict)
    #print(ArUco_details_dict[1][0][1])
    y1=ArUco_details_dict[3][0][0]
    y2=ArUco_details_dict[1][0][0]
    x1=ArUco_details_dict[3][0][1]
    x2=ArUco_details_dict[1][0][1]
    # y1=y1-3
    # y2=y2+3
    x1=x1-4
    x2=x2+11
    print(x1,x2,y1,y2)
    warped_image=image[x1:x2,y1:y2]
    # warped_image=image
    cv2.imshow('wraped',warped_image)
    cv2.waitKey(1000)
    image_dir_path = "images"
    cv2.imwrite(f"{image_dir_path}/in{30}.png", warped_image)

######################################################################################


    return warped_image

def transform_values(image):

    """
    Purpose:
    ---
    This function takes the image as an argument and returns the 
    position and orientation of the ArUco marker (with id 5), in the 
    CoppeliaSim scene.

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by camera

    Returns:
    ---
    `scene_parameters` : [ list ]
            a list containing the position and orientation of ArUco 5
            scene_parameters = [c_x, c_y, c_angle] where
            c_x is the transformed x co-ordinate [float]
            c_y is the transformed y co-ordinate [float]
            c_angle is the transformed angle [angle]
    
    HINT:
        Initially the image should be cropped using perspective transform 
        and then values of ArUco (5) should be transformed to CoppeliaSim
        scale.
    
    Example call:
    ---
    scene_parameters = transform_values(image)
    """   
    scene_parameters = []
#################################  ADD YOUR CODE HERE  ###############################
    #warped_image = perspective_transform(image)
    warped_image=image
    ArUco_details_dict,ArUco_corners=detect_ArUco_details(warped_image)

    if 5 in ArUco_details_dict.keys():
        #ArUco_details_dict,ArUco_corners=detect_ArUco_details(warped_image)
        #print(ArUco_details_dict,warped_image.shape)
        #print(type(ArUco_corners),ArUco_details_dict[5][0][0])
        w=warped_image.shape[1]
        h=warped_image.shape[0]
        wm=w/2
        hm=h/2
        c1=ArUco_details_dict[5][0][0]
        c1m=wm-c1
        c1m=float(c1m)
        c2=ArUco_details_dict[5][0][1]
        c2m=c2-hm
        c2m=float(c2m)
        #print(c1m,c2m,wm,hm)
        a1=ArUco_details_dict[5][1]
        cop1=(c1m/wm)*0.9550
        cop2=(c2m/hm)*0.9550
        # cop1=0.9950-cop1
        # print(cop1,cop2,a1)ssssss
        if a1 >= 0:
            ang1=180-a1
            ang1=-ang1
        if a1 < 0:
            ang1=180+a1
        # print(cop1,cop2,a1,ang1)
    ######################################################################################
        c_x=-cop1
        c_y=-cop2
        c_angle=-ang1
        scene_parameters.append(c_x)
        scene_parameters.append(c_y)
        scene_parameters.append(c_angle)
        #print(scene_parameters)
    return scene_parameters


def set_values(scene_parameters,client):
    """
    Purpose:
    ---
    This function takes the scene_parameters, i.e. the transformed values for
    position and orientation of the ArUco marker, and sets the position and 
    orientation in the CoppeliaSim scene.

    Input Arguments:
    ---
    `scene_parameters` :	[ list ]
            list of co-ordinates and orientation obtained from transform_values()
            function
    Returns:
    ---
    None
    HINT:
        Refer Regular API References of CoppeliaSim to find out functions that can
        set the position and orientation of an object.
    
    Example call:
    ---
    set_values(scene_parameters)
    """   
    # aruco_handle = sim.getObject('/aruco_5')
#################################  ADD YOUR CODE HERE  ###############################
    # client = RemoteAPIClient()
    #print(scene_parameters)
    if len(scene_parameters) > 0:
        value=[]
        value.append(scene_parameters[0])
        value.append(scene_parameters[1])
        value.append(0.055998)
        l=scene_parameters[2]
        l=int(l)
        sim = client.getObject('sim') 
        aruco_handle = sim.getObject('/alphabot')
        m=sim.getObjectMatrix(aruco_handle,-1)
        position=sim.getObjectPosition(aruco_handle,-1)
        relativeToObjectHandle= sim.getObject('/Arena')
        axis={m[2],m[5],m[9]}
        # pose=sim.rotateAroundAxis(m,axis,position,l*0.017)
        Angle=[]
        l=scene_parameters[2]
        # if l == -180:
        l=l*0.017444444
        Angle.append(-1.5699)

        Angle.append(l)
        Angle.append(-1.5699)
        # Angle.append(scene_parameters[2])0.017444444
        # l=scene_parameters[2]
        # # if l == -180:
        # l=l*0.017444444
        # if l == 180:
        #     l=0
        # Angle.append(l)
        # Angle.+append(-90)

        #print("-----------------------------------",Angle)
        sim.setObjectPosition(aruco_handle,relativeToObjectHandle,value)
        sim.setObjectOrientation(aruco_handle,relativeToObjectHandle,Angle)
        # sim.setObjectMatrix(aruco_handle,-1,pose)-1.0410e+01 +9.1000e+01


######################################################################################ss

    return None
def detect_ArUco_details(image):
    
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a dictionary such
    that the id of the ArUco marker is the key and a list of details of the marker
    is the value for each item in the dictionary. The list of details include the following
    parameters as the items in the given order
        [center co-ordinates, angle from the vertical, list of corner co-ordinates] 
    This order should be strictly maintained in the output

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by cv2 library
    Returns:
    ---
    `ArUco_details_dict` : { dictionary }
            dictionary containing the details regarding the ArUco marker
    
    Example call:
    ---
    ArUco_details_dict = detect_ArUco_details(image)
    """    
    ArUco_details_dict = {} #should be sorted in ascending order of ids
    ArUco_corners = {}
    ArUco_corners = {}
    marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
    param_markers = aruco.DetectorParameters_create()
    dict ={}
    ArUco_corners ={}

    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(image, marker_dict, parameters=param_markers)
    # rvec, tvec, x = aruco.estimatePoseSingleMarkers(corners, 0.04, cameraMatrix, distCoeffs)
    # rmat, jacobian = cv2.Rodrigues(rvec)
    # world_angle = math.acos(rmat[0][0]) * 57.296
    # print(world_angle)
    
    
    
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            # cv.polylines(
            #     frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
            # )
            # aruco.drawDetectedMarkers(frame,marker_corners,marker_IDs)
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            lisst=[]
            bottom_left = corners[3].ravel()
            pt1=[]
            pt1.append(int((corners[1][0]+corners[0][0])/2))
            pt1.append(int((corners[1][1]+corners[0][1])/2))
            # print(pt1)

            lp=[]
            lp.append(top_right[0])
            lp.append(top_right[1])
            lisst.append(lp)
            lp=[]
            lp.append(top_left[0])
            lp.append(top_left[1])
            lisst.append(lp)
            lp=[]
            lp.append(bottom_right[0])
            lp.append(bottom_right[1])
            lisst.append(lp)
            lp=[]
            lp.append(bottom_left[0])
            lp.append(bottom_left[1])
            lisst.append(lp)
            w=int(ids[0])
            ArUco_corners[w]=lisst
        
            cx = (top_right[0]+top_left[0]+bottom_right[0]+bottom_left[0])/4
            cx=int(cx)
            cy = (top_right[1]+top_left[1]+bottom_right[1]+bottom_left[1])/4
            cy=int(cy)
            list =[]
            list.append(cx)
            list.append(cy)
            trigger=0
            # angle_list_1 = list(range(359,0,-1))
            # angle_list_2 = list(range(359,0,-1))
            # angle_list_2 = angle_list_2[-90:] + angle_list_2[:-90]  
            # print(pt1,list)          
            x=list[0]-pt1[0] # unpacking tuple
            y=list[1]-pt1[1]
            angle=math.atan2(x,y) #takes 2 points nad give angle with respect to horizontal axis in range(-180,180)
            ant=math.atan(angle)
            #print(ant)
            angle = (angle*180)/np.pi
            #print("-------------",angle)
            angle=int(angle)
            angle=math.ceil(angle)
            if angle == -180 :
                angle =180
            # if angle > 0 and angle > 90:
            #     angle =angle
            # elif angle > 0 and angle < 90:
            #     angle =angle + 90
            #     angle = -angle
            if angle < 0 and angle < -90:
                angle = angle
            #     angle = -angle
            # elif angle < 0 and angle >90:
            #     angle = -angle
            #     angle = 90 -angle
            # print(angle)
            # if trigger == 0:
            #     angle = angle_list_2[angle]
            # else:
            #     angle = angle_list_1[angle]
            # v=np.vectorize(3,5)
            # w=np.vectorize(3,9)
            # print(v+w)
            

            
            small =[]
            small.append(list)
            small.append(angle)
            k=int(ids[0])
            #print(type(k))
            #k=int(k)
            ArUco_corners[k]= lisst
            dict[k] = small
    big = []
    # print("--------------",dict)
    Detected_ArUco_markers ={}
    # # dict1 = sorted(ArUco_marker_angles.items())
    ArUco_details_dict=dict
    # print(ArUco_corners)



    # cv.imshow("frame", frame)
    # cv.destroyAllWindows()

    ##############	ADD YOUR CODE HERE	##############
   
    ##################################################
    #print(ArUco_details_dict)
    return ArUco_details_dict, ArUco_corners 
