'''

    시각화 방법
    1. matplotlib 라이브러리 이용
    2. seaborn 라이브러리 이용 (matplotlib 기반)
    3. pandas 시각화 (matplotlib 기반)

    pip install matplotlib

    import matplotlib.pyplot as plt
'''

import matplotlib.pyplot as plt

#도화지 얻기
fig = plt.figure()

#하나의 붓 얻기
ax = plt.axes()

#시각화 완료
plt.show()


# print(dir(fig))
# print(dir(ax))
# print(dir(plt))
'''
['_PROPERTIES_EXCLUDED_FROM_SET', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
  '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
   '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
    '__str__', '__subclasshook__', '__weakref__', '_add_axes_internal', '_agg_filter',
     '_align_label_groups', '_alpha', '_animated', '_axobservers', '_axstack', '_button_pick_id'
     , '_callbacks', '_canvas_callbacks', '_check_layout_engines_compat', '_clipon', '_clippath'
     , '_cm_set', '_default_contains', '_dpi', '_fig_callbacks', '_fully_clipped_to_axes', '_gci'
     , '_get_dpi', '_get_draw_artists', '_get_renderer', '_gid', '_in_layout', '_internal_update',
      '_label', '_layout_engine', '_localaxes', '_mouse_key_ids', '_mouseover'
      , '_normalize_grid_string', '_original_dpi', '_path_effects', '_picker'
, '_process_projection_requirements', '_rasterized', '_remove_method', '_repr_html_'
, '_scroll_pick_id', '_set_alpha_for_array', '_set_artist_props', '_set_dpi', '_set_gc_clip'
, '_sketch', '_snap', '_stale', '_sticky_edges', '_suplabels', '_suptitle', '_supxlabel'
, '_supylabel', '_transform', '_transformSet', '_update_props', '_update_set_signature_and_docstring'
, '_url', '_visible'

, 'add_artist', 'add_axes', 'add_axobserver', 'add_callback', 'add_gridspec', 'add_subfigure'
, 'add_subplot', 'align_labels', 'align_xlabels', 'align_ylabels', 'artists', 'autofmt_xdate'
, 'axes', 'bbox', 'bbox_inches', 'callbacks', 'canvas', 'clear', 'clf', 'clipbox', 'colorbar'
, 'contains', 'convert_xunits', 'convert_yunits', 'delaxes', 'dpi', 'dpi_scale_trans', 'draw'
, 'draw_artist', 'draw_without_rendering', 'execute_constrained_layout', 'figbbox', 'figimage'
, 'figure', 'findobj', 'format_cursor_data', 'frameon', 'gca', 'get_agg_filter', 'get_alpha'
, 'get_animated', 'get_axes', 'get_children', 'get_clip_box', 'get_clip_on', 'get_clip_path'
, 'get_constrained_layout', 'get_constrained_layout_pads', 'get_cursor_data'
, 'get_default_bbox_extra_artists', 'get_dpi', 'get_edgecolor', 'get_facecolor', 'get_figheight'
, 'get_figure', 'get_figwidth', 'get_frameon', 'get_gid', 'get_in_layout', 'get_label'
, 'get_layout_engine', 'get_linewidth', 'get_mouseover', 'get_path_effects', 'get_picker'
, 'get_rasterized', 'get_size_inches', 'get_sketch_params', 'get_snap', 'get_tight_layout'
, 'get_tightbbox', 'get_transform', 'get_transformed_clip_path_and_affine', 'get_url'
, 'get_visible', 'get_window_extent', 'get_zorder', 'ginput', 'have_units', 'images'
, 'is_transform_set', 'legend', 'legends', 'lines', 'mouseover', 'number', 'patch'
, 'patches', 'pchanged', 'pick', 'pickable', 'properties', 'remove', 'remove_callback'
, 'savefig', 'sca', 'set', 'set_agg_filter', 'set_alpha', 'set_animated', 'set_canvas'
, 'set_clip_box', 'set_clip_on', 'set_clip_path', 'set_constrained_layout'
, 'set_constrained_layout_pads', 'set_dpi', 'set_edgecolor', 'set_facecolor'
, 'set_figheight', 'set_figure', 'set_figwidth', 'set_frameon', 'set_gid', 'set_in_layout'
, 'set_label', 'set_layout_engine', 'set_linewidth', 'set_mouseover', 'set_path_effects'
, 'set_picker', 'set_rasterized', 'set_size_inches', 'set_sketch_params', 'set_snap'
, 'set_tight_layout', 'set_transform', 'set_url', 'set_visible', 'set_zorder', 'show', 'stale'
, 'stale_callback', 'sticky_edges', 'subfigs', 'subfigures', 'subplot_mosaic', 'subplotpars'
, 'subplots', 'subplots_adjust', 'suppressComposite', 'suptitle', 'supxlabel', 'supylabel'
, 'text', 'texts', 'tight_layout', 'transFigure', 'transSubfigure', 'update', 'update_from'
, 'waitforbuttonpress', 'zorder']

['ArtistList', '_AxesBase__clear', '_PROPERTIES_EXCLUDED_FROM_SET', '__class__', '__delattr__'
, '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'
, '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__'
, '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__'
, '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_text'
, '_adjustable', '_agg_filter', '_alias_map', '_alpha', '_anchor', '_animated', '_aspect'
, '_autotitlepos', '_axes', '_axes_class', '_axes_locator', '_axis_map', '_axis_names'
, '_axisbelow', '_box_aspect', '_callbacks', '_check_no_units', '_children', '_clipon'
, '_clippath', '_cm_set', '_colorbars', '_convert_dx', '_current_image', '_default_contains'
, '_deprecate_noninstance', '_errorevery_to_mask', '_facecolor', '_fill_between_x_or_y', '_frameon'
, '_fully_clipped_to_axes', '_gci', '_gen_axes_patch', '_gen_axes_spines', '_get_aspect_ratio'
, '_get_lines', '_get_pan_points', '_get_patches_for_fill', '_get_view', '_gid', '_gridOn'
, '_in_layout', '_init_axis', '_internal_update', '_label', '_label_outer_xaxis', '_label_outer_yaxis'
, '_left_title', '_make_twin_axes', '_mouseover', '_mouseover_set', '_navigate', '_navigate_mode'
, '_originalPosition', '_parse_scatter_color_args', '_path_effects', '_pcolor_grid_deprecation_helper'
, '_pcolorargs', '_picker', '_position', '_prepare_view_from_bbox', '_process_unit_info'
, '_projection_init', '_quiver_units', '_rasterization_zorder', '_rasterized', '_remove_legend'
, '_remove_method', '_request_autoscale_view', '_right_title', '_sci', '_set_alpha_for_array'
, '_set_artist_props', '_set_gc_clip', '_set_lim_and_transforms', '_set_position'
, '_set_title_offset_trans', '_set_view', '_set_view_from_bbox', '_shared_axes', '_sharex'
, '_sharey', '_sketch', '_snap', '_stale', '_stale_viewlims', '_sticky_edges', '_subclass_uses_cla'
, '_subplotspec', '_tight', '_transform', '_transformSet', '_twinned_axes', '_unit_change_handler'
, '_unstale_viewLim', '_update_image_limits', '_update_line_limits', '_update_patch_limits'
, '_update_props', '_update_set_signature_and_docstring', '_update_title_position'
, '_update_transScale', '_url', '_use_sticky_edges', '_validate_converted_limits', '_viewLim'
, '_visible', '_xaxis_transform', '_xmargin', '_yaxis_transform', '_ymargin', 'acorr'
, 'add_artist', 'add_callback', 'add_child_axes', 'add_collection', 'add_container', 'add_image'
, 'add_line', 'add_patch', 'add_table', 'angle_spectrum', 'annotate', 'apply_aspect', 'arrow'
, 'artists', 'autoscale', 'autoscale_view', 'axes', 'axhline', 'axhspan', 'axis', 'axison'
, 'axline', 'axvline', 'axvspan', 'bar', 'bar_label', 'barbs', 'barh', 'bbox', 'boxplot'
, 'broken_barh', 'bxp', 'callbacks', 'can_pan', 'can_zoom', 'child_axes', 'cla', 'clabel'
, 'clear', 'clipbox', 'cohere', 'collections', 'containers', 'contains', 'contains_point'
, 'contour', 'contourf', 'convert_xunits', 'convert_yunits', 'csd', 'dataLim', 'drag_pan'
, 'draw', 'draw_artist', 'end_pan', 'errorbar', 'eventplot', 'figure', 'fill', 'fill_between'
, 'fill_betweenx', 'findobj', 'fmt_xdata', 'fmt_ydata', 'format_coord', 'format_cursor_data'
, 'format_xdata', 'format_ydata', 'get_adjustable', 'get_agg_filter', 'get_alpha', 'get_anchor'
, 'get_animated', 'get_aspect', 'get_autoscale_on', 'get_autoscalex_on', 'get_autoscaley_on'
, 'get_axes_locator', 'get_axisbelow', 'get_box_aspect', 'get_children', 'get_clip_box'
, 'get_clip_on', 'get_clip_path', 'get_cursor_data', 'get_data_ratio'
, 'get_default_bbox_extra_artists', 'get_facecolor', 'get_fc', 'get_figure', 'get_frame_on'
, 'get_gid', 'get_gridspec', 'get_images', 'get_in_layout', 'get_label', 'get_legend'
, 'get_legend_handles_labels', 'get_lines', 'get_mouseover', 'get_navigate', 'get_navigate_mode'
, 'get_path_effects', 'get_picker', 'get_position', 'get_rasterization_zorder', 'get_rasterized'
, 'get_renderer_cache', 'get_shared_x_axes', 'get_shared_y_axes', 'get_sketch_params', 'get_snap'
, 'get_subplotspec', 'get_tightbbox', 'get_title', 'get_transform'
, 'get_transformed_clip_path_and_affine', 'get_url', 'get_visible', 'get_window_extent'
, 'get_xaxis', 'get_xaxis_text1_transform', 'get_xaxis_text2_transform', 'get_xaxis_transform'
, 'get_xbound', 'get_xgridlines', 'get_xlabel', 'get_xlim', 'get_xmajorticklabels'
, 'get_xminorticklabels', 'get_xscale', 'get_xticklabels', 'get_xticklines', 'get_xticks'
, 'get_yaxis', 'get_yaxis_text1_transform', 'get_yaxis_text2_transform', 'get_yaxis_transform'
, 'get_ybound', 'get_ygridlines', 'get_ylabel', 'get_ylim', 'get_ymajorticklabels'
, 'get_yminorticklabels', 'get_yscale', 'get_yticklabels', 'get_yticklines', 'get_yticks'
, 'get_zorder', 'grid', 'has_data', 'have_units', 'hexbin', 'hist', 'hist2d', 'hlines'
, 'ignore_existing_data_limits', 'images', 'imshow', 'in_axes', 'indicate_inset'
, 'indicate_inset_zoom', 'inset_axes', 'invert_xaxis', 'invert_yaxis', 'is_transform_set'
, 'label_outer', 'legend', 'legend_', 'lines', 'locator_params', 'loglog', 'magnitude_spectrum'
, 'margins', 'matshow', 'minorticks_off', 'minorticks_on', 'mouseover', 'name', 'patch', 'patches'
, 'pchanged', 'pcolor', 'pcolorfast', 'pcolormesh', 'phase_spectrum', 'pick', 'pickable', 'pie'
, 'plot', 'plot_date', 'properties', 'psd', 'quiver', 'quiverkey', 'redraw_in_frame', 'relim'
, 'remove', 'remove_callback', 'reset_position', 'scatter', 'secondary_xaxis', 'secondary_yaxis'
, 'semilogx', 'semilogy', 'set', 'set_adjustable', 'set_agg_filter', 'set_alpha', 'set_anchor'
, 'set_animated', 'set_aspect', 'set_autoscale_on', 'set_autoscalex_on', 'set_autoscaley_on'
, 'set_axes_locator', 'set_axis_off', 'set_axis_on', 'set_axisbelow', 'set_box_aspect', 'set_clip_box'
, 'set_clip_on', 'set_clip_path', 'set_facecolor', 'set_fc', 'set_figure', 'set_frame_on', 'set_gid'
, 'set_in_layout', 'set_label', 'set_mouseover', 'set_navigate', 'set_navigate_mode'
, 'set_path_effects', 'set_picker', 'set_position', 'set_prop_cycle', 'set_rasterization_zorder'
, 'set_rasterized', 'set_sketch_params', 'set_snap', 'set_subplotspec', 'set_title', 'set_transform'
, 'set_url', 'set_visible', 'set_xbound', 'set_xlabel', 'set_xlim', 'set_xmargin', 'set_xscale'
, 'set_xticklabels', 'set_xticks', 'set_ybound', 'set_ylabel', 'set_ylim', 'set_ymargin'
, 'set_yscale', 'set_yticklabels', 'set_yticks', 'set_zorder', 'sharex', 'sharey', 'specgram'
, 'spines', 'spy', 'stackplot', 'stairs', 'stale', 'stale_callback', 'start_pan', 'stem', 'step'
, 'sticky_edges', 'streamplot', 'table', 'tables', 'text', 'texts', 'tick_params', 'ticklabel_format'
, 'title', 'titleOffsetTrans', 'transAxes', 'transData', 'transLimits', 'transScale', 'tricontour'
, 'tricontourf', 'tripcolor', 'triplot', 'twinx', 'twiny', 'update', 'update_datalim', 'update_from'
, 'use_sticky_edges', 'viewLim', 'violin', 'violinplot', 'vlines', 'xaxis', 'xaxis_date'
, 'xaxis_inverted', 'xcorr', 'yaxis', 'yaxis_date', 'yaxis_inverted', 'zorder']

['Annotation', 'Arrow', 'Artist', 'AutoLocator', 'Axes', 'Button', 'Circle', 'Enum', 'ExitStack'
, 'Figure', 'FigureBase', 'FigureCanvasBase', 'FixedFormatter', 'FixedLocator', 'FormatStrFormatter'
, 'Formatter', 'FuncFormatter', 'GridSpec', 'IndexLocator', 'Line2D', 'LinearLocator', 'Locator'
, 'LogFormatter', 'LogFormatterExponent', 'LogFormatterMathtext', 'LogLocator', 'MaxNLocator'
, 'MouseButton', 'MultipleLocator', 'Normalize', 'NullFormatter', 'NullLocator', 'Number'
, 'PolarAxes', 'Polygon', 'Rectangle', 'ScalarFormatter', 'Slider', 'Subplot', 'SubplotSpec'
, 'Text', 'TickHelper', 'Widget', '_NON_PLOT_COMMANDS', '_REPL_DISPLAYHOOK', '_ReplDisplayHook'
, '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__'
, '__spec__', '_api', '_auto_draw_if_interactive', '_backend_mod', '_copy_docstring_and_deprecators'
, '_docstring', '_draw_all_if_interactive', '_get_backend_mod', '_get_required_interactive_framework'
, '_interactive_bk', '_log', '_pylab_helpers', '_warn_if_gui_out_of_main_thread', 'acorr'
, 'angle_spectrum', 'annotate', 'arrow', 'autoscale', 'autumn', 'axes', 'axhline', 'axhspan'
, 'axis', 'axline', 'axvline', 'axvspan', 'bar', 'bar_label', 'barbs', 'barh', 'bone', 'box'
, 'boxplot', 'broken_barh', 'cbook', 'cla', 'clabel', 'clf', 'clim', 'close', 'cm', 'cohere'
, 'color_sequences', 'colorbar', 'colormaps', 'connect', 'contour', 'contourf', 'cool', 'copper'
, 'csd', 'cycler', 'delaxes', 'disconnect', 'draw', 'draw_all', 'draw_if_interactive', 'errorbar'
, 'eventplot', 'figaspect', 'figimage', 'figlegend', 'fignum_exists', 'figtext', 'figure', 'fill'
, 'fill_between', 'fill_betweenx', 'findobj', 'flag', 'functools', 'gca', 'gcf', 'gci', 'get'
, 'get_backend', 'get_cmap', 'get_current_fig_manager', 'get_figlabels', 'get_fignums'
, 'get_plot_commands', 'get_scale_names', 'getp', 'ginput', 'gray', 'grid', 'hexbin', 'hist'
, 'hist2d', 'hlines', 'hot', 'hsv', 'importlib', 'imread', 'imsave', 'imshow', 'inferno'
, 'inspect', 'install_repl_displayhook', 'interactive', 'ioff', 'ion', 'isinteractive'
, 'jet', 'legend', 'locator_params', 'logging', 'loglog', 'magma', 'magnitude_spectrum'
, 'margins', 'matplotlib', 'matshow', 'minorticks_off', 'minorticks_on', 'mlab', 'new_figure_manager'
, 'nipy_spectral', 'np', 'pause', 'pcolor', 'pcolormesh', 'phase_spectrum', 'pie', 'pink', 'plasma'
, 'plot', 'plot_date', 'polar', 'prism', 'psd', 'quiver', 'quiverkey', 'rc', 'rcParams'
, 'rcParamsDefault', 'rcParamsOrig', 'rc_context', 'rcdefaults', 'rcsetup', 're', 'register_cmap'
, 'rgrids', 'savefig', 'sca', 'scatter', 'sci', 'semilogx', 'semilogy', 'set_cmap', 'set_loglevel'
, 'setp', 'show', 'specgram', 'spring', 'spy', 'stackplot', 'stairs', 'stem', 'step', 'streamplot'
, 'style', 'subplot', 'subplot2grid', 'subplot_mosaic', 'subplot_tool', 'subplots', 'subplots_adjust'
, 'summer', 'suptitle', 'switch_backend', 'sys', 'table', 'text', 'thetagrids', 'threading'
, 'tick_params', 'ticklabel_format', 'tight_layout', 'time', 'title', 'tricontour', 'tricontourf'
, 'tripcolor', 'triplot', 'twinx', 'twiny', 'uninstall_repl_displayhook', 'violinplot', 'viridis'
, 'vlines', 'waitforbuttonpress', 'winter', 'xcorr', 'xkcd', 'xlabel', 'xlim', 'xscale', 'xticks'
, 'ylabel', 'ylim', 'yscale', 'yticks']

'''
