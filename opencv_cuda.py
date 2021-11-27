import cv2

def bench(image_file, gdim=1, rep=100):
    # load an image
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    # upload into GPU memory
    src = cv2.cuda_GpuMat()
    src.upload(img)
    # prepare blur kernel with gdim x gdim conv mtx
    blur = cv2.cuda.createGaussianFilter(cv2.CV_8UC3,cv2.CV_8UC3,(gdim,gdim),0)
    # repeat task rep times
    for iteration in range(rep):
        blur.apply(src,src)
    # download result image into host memory
    result = src.download()
    # show result image
    cv2.imshow("CUDA", result)
