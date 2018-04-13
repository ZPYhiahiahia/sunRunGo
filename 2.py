import cv2 as cv
import numpy as np
def access_pixels(image):
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(channels)
    for row in range(height):
        for cols in range(width):
            for c in range(channels):
                pv = image[row,cols,c]
                image[row,cols,c] = 1000
    cv.imshow("test",image)
def create_image():
    img = np.zeros([400,400,3],np.uint8)
    img[: , : , 0] = 255
    #img[: , : , 1] = 255
    cv.imshow("1",img)
src = cv.imread("test.jpg")
src = cv.resize(src,(300,300))#blue,green,red
create_image()
# access_pixels(src)
cv.waitKey(0)
