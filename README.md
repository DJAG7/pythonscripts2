# Python Scripts Documentation
This is the documentation for Problem Statement 2

## Automated Backup Script - Q2
*Write a script to automate the backup of a specified directory to a remote server or a cloud storage solution. The script should provide a report on the success or failure of the backup operation.*

This script performs automated backups of a specified directory to an Amazon S3 bucket. It includes timestamping in filenames for version control and logs the status of each file upload.

### Requirements
- `boto3` - AWS SDK for Python
- aws cli
- Python 3.11 +

### Usage
To enable the usage of the script, run ```aws configure ```
Configure using IAM secret keys

![image](https://github.com/user-attachments/assets/1c9831f9-aa80-4be6-a491-4c0cc7d4fa91)

To use the script, run the following command:
`python automated-backup.py <source_directory> <bucket_name>`

OUTPUT-

![image](https://github.com/user-attachments/assets/cc070349-1b95-4cd4-a8d9-f804d939c0e1)

You can see it uploaded to s3 as well

![image](https://github.com/user-attachments/assets/01eb000b-9037-472e-b9a9-90a0a18a3fc3)


### Description
- **`gethelp()`**: Displays usage information if the script is run with incorrect arguments.
- **`backup(source, bucket_name)`**: 
  - Sets up logging for the backup process.
  - Creates an S3 client to interact with the AWS S3 service.
  - Checks if the source directory exists and uploads files from the directory to the specified S3 bucket, including a timestamp in the filename for version control.
  - Logs success or error messages during the upload process.

## Log Analysis Script

### Overview
This script analyzes web server logs to generate a detailed report. It provides insights into the total number of requests, the percentage of successful requests, the most active user (by IP address), and the counts of each HTTP request method.

### Requirements
- Python 3.x

### Description
- **`parse_log(file_path)`**: Reads the log file and returns its lines as a list.
- **`total_requests(log_entries)`**: Counts the total number of log entries.
- **`successful_requests(log_entries)`**: Calculates the percentage of successful requests, based on status codes in the range 200-299.
- **`most_active_user(log_entries)`**: Identifies the IP address with the most requests.
- **`request_categories(log_entries)`**: Counts occurrences of various HTTP request methods (GET, POST, PUT, DELETE).
- **`generate_report(file_path)`**: Generates and prints a comprehensive log analysis report, including the total request count, percentage of successful requests, most active user, and request method counts.

### Usage
To use the script, ensure you have a log file named `logs.txt` in the same directory. Run the script to generate the report:
`python log_analysis.py`

Make sure the log file is correctly formatted and accessible.

OUTPUT-

![image](https://github.com/user-attachments/assets/35dedba2-6d9b-4573-acef-d11e065bd4f7)

---




