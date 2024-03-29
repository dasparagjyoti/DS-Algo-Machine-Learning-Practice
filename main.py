import cv2


img = cv2.imread("d.jpeg") # path of the image file
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #using otsu's global threshold

# Properties of given image
print("The properties of the image are:")
print("Shape:" + str(img.shape))
print("Total no. of pixels:" + str(img.size))
print("Data type of image:" + str(img.dtype))


# Removing Horizontal Line
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1))
detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts_1 = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_1 = cnts_1[0] if len(cnts_1) == 2 else cnts_1[1]
for c in cnts_1:
    cv2.drawContours(img, [c], -1, (255, 255, 255), 2)

# Image Repair
repair_kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 9))
finalresult = 255 - cv2.morphologyEx(255 - img, cv2.MORPH_CLOSE, repair_kernel1, iterations=1)

cv2.imshow('thresh', thresh)
cv2.imshow('detected_lines', detected_lines)
cv2.imshow('image', img)
cv2.imshow('finalresult', finalresult)
cv2.waitKey()

//What if we consider noise

