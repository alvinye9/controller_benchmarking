from data_processor import DataProcessor

simulator = "CODEGEN"
# Specify the path to your CSV file
csv_file_path = 'vegas_ADRC_CODEGEN.csv'
processor = DataProcessor(csv_file_path, simulator)

# ## Call the function to preprocess data, comment this out if edited file looks good
# processor.preprocess_data()

csv_file_path = 'vegas_ADRC_CODEGEN_edited.csv'
processor = DataProcessor(csv_file_path, simulator)

print(" === METRICS FOR ADRC/VEGAS/CODEGEN/100mph (29MAR) === ")
# Calculate and print the lap time
lap_time = processor.calculate_lap_time()
print("Lap Time:", lap_time)

print("SECTOR 1")
# Sector 1 (bounded laterally, partially bounded longitudinally)
x_lower=-824
x_upper=-503
y_lower=691
y_upper= None
bound_case = 1 


yaw_rate_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_rate_des',
    current_val_col= '/control/ADRC_debug_signals/yaw_rate', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
     bound_case=bound_case)
print("Yaw Rate Error Metric:", yaw_rate_error_metric)

yaw_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
     bound_case=bound_case)
print("Yaw Error Metric:", yaw_error_metric)

speed_error_metric = processor.calculate_error_metric( 
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Speed Error Metric:", speed_error_metric)

lat_error_metric = processor.calculate_error_metric_single_value(
    error_val_col= '/control/ADRC_debug_signals/lat_error', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Lateral Error Metric:", lat_error_metric)

lookahead_error_metric = processor.calculate_error_metric_single_value(
    error_val_col= '/lookahead_error/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Lookahead Error Metric:", lookahead_error_metric)

avg_lat_error = processor.calculate_average_val(
    current_val_col= '/control/ADRC_debug_signals/lat_error',
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Lateral Error:", avg_lat_error[0], " Average Absolute Lateral Error:", avg_lat_error[1])

avg_yaw_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Yaw Error:", avg_yaw_error[0], " Average Absolute Yaw Error:", avg_yaw_error[1])

avg_speed_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Speed Error:", avg_speed_error[0], " Average Absolute Speed Error:", avg_speed_error[1])
    
avg_lookahead_error = processor.calculate_average_val(
    current_val_col= '/lookahead_error/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Lookahead Error:", avg_lookahead_error[0], " Average Absolute Lookahead Error:", avg_lookahead_error[1])


print("SECTOR 2")
x_lower = -364
x_upper=-59
y_lower=None
y_upper= 359
bound_case = 3

yaw_rate_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_rate_des',
    current_val_col= '/control/ADRC_debug_signals/yaw_rate', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
     bound_case=bound_case)
print("Yaw Rate Error Metric:", yaw_rate_error_metric)

yaw_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
     bound_case=bound_case)
print("Yaw Error Metric:", yaw_error_metric)

speed_error_metric = processor.calculate_error_metric( 
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Speed Error Metric:", speed_error_metric)

lat_error_metric = processor.calculate_error_metric_single_value(
    error_val_col= '/control/ADRC_debug_signals/lat_error', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Lateral Error Metric:", lat_error_metric)

lookahead_error_metric = processor.calculate_error_metric_single_value(
    error_val_col= '/lookahead_error/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Lookahead Error Metric:", lookahead_error_metric)

avg_lat_error = processor.calculate_average_val(
    current_val_col= '/control/ADRC_debug_signals/lat_error',
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Lateral Error:", avg_lat_error[0], " Average Absolute Lateral Error:", avg_lat_error[1])

avg_yaw_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Yaw Error:", avg_yaw_error[0], " Average Absolute Yaw Error:", avg_yaw_error[1])

avg_speed_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Speed Error:", avg_speed_error[0], " Average Absolute Speed Error:", avg_speed_error[1])

avg_lookahead_error = processor.calculate_average_val(
    current_val_col= '/lookahead_error/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Lookahead Error:", avg_lookahead_error[0], " Average Absolute Lookahead Error:", avg_lookahead_error[1])