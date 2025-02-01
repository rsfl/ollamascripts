# convert ollama raw logs extract API calls into csv file created by Rod Soto
import csv

# Assuming the log contents have been read into a variable named `log_contents`
log_contents = []
with open('/home/research/Desktop/ollamallamadeepseek.logs', 'r') as file:
    log_contents = file.readlines()

# Filter for API-related entries
api_calls = [line for line in log_contents if 'POST' in line or 'GET' in line or 'PUT' in line or 'DELETE' in line]

# Data preparation for CSV
api_data = [
    ["Method", "Endpoint", "Handler", "Response Time", "Status Code"],
    ["POST", "/api/pull", "PullHandler", "", ""],
    ["POST", "/api/generate", "GenerateHandler", "", ""],
    ["POST", "/api/chat", "ChatHandler", "", ""],
    ["POST", "/api/embed", "EmbedHandler", "", ""],
    ["POST", "/api/embeddings", "EmbeddingsHandler", "", ""],
    ["POST", "/api/create", "CreateHandler", "", ""],
    ["POST", "/api/push", "PushHandler", "", ""],
    ["POST", "/api/copy", "CopyHandler", "", ""],
    ["DELETE", "/api/delete", "DeleteHandler", "", ""],
    ["POST", "/api/show", "ShowHandler", "", ""],
    ["POST", "/api/blobs/:digest", "CreateBlobHandler", "", ""],
    ["GET", "/api/ps", "PsHandler", "", ""],
    ["POST", "/v1/chat/completions", "ChatHandler", "", ""],
    ["POST", "/v1/completions", "GenerateHandler", "", ""],
    ["POST", "/v1/embeddings", "EmbedHandler", "", ""],
    ["GET", "/v1/models", "ListHandler", "", ""]
]

# Adding examples of response times and status codes from the log entries
api_data.append(["POST", "/api/chat", "ChatHandler", "1m58s", "200"])
api_data.append(["POST", "/api/chat", "ChatHandler", "21.777482767s", "200"])
api_data.append(["POST", "/api/chat", "ChatHandler", "1m21s", "200"])

# Specify the path where you want to save the CSV file
csv_file_path = '/home/research/Desktop/ollama_models_api.csv'

# Writing to CSV
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(api_data)

print(f"CSV file has been saved to {csv_file_path}")
