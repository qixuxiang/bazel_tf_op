# ComputerGraphics Tuebingen, 2018

# manually generated file
import tensorflow as tf
import os
from tensorflow.python.framework import ops

__all__ = ['matrix_add', 'matrix_add_grad']

path = os.path.join(os.path.dirname(__file__), '/home/gitplace/bazel_tf_op/bazel-bin/op/libmatrix_add_op.so')
_matrix_add_module = tf.load_op_library(path)

matrix_add = _matrix_add_module.matrix_add
matrix_add_grad = _matrix_add_module.matrix_add_grad


@ops.RegisterGradient("MatrixAdd")
def _MatrixAddGrad(op, *grads):
    bias = op.get_attr('bias')
    matA = op.inputs[0]
    matB = op.inputs[1]
    # top = op.outputs[0]
    topdiff = grads[0]
    return _matrix_add_module.matrix_add_grad(matA, matB, topdiff, bias=bias)
