from data_processor import DataProcessor

simulator = "CODEGEN"
csv_file_path = 'vegas_MPC_CODEGEN.csv'
processor = DataProcessor(csv_file_path, simulator)
# processor.preprocess_data()
csv_file_path = 'vegas_MPC_CODEGEN_edited.csv'
processor = DataProcessor(csv_file_path, simulator)


print(" === METRICS FOR MPC/VEGAS/CODEGEN/100mph (29MAR) === ")
# Calculate and print the lap time
lap_time = processor.calculate_lap_time()
print("Lap Time:", lap_time)

print("SECTOR 1")
# Sector 1 (bounded laterally, partially bounded longitudinally)
x_lower=-824
x_upper=-503
y_lower=691
y_upper= None
bound_case = 1 #1 is top, 2 is left, 3 is bottom, 4 is right


yaw_rate_error_metric = processor.calculate_error_metric(
    ref_val_col= '/desired_yaw_rate/data', 
    current_val_col= '/current_yaw_rate/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Yaw Rate Error Metric:", yaw_rate_error_metric)

yaw_error_metric = processor.calculate_error_metric_single_value(
    error_val_col= '/heading_error/data', 
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
    error_val_col= '/lateral_error/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Lateral Error Metric:", lat_error_metric)

avg_lat_error = processor.calculate_average_val(
    current_val_col= '/lateral_error/data',
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Lateral Error:", avg_lat_error[0], " Average Absolute Lateral Error:", avg_lat_error[1])

avg_yaw_error = processor.calculate_average_val(
    current_val_col= '/heading_error/data',  
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Yaw Error:", avg_yaw_error[0], " Average Absolute Yaw Error:", avg_yaw_error[1])

avg_speed_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Speed Error:", avg_speed_error[0], " Average Absolute Speed Error:", avg_speed_error[1])




print("SECTOR 2")
x_lower = -364
x_upper=-59
y_lower=None
y_upper= 359
bound_case = 3

yaw_rate_error_metric = processor.calculate_error_metric(
    ref_val_col= '/desired_yaw_rate/data', 
    current_val_col= '/current_yaw_rate/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Yaw Rate Error Metric:", yaw_rate_error_metric)

yaw_error_metric = processor.calculate_error_metric_single_value( 
    error_val_col= '/heading_error/data', 
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
    error_val_col= '/lateral_error/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Lateral Error Metric:", lat_error_metric)

avg_lat_error = processor.calculate_average_val(
    current_val_col= '/lateral_error/data',
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Lateral Error:", avg_lat_error[0], " Average Absolute Lateral Error:", avg_lat_error[1])

avg_yaw_error = processor.calculate_average_val(
    current_val_col= '/heading_error/data',  
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Yaw Error:", avg_yaw_error[0], " Average Absolute Yaw Error:", avg_yaw_error[1])

avg_speed_error = processor.calculate_average_val_two_vals(
    ref_val_col= '/planning/desired_velocity/data', 
    current_val_col= '/localization/vehicle_speed/data', 
    x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
    bound_case=bound_case)
print("Average Speed Error:", avg_speed_error[0], " Average Absolute Speed Error:", avg_speed_error[1])



# #testing...
# csv_file_path = 'test_set.csv'
# x_lower=1
# x_upper=3
# y_lower=3
# y_upper= None
# bound_case=1 

# yaw_rate_error_metric = calculate_error_metric(csv_file_path, 
#                                                ref_val_col= '/desired_yaw_rate/data', 
#                                                current_val_col= '/current_yaw_rate/data', 
#                                                x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
#                                                bound_case=bound_case)
# print("Yaw Rate Error Metric:", yaw_rate_error_metric) #correct

# # Calculate and print the yaw error metric
# yaw_error_metric = calculate_error_metric_single_value(csv_file_path, 
#                                                        error_val_col= '/heading_error/data', 
#                                                        x_lower=x_lower, x_upper=x_upper, y_lower=y_lower, y_upper=y_upper,
#                                                        bound_case=bound_case)
# print("Yaw Error Metric:", yaw_error_metric) #correct