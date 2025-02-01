#webui logs to csv created by Rod Soto

import csv
import re

# Define the path to your log file
log_file_path = '/home/research/Desktop/webui.log'

# Function to parse log file and extract relevant data
def parse_log_file(file_path):
    parsed_data = []
    # Regex pattern to match log entries with HTTP methods
    pattern = re.compile(r'INFO:\s+(\d+\.\d+\.\d+\.\d+:\d+) - "(GET|POST) (/.+?) HTTP/1.1" (\d{3}) OK')

    # Open and read the log file
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                ip_port = match.group(1)
                method = match.group(2)
                endpoint = match.group(3)
                status = match.group(4)
                # Try to extract UUID from the endpoint
                uuid_match = re.search(r'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', endpoint)
                uuid = uuid_match.group(1) if uuid_match else "No UUID Found"
                parsed_data.append([ip_port, method, endpoint, status, uuid])
    return parsed_data

# Call the function and pass the path of your log file
log_data = parse_log_file(log_file_path)

# Specifying the CSV file path
csv_file_path = '/home/research/Desktop/webui.csv'

# Writing data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IP:Port", "Method", "Endpoint", "Status Code", "UUID"])
    writer.writerows(log_data)

print(f"CSV file has been saved to {csv_file_path}")
