import cv2
import numpy as np

frame=cv2.imread('maze_14.png')

hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
li = []
l_b = np.array([10,50,50])
u_b = np.array([25,225,225])


mask=cv2.inRange(hsv,(0,100,20),(10,255,255))
res= cv2.bitwise_and(frame ,frame ,mask=mask)
# cv2.imshow("frames", frame)
# cv2.imshow("hsv", hsv)
cv2.imshow("musk", mask)
cv2.imshow("res", res)
imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
# cv2.imshow('thresh image ',thrash)

contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.waitKey(1)
# cv2.imshow(" new", frame)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(frame, [approx], 0, (0, 255, 155), 2)
    cv2.imshow('contour',frame)
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
    elif cx == 700 :
        w='G'
        
    q=w+str(cy)
    li.append(q)

print("'traffic signals':",end ='')
print(li)
cv2.waitKey(0)
