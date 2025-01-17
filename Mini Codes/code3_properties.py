import cv2 
import mediapipe

img = cv2.imread("Images/Image_1.jpeg",1)

#height,width,number of channels in image
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size

print("Image Dimension :", dimensions)
print("Image Height :", height)
print("Image Width :", width)
print("Number of Channels :", channels)
print("Image size :", size1)

b,g,r = cv2.split(img)
merged_img_bgr = cv2.merge((b,g,r))
merged_img_rgb = cv2.merge((r,g,b))

cv2.imshow("original image",img)
cv2.imshow("colour_b image",b)
cv2.imshow("colour_g image",g)
cv2.imshow("colour_r image",g)

cv2.imshow('merged_bgr', merged_img_bgr)
cv2.imshow('merged_rgb', merged_img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()