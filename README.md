

# bazel_nvcc
```
use nvcc compiler and tensorflow  in bazel
```
# how to build
```
build -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"  op:matrix_add_op
python op/test_matrix_add.py
```
