package(default_visibility = ["//visibility:public"])

config_setting(
    name = "useCUDA",
    values = {
      "copt": "-DuseCUDA",
    },
)

cc_library(
  name = "matrix_add_op",
  srcs = select({":useCUDA": ["matrix_add_kernel.cc"],
                 "//conditions:default": []
               }) + ["matrix_add_op.h","matrix_add_op.cc","matrix_add.cc"],
  deps = ["@cuda//:main","@tf//:main"],
)

cc_binary(
  name = "main",
  srcs = ["main.cc"],
  deps = [":matrix_add_op"],
)