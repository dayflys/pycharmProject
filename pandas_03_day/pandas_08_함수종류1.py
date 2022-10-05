'''

    함수

    1. DataFrame의 함수

    2. Series의 함수

'''

#df 함수
import pandas as pd
print(dir(pd.DataFrame))
'''['T', '_AXIS_LEN', '_AXIS_NAMES', '_AXIS_NUMBERS', '_AXIS_ORDERS', '_AXIS_TO_AXIS_NUMBER', '_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', '__array__', '__array_priority__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__contains__', '__copy__', '__dataframe__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__finalize__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '__xor__', '_accessors', '_accum_func', '_add_numeric_operations', '_agg_by_level', '_agg_examples_doc', '_agg_summary_and_see_also_doc', '_align_frame', '_align_series', '_append', '_arith_method', '_as_manager', '_box_col_values', '_can_fast_transpose', '_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', '_combine_frame', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_from_arguments', '_construct_result', '_constructor', '_constructor_sliced', '_convert', '_count_level', '_data', '_dir_additions', '_dir_deletions', '_dispatch_frame_op', '_drop_axis', '_drop_labels_or_levels', '_ensure_valid_index', '_find_valid_index', '_from_arrays', '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cleaned_column_resolvers', '_get_column_array', '_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', '_get_numeric_data', '_get_value', '_getitem_bool_array', '_getitem_multilevel', '_gotitem', '_hidden_attrs', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_mgr', '_inplace_method', '_internal_names', '_internal_names_set', '_is_copy', '_is_homogeneous_type', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_iset_item', '_iset_item_mgr', '_iset_not_inplace', '_iter_column_arrays', '_ixs', '_join_compat', '_logical_func', '_logical_method', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_min_count_stat_function', '_needs_reindex_multi', '_protect_consolidate', '_reduce', '_reduce_axis1', '_reindex_axes', '_reindex_columns', '_reindex_index', '_reindex_multi', '_reindex_with_indexers', '_rename', '_replace_columnwise', '_repr_data_resource_', '_repr_fits_horizontal_', '_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_series', '_set_axis', '_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_item', '_set_item_frame_value', '_set_item_mgr', '_set_value', '_setitem_array', '_setitem_frame', '_setitem_slice', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_stat_function', '_stat_function_ddof', '_take', '_take_with_is_copy', '_to_dict_of_blocks', '_typ', '_update_inplace', '_validate_dtype', '_values', '_where', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'sparse', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_orc', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tshift', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']'''
