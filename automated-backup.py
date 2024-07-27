import boto3
import os
import sys
import logging
from datetime import datetime

def gethelp():
    print("Usage: python automated-backup.py <source_directory> <bucket_name>")

def backup(source, bucket_name):
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    # Create S3 client
    s3 = boto3.client('s3')

    if not os.path.exists(source):
        logger.error("Source Directory not found")
        return

    try:
        # Create timestamp
        timestamp = datetime.now().strftime("%H.%M.%S_%d.%m.%y")

        # Upload files
        for filename in os.listdir(source):
            src_path = os.path.join(source, filename)
            if os.path.isfile(src_path):
                dst_path = f"backup_{timestamp}_{filename}"  # Including timestamp in the filename
                try:
                    s3.upload_file(src_path, bucket_name, dst_path)
                    logger.info(f"Successfully uploaded {filename} to {dst_path}")
                except Exception as e:
                    logger.error(f"Error uploading {filename}: {e}")
        logger.info("Backup completed.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] == "-h":
        print("Error: Required Arguments not given")
        gethelp()
    else:
        source_directory = sys.argv[1]
        bucket_name = sys.argv[2]
        try:
            backup(source_directory, bucket_name)
        except Exception as e:
            print(f"Error Occurred: {e}")
