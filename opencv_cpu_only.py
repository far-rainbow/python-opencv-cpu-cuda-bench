import time
import cv2

def bench(image_file, gdim=3, rep=100):
    # load an image
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    for iteration in range(rep):
        img = cv2.GaussianBlur(img,(gdim,gdim),0)
    cv2.imshow("CPU", img)
