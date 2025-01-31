# script to convert ollama logs into csv created by Rod Soto

import pandas as pd
import re

# Path to the log file
file_path = '/home/research/Desktop/ollamallamadeepseek.logs'

# Function to parse log entries
def parse_log_entry(line):
    # Extract timestamp
    timestamp_match = re.search(r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})', line)
    timestamp = timestamp_match.group(0) if timestamp_match else ''

    # Extract level
    level_match = re.search(r'level=(\w+)', line)
    level = level_match.group(1) if level_match else ''

    # Extract source
    source_match = re.search(r'source=([^\s]+)', line)
    source = source_match.group(1) if source_match else ''

    # Extract message
    message_match = re.search(r'msg="([^"]+)"', line)
    message = message_match.group(1) if message_match else line.strip()  # Default to full line if no msg pattern

    return [timestamp, level, source, message]

# Read the entire log file
with open(file_path, 'r') as file:
    log_entries = file.readlines()

# Parse each log entry
parsed_data = [parse_log_entry(line) for line in log_entries if line.strip()]

# Creating a DataFrame
df_logs = pd.DataFrame(parsed_data, columns=['Timestamp', 'Level', 'Source', 'Message'])

# Path for the CSV output
csv_file_path = '/home/research/Desktop/test_parsed_logs.csv'

# Save the DataFrame to a CSV file
df_logs.to_csv(csv_file_path, index=False)

print(f"Log data has been parsed and saved to {csv_file_path}")
