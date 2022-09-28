'''

    범용 함수 (universial function)

    1. 개념
        데이터의 요소별로 연산을 수행하는 함수 => 이로인해 벡터 연산이 가능하게 한다.

    문자열 함수 => np.char.함수 로 이용한다.

    문자열 관련 범용 함수

    1. 문법

        np.char.함수명

'''

import numpy as np

# print(dir(np.char))
'''
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__'
, '__name__', '__package__', '__spec__', '_binary_op_dispatcher', '_center_dispatcher'
, '_clean_args', '_code_dispatcher', '_count_dispatcher', '_endswith_dispatcher'
, '_expandtabs_dispatcher', '_get_num_chars', '_globalvar', '_join_dispatcher'
, '_just_dispatcher', '_mod_dispatcher', '_multiply_dispatcher', '_partition_dispatcher'
, '_replace_dispatcher', '_split_dispatcher', '_splitlines_dispatcher'
, '_startswith_dispatcher', '_strip_dispatcher', '_to_string_or_unicode_array'
, '_translate_dispatcher', '_unary_op_dispatcher', '_use_unicode', '_vec_string'
, '_zfill_dispatcher'

, 'add', 'array', 'array_function_dispatch', 'asarray', 'asbytes', 'bool_'
, 'capitalize', 'center', 'character', 'chararray', 'compare_chararrays'
, 'count', 'decode', 'encode', 'endswith', 'equal', 'expandtabs', 'find'
 'functools', 'greater', 'greater_equal', 'index', 'int_', 'integer'
 , 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric'
 , 'isspace', 'istitle', 'isupper', 'join', 'less', 'less_equal', 'ljust'
 , 'lower', 'lstrip', 'mod', 'multiply', 'narray', 'ndarray', 'not_equal'
 , 'numpy', 'object_', 'overrides', 'partition', 'replace', 'rfind', 'rindex'
 , 'rjust', 'rpartition', 'rsplit', 'rstrip', 'set_module', 'split'
 , 'splitlines', 'startswith', 'str_len', 'string_', 'strip', 'swapcase'
 , 'title', 'translate', 'unicode_', 'upper', 'zfill']
'''
print(dir(np.str_))
'''
['T', '__abs__', '__add__', '__and__', '__array__', '__array_interface__'
, '__array_priority__', '__array_struct__', '__array_wrap__', '__bool__'
, '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__dir__'
, '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__'
, '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__'
, '__init_subclass__', '__int__', '__invert__', '__iter__', '__le__', '__len__', '__lshift__'
, '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__'
, '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__'
, '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__'
, '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setstate__'
, '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__'

, 'all', 'any', 'argmax', 'argmin', 'argsort', 'astype', 'base', 'byteswap', 'capitalize'
, 'casefold', 'center', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'count'
, 'cumprod', 'cumsum', 'data', 'diagonal', 'dtype', 'dump', 'dumps', 'encode', 'endswith'
, 'expandtabs', 'fill', 'find', 'flags', 'flat', 'flatten', 'format', 'format_map', 'getfield'
, 'imag', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier'
, 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'item', 'itemset'
, 'itemsize', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'max', 'mean', 'min', 'nbytes'
, 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real'
, 'removeprefix', 'removesuffix', 'repeat', 'replace', 'reshape', 'resize', 'rfind', 'rindex'
, 'rjust', 'round', 'rpartition', 'rsplit', 'rstrip', 'searchsorted', 'setfield', 'setflags'
, 'shape', 'size', 'sort', 'split', 'splitlines', 'squeeze', 'startswith', 'std', 'strides'
, 'strip', 'sum', 'swapaxes', 'swapcase', 'take', 'title', 'tobytes', 'tofile', 'tolist'
, 'tostring', 'trace', 'translate', 'transpose', 'upper', 'var', 'view', 'zfill']
'''

