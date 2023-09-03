'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 1B of Pharma Bot (PB) Theme (eYRC 2022-23).
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
# Filename:			task_1b.py
# Functions:		detect_Qr_details, detect_ArUco_details
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the five available  ##
## modules for this task                                    ##
##############################################################
import numpy as np
import cv2
from cv2 import aruco
import math
from pyzbar import pyzbar
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_Qr_details(image):

    """
    Purpose:
    ---
    This function takes the image as an argument and returns a dictionary such
    that the message encrypted in the Qr code is the key and the center
    co-ordinates of the Qr code is the value, for each item in the dictionary

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by cv2 library
    Returns:
    ---
    `Qr_codes_details` : { dictionary }
            dictionary containing the details regarding the Qr code
    
    Example call:
    ---
    Qr_codes_details = detect_Qr_details(image)
    """    
    Qr_codes_details = {}
    # img=cv2.imread('qr_1.png')
    d=pyzbar.decode(image)
    # print(d)
    # Dict ={}
    for i in d:
        # print(i.data)
        li =[]
        k=i.data.decode('utf-8')
        # print(k)
        # print(i.rect)
        x,y,w,h=i.polygon
        # print(x[0])
        cx=(x[0]+y[0]+w[0]+h[0])/4
        cy=(x[1]+y[1]+w[1]+h[1])/4
        li.append(cx)
        li.append(cy)
        Qr_codes_details[k]=li

        # print(cx,cy)
        # print(i.polygon)
    # print(Qr_codes_details)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)


    ##############	ADD YOUR CODE HERE	##############
    
    ##################################################
    
    return Qr_codes_details    

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
    cv2.imshow('imxage',image)
    cv2.waitKey(2000)
    ArUco_details_dict = {} #should be sorted in ascending order of ids
    ArUco_corners = {}
    # marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
    # param_markers = aruco.DetectorParameters_create()
    dict ={}
    small =[]
    ArUco_corners ={}
    
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
    parameters =  cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)

    #frame = cv.imread(...)

    marker_corners, marker_IDs, rejectedCandidates = detector.detectMarkers(image)
    print(marker_corners)
    print(marker_IDs)

    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # marker_corners, marker_IDs, reject = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)

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
            lp=[]
            lp.append(top_left[0])
            lp.append(top_left[1])
            lisst.append(lp)
            lp=[]
            lp.append(top_right[0])
            lp.append(top_right[1])
            lisst.append(lp)
            lp=[]
            lp.append(bottom_right[0])
            lp.append(bottom_right[1])
            lisst.append(lp)
            lp=[]
            lp.append(bottom_left[0])
            lp.append(bottom_left[1])
            lisst.append(lp)
            w=ids[0]
            ArUco_corners[w]=lisst
        
            cx = (top_right[0]+top_left[0]+bottom_right[0]+bottom_left[0])/4
            cx=int(cx)
            cy = (top_right[1]+top_left[1]+bottom_right[1]+bottom_left[1])/4
            cy=int(cy)
            list =[]
            list.append(cx)
            list.append(cy)
            small.append(list)
            k=ids[0]
            k=int(k)
            ArUco_corners[k]= lisst
            dict[k] = list
    big = []
    Detected_ArUco_markers ={}
    print(marker_IDs)
    for i in range(0,marker_IDs.shape[0]):
        Detected_ArUco_markers[marker_IDs[i][0,]] = marker_corners[i][0,]
    ArUco_marker_angles = {}
    cnt = 0
    ans_x = 0
    ans_y = 0
    midpoint_x = 0
    midpoint_y = 0
    right_x = 0
    right_y = 0
    m=0
    for i in Detected_ArUco_markers:
        for j in Detected_ArUco_markers[i]:
            if (cnt%4) == 0:
                ans_x = j[0,]
                ans_y = j[1,]
                midpoint_x = ans_x
                midpoint_y = ans_y
                cnt = 1
            else:
                cnt += 1
                if cnt == 2:
                    midpoint_x = (midpoint_x + j[0,])/2
                    midpoint_y = (midpoint_y + j[1,])/2
                    right_x = j[0,]
                    right_y = j[1,]
                ans_x += j[0,]
                ans_y += j[1,]
        ans_x = int(ans_x/4)
        ans_y = int(ans_y/4)
        midpoint_x = int(midpoint_x)
        midpoint_y = int(midpoint_y)
        # cv.circle(frame,(ans_x,ans_y), 5, (0,0,255), -1)
        # cv.line(frame,(ans_x,ans_y),(midpoint_x,midpoint_y),(255,0,0),5)
        midpoint_x = midpoint_x - ans_x
        midpoint_y = -(midpoint_y - ans_y)

        ans_x = 0
        ans_y = 0
        id_str = str(i)
        # font = cv.FONT_HERSHEY_SIMPLEX
        big =[]
        if midpoint_y < 0:
            ang = str(int((360-np.arccos(np.inner([1,0],[midpoint_x,midpoint_y])/np.linalg.norm([midpoint_x,midpoint_y]))*180/np.pi)))
            ang = ang.replace('(','').replace(')','')  
            ang=int(ang)
            angg=ang

            if angg>=90 and angg<=270 :
                angg=angg-90
            elif angg<=90 :
                angg=90-angg
                angg=-angg
            else :
                angg = 90 + (360-angg)
                angg=-angg
            ang=angg
            big.append(small[m])
            big.append(ang)
            ArUco_marker_angles[i] = big
            m=m+1
        else:
            ang = str(int((np.arccos(np.inner([1,0],[midpoint_x,midpoint_y])/np.linalg.norm([midpoint_x,midpoint_y]))*180/np.pi)))
            ang = ang.replace('(','').replace(')','')  
            ang=int(ang)
            angg=ang

            if angg>=90 or angg<=270 :
                angg=angg-90
            elif angg<=90 :
                angg=90-angg
                angg=-angg
            else :
                angg = 90 + (360-angg)
                angg=-angg
            ang=angg
            big.append(small[i])
            big.append(ang)
            ArUco_marker_angles[i] = big
            m=m+1

    # dict1 = sorted(ArUco_marker_angles.items())
    ArUco_details_dict=ArUco_marker_angles

    # cv.imshow("frame", frame)
    # cv.destroyAllWindows()
    
    ##############	ADD YOUR CODE HERE	##############
   
    ##################################################
    
    return ArUco_details_dict, ArUco_corners 

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THE CODE BELOW #########	

# marking the Qr code with center and message

def mark_Qr_image(image, Qr_codes_details):
    for message, center in Qr_codes_details.items():
        encrypted_message = message
        x_center = int(center[0])
        y_center = int(center[1])
        
        cv2.circle(img, (x_center, y_center), 5, (0,0,255), -1)
        cv2.putText(image,str(encrypted_message),(x_center + 20, y_center+ 20),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)

    return image

# marking the ArUco marker with the center, angle and corners

def mark_ArUco_image(image,ArUco_details_dict, ArUco_corners):    
    for ids, details in ArUco_details_dict.items():
        center = details[0]
        cv2.circle(image, center, 5, (0,0,255), -1)
        corner = ArUco_corners[int(ids)]
        cv2.circle(image, (int(corner[0][0]), int(corner[0][1])), 5, (50, 50, 50), -1)
        cv2.circle(image, (int(corner[1][0]), int(corner[1][1])), 5, (0, 255, 0), -1)
        cv2.circle(image, (int(corner[2][0]), int(corner[2][1])), 5, (128, 0, 255), -1)
        cv2.circle(image, (int(corner[3][0]), int(corner[3][1])), 5, (255, 255, 255), -1)

        tl_tr_center_x = int((corner[0][0] + corner[1][0]) / 2)
        tl_tr_center_y = int((corner[0][1] + corner[1][1]) / 2) 

        cv2.line(image,center,(tl_tr_center_x, tl_tr_center_y),(255,0,0),5)
        display_offset = 2*int(math.sqrt((tl_tr_center_x - center[0])**2+(tl_tr_center_y - center[1])**2))
        cv2.putText(image,str(ids),(center[0]+int(display_offset/2),center[1]),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        angle = details[1]
        cv2.putText(image,str(angle),(center[0]-display_offset,center[1]),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    return image

if __name__ == "__main__":

    # path directory of images in test_images folder
    img_dir_path = "public_test_cases/"

    # choose whether to test Qr or ArUco images
    choice = input('\nWhich images do you want to test ? => "q" or "a": ')

    if choice == 'q':

        marker = 'qr'

    else:

        marker = 'aruco'

    for file_num in range(0,1):
        img_file_path = img_dir_path +  marker + '_' + str(file_num) + '.png'
        print(img_file_path)

        # read image using opencv
        img = cv2.imread(img_file_path)
        cv2.imshow('ddd',img)

        print('\n==================h==========================')
        print('\nFor '+ marker  +  str(file_num) + '.png')

        # testing for Qr images
        if choice == 'q':
            cv2.waitKey(2000)
            #Qr_codes_details = detect_ArUco_details(img)
            ArUco_details_dict, ArUco_corners=detect_ArUco_details(img)
            # print("Detected details of Qr: " , Qr_codes_details)

            # displaying the marked image
            img = mark_ArUco_image(img, ArUco_details_dict, ArUco_corners)
            cv2.imshow("img",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # testing for ArUco images
        else:    
            Qr_codes_details = detect_Qr_details(img)
            print("Detected details of ArUco: " , Qr_codes_details)

            #displaying the marked image
            img = mark_Qr_image(img, Qr_codes_details)  
            cv2.imshow("img",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()