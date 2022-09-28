'''

    타입 변환하는 2가지 방법

    1. dtype 속성 이용

    2. astype 함수 이용

'''
import numpy as np

'''
['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__'
, '__array_function__', '__array_interface__', '__array_prepare__', '__array_priority__'
, '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__'
, '__class_getitem__', '__complex__', '__contains__', '__copy__', '__deepcopy__'
, '__delattr__', '__delitem__', '__dir__', '__divmod__', '__dlpack__', '__dlpack_device__'
, '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__'
, '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__'
, '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__'
, '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__'
, '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__'
, '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__'
, '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__'
, '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__'
, '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__'
, '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__'
, '__subclasshook__', '__truediv__', '__xor__'
, 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base'
, 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes'
, 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill'
, 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize'
, 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition'
, 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round'
, 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std'
, 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring
', 'trace', 'transpose', 'var', 'view']
'''

#1. int ---> float
arr = np.array([10,20,30])
arr2 = arr.astype(np.float64)
arr3 = np.array([10,20,30]).astype(np.float64)
print(arr2, arr2.dtype) #[10. 20. 30.] float64
print(arr3, arr3.dtype) #[10. 20. 30.] float64

#2. float --> int
arr = np.array([1.34,2.5,3.8])
arr2 = arr.astype(np.int64)
arr3 = np.array([1.34,2.5,3.8]).astype(np.int64)
print(arr2, arr2.dtype) #[1 2 3] int64
print(arr3, arr3.dtype) #[1 2 3] int64

#3. int --> 문자열
arr = np.array([10,20,30])
arr2 = arr.astype(np.string_)
arr3 = np.array([10,20,30]).astype(np.str_)
print(arr2, arr2.dtype) #[b'10' b'20' b'30'] |S21
print(arr3, arr3.dtype) #['10' '20' '30'] <U21

#4. 문자열 --> 정수
arr = np.array(['10',"20",'30'])
arr2 = arr.astype(np.int64)
print(arr2, arr2.dtype) #[10 20 30] int64


