

# bazel_nvcc
```
use nvcc compiler and tensorflow  in bazel
```
# how to build
```
bazel build -c opt --copt="-fPIC" op:matrix_add_op
python op/test_matrix_add.py
```
