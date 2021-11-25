import time
import cv2

def bench(image_file, gdim=3, rep=100):
    # load an image
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    for iteration in range(rep):
        img = cv2.GaussianBlur(img,(gdim,gdim),0)
    cv2.imshow("CPU", img)

    # img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    # img2 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    # contours, hierarchy = cv2.findContours(img2, cv2.RETR_EXTERNAL, 
    #                                           cv2.CHAIN_APPROX_SIMPLE)
    # src = cv2.cuda_GpuMat()
    # src.upload(img)
    #
    # clahe = cv2.cuda.createCLAHE(clipLimit=8.0, tileGridSize=(8,8))
    # #blur = cv2.cuda.createGaussianFilter(cv2.CV_8UC1,cv2.CV_8UC1,(25,25),0)
    #
    # dst2 = clahe.apply(src, cv2.cuda_Stream.Null())
    # #dst2 = blur.apply(dst)
    #
    # result = dst2.download()
    #
    # cv2.drawContours(result, contours, -1, (0,0,0), 2)
    #
    # cv2.imshow("result", result)
    # cv2.waitKey(0)
