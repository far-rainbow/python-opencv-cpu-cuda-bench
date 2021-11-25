''' OpenCV CUDA vs OpenCV cpu-only benchmark '''
from timeit import default_timer as timer
import cv2
import opencv_cuda
import opencv_cpu_only

GDIM = 15
REP = 3000
USLEEP = 50
IMAGE_FILE = 'img/image.jpg'

def main():
    # print OpenCV version
    print(f'{cv2.__version__=}')
    cv2.cuda.printCudaDeviceInfo(cv2.cuda.getDevice())
    
    # CPU TASK
    start = timer()
    opencv_cpu_only.bench(IMAGE_FILE, gdim=GDIM, rep=REP)
    end = timer()
    cv2.waitKey(USLEEP)
    print(f'CPU TASK: {end - start}')
    
    # GPU TASK
    start = timer()
    opencv_cuda.bench(IMAGE_FILE, gdim=GDIM, rep=REP)
    end = timer()
    cv2.waitKey(USLEEP)
    print(f'CUDA TASK: {end - start}')
    cv2.waitKey()

if __name__ == '__main__':
    main()
