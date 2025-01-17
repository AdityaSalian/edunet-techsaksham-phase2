import cv2
print(cv2.__version__)

img = cv2.imread(r"Images/Image_1.jpeg",1)
print(img)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)


cv2.imshow('color_image',img)
cv2.imshow('gray_image',img1)
cv2.imshow('RGB_image',img2)
cv2.imshow('HSV_image',img3)
cv2.imshow('LAB_image',img4)

cv2.waitKey(0)

cv2.destroyAllWindows()