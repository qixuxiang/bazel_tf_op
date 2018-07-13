package(default_visibility = ["//visibility:public"])

cc_library(
    name = "main",
    srcs = [
        "libtensorflow_framework.so",
    ],
    hdrs = glob([
        "include/**/*.h",
        "include/**/*.hpp",
        "include/**/*",
    ]),
    includes = ["include/"],
    linkopts = ["-Wl,-rpath,-ltensorflow_framework,-lm /home/soft/conda3/envs/tf_pip/lib/python2.7/site-packages/tensorflow/"],
)
