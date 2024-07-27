import re
from collections import Counter

# Parse log file
def parse_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Return the total number of requests
def total_requests(log_entries):
    return len(log_entries)

# Return the percentage of successful requests (status code 200-299)
def successful_requests(log_entries):
    total = len(log_entries)
    successful = sum(1 for entry in log_entries if re.search(r'\" [2-5][0-9][0-9] ', entry))
    if total == 0:
        return 0
    return (successful / total) * 100

# Return the IP address with the most requests
def most_active_user(log_entries):
    ip_addresses = []
    for entry in log_entries:
        match = re.match(r'^(\S+)', entry)
        if match:
            ip_addresses.append(match.group(1))
    if not ip_addresses:
        return 'No IP addresses found', 0
    most_common_ip, count = Counter(ip_addresses).most_common(1)[0]
    return most_common_ip, count

# Return counts for each HTTP request method
def request_categories(log_entries):
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    counts = {method: 0 for method in methods}
    for entry in log_entries:
        for method in methods:
            if f'"{method} ' in entry:
                counts[method] += 1
    return counts

# Generate and print the report based on the log file
def generate_report(file_path):
    log_entries = parse_log(file_path)
    
    print("Log Analysis Report")
    print("--------------------")
    
    total = total_requests(log_entries)
    print(f"Total Requests Count: {total}")
    
    success_percentage = successful_requests(log_entries)
    print(f"Percentage of Successful Requests: {success_percentage:.2f}%")
    
    most_active_ip, count = most_active_user(log_entries)
    print(f"Most Active User (IP): {most_active_ip} with {count} requests")
    
    categories = request_categories(log_entries)
    print("HTTP Request Categories:")
    for method, count in categories.items():
        print(f"{method}: {count}")

if __name__ == "__main__":
    # Define the log file path directly. You can use the github logs file that I have 
    log_file_path = 'logs.txt'
    
    try:
        generate_report(log_file_path)
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
