import numpy as np
import cv2 
font = cv2.FONT_HERSHEY_SIMPLEX
#create a black image
img = cv2.imread(r"Images/Image_4.jpg",1)
cv2.putText(img,'Yoga Pose',(20,45),font,2,(0,200,140),5)
#Display the image
cv2.imshow('image',img)
cv2.waitKey(0)