from data_processor import DataProcessor


simulator = "AWSIM"
csv_file_path = 'vegas_ADRC_AWSIM.csv'
processor = DataProcessor(csv_file_path, simulator)
# processor.preprocess_data()
csv_file_path = 'vegas_ADRC_AWSIM_edited.csv'
processor = DataProcessor(csv_file_path, simulator)

print(" === METRICS FOR ADRC/VEGAS/AWSIM/100mph (V9) === ")
# Calculate and print the lap time
lap_time = processor.calculate_lap_time()
print("Lap Time:", lap_time)

print("SECTOR 1")
# Sector 1 (bounded laterally, partially bounded longitudinally)
lat_lower=36.274
lat_upper=36.278
lon_lower=-115.013
lon_upper= None
bound_case = 1 


yaw_rate_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_rate_des',
    current_val_col= '/control/ADRC_debug_signals/yaw_rate', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Yaw Rate Error Metric:", yaw_rate_error_metric)

yaw_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw',
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
     bound_case=bound_case)
print("Yaw Error Metric:", yaw_error_metric)

speed_error_metric = processor.calculate_error_metric( 
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data',
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Speed Error Metric:", speed_error_metric)

lat_error_metric = processor.calculate_error_metric_single_value( 
    error_val_col= '/control/ADRC_debug_signals/lat_error', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Lateral Error Metric:", lat_error_metric)

lookahead_error_metric = processor.calculate_error_metric_single_value( 
    error_val_col= '/lookahead_error/data',  
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Lookahead Error Metric:", lookahead_error_metric)


avg_lat_error = processor.calculate_average_val(
    current_val_col= '/control/ADRC_debug_signals/lat_error', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Lateral Error:", avg_lat_error[0], " Average Absolute Lateral Error:", avg_lat_error[1])

avg_yaw_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Yaw Error:", avg_yaw_error[0], " Average Absolute Yaw Error:", avg_yaw_error[1])

avg_speed_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data',
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Speed Error:", avg_speed_error[0], " Average Absolute Speed Error:", avg_speed_error[1])

avg_lookahead_error = processor.calculate_average_val(
    current_val_col= '/lookahead_error/data', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Lookahead Error:", avg_lookahead_error[0], " Average Absolute Lookahead Error:", avg_lookahead_error[1])


print("SECTOR 2")
lat_lower = 36.278
lat_upper= 36.281
lon_lower=None
lon_upper= -115.006
bound_case = 3

yaw_rate_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_rate_des',
    current_val_col= '/control/ADRC_debug_signals/yaw_rate', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Yaw Rate Error Metric:", yaw_rate_error_metric)

yaw_error_metric = processor.calculate_error_metric(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw',
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
     bound_case=bound_case)
print("Yaw Error Metric:", yaw_error_metric)

speed_error_metric = processor.calculate_error_metric( 
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data',
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Speed Error Metric:", speed_error_metric)

lat_error_metric = processor.calculate_error_metric_single_value( 
    error_val_col= '/control/ADRC_debug_signals/lat_error', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Lateral Error Metric:", lat_error_metric)

lookahead_error_metric = processor.calculate_error_metric_single_value( 
    error_val_col= '/lookahead_error/data',  
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Lookahead Error Metric:", lookahead_error_metric)


avg_lat_error = processor.calculate_average_val(
    current_val_col= '/control/ADRC_debug_signals/lat_error', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Lateral Error:", avg_lat_error[0], " Average Absolute Lateral Error:", avg_lat_error[1])

avg_yaw_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/control/ADRC_debug_signals/yaw_hat',
    current_val_col= '/control/ADRC_debug_signals/yaw', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Yaw Error:", avg_yaw_error[0], " Average Absolute Yaw Error:", avg_yaw_error[1])

avg_speed_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data',
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Speed Error:", avg_speed_error[0], " Average Absolute Speed Error:", avg_speed_error[1])

avg_lookahead_error = processor.calculate_average_val(
    current_val_col= '/lookahead_error/data', 
    x_lower=lat_lower, x_upper=lat_upper, y_lower=lon_lower, y_upper=lon_upper,
    bound_case=bound_case)
print("Average Lookahead Error:", avg_lookahead_error[0], " Average Absolute Lookahead Error:", avg_lookahead_error[1])