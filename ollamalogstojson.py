# turn ollama logs into json created by Rod Soto

import re
import json

# Function to parse and convert logs to JSON
def convert_logs_to_json(file_path):
    json_logs = []
    # Regex patterns for different log formats
    config_pattern = re.compile(r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) (\S+): (\S+) server config env="(.+)"')
    standard_log_pattern = re.compile(r'time=(.+?) level=(\S+) source=(\S+):(\d+) msg="(.+)"')
    gin_debug_pattern = re.compile(r'\[GIN-debug\] (\[[A-Z]+\]) (.+)')

    with open(file_path, 'r') as file:
        for line in file:
            if config_match := config_pattern.match(line):
                datetime, file_name, level, env = config_match.groups()
                env_dict = {}
                # Properly formatting the environment string to create a JSON object
                env_items = env.replace("map[", "").replace("]", "").split(" ")
                for item in env_items:
                    if ":" in item:
                        key, value = item.split(":", 1)  # Split only on the first colon
                        env_dict[key] = value.strip('"')  # Remove quotes if present
                json_logs.append({"datetime": datetime, "file": file_name, "level": level, "environment": env_dict})
            elif standard_match := standard_log_pattern.match(line):
                datetime, level, source, lineno, msg = standard_match.groups()
                json_logs.append({"datetime": datetime, "level": level, "source": source, "line": lineno, "message": msg})
            elif gin_match := gin_debug_pattern.match(line):
                warning_level, msg = gin_match.groups()
                json_logs.append({"level": warning_level, "message": msg})
            else:
                # Handling lines that do not match any known pattern
                json_logs.append({"message": line.strip()})

    return json_logs

# Specify the path to your log file
log_file_path = '/home/research/Desktop/ollamallamadeepseek.logs'

# Process the log file and convert it to JSON
full_json_logs = convert_logs_to_json(log_file_path)

# Write the JSON output to a new file
output_json_path = '/home/research/Desktop/ollamallamadeepseek.json'
with open(output_json_path, 'w') as json_file:
    json.dump(full_json_logs, json_file, indent=4)

print(f"Logs have been converted to JSON and saved to {output_json_path}")
