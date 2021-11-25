# python-opencv-cpu-cuda-bench
Simple OpenCV CPU-ONLY vs. CUDA benchmark

# important note
**you have to build CUDA capable OpenCV module to start this benchmark**<br>
*pip and Anaconda's conda/conda-forge/nvidia/intel channels has cpu-only versions yet (!)

# example benchmark output
**ASUS TUF Gaming FX706LI-H705<br>
Win10<br>
15x15 conv blur matrix<br>
3000 iterations**

cv2.\__version__='4.5.4'<br>
*** CUDA Device Query (Runtime API) version (CUDART static linking) *** 

Device count: 1

Device 0: "NVIDIA GeForce GTX 1650 Ti"<br>
  CUDA Driver Version / Runtime Version          11.50 / 11.50<br>
  CUDA Capability Major/Minor version number:    7.5<br>
  Total amount of global memory:                 4096 MBytes (4294639616 bytes)<br>
  GPU Clock Speed:                               1.49 GHz<br>
  Max Texture Dimension Size (x,y,z)             1D=(131072), 2D=(131072,65536), 3D=(16384,16384,16384)<br>
  Max Layered Texture Size (dim) x layers        1D=(32768) x 2048, 2D=(32768,32768) x 2048<br>
  Total amount of constant memory:               65536 bytes<br>
  Total amount of shared memory per block:       49152 bytes<br>
  Total number of registers available per block: 65536<br>
  Warp size:                                     32<br>
  Maximum number of threads per block:           1024<br>
  Maximum sizes of each dimension of a block:    1024 x 1024 x 64<br>
  Maximum sizes of each dimension of a grid:     2147483647 x 65535 x 65535<br>
  Maximum memory pitch:                          2147483647 bytes<br>
  Texture alignment:                             512 bytes<br>
  Concurrent copy and execution:                 Yes with 2 copy engine(s)<br>
  Run time limit on kernels:                     Yes<br>
  Integrated GPU sharing Host Memory:            No<br>
  Support host page-locked memory mapping:       Yes<br>
  Concurrent kernel execution:                   Yes<br>
  Alignment requirement for Surfaces:            Yes<br>
  Device has ECC support enabled:                No<br>
  Device is using TCC driver mode:               No<br>
  Device supports Unified Addressing (UVA):      Yes<br>
  Device PCI Bus ID / PCI location ID:           1 / 0<br>
  Compute Mode:<br>
      Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) <br>

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version  = 11.50, CUDA Runtime Version = 11.50, NumDevs = 1

**CPU TASK: 5.0984488<br>
CUDA TASK: 1.6909807999999993**

*As you can see CUDA heavy task is nearly three times faster than CPU-ONLY*
