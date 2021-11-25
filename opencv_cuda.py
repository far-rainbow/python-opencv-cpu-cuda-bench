import cv2

def bench(image_file, gdim=1, rep=100):
    # load an image
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    src = cv2.cuda_GpuMat()
    src.upload(img)
    blur = cv2.cuda.createGaussianFilter(cv2.CV_8UC3,cv2.CV_8UC3,(gdim,gdim),0)
    for iteration in range(rep):
        blur.apply(src,src)
    result = src.download()
    cv2.imshow("CUDA", result)
