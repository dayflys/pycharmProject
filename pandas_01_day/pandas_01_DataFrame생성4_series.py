'''

    series 이용

    가. series 생성
    s1 = pd.Series()
    s2 = pd.Series()

    나. DataFrame 생성
    df = pd.DataFrame([s1,s2,....])

'''

import pandas as pd
import numpy as np

# print(dir(pd.Series))
'''
['T', '_AXIS_LEN', '_AXIS_NAMES', '_AXIS_NUMBERS', '_AXIS_ORDERS', '_AXIS_TO_AXIS_NUMBER'
, '_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', '__array__'
, '__array_priority__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__'
, '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__'
, '__dir__', '__divmod__', '__doc__', '__eq__', '__finalize__', '__float__', '__floordiv__'
, '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__'
, '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__'
, '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__isub__'
, '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__long__', '__lt__', '__matmul__'
, '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__'
, '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__'
, '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__'
, '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__'
, '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '__xor__'
, '_accessors', '_accum_func', '_add_numeric_operations', '_agg_by_level', '_agg_examples_doc'
, '_agg_see_also_doc', '_align_frame', '_align_series', '_append', '_arith_method', '_as_manager'
, '_binop', '_can_hold_na', '_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting'
, '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_setitem_copy'
, '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', '_consolidate'
, '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_from_arguments'
, '_construct_result', '_constructor', '_constructor_expanddim', '_convert', '_convert_dtypes'
, '_data', '_dir_additions', '_dir_deletions', '_drop_axis', '_drop_labels_or_levels', '_duplicated'
, '_find_valid_index', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers'
, '_get_block_manager_axis', '_get_bool_data', '_get_cacher', '_get_cleaned_column_resolvers'
, '_get_index_resolvers', '_get_label_or_level_values', '_get_numeric_data', '_get_value'
, '_get_values', '_get_values_tuple', '_get_with', '_gotitem', '_hidden_attrs', '_indexed_same'
, '_info_axis', '_info_axis_name', '_info_axis_number', '_init_dict', '_init_mgr', '_inplace_method'
, '_internal_names', '_internal_names_set', '_is_cached', '_is_copy', '_is_label_or_level_reference'
, '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_ixs'
, '_logical_func', '_logical_method', '_map_values', '_maybe_update_cacher', '_memory_usage'
, '_metadata', '_min_count_stat_function', '_needs_reindex_multi', '_protect_consolidate'
, '_reduce', '_reindex_axes', '_reindex_indexer', '_reindex_multi', '_reindex_with_indexers'
, '_rename', '_replace_single', '_repr_data_resource_', '_repr_latex_', '_reset_cache'
, '_reset_cacher', '_set_as_cached', '_set_axis', '_set_axis_name', '_set_axis_nocheck'
, '_set_is_copy', '_set_labels', '_set_name', '_set_value', '_set_values', '_set_with'
, '_set_with_engine', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number'
, '_stat_function', '_stat_function_ddof', '_take', '_take_with_is_copy', '_typ'
, '_update_inplace', '_validate_dtype', '_values', '_where'

, 'abs', 'add', 'add_prefix'
, 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'argmax'
, 'argmin', 'argsort', 'array', 'asfreq', 'asof', 'astype', 'at', 'at_time', 'attrs'
, 'autocorr', 'axes', 'backfill', 'between', 'between_time', 'bfill', 'bool', 'cat', 'clip'
, 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'count', 'cov'
, 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'divmod', 'dot'
, 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dt', 'dtype', 'dtypes', 'duplicated', 'empty'
, 'eq', 'equals', 'ewm', 'expanding', 'explode', 'factorize', 'ffill', 'fillna', 'filter', 'first'
, 'first_valid_index', 'flags', 'floordiv', 'ge', 'get', 'groupby', 'gt', 'hasnans', 'head', 'hist'
, 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'interpolate', 'is_monotonic'
, 'is_monotonic_decreasing', 'is_monotonic_increasing', 'is_unique', 'isin', 'isna', 'isnull'
, 'item', 'items', 'iteritems', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le'
, 'loc', 'lt', 'mad', 'map', 'mask', 'max', 'mean', 'median', 'memory_usage', 'min', 'mod', 'mode'
, 'mul', 'multiply', 'name', 'nbytes', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest'
, 'nunique', 'pad', 'pct_change', 'pipe', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile'
, 'radd', 'rank', 'ravel', 'rdiv', 'rdivmod', 'reindex', 'reindex_like', 'rename', 'rename_axis'
, 'reorder_levels', 'repeat', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul'
, 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'searchsorted', 'sem', 'set_axis',
 'set_flags', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values'
 , 'sparse', 'squeeze', 'std', 'str', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail'
 , 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_frame', 'to_hdf', 'to_json'
 , 'to_latex', 'to_list', 'to_markdown', 'to_numpy', 'to_period', 'to_pickle', 'to_sql', 'to_string'
 , 'to_timestamp', 'to_xarray', 'tolist', 'transform', 'transpose', 'truediv', 'truncate', 'tshift'
 , 'tz_convert', 'tz_localize', 'unique', 'unstack', 'update', 'value_counts', 'values', 'var'
 , 'view', 'where', 'xs']
'''

s1 = pd.Series([10,20,30], name='age')
print(s1, type(s1))
'''
0    10
1    20
2    30
Name: age, dtype: int64 <class 'pandas.core.series.Series'>
'''
s2 = pd.Series(['홍길동','이순신','강감찬'], name='username')
print(s2)
'''
0    홍길동
1    이순신
2    강감찬
Name: username, dtype: object ==> 이 형태를 띄면 series 라고 생각하자

'''

df = pd.DataFrame([s1,s2])
print(df)
'''
            0    1    2
age        10   20   30
username  홍길동  이순신  강감찬 ==> 기본적으로 series는 행 병합이 되서 나온다.
'''
print(df.T)
'''
  age username
0  10      홍길동
1  20      이순신
2  30      강감찬
'''

