import time
import cv2

def bench(image_file, gdim=3, rep=100):
    # load an image
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    # repeat task rep times
    for iteration in range(rep):
        # blur image with gdim x gdim conv mtx
        img = cv2.GaussianBlur(img,(gdim,gdim),0)
    # show result image
    cv2.imshow("CPU", img)
