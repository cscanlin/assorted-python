- name: perfect_order_rate_chart
  title: 'OPERATIONS: Perfect Order Rate'
  type: looker_column
  model: dotandbo
  explore: line_items
  dimensions: [orders.completed_month]
  measures: [line_items.percent_quantity_late, line_items.percent_quantity_returned_excluding_remorse,
    line_items.percent_quantity_canceled_our_fault]
  filters:
    orders.completed_date: after 2014/10/01
  sorts: [orders.completed_month]
  limit: 500
  height: 8
  show_y_axis_labels: true
  show_y_axis_ticks: true
  y_axis_gridlines: true
  y_axis_combined: true
  y_axis_max: ['40']
  y_axis_min: ['1']
  show_x_axis_label: true
  show_x_axis_ticks: true
  x_axis_gridlines: false
  show_value_labels: false
  show_null_labels: false
  show_view_names: true
  show_dropoff: false
  stacking: normal
  x_axis_scale: auto
  hide_legend: false
