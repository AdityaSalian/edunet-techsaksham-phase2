import cv2

img = cv2.imread(r"Images/Image_1.jpeg",0)
print(img)
status = cv2.imwrite('photo_write.jpeg',img)
print("Image written to file-system: ",status)