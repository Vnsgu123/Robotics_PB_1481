'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 1A of Pharma Bot (PB) Theme (eYRC 2022-23).
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
# Filename:			task_1a.py
# Functions:		detect_traffic_signals, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#					detect_medicine_packages, detect_arena_parameters
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import cv2
import numpy as np
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_traffic_signals(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals are present in the image

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present
	
	Example call:
	---
	traffic_signals = detect_traffic_signals(maze_image)
	"""    
	traffic_signals = []

	##############	ADD YOUR CODE HERE	##############
	hsv = cv2.cvtColor(maze_image,cv2.COLOR_BGR2HSV)
	traffic_signals = []
	l_b = np.array([10,50,50])
	u_b = np.array([25,225,225])


	mask=cv2.inRange(hsv,(0,100,20),(10,255,255))
	res= cv2.bitwise_and(maze_image ,maze_image ,mask=mask)
	# cv2.imshow("frames", frame)
	# cv2.imshow("hsv", hsv)
	# cv2.imshow("musk", mask)
	# cv2.imshow("res", res)
	imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
	_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
	# cv2.imshow('thresh image ',thrash)

	contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	cv2.waitKey(1)
	# cv2.imshow(" new", frame)
	for contour in contours:
		approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
		# cv2.drawContours(maze_image, [approx], 0, (0, 255, 155), 2)
		# cv2.imshow('contour',frame)
		M = cv2.moments(contour)
		if M['m00'] != 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
		# print(cx,cy)
		cy=cy/100
		cy=int(cy)
		if cx == 100:
			w='A'
		elif cx == 200:
			w='B'
		elif cx == 300:
			w='C'
		elif cx == 400:
			w='D'
		elif cx == 500:
			w='E'
		elif cx == 600:
			w='F'
		else :
			w='G'
			
		q=w+str(cy)
		traffic_signals.append(q)
	
	traffic_signals.sort()

	# print("'traffic signals':",end ='')
	# print(traffic_signals)
	cv2.waitKey(0)
	##################################################
	
	return traffic_signals
	

def detect_horizontal_roads_under_construction(maze_image):
	
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

	##############	ADD YOUR CODE HERE	##############
	q=100
	w=200
	for j in range(1,7):
		qq=96
		ww=105
			
		for i in range(1,8):
			
			crop_img=maze_image[qq:ww ,q:w]
			# cv2.imshow('cropimge',crop_img)
			cv2.waitKey(2)
			gray = cv2.cvtColor(crop_img,cv2.COLOR_RGB2HSV)
			mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
			res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# print(len(contours))
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',crop_img)
				
				
				if j==1 :    
					u='A'+str(i)
					z='B'+str(i)
					v=u+'-'+z
				elif j==2 :
					u='B'+str(i)
					z='C'+str(i)
					v=u+'-'+z
				elif j==3 :
					u='C'+str(i)
					z='D'+str(i)
					v=u+'-'+z
				elif j==4 :
					u='D'+str(i)
					z='E'+str(i)
					v=u+'-'+z
				elif j==5 :
					u='E'+str(i)
					z='F'+str(i)
					v=u+'-'+z
				elif j==6 :
					u='F'+str(i)
					z='G'+str(i)
					v=u+'-'+z
					
				# print(v)
				horizontal_roads_under_construction.append(v)
				# print(list)
			


			qq=qq+100
			ww=ww+100
		q=q+100
		w=w+100
  	
	##################################################
	cv2.waitKey(0)
	return horizontal_roads_under_construction	

def detect_vertical_roads_under_construction(maze_image):

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

	##############	ADD YOUR CODE HERE	##############
	qq=95
	ww=107
	for j in range(1,8):
		q=100
		w=200
			
		for i in range(1,7):
			
			crop_img=maze_image[q:w ,qq:ww]
			# cv2.imshow('cropimge',crop_img)
			cv2.waitKey(2)
			gray = cv2.cvtColor(crop_img ,cv2.COLOR_RGB2HSV)
			mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
			res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# print(len(contours))
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',crop_img)
				k=i
				l=i+1
				
				if j==1 :    
					u='A'+str(k)
					z='A'+str(l)
					v=u+'-'+z
				elif j==2 :
					u='B'+str(k)
					z='B'+str(l)
					v=u+'-'+z
				elif j==3 :
					u='C'+str(k)
					z='C'+str(l)
					v=u+'-'+z
				elif j==4 :
					u='D'+str(k)
					z='D'+str(l)
					v=u+'-'+z
				elif j==5 :
					u='E'+str(k)
					z='E'+str(l)
					v=u+'-'+z
				elif j==6 :
					u='F'+str(k)
					z='F'+str(l)
					v=u+'-'+z
				elif j==7 :
					u='G'+str(k)
					z='G'+str(l)
					v=u+'-'+z
					
				# print(v)
				vertical_roads_under_construction.append(v)
				# print(list)
			


			q=q+100
			w=w+100
		qq=qq+100
		ww=ww+100
	# print("'vertical_road_under_construction':",end ='')
	# print(vertical_roads_under_construction)

	cv2.waitKey(0)	
	##################################################
	
	return vertical_roads_under_construction


def detect_medicine_packages(maze_image):

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
	medicine_packages_present = []

	##############	ADD YOUR CODE HERE	##############
	z=100
	q=200
	for i in range(0,6):
		# print(z,q)
		cropped_image = maze_image[100:200 , z:q]
		# cv2.waitKey(0)
		# print(z,q)
		# cv2.imshow('corp 1',cropped_image)
		gray = cv2.cvtColor(cropped_image ,cv2.COLOR_RGB2HSV)
		# cv2.imshow('gray image ',gray)
		for p in range(0,4):
			# print(p)
			if p==3:
				l_b =(25,50,70)
				h_b =(52,255,255)
			elif p==2:
				l_b =(128,50,70)
				h_b =(160,255,255)
			elif p==1:
				l_b =(90,50,70)
				h_b =(128,255,255)

			elif p==0 :
				# print("ooooo")
				l_b =(52,50,70)
				h_b =(89,255,255)


			mask = cv2.inRange(gray ,l_b, h_b)
			res = cv2.bitwise_and(cropped_image ,cropped_image, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(cropped_image, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',cropped_image)
				x = approx.ravel()[0]
				y = approx.ravel()[1] - 5
				if len(approx) == 3:
					# print('triangle',p)
					li=[]
					www=str(i+1)
					vv='Shop_'+www
					li.append(vv)
					if p==0:    
						li.append('Green')
					elif p==1:
						li.append('Orange')
					elif p==2:
						li.append('Pink')
					else :
						li.append('Skyblue')
					li.append('Triangle')
					M = cv2.moments(contour)
					if M['m00'] != 0:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					# cv.drawContours(image, [i], -1, (0, 255, 0), 2)
					l=[]
					e=i+1
					cx=e*100+cx
					cy=100+cy
					l.append(cx)
					l.append(cy)
					li.append(l)
					# print(cx,cy)
					# print(li)
					medicine_packages_present.append(li)
					# cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
				elif len(approx) == 4:
					
					li=[]
					ww=str(i+1)
					v='Shop_'+ww
					li.append(v)
					if p==0:    
						li.append('Green')
					elif p==1:
						li.append('Orange')
					elif p==2:
						li.append('Pink')
					else :
						li.append('Skyblue')
					li.append('Square')
					M = cv2.moments(contour)
					if M['m00'] != 0:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					# cv.drawContours(image, [i], -1, (0, 255, 0), 2)
					l=[]
					t=i+1
					cx=t*100+cx
					cy=100+cy
					l.append(cx)
					l.append(cy)
					li.append(l)
					# print(cx,cy)
					# print(li)
					medicine_packages_present.append(li)
				else:
					li=[]
					w=str(i+1)
					f='Shop_'+w
					li.append(f)
					if p==0:    
						li.append('Green')
					elif p==1:
						li.append('Orange')
					elif p==2:
						li.append('Pink')
					else :
						li.append('Skyblue')
					li.append('Circle')
					M = cv2.moments(contour)
					if M['m00'] != 0:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					# cv.drawContours(image, [i], -1, (0, 255, 0), 2)
					l=[]
					g=i+1
					cx=g*100+cx
					cy=100+cy
					l.append(cx)
					l.append(cy)
					li.append(l)
					# print(cx,cy)
					# print(li)
					medicine_packages_present.append(li)
					# cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

		# cv2.waitKey()
		z=z+100
		q=q+100
	# print(medicine_packages_present)
	cv2.waitKey(0)
	##################################################

	return medicine_packages_present

def detect_arena_parameters(maze_image):
    
	# """
	# Purpose:
	# ---
	# This function takes the image as an argument and returns a dictionary
	# containing the details of the different arena parameters in that image

	# The arena parameters are of four categories:
	# i) traffic_signals : list of nodes having a traffic signal
	# ii) horizontal_roads_under_construction : list of missing horizontal links
	# iii) vertical_roads_under_construction : list of missing vertical links
	# iv) medicine_packages_present : list containing details of medicine packages

	# These four categories constitute the four keys of the dictionary

	# Input Arguments:
	# ---
	# `maze_image` :	[ numpy array ]
	# numpy array of image returned by cv2 library
	# Returns:
	# ---
	# `arena_parameters` : { dictionary }
	# 		dictionary containing details of the arena parameters
	
	# Example call:
	# ---
	# arena_parameters = detect_arena_parameters(maze_image)
	# """    
    traffic_signals = []
    arena_parameters = {} 
    # traffic_signals = []
    traffic_signals = detect_traffic_signals(maze_image)
    arena_parameters["traffic_signals"]=traffic_signals
    horizontal_roads_under_construction = []
    horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
    arena_parameters['horizontal_roads_under_construction']=horizontal_roads_under_construction
    vertical_roads_under_construction = []
    vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
    arena_parameters['vertical_roads_under_construction']=vertical_roads_under_construction
    medicine_packages_present=[]
    medicine_packages_present = detect_medicine_packages(maze_image)
    arena_parameters['medicine_packages_present']=medicine_packages_present
	##############	ADD YOUR CODE HERE	##############
	
	##################################################
	
    return arena_parameters

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########	

if __name__ == "__main__":

    # path directory of images in test_images folder
	img_dir_path = "public_test_images/"

    # path to 'maze_0.png' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
	
	# read image using opencv
	maze_image = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor maze_' + str(file_num) + '.png')

	# detect and print the arena parameters from the image
	arena_parameters = detect_arena_parameters(maze_image)

	print("Arena Prameters: " , arena_parameters)

	# display the maze image
	cv2.imshow("image", maze_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 15):
			
			# path to maze image file
			img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
			
			# read image using opencv
			maze_image = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor maze_' + str(file_num) + '.png')
			
			# detect and print the arena parameters from the image
			arena_parameters = detect_arena_parameters(maze_image)

			print("Arena Parameter: ", arena_parameters)
				
			# display the test image
			cv2.imshow("image", maze_image)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()