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

# Team ID:			[1481]
# Author List:		[ maitrey,arin,rushil,hardik ]
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
        cx=int((x[0]+y[0]+w[0]+h[0])/4)
        cy=int((x[1]+y[1]+w[1]+h[1])/4)
        li.append(cx)
        li.append(cy)
        Qr_codes_details[k]=li


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
    ArUco_details_dict = {} #should be sorted in ascending order of ids
    ArUco_corners = {}
    ArUco_corners = {}
    marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
    param_markers = aruco.DetectorParameters_create()
    dict ={}
    ArUco_corners ={}

    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)
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
    #print(ArUco_corners)
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
#     vid = cv2.VideoCapture(0)
  
#     while(True):
        
#         # Capture the video frame
#         # by frame
#         ret, frame = vid.read()
    
#         # Display the resulting frame
#         cv2.imshow('frame', frame)
#         ArUco_details_dict, ArUco_corners = detect_ArUco_details(frame)
#         print("Detected details of ArUco: " , ArUco_details_dict)

#         #displaying the marked image
#         img = mark_ArUco_image(frame, ArUco_details_dict, ArUco_corners)  
#         cv2.imshow("imgqq",img)

        
#         # the 'q' button is set as the
#         # quitting button you may use any
#         # desired button of your choice
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
  
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

    for file_num in range(0,2):
        img_file_path = img_dir_path +  marker + '_' + str(file_num) + '.png'

        # read image using opencv
        img = cv2.imread(img_file_path)

        print('\n============================================')
        print('\nFor '+ marker  +  str(file_num) + '.png')

        # testing for Qr images
        if choice == 'q':
            Qr_codes_details = detect_Qr_details(img)
            print("Detected details of Qr: " , Qr_codes_details)

            # displaying the marked image
            img = mark_Qr_image(img, Qr_codes_details)
            cv2.imshow("img",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # testing for ArUco images
        else:    
            ArUco_details_dict, ArUco_corners = detect_ArUco_details(img)
            print("Detected details of ArUco: " , ArUco_details_dict)

            #displaying the marked image
            img = mark_ArUco_image(img, ArUco_details_dict, ArUco_corners)  
            cv2.imshow("img",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()