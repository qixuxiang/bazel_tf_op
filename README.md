

# bazel_tf_op
```
add a custom tensorflow op in bazel
```
# how to build
```
bazel build -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"  op:matrix_add_op
python op/test_matrix_add.py
```
