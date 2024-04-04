import csv

class DataProcessor:
    def __init__(self, csv_file, simulator):
        self.csv_file = csv_file
        self.simulator = simulator # "AWSIM" or "CODEGEN"

    def preprocess_data(self):
        # Open the original CSV file for reading
        with open(self.csv_file, 'r') as original_file:
            reader = csv.reader(original_file)
            headers = next(reader)  # Extract headers 
            data = list(reader)

        ### Normalize the time values by subtracting all by the first val ###
        # Extract the value of the first row to use as the subtractor
        first_row_time = float(data[0][0])
        # Subtract the value of the first row from all rows in the first column
        for row in data:
            row[0] = str(float(row[0]) - first_row_time)

        ### Populate empty rows with the previous non-empty value ###
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '':
                    if i == 0:
                        data[i][j] = '0'  # If it's the first row, set to 0
                    else:
                        data[i][j] = data[i-1][j] #if it is not the first row, use previous row's value

        # Create a new CSV file for writing
        output_file = self.csv_file.split('.')[0] + '_edited.csv'

        # Write the modified data to the new CSV file
        with open(output_file, 'w', newline='') as edited_file:
            writer = csv.writer(edited_file)
            writer.writerow(headers)  # Write headers
            writer.writerows(data)

        print(f"File '{output_file}' created with modified data.")

    def calculate_lap_time(self):
        # Open the CSV file for reading
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            # Skip header
            next(reader)
            data = list(reader)

        # Extract the value of the first and last row to calculate lap time
        first_row_time = float(data[0][0])
        last_row_time = float(data[-1][0])

        # Calculate lap time
        lap_time = last_row_time - first_row_time

        return lap_time

    # 1/N * SUM((ref-curr)^2)
    def calculate_error_metric(self, ref_val_col, current_val_col, x_lower, x_upper, y_lower, y_upper, bound_case):
        # Initialize yaw_error_metric
        error_metric = 0
        count = 0
        
        # Open the CSV file for reading
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            next(reader)

            # Flag to indicate whether we're inside the desired range of rows
            inside_range = False
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Extract relevant values from the row
                desired_val = float(row[ref_val_col])
                current_val = float(row[current_val_col])

                if(self.simulator == "CODEGEN"):
                    x_pos = float(row['/odometry/global_filtered/pose/pose/position/x'])
                    y_pos = float(row['/odometry/global_filtered/pose/pose/position/y'])
                elif(self.simulator == "AWSIM"):
                    x_pos = float(row['/novatel_bottom/inspva/latitude'])
                    y_pos = float(row['/novatel_bottom/inspva/longitude'])
                else:
                    raise Exception("ERROR NO SUCH SIMULATOR: ", self.simulator)        
                           
                # Check if the conditions for range are met
                if bound_case == 1: #top part of track
                    if x_lower <= x_pos <= x_upper and y_pos >= y_lower:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 2: #left
                    if y_lower <= y_pos <= y_upper and x_pos <= x_upper:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 3: #bottom
                    if x_lower <= x_pos <= x_upper and y_pos <= y_upper:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 4: #right
                    if y_lower <= y_pos <= y_upper and x_pos >= x_lower:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                # If inside the desired range, calculate yaw_error_metric
                if inside_range:
                    count += 1
                    # Calculate the square of the difference between desired_yaw and current_yaw_rate
                    error_metric += (desired_val - current_val) ** 2

        # Divide yaw_error_metric by count if count is not zero
        if count != 0:
            error_metric /= count
        return error_metric


    def calculate_error_metric_single_value(self, error_val_col, x_lower, x_upper, y_lower, y_upper, bound_case):
        # Initialize yaw_error_metric
        error_metric = 0
        count = 0
        
        # Open the CSV file for reading
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            next(reader)

            # Flag to indicate whether we're inside the desired range of rows
            inside_range = False
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Extract relevant values from the row
                error_val = float(row[error_val_col])

                if(self.simulator == "CODEGEN"):
                    x_pos = float(row['/odometry/global_filtered/pose/pose/position/x'])
                    y_pos = float(row['/odometry/global_filtered/pose/pose/position/y'])
                elif(self.simulator == "AWSIM"):
                    x_pos = float(row['/novatel_bottom/inspva/latitude'])
                    y_pos = float(row['/novatel_bottom/inspva/longitude'])
                else:
                    raise Exception("ERROR NO SUCH SIMULATOR: ", self.simulator)   
                
                if bound_case == 1: #top part of track
                    if x_lower <= x_pos <= x_upper and y_pos >= y_lower:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 2: #left
                    if y_lower <= y_pos <= y_upper and x_pos <= x_upper:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 3: #bottom
                    if x_lower <= x_pos <= x_upper and y_pos <= y_upper:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 4: #right
                    if y_lower <= y_pos <= y_upper and x_pos >= x_lower:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False
                
                # If inside the desired range, calculate yaw_error_metric
                if inside_range:
                    count += 1
                    # Calculate the square of the difference between desired_yaw and current_yaw_rate
                    error_metric += error_val ** 2

        # Divide yaw_error_metric by count if count is not zero
        if count != 0:
            error_metric /= count
        return error_metric

    def calculate_average_val(self, current_val_col, x_lower, x_upper, y_lower, y_upper, bound_case):
        # Initialize yaw_error_metric
        sum= 0
        abs_sum = 0
        count = 0
        
        # Open the CSV file for reading
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            next(reader)

            # Flag to indicate whether we're inside the desired range of rows
            inside_range = False
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Extract relevant values from the row
                current_val = float(row[current_val_col])

                if(self.simulator == "CODEGEN"):
                    x_pos = float(row['/odometry/global_filtered/pose/pose/position/x'])
                    y_pos = float(row['/odometry/global_filtered/pose/pose/position/y'])
                elif(self.simulator == "AWSIM"):
                    x_pos = float(row['/novatel_bottom/inspva/latitude'])
                    y_pos = float(row['/novatel_bottom/inspva/longitude'])
                else:
                    raise Exception("ERROR NO SUCH SIMULATOR: ", self.simulator) 
                            
                # Check if the conditions for range are met
                if bound_case == 1: #top part of track
                    if x_lower <= x_pos <= x_upper and y_pos >= y_lower:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 2: #left
                    if y_lower <= y_pos <= y_upper and x_pos <= x_upper:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 3: #bottom
                    if x_lower <= x_pos <= x_upper and y_pos <= y_upper:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                if bound_case == 4: #right
                    if y_lower <= y_pos <= y_upper and x_pos >= x_lower:
                        inside_range = True
                    else:
                        # If not within the range, reset the flag
                        inside_range = False

                # If inside the desired range, calculate yaw_error_metric
                if inside_range:
                    count += 1
                    # Calculate the square of the difference between desired_yaw and current_yaw_rate
                    sum += current_val
                    abs_sum += abs(current_val)

        # Divide yaw_error_metric by count if count is not zero
        if count != 0:
            sum /= count
            abs_sum /= count
        return sum, abs_sum

    def calculate_average_val_two_vals(self, ref_val_col, current_val_col, x_lower, x_upper, y_lower, y_upper, bound_case):
        # Initialize yaw_error_metric
        sum= 0
        abs_sum = 0
        count = 0
        
        # Open the CSV file for reading
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            next(reader)

            # Flag to indicate whether we're inside the desired range of rows
            inside_range = False
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Extract relevant values from the row
                current_val = float(row[current_val_col])
                ref_val = float(row[ref_val_col])

                if(self.simulator == "CODEGEN"):
                    x_pos = float(row['/odometry/global_filtered/pose/pose/position/x'])
                    y_pos = float(row['/odometry/global_filtered/pose/pose/position/y'])
                elif(self.simulator == "AWSIM"):
                    x_pos = float(row['/novatel_bottom/inspva/latitude'])
                    y_pos = float(row['/novatel_bottom/inspva/longitude'])
                else:
                    raise Exception("ERROR NO SUCH SIMULATOR: ", self.simulator)   
                            
                # Check if the conditions for range are met
                if bound_case == 1: #top part of track
                    if x_lower <= x_pos <= x_upper and y_pos >= y_lower:
                        inside_range = True
                    else:
                        inside_range = False

                if bound_case == 2: #left
                    if y_lower <= y_pos <= y_upper and x_pos <= x_upper:
                        inside_range = True
                    else:
                        inside_range = False

                if bound_case == 3: #bottom
                    if x_lower <= x_pos <= x_upper and y_pos <= y_upper:
                        inside_range = True
                    else:
                        inside_range = False

                if bound_case == 4: #right
                    if y_lower <= y_pos <= y_upper and x_pos >= x_lower:
                        inside_range = True
                    else:
                        inside_range = False

                # If inside the desired range, calculate yaw_error_metric
                if inside_range:
                    count += 1
                    # Calculate the square of the difference between desired_yaw and current_yaw_rate
                    sum += (ref_val - current_val)
                    abs_sum += abs(ref_val - current_val)

        # Divide yaw_error_metric by count if count is not zero
        if count != 0:
            sum /= count
            abs_sum /= count
        return sum, abs_sum
