# Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html

# Packages
## Work with aws
import boto3
## Tracking the upload status
import os
import sys
import threading

# Paths
## Main directory
module_path = os.path.abspath(os.path.join('..'))
## raw-data directory
raw_data_path = module_path + "/bucket/raw/"

# Functions
## Define the class to see the progress
class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

print('SUCCESS - GENERAL SETTINGS\n')

# Task
## Client to access the Amazon S3 bucket
s3_client = boto3.client('s3')
## Upload data to raw layer
file_name_list = [
    "RAIS_VINC_PUB_CENTRO_OESTE.txt", 
    "RAIS_VINC_PUB_MG_ES_RJ.txt", 
    "RAIS_VINC_PUB_NORDESTE.txt",
    "RAIS_VINC_PUB_NORTE.txt", 
    "RAIS_VINC_PUB_SP.txt", 
    "RAIS_VINC_PUB_SUL.txt"
    ]

bucket_name = "datalake-masca-md1-challenge2-tf"

object_name_list = [
    "RAIS_VINC_PUB_CENTRO_OESTE.txt", 
    "RAIS_VINC_PUB_MG_ES_RJ.txt", 
    "RAIS_VINC_PUB_NORDESTE.txt",
    "RAIS_VINC_PUB_NORTE.txt", 
    "RAIS_VINC_PUB_SP.txt", 
    "RAIS_VINC_PUB_SUL.txt"
    ]

for i in range(0, len(file_name_list)):
    print("\n\n\n\n", i, "\n\n\n\n")
    file_name = raw_data_path + file_name_list[i]
    object_name = "raw/" + object_name_list[i]
    s3_client.upload_file(file_name, bucket_name, object_name, Callback=ProgressPercentage(file_name))

print('\n>>> UPLOAD IS DONE <<<\n')